# MCP Competitive Analysis

Automated weekly competitive intelligence digest tracking the use, support,
positioning and offering of Model Context Protocol (MCP) and MCP-adjacent
capabilities by selected MDM / PIM / DAM vendors:

- Informatica
- SAP MDG
- Reltio
- Profisee
- Akeneo
- Salsify
- Inriver
- Pimcore
- Syndigo

## How it runs

1. A Cursor Cloud Agent runs on a weekly cron (Fridays, 15:00 UTC).
2. The agent researches the past week's news per vendor, computes a delta vs.
   the stored baseline, and writes two artefacts to `reports/`:
   - `YYYY-MM-DD_weekly_mcp_competitive_update.md`   (Markdown source of truth)
   - `YYYY-MM-DD_weekly_mcp_competitive_update.html` (email-ready HTML body)
3. The agent commits both files to its working branch and pushes.
4. A GitHub Actions workflow (`.github/workflows/email-weekly-report.yml`) runs
   shortly afterwards, picks up the latest HTML report from `reports/` on the
   default branch and emails it as an HTML message to the configured
   recipient(s) — default `mjan@stibosystems.com`.

## One-off / manual send

The workflow can be triggered manually from the **Actions** tab via
`workflow_dispatch`, optionally passing an explicit `report_path`.

You can also run the sender script locally:

```bash
export SMTP_HOST=smtp.sendgrid.net
export SMTP_PORT=587
export SMTP_USERNAME=apikey
export SMTP_PASSWORD=...            # SendGrid API key, Office365 app password, etc.
export MAIL_FROM="MCP CI <ci@example.com>"
export MAIL_TO="mjan@stibosystems.com"
python scripts/send_report_email.py
```

## Required GitHub Actions secrets

Add the following under **Settings → Secrets and variables → Actions**:

| Secret           | Required | Notes                                                          |
|------------------|----------|----------------------------------------------------------------|
| `SMTP_HOST`      | yes      | e.g. `smtp.sendgrid.net`, `smtp.office365.com`, `smtp.gmail.com` |
| `SMTP_PORT`      | yes      | `587` for STARTTLS, `465` for SMTPS                            |
| `SMTP_USERNAME`  | yes      | For SendGrid this is literally `apikey`                        |
| `SMTP_PASSWORD`  | yes      | SMTP password, app password, or API key                        |
| `SMTP_SECURITY`  | no       | `starttls` (default), `ssl`, or `none`                         |
| `MAIL_FROM`      | yes      | Verified sender on the SMTP provider                           |
| `MAIL_TO`        | no       | Defaults to `mjan@stibosystems.com`; comma-separate for multi  |

Once the secrets are set, the next Friday cron run will trigger both the report
generation and the email delivery automatically.

## Layout

```
reports/                              Weekly Markdown + HTML reports
scripts/send_report_email.py          SMTP sender (used by the workflow)
.github/workflows/email-weekly-report.yml   Scheduled emailer
```
