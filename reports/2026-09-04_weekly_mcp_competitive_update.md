# Weekly MCP Competitive Update — August 28, 2026 to September 4, 2026

Subject: Weekly MCP Competitive Update – August 28, 2026 to September 4, 2026
To: mjan@stibosystems.com

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

## 1. Executive Summary

- Reltio launched its first high-profile paid-media push since the SAP acquisition — two Manish Sood pieces on WSJ Custom Content (Sept 3) and a Business Insider-originated op-ed (Sept 2) reframe Reltio as the "system of context" for agentic AI. MCP-adjacent positioning only; no product news.
- Salsify accelerated its Agentic Commerce Readiness cadence — Part 2 of the "AI in Salsify" webinar aired Sept 2 with customer The Legacy Companies, and a long-form Sept 3 blog codifies "AEO 101" using the July Searchable data where Amazon barely appeared in ChatGPT shopping results.
- Pimcore Platform 2026.2.11 shipped Sept 1 as a bugfix-only point release; no MCP or Agent Bundle changes since the Aug 27 Tenzing announcement.
- Inriver published a Sept 1 follow-up piece extending its AEO Masterclass, previewing a Sept 22 live walkthrough inside a real Inriver PIM instance — MCP-adjacent but suggests upcoming demoware for the MCP endpoint stack.
- Five weeks post-spec, still zero public MCP 2026-07-28 compatibility statements across the nine tracked vendors; Informatica MCP docs remain on protocol 2025-06-18.

## 2. Key Updates This Week

### Company: Reltio
Status: **Updated**
Summary: Reltio's CEO Manish Sood authored a coordinated paid-media wave: a WSJ Custom Content pair on Sept 3 ("The AI Agents Are Ready—Your Data Isn't" and a CarMax customer story), plus a Sept 2 sponsored op-ed under Reltio's "an SAP company" branding. All three frame data debt as the reason enterprise AI stalls and pitch a "system of context" — Reltio's post-SAP repositioning language — as the antidote. No new product; the 2026.1.9.0 release (Aug 28) remains current.
Why it matters: First large-scale outbound campaign under the SAP umbrella; sharpens the "governed context beneath the agent" narrative that competes directly with Stibo Systems' MCP-and-governance messaging.
Source:
- [The AI Agents Are Ready—Your Data Isn't (WSJ Custom Content, Sept 3)](https://partners.wsj.com/reltio/the-age-of-intelligence/the-ai-agents-are-ready-your-data-isnt/)
- [CarMax's Data Engine Is Beating Rivals at Their Own Game (WSJ Custom Content, Sept 3)](https://partners.wsj.com/reltio/the-age-of-intelligence/carmaxs-data-engine-is-beating-rivals-at-their-own-game/)

### Company: Salsify
Status: **Updated**
Summary: Part 2 of the three-part "AI in Salsify: A Practical Playbook for Agentic Commerce Readiness" ran live Sept 2 with The Legacy Companies demoing Angie / SalsifyIQ workflows. A companion Sept 3 blog, "AEO 101: Why AI Agents Hate Incomplete Product Content," argues that catalog completeness — not scale or ad spend — determines AI-recommendation visibility, citing Searchable's July data (Target 25.5%, Walmart 20.3%, Amazon almost absent in ChatGPT shopping results). Part 3, focused on "powering agentic experiences," is teed up for September.
Why it matters: Salsify continues to own the "agentic shelf" vocabulary; the AEO framing reinforces PXM catalog completeness as the pre-condition for AI-agent visibility. MCP-adjacent; still no new MCP capabilities announced.
Source:
- [AEO 101: Why AI Agents Hate Incomplete Product Content (Salsify blog, Sept 3)](https://www.salsify.com/blog/aeo-101-why-ai-agents-hate-incomplete-product-content)
- [AI in Salsify Webinar Series — Part 2 (Sept 2)](https://www.salsify.com/resources/webinar/ai-in-salsify-a-practical-playbook-for-agentic-commerce-readiness)

### Company: Inriver
Status: **Updated**
Summary: Sept 1 resource "You started fixing your product data. Now it has to hold at scale." extends Episode 1 of Inriver's AEO Masterclass, arguing that a flexible data model plus agentic orchestration is required to sustain AI-ready structured data across catalogs. Trails Episode 2 (Sept 22) as a live walkthrough inside a real Inriver PIM instance covering structured-data workflows relevant to the MCP endpoint stack.
Why it matters: Keeps Inriver visible in the ACP/UCP/MCP three-protocol frame it established Aug 17; the Sept 22 live-PIM walkthrough is worth tracking for concrete MCP endpoint demoware.
Source:
- [You started fixing your product data. Now it has to hold at scale. (Inriver, Sept 1)](https://www.inriver.com/resources/you-started-fixing-your-product-data-now-it-has-to-hold-at-scale/)

### Company: Pimcore
Status: **Updated**
Summary: Pimcore Platform v2026.2.11 was released on GitHub on Sept 1 as a bugfix-only point release (workflow, thumbnails, DataObject inheritance, application-log housekeeping, WYSIWYG). No changes to the Agent Bundle or MCP-based Agent SDK, and no follow-up statements from Tenzing since the Aug 27 acquisition announcement.
Why it matters: Confirms platform stability continuity through the change of control; the MCP roadmap remains as previously communicated.
Source:
- [pimcore/pimcore v2026.2.11 release notes (GitHub, Sept 1)](https://github.com/pimcore/pimcore/releases/tag/v2026.2.11)

## 3. Notable Patterns

- Post-acquisition Reltio is investing in top-of-funnel narrative infrastructure (WSJ, Business Insider) around "system of context" language rather than in additional product news — a signal that SAP wants Reltio's positioning, not just its capability, to land in the enterprise buyer's vocabulary.
- Digital-shelf vendors (Salsify, Inriver) are converging on Answer Engine Optimization / AI-visibility as the near-term buyer pain, framed as an upstream data-completeness problem that MCP-adjacent PIM/PXM platforms solve.
- Silence on MCP 2026-07-28 compatibility persists into week five; Informatica MCP docs still cite protocol 2025-06-18, and no other tracked vendor has issued a public statement.

## 4. No Relevant Updates

- **Informatica** — only owned-channel LinkedIn activity in the window (Dreamforce Sept 15–17 promotion, "AI agents fail because of data" post); MCP docs unchanged and still on protocol 2025-06-18.
- **SAP MDG** — no MDG-specific news; the Sept 1 Bar & Bench item covers India-side legal closing of the SAP–Reltio deal only.
- **Profisee** — no public news; 2026.R2 (July 8) remains current.
- **Akeneo** — no primary-source news; Ecommerce Times ran another Adobe-acquires-Akeneo piece on Aug 31 with no adobe.com, akeneo.com, PR Newswire, or BusinessWire corroboration. Excluded per source rule.
- **Syndigo** — Sept 1 blog "Why Product Experience Is Rising on the C-Suite Agenda" and a "Syndication 101" post continue general PXM thought leadership; no new MCP or product news.

## 5. Suggested Follow-Up

- Read the WSJ Custom Content pair in full and consider whether Stibo Systems should push back on Reltio's "system of context" claim with an equivalent governed-master-data-plane framing before that vocabulary sets.
- Add Inriver's Sept 22 AEO Masterclass Episode 2 (live inside a real Inriver PIM) to the monitoring list — first opportunity to see concrete Inriver MCP endpoint demoware since the June 30 Summer release.
- Continue tracking for the first vendor to publish a public MCP 2026-07-28 compatibility statement; five weeks post-spec, the first-mover advantage is still available.
