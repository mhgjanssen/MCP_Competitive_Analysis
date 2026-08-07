# Weekly MCP Competitive Update – July 31, 2026 to August 7, 2026

**To:** mjan@stibosystems.com  
**Subject:** Weekly MCP Competitive Update – July 31, 2026 to August 7, 2026

---

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

## 1. Executive Summary

- **Reltio's 2026.1.7.0 landed in Production on July 31** and, contrary to preliminary notes, its headline capabilities are **Reltio IDE** (a VS Code + Cursor extension for AI-assisted business configuration authoring), **AgentFlow Mobile GA on iOS/Android**, and **auto-generated diagrams inside AgentFlow conversations** — collectively pushing MCP-backed agent authoring and consumption further into developer and mobile surfaces.
- **Inriver launched the inaugural Product Data Maturity Index (PDMI)** on August 5, positioning itself as the category thought leader for operational AI/agentic-commerce readiness. Zero of the 117 organizations that self-declared "fully ready for agentic commerce" cleared the operational bar — a strong narrative asset for any AI-ready MDM/PIM messaging.
- **Informatica's "trusted data for AI agents" narrative continued to amplify** through a fresh WorkAI interview (Aug 2) with APAC Data Governance lead Anand Ramamoorthy; the underlying MCP protocol version documented for Informatica MCP servers remains `2025-06-18`.
- **None of the nine tracked vendors has yet published an explicit compatibility statement for the MCP `2026-07-28` specification** (Tier‑1 SDKs GA since July 28). Google's Aug 5 developer post confirms wide adoption elsewhere, so competitive pressure to make the statement is now building.
- **SAP MDG, Profisee, Akeneo, Pimcore** produced no new MCP-relevant news this week; light MCP-adjacent activity from **Salsify** (change-management blog, Aug 4) and **Syndigo** (Wells network onboarding, Aug 4).

## 2. Key Updates This Week

### Company: Reltio
**Status:** Updated  
**Summary:** The 2026.1.7.0 release deployed to Production on **July 31, 2026**. The actual new capabilities are **Reltio IDE** (a `.vsix` extension for VS Code and Cursor that lets data modelers author entity types, relationship types, hierarchies and reference attributes via natural-language prompts with real-time validation, ontology visualization and diff-before-deploy), **AgentFlow Mobile GA** for iOS and Android (voice/text queries, tenant switching, agent marketplace, PDF/Markdown conversation sharing) and **contextual diagrams in AgentFlow conversations** (relationship maps, flowcharts, timelines auto-generated from a prompt). Bi-weekly release 2026.1.8.0 rolls out to DEV/TEST today (Aug 7), PRD on Aug 14.  
**Why it matters:** Extends the governed, MCP-backed Reltio surface into two new personas — developers/implementers (IDE) and on-the-go business users (mobile) — narrowing the "developer productivity" gap versus Profisee's Aisey and Akeneo's Agentic Ziggy.  
**Source:**
- [Reltio 2026.1 bi-weekly Release Notes — 2026.1.7.0 (July 31, 2026)](https://docs.reltio.com/en/reltio/whats-new-and-notable/whats-new-at-a-glance/release-notes-at-a-glance/2026.1-release-notes/2026.1-bi-weekly-release-notes-rn)
- [Reltio Release cadence and delivery schedule (2026.1.8.0 to DEV/TEST Aug 7)](https://docs.reltio.com/en/reltio/whats-new-and-notable/whats-new-at-a-glance/release-notes-at-a-glance/release-cadence-and-delivery-schedule)

### Company: Inriver
**Status:** New  
**Summary:** Inriver published its inaugural **Product Data Maturity Index (PDMI)** on **August 5, 2026** — "The Product Data Paradox" — surveying 405 senior marketing, technology and data leaders in industrial manufacturing and wholesale distribution across the US and Europe (research by Silicon Valley Research Group). Headline finding: of 117 organizations claiming to be fully ready for agentic commerce, **zero** met the operational benchmark; only 13.6% have end-to-end product-data automation with an audit trail, and fewer than 12% track AEO/AI-search performance.  
**Why it matters:** MCP-adjacent. This is the first vendor-authored benchmark for operational agentic-commerce readiness in PIM. Expect it to be quoted in customer decks and analyst notes for months, and Inriver to anchor pipeline conversations on the "confidence vs. calibration" gap it names.  
**Source:**
- [Product Data Blind Spots Challenge Manufacturers' AI Ambitions, New Benchmark Finds — Inriver / GlobeNewswire (Aug 5, 2026)](https://www.globenewswire.com/news-release/2026/08/05/3339376/0/en/Product-Data-Blind-Spots-Challenge-Manufacturers-AI-Ambitions-New-Benchmark-Finds.html)
- [The Product Data Paradox and Maturity Index — Inriver research hub](https://www.inriver.com/resources/product-data-paradox-research/)

### Company: Informatica
**Status:** Updated  
**Summary:** Fresh WorkAI editorial (published Aug 2, 2026) with APAC Director of Data Governance & Quality **Anand Ramamoorthy** positions Informatica as the governance/metadata/quality layer under Salesforce's activation surface for AI agents post-acquisition — the strongest personal-narrative amplification of the "trusted data for every agent" story since Informatica World. Salesforce also confirmed (Aug 5) that Q2 FY27 results will be released Aug 26, with Q1 already disclosing $1.1B Informatica Cloud ARR and Informatica contributing >4pp to Q2 revenue growth guidance. Separately, the Informatica MCP servers "Getting Started" documentation now shows an "Updated: August 2026" stamp, but explicitly still documents MCP protocol `2025-06-18` — **no compatibility statement yet for the new `2026-07-28` spec**.  
**Why it matters:** Reinforces that the Salesforce–Informatica combination is being sold as the enterprise-agent trust layer, while the missing `2026-07-28` compatibility statement remains the most visible protocol-level gap for a vendor whose entire pitch is "MCP everywhere."  
**Source:**
- [Enterprise AI Needs Trusted Data More Than Better Models: Informatica's Anand Ramamoorthy — WorkAI.TV (Aug 2, 2026)](https://workai.tv/news/2026/08/ai-data/enterprise-ai-needs-trusted-data-more-than-better-models-informaticas-anand-ramamoorthy/)
- [Salesforce Announces Date of Second Quarter Fiscal 2027 Earnings Release and Webcast (Aug 5, 2026)](https://investor.salesforce.com/news/news-details/2026/Salesforce-Announces-Date-of-Second-Quarter-Fiscal-2027-Earnings-Release-and-Webcast/default.aspx)
- [Introduction to Informatica MCP servers — Updated August 2026 (protocol version 2025-06-18)](https://docs.informatica.com/claire/mcp-servers/current-version/getting-started-with-informatica-mcp-servers/introduction-to-informatica-mcp-servers.html)

### Company: Syndigo
**Status:** Updated  
**Summary:** Wells (Portugal's leading health/beauty/wellness retailer) went live on the Syndigo commerce network on Aug 4, 2026 — brands can now publish Enhanced Content directly into wells.pt. Companion Aug 5 Syndigo webinar with Krustez, "Beyond Compliance: Turning Product Data into Competitive Advantage," continues the "partner-ready content drives agent-era discoverability" theme.  
**Why it matters:** MCP-adjacent. Not a new MCP capability, but continued growth of the syndication substrate that Synapse/Agentic PXM depends on for downstream reach into "human + agent" shopping surfaces.  
**Source:**
- [Wells is now live with Syndigo — LinkedIn (Aug 4, 2026)](https://www.linkedin.com/posts/syndigo_wells-syndigo-enhancedcontent-activity-7490345969822220288-rKJx)
- [Beyond Compliance: Turning Product Data into Competitive Advantage — Syndigo × Krustez (Aug 5, 2026)](https://www.linkedin.com/posts/syndigo_productdata-pxm-gdsn-activity-7490376286796808192-3Vk-)

### Company: Salsify
**Status:** Updated  
**Summary:** New Salsify blog post "Navigating Change Management in the Modern Commerce Era" (Aug 4, 2026) frames agentic-commerce readiness as an organizational-change problem, quoting DSS 2026 speaker Livak Gilbert that content needs will grow **5x** to serve agentic systems. Reinforces last week's launch of the three-part "AI in Salsify: A Practical Playbook for Agentic Commerce Readiness" webinar series. No new MCP capabilities.  
**Why it matters:** MCP-adjacent. Signals Salsify is stretching its "agentic shelf" push from a product marketing story into an executive/change-management sales motion — an angle Stibo could match or challenge in mid-market PIM conversations.  
**Source:**
- [Navigating Change Management in the Modern Commerce Era — Salsify blog (Aug 4, 2026)](https://www.salsify.com/blog/navigating-change-management-in-the-modern-commerce-era)

## 3. Notable Patterns

- **MCP `2026-07-28` is now the elephant in the room.** Nine days after ship date, none of the nine tracked vendors has posted an explicit compatibility statement, even though Anthropic, AWS AgentCore Gateway and Google are already operating on it (Google Developers Blog, Aug 5). Informatica's docs still cite `2025-06-18`; SAP's Architecture Center says "SAP manages protocol compatibility; customers are shielded from breaking spec changes" — a hedged position rather than an explicit statement.
- **Agent authoring surfaces are diversifying by persona.** Reltio's new IDE targets VS Code/Cursor developers; AgentFlow Mobile targets sales/service on the go; both sit on the Reltio MCP Server. Combined with Profisee Aisey (Word doc → configured MDM), Akeneo Agentic Ziggy and Pimcore Agent SDK, the competitive frontier has shifted from "we expose MCP" to "who owns each persona's entry point into MCP-backed data."
- **Research and change-management narratives are becoming a competitive weapon.** Inriver's PDMI benchmark and Salsify's change-management blog both frame AI-readiness as an *operational* rather than technical problem — this is a deliberate move to raise the bar and to reset RFP evaluation criteria, and merits a proactive Stibo response.

## 4. No Relevant Updates

- **SAP MDG** — No MDG-specific news this week; the July MCP Gateway GA + AI Agent Hub / Joule Studio positioning remains current.
- **Profisee** — No new public news this week; 2026.R2 (July 8) remains current.
- **Akeneo** — No new public news this week aside from a routine Aug 4 LinkedIn thought-leadership post on AI enrichment nuances; Summer 2026 "Agentic Ziggy" release remains current.
- **Pimcore** — No new public news this week; Platform 2026.2 GA (July 9) and patch v2026.2.4 (July 21) remain current.

## 5. Suggested Follow-Up

1. Watch the Aug 26 Salesforce Q2 FY27 earnings call for any explicit Informatica MCP `2026-07-28` compatibility signal or new joint agent-governance framing.
2. Consider producing (or partnering on) a Stibo counter-benchmark to Inriver's PDMI focused on MDM operational maturity for agentic use cases — the "confidence vs. calibration" framing is very quotable and currently uncontested.
3. Track whether Reltio's IDE-in-Cursor/VS-Code motion pushes competitors (Profisee, Informatica, SAP MDG) to release similar developer surfaces; this is the fastest-moving front for MCP-backed agent authoring right now.

---

*Automated weekly MCP competitive intelligence digest. Sources cited inline; classifications (New / Updated) are computed against the previous baseline (2026-07-31).*
