#!/usr/bin/env python3
"""Send the latest weekly MCP competitive intelligence report as an HTML email.

Picks the most recent file matching ``reports/*_weekly_mcp_competitive_update.html``
and sends it to the configured recipient(s) over SMTP.

Required environment variables:
    SMTP_HOST       SMTP server hostname (e.g. smtp.sendgrid.net, smtp.office365.com)
    SMTP_PORT       SMTP server port (e.g. 587 for STARTTLS, 465 for SMTPS, 25 plain)
    SMTP_USERNAME   SMTP username (for SendGrid this is literally "apikey")
    SMTP_PASSWORD   SMTP password / API key
    MAIL_FROM       From address (must be a verified sender on the SMTP provider)
    MAIL_TO         Comma-separated recipient list
                    Default: mjan@stibosystems.com

Optional:
    SMTP_SECURITY   "starttls" (default), "ssl", or "none"
    MAIL_SUBJECT    Override subject line (default derived from the report date)
    REPORTS_DIR     Path to the reports directory (default: ./reports)
"""

from __future__ import annotations

import glob
import html
import os
import re
import smtplib
import ssl
import sys
from email.message import EmailMessage
from pathlib import Path


DEFAULT_RECIPIENT = "mjan@stibosystems.com"


def find_latest_report(reports_dir: Path) -> Path:
    pattern = str(reports_dir / "*_weekly_mcp_competitive_update.html")
    matches = sorted(glob.glob(pattern))
    if not matches:
        raise FileNotFoundError(
            f"No HTML reports found in {reports_dir} matching *_weekly_mcp_competitive_update.html"
        )
    return Path(matches[-1])


def derive_subject(report_path: Path) -> str:
    """Use the <title> tag if present, otherwise fall back to the filename date."""
    html = report_path.read_text(encoding="utf-8")
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    stem_date = report_path.stem.split("_", 1)[0]
    return f"Weekly MCP Competitive Update – {stem_date}"


def build_plain_text_fallback(html_body: str) -> str:
    text = re.sub(r"<style.*?</style>", "", html_body, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<script.*?</script>", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<head.*?</head>", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</(p|div|tr|h[1-6])>", "\n\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<li[^>]*>", "- ", text, flags=re.IGNORECASE)
    text = re.sub(r"</li>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<a [^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>",
                  r"\2 (\1)", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def send(report_path: Path) -> None:
    host = os.environ.get("SMTP_HOST")
    port = int(os.environ.get("SMTP_PORT", "587"))
    username = os.environ.get("SMTP_USERNAME")
    password = os.environ.get("SMTP_PASSWORD")
    mail_from = os.environ.get("MAIL_FROM")
    mail_to = os.environ.get("MAIL_TO", DEFAULT_RECIPIENT)
    security = os.environ.get("SMTP_SECURITY", "starttls").lower()
    subject = os.environ.get("MAIL_SUBJECT") or derive_subject(report_path)

    missing = [
        name for name, value in {
            "SMTP_HOST": host,
            "SMTP_USERNAME": username,
            "SMTP_PASSWORD": password,
            "MAIL_FROM": mail_from,
        }.items() if not value
    ]
    if missing:
        raise SystemExit(
            "Missing required environment variables: " + ", ".join(missing)
        )

    html_body = report_path.read_text(encoding="utf-8")
    text_body = build_plain_text_fallback(html_body)
    recipients = [addr.strip() for addr in mail_to.split(",") if addr.strip()]

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = mail_from
    msg["To"] = ", ".join(recipients)
    msg.set_content(text_body)
    msg.add_alternative(html_body, subtype="html")

    print(f"Sending '{subject}' to {recipients} via {host}:{port} ({security})")

    if security == "ssl":
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host, port, context=context, timeout=30) as smtp:
            smtp.login(username, password)
            smtp.send_message(msg, from_addr=mail_from, to_addrs=recipients)
    else:
        with smtplib.SMTP(host, port, timeout=30) as smtp:
            smtp.ehlo()
            if security == "starttls":
                smtp.starttls(context=ssl.create_default_context())
                smtp.ehlo()
            smtp.login(username, password)
            smtp.send_message(msg, from_addr=mail_from, to_addrs=recipients)

    print("Sent successfully.")


def main(argv: list[str]) -> int:
    reports_dir = Path(os.environ.get("REPORTS_DIR", "reports"))
    if len(argv) > 1:
        report_path = Path(argv[1])
    else:
        report_path = find_latest_report(reports_dir)
    print(f"Using report: {report_path}")
    send(report_path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
