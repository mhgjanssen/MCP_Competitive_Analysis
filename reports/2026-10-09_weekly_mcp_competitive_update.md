# Weekly MCP Competitive Update – October 2, 2026 to October 9, 2026

**To:** mjan@stibosystems.com
**From:** MCP Competitive Intelligence Agent
**Subject:** Weekly MCP Competitive Update – October 2, 2026 to October 9, 2026

---

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

## 1. Executive Summary

- **SAP AI Agent Hub reached GA on Oct 1, 2026** (confirmed by Oct 8 SAP News Center piece "How Joule Work and SAP Business AI Platform Are Powering the Next Generation of Business AI"). It is positioned as a vendor-agnostic command center for the discovery and governance of **AI agents, LLMs, and MCP servers across SAP and non-SAP environments** — **only verified MCP servers can be called in production** — and now gates SAP's broader autonomous-enterprise narrative. New **SAP Signavio Agent Mining** measures per-agent outcomes.
- **Reltio 2026.1.12.0 (PRD Oct 9, 2026)** ships the **5th SAP-branded "SAP Reltio Velocity Pack" — Banking**, a standalone retail + commercial banking pack distinct from Reltio for Financial Services, plus materialized-hierarchy structural validation and merge/unmerge connection preservation.
- **Profisee Anywhere (Sept 30 at FabCon Europe)** — Profisee's SaaS MDM now runs **natively inside Microsoft Fabric OneLake** (GA Dec 2026), with a new **Fabric SQL Database Connector** shipping in the 26R3 release this week. Profisee claims the only MDM platform where data is stewarded natively inside Fabric without leaving OneLake.
- **Pimcore Platform Version 2026.3.1 (Oct 6 GitHub)** — security-focused bugfix on top of 2026.3; **Oct 6 post-DMEXCO panel "AI Agents in Data & Experience Management: Hype, Help, or Game Changer?"** delivered by Dietmar Rietsch with seven partners.
- **Inriver Oct 7 resource** publishes a four-measure **AI content-control framework** (limit AI scope, decision owner, verification against trusted data, approval log) citing McKinsey's 2026 AI trust survey — MCP-adjacent governance-of-agents messaging.

## 2. Key Updates This Week

### Company: SAP MDG
**Status:** New
**Summary:** SAP's **AI Agent Hub reached general availability on Oct 1, 2026** (SAP News Center, Oct 8). It is a **vendor-agnostic command center** that automatically discovers and inventories **AI agents, LLMs, and MCP servers across SAP, Microsoft, Google, AWS, Databricks and ServiceNow**, with evaluation + verification workflows and runtime enforcement — **only verified MCP servers can be called in production**, and access is automatically revoked when verification status changes. New **SAP Signavio Agent Mining** measures per-agent outcomes. The same week, SAP published **"The MDM Renaissance: What AI-Native, Autonomous Master Data Looks Like in SAP Business Data Cloud"** (SAP Community, Corrie Brague, Sept 25) and **"SAP Reltio in the SAP Business AI Platform Architecture"** (SAP Community, JoseBastidas, Oct 7, with four-phase integration roadmap webinar). SAP MDG is being integrated into SAP BDC via Unified Customer Layer with full data-product exposure by end of year.
**Why it matters:** Explicit SAP policy that production AI agents can only use *verified* MCP servers — the first large-vendor governance gate for MCP in the tracked set — directly reinforces the "governed master data as the trust layer for agents" message and raises the bar competitors must meet.
**Source:**
- [How Joule Work and SAP Business AI Platform Are Powering the Next Generation of Business AI (SAP News Center, Oct 8, 2026)](https://news.sap.com/2026/10/joule-work-sap-business-ai-platform-power-next-generation-business-ai/)
- [SAP AI Agent Hub product page](https://www.sap.com/products/artificial-intelligence/ai-agent-hub.html)
- [Agentic AI & AI Agents on SAP Business AI Platform (SAP Architecture Center)](https://architecture.learning.sap.com/docs/ref-arch/98efa0)
- [The MDM Renaissance: What AI-Native, Autonomous Master Data Looks Like in SAP Business Data Cloud (SAP Community)](https://community.sap.com/t5/data-and-ai-professionals-blog-posts/what-ai-native-autonomous-master-data-looks-like-in-sap-business-data-cloud/ba-p/14490833)
- [SAP Reltio in the SAP Business AI Platform Architecture (SAP Community, Oct 7)](https://community.sap.com/t5/data-and-ai-professionals-blog-posts/sap-reltio-in-the-sap-business-ai-platform-architecture/ba-p/14498303)

### Company: Reltio
**Status:** Updated
**Summary:** **Reltio 2026.1.12.0 PRD Oct 9, 2026** introduces the **5th SAP-branded "SAP Reltio Velocity Pack" — Banking**, a standalone retail + commercial banking pack with banking product catalog, deposit/card/loan account types, bankers/branches/signers roles, due diligence, verification, risk and screening, household + ownership-and-control structures. Explicitly positioned as *different from* Reltio for Financial Services (wealth/advisory model). Promised time-to-value: 90 days. The release also adds **structural validation for materialized hierarchies** via APIs and **preserves hierarchy connections through merge/unmerge** using stored crosswalks. **2026.2 Preview Oct 16, GA Oct 23.**
**Why it matters:** Confirms the four SAP-branded Velocity Packs from Sept 25 were not a one-off — SAP-Reltio productised content for vertical SAP accounts is now a sustained biweekly release pattern. Banking is the first standalone industry pack *outside* Financial Services and signals Reltio widening the SAP channel beyond its historical FS footprint.
**Source:**
- [Reltio 2026.1 bi-weekly Release Notes — 2026.1.12.0 (Oct 9, 2026)](https://docs.reltio.com/en/reltio/release-notes-at-a-glance/2026.1-release-notes/2026.1-bi-weekly-release-notes-rn)
- [Release cadence and delivery schedule (2026.2 GA Oct 23)](https://docs.reltio.com/en/reltio/release-notes-at-a-glance/release-cadence-and-delivery-schedule)

### Company: Profisee
**Status:** New
**Summary:** **Sept 30, 2026 press release at Microsoft Fabric Community Conference Europe (Barcelona)**: **Profisee Anywhere** allows organizations to use Profisee's SaaS MDM to steward master data **natively inside Microsoft Fabric OneLake** — Profisee claims it is the only MDM platform where data is created, managed and governed over time *without ever leaving* Fabric OneLake. Paired with the existing certified Microsoft Fabric workload. Also announced: **Fabric SQL Database Connector** (ingest from Fabric SQL databases, publish mastered data back) **launching with the 26R3 release of the Profisee Platform the week of the conference**. **Profisee Anywhere GA December 2026.** Profisee delivered the free **virtual Data Hero Summit on Oct 8, 2026** (keynote by Malcolm Hawker: "trust = meaning + truth; MDM gets truth into the machine").
**Why it matters:** Profisee doubles down on the Microsoft stack as its primary AI distribution surface — "data never leaves Fabric" directly addresses governance concerns around moving data for AI/MDM and extends the Profisee MCP Server pattern of serving governed truth to any Microsoft Copilot / Claude / ChatGPT agent, now with Fabric-native storage.
**Source:**
- [Profisee Introduces Profisee Anywhere, Letting Organizations Manage Data Directly in Microsoft Fabric OneLake (Press release, Sept 30, 2026)](https://profisee.com/press-release/profisee-introduces-profisee-anywhere-letting-organizations-manage-data-directly-in-microsoft-fabric-onelake/)
- [2026 Data Hero Summit (Oct 8, 2026)](https://profisee.com/data-hero-summit/)

### Company: Pimcore
**Status:** Updated
**Summary:** **Pimcore Platform Version 2026.3.1 GitHub release on Oct 6, 2026** — maintenance release on top of 2026.3 with four security fixes (PDF scanner payload inspection, SQL validator desync in Custom Reports, document view permission enforcement on unpublished/preview access, generated model class description sanitization), a per-element-type version storage feature, storage-queue retry handling, focal-point cover-transformation fix and asset-upload version-skip option. **No new Agent Bundle, Datahub MCP or Pimcore Agent SDK changes.** Pimcore also delivered the **Oct 6 online panel "AI Agents in Data & Experience Management: Hype, Help, or Game Changer?"** hosted by Dietmar Rietsch with Arrabiata, Divante (Cloudflight), elbkapitäne, NETFORMIC, NSPYR, Strix and swoox.io — framed as separating hype from reality for AI agents in PIM / MDM / DAM / DXP / CDP / commerce.
**Why it matters:** Shows Pimcore's post-Tenzing cadence delivering security and operability on top of the 2026.3 MCP-final + native OAuth 2.0 server release the previous week; the partner panel is Pimcore's first collective implementation-partner message about agentic PIM/MDM under the new ownership.
**Source:**
- [Pimcore v2026.3.1 (GitHub release, Oct 6, 2026)](https://github.com/pimcore/pimcore/releases)
- [AI Agents in Data & Experience Management: Hype, Help, or Game Changer? (Oct 6, 2026)](https://pimcore.com/ai-agents-hype-help-game-changer)

### Company: Inriver
**Status:** Updated
**Summary:** **Oct 7, 2026 resource "How to solve your AI content control problem once and for all"** publishes a four-measure framework for governing AI-generated product content: (1) limit what the AI can change, (2) assign a decision owner, (3) add a verification step against trusted data, (4) keep an approval log before publication. Explicitly cites the McKinsey 2026 AI trust survey (~500 orgs — "nearly two-thirds cite security and risk concerns as the top barrier to fully scaling agentic AI"). Positions Inriver's agentic orchestration + verification/validation layer as the platform substrate: AI agents and LLMs run across content, e-commerce, data, and product-development workflows, with every product-data-based agentic workflow checked against trusted PIM data before any output reaches a channel. MCP-adjacent — the piece speaks to AI governance for product data without naming a specific protocol.
**Why it matters:** Extends Inriver's protocol-stack framing (ACP / UCP / MCP) with an operational control-plane message: PIM is where the verification layer lives. Direct competitive pressure on Stibo's own agent-governance narrative; Inriver is now first in the tracked set to publish a prescriptive AI-content-control checklist tied to a credible third-party survey.
**Source:**
- [How to solve your AI content control problem once and for all (Inriver resource, Oct 7, 2026)](https://www.inriver.com/resources/ai-content-control-problem/)

## 3. Notable Patterns

- **"Verified MCP servers only" becomes an explicit SAP policy.** SAP AI Agent Hub GA (Oct 1) restricts production invocation to MCP servers that have passed a formal verification workflow and automatically revokes access when verification status changes. This is the first large-vendor runtime gate on MCP in the tracked set and reframes "MCP support" as a governance *and* identity question, not only an integration one. Pimcore's 2026.3 native OAuth 2.0 server and Informatica's Secure MCP Gateway are the vendor-side analogues.
- **SAP's two-SKU MDM story continues to productise.** Reltio 2026.1.12.0 adds the 5th SAP-branded Velocity Pack (Banking) one week after the first four. The "SAP MDG at source + SAP Reltio for enterprise unification" architecture codified Sept 30 is now backed by weekly content releases, not just positioning.
- **Fabric OneLake becomes a competitive battleground for governed MDM.** Profisee Anywhere joins Reltio (Databricks Zero-Copy), Pimcore Embeddings (adapter-based providers), SAP Reltio (SAP BDC) and Informatica (Headless Data Management across every major cloud) in a cross-vendor race to put MDM/PIM state *inside* the customer's primary analytics / AI data store rather than beside it — governance posture matters because the data no longer moves.

## 4. No Relevant Updates

- **Informatica** — Sept 28 blog "Powering your Enterprise AI with Informatica Plugin for Claude" and Sept 25 Computer Weekly interview continue to be the latest primary content; no new MCP capability or press release in the Oct 2–9 window. MCP docs still cite protocol 2025-06-18 (ten weeks post-spec).
- **Akeneo** — No new primary-source press release this week; Sept 30 leadership appointments remain the latest. Follow-on coverage limited to Retail Technology Innovation Hub (Oct 1-2) already captured last week.
- **Salsify** — No new primary content; "AI in Salsify Part 3 — Powering Agentic Experiences" US airing is **Oct 27**. "What's New at Salsify? Q3 2026" webinar page is live but not yet dated for the Oct 2-9 window.
- **Syndigo** — Oct 1-2 DAM New York / PIM/PXM NYC Booth 38 + Vinny Maurici "How PIM Gets Products Chosen Across AI, In-Store Experiences, and Online" session delivered Oct 2; already covered in last week's report. No net new product news.

## 5. Suggested Follow-Up

- **Monitor whether SAP AI Agent Hub's "verified MCP servers only" rule becomes a buyer requirement in SAP accounts.** If it propagates, every tracked vendor's MCP server will need an SAP verification workflow entry — a potential moat for SAP-aligned vendors (SAP MDG, SAP Reltio) and a question Stibo should pre-empt.
- **Watch Reltio 2026.2 Preview (Oct 16) and GA (Oct 23).** With five SAP-branded Velocity Packs in six weeks, the headline 2026.2 release is likely where the full SAP-Reltio content portfolio consolidates — the key Reltio product milestone of Q4.
- **Review Profisee Anywhere against Stibo's own Fabric / Databricks / Snowflake story.** "MDM native inside the customer's primary data store" is becoming table stakes; consider whether Stibo's MCP messaging should emphasise *where governed data lives* as explicitly as it emphasises *how agents access it*.
