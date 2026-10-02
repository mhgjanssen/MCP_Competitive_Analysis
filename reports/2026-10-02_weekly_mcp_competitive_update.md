Subject: Weekly MCP Competitive Update – September 25, 2026 to October 2, 2026

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

## 1. Executive Summary

- **SAP officially discontinues the SAP BTP-based SAP Master Data Governance, cloud edition** (SAP Community blog, Sept 30). Future MDM footprint = SAP MDG on S/4HANA (central governance at source) + SAP Reltio (enterprise-wide unification) as two complementary components of SAP Business Data Cloud. First time SAP publicly ends a cloud MDG SKU and formally cedes the non-SAP unification role to Reltio.
- **Pimcore Platform Version 2026.3 GA (Sept 30)** promotes **Datahub Simple REST MCP support from beta to "final,"** turns Pimcore into a **native OAuth 2.0 server** for external AI agents, and ships an **embeddings-based semantic search / duplicate detection** service. Agent Bundle beta adds **headless Agent Tasks** and Workflow Engine integration.
- **Reltio 2026.1.11.0 PRD (Sept 25)** ships **four SAP-branded "SAP Reltio Velocity Packs"** (SAP S/4HANA, Mill Products & Mining, Retail, CPG) — the first productised SAP-branded content packs since the acquisition — plus exportable AgentFlow job record reports with full conversation transcripts.
- **Informatica's Dreamforce messaging kept amplifying** this week: Sept 28 primary blog "Powering your Enterprise AI with Informatica Plugin for Claude" and a Sept 25 Computer Weekly piece ("Informatica wants AI agents to stop making up the numbers") pushing trust indicators on every Claude answer.
- **Nine weeks post-spec, still zero MCP 2026-07-28 compatibility statements** across the tracked set. Pimcore's "Datahub Simple REST MCP support reaches final" is the week's closest native-MCP-stack GA event.

## 2. Key Updates This Week

### SAP MDG — New

**Summary:** The Sept 30 SAP Community blog "The Evolution of SAP Master Data Governance with SAP Business Data Cloud" (Andreas Seifried, SAP) formally announces the **discontinuation of the SAP BTP-based SAP Master Data Governance, cloud edition**: existing subscriptions honoured through contract end, no renewals, free tier withdrawn, phased out of BTPEA/CPEA/PayGo. SAP positions SAP MDG (S/4HANA, central governance at source) and SAP Reltio (enterprise-wide unification across SAP + non-SAP) as the two complementary MDM components inside SAP Business Data Cloud. SAP S/4HANA Cloud Private Edition and Public Edition are now the recommended MDG deployment targets.

**Why it matters:** SAP has publicly ceded the non-SAP unification role to Reltio and simplified its MDM story to a two-SKU architecture — materially sharpens the competitive frame Stibo Systems faces inside SAP accounts, especially for cross-system / non-SAP master-data use cases.

**Source:**
- [The Evolution of SAP Master Data Governance with SAP Business Data Cloud (SAP Community, Sept 30, 2026)](https://community.sap.com/t5/technology-blog-posts-by-sap/the-evolution-of-sap-master-data-governance-with-sap-business-data-cloud/ba-p/14492236)

### Pimcore — Updated

**Summary:** **Pimcore Platform Version 2026.3 GA (Sept 30, 2026)**. Three MCP / agent-relevant items: (1) **Datahub Simple REST MCP support reaches "final"** (previously beta); (2) **Pimcore evolves into a full OAuth 2.0 server built on existing Pimcore user accounts** — standardised authentication for external AI agents, chat assistants and MCP integrations without a separate identity layer; (3) **Pimcore Embeddings** — a new vector-embeddings service for images and textual metadata enabling **semantic search and duplicate / near-duplicate detection** across assets and data objects via an adapter-based provider model. **Pimcore Agent Bundle** stays beta but now supports **headless Agent Tasks** (external tools and integrations can delegate work to Pimcore Agent programmatically) and integrates with the Pimcore Workflow Engine. First post-Tenzing-majority-stake product release.

**Why it matters:** The combination of final MCP + native OAuth 2.0 + headless agent tasks + embeddings-powered semantic search gives Pimcore one of the most complete open-core PIM/MDM stacks for agent-ready, governed data access in the tracked set.

**Source:**
- [Pimcore Platform Version 2026.3: Faster Data Operations, Extensible Portals, and the Next Step Toward Intelligent PXM (Pimcore blog, Sept 30, 2026)](https://pimcore.com/en/resources/blog/pimcore-platform-version-2026-3)

### Reltio — Updated

**Summary:** **Reltio 2026.1.11.0 PRD Sept 25, 2026**. First release post-SAP close to productise SAP-branded content: **four new "SAP Reltio Velocity Packs"** — **SAP S/4HANA** (business partners, materials, finance), **Mill Products & Mining**, **Retail** (customers across channels, GS1 identifiers, SAP S/4HANA for Retail mappings), and **Consumer Packaged Goods** (GDSN publication, trade data). Each is a preconfigured data model with matching, survivorship and reference data so customers skip model build. AgentFlow-side: **downloadable job record reports** (CSV / JSONL) for automated long-running tasks, with optional per-record conversation transcript — closes the audit gap on long-running agentic jobs. Plus hierarchy integrity checks on entity merges and drag-and-drop node reorganisation. **2026.2 Preview rolls Oct 16, GA Oct 23.**

**Why it matters:** Velocity Packs convert the "Reltio, an SAP company" message into shrink-wrapped SAP-branded accelerators by industry — raises the bar in SAP-heavy accounts and formalises the MDG-vs-Reltio split codified by SAP this week.

**Source:**
- [2026.1 bi-weekly Release Notes (Sept 25, 2026)](https://docs.reltio.com/en/reltio/release-notes-at-a-glance/2026.1-release-notes/2026.1-bi-weekly-release-notes-rn)
- [Release cadence and delivery schedule (2026.2 GA Oct 23)](https://docs.reltio.com/en/reltio/release-notes-at-a-glance/release-cadence-and-delivery-schedule)

### Informatica — Updated

**Summary:** Two amplifications of the Dreamforce / Claude plugin story. (1) **Sept 28 Informatica blog "Powering your Enterprise AI with Informatica Plugin for Claude"** restates the plugin's architecture — reusable Catalog and Data Discovery Skill plus connectors to the **Informatica Secure MCP Gateway** fronting the **Catalog Discovery MCP** and **CLAIRE Data Exploration Agent MCP** — now listed on the Claude Plugin Marketplace, and framed as the fix for the Knowledge, Trust and Action gaps in enterprise AI. (2) **Sept 25 Computer Weekly piece "Informatica wants AI agents to stop making up the numbers"** (Pathak interview) emphasises **trust indicators attached to every data point Claude returns** — source, definitions, data quality, lineage (e.g. "did this come from Salesforce?") — as the differentiator vs vanilla model answers.

**Why it matters:** Reinforces Informatica's "proof-of-trust" positioning on top of its Claude-plugin / MCP play — a narrative Stibo should watch when framing governed MDM as a trust layer for agents, not just a data pipe.

**Source:**
- [Powering your Enterprise AI with Informatica Plugin for Claude (Informatica blog, Sept 28, 2026)](https://www.informatica.com/blogs/powering-your-enterprise-ai-with-informatica-plugin-for-claude.html)
- [Informatica wants AI agents to stop making up the numbers (Computer Weekly, Sept 25, 2026)](https://www.computerweekly.com/news/366650974/Informatica-wants-AI-agents-to-stop-making-up-the-numbers)

### Akeneo — Updated

**Summary:** **Sept 30, 2026 primary-source press release "Akeneo Continues to Invest in the Future of Commerce with Strategic Leadership Appointments"** — **Carole Offredo (ex-Dataiku, nearly a decade in enterprise-AI marketing) as CMO**, **Jean Lethuillier as VP Customer Success**, **Edouard Dewulf as Senior Director Global Center of Excellence**. Release explicitly ties the hires to the US expansion and the **next phase of agentic commerce**, cites the PricingHUB acquisition and Agentic Ziggy as the product foundation, and references top ranking in Info-Tech SoftwareReviews PIM Data Quadrant (July 2026) and Exemplary Vendor in ISG Buyers Guide 2026. MCP-adjacent (no new MCP capability).

**Why it matters:** Signals Akeneo is pivoting its go-to-market around enterprise AI buyers — a lift in the sales motion against which Stibo competes directly in product data for AI.

**Source:**
- [Akeneo Continues to Invest in the Future of Commerce with Strategic Leadership Appointments (Akeneo press release, Sept 30, 2026)](https://www.akeneo.com/press-release/akeneo-continues-to-invest-in-the-future-of-commerce-with-strategic-leadership-appointments/)
- [Retail Technology Innovation Hub coverage (Oct 2, 2026)](https://retailtechinnovationhub.com/home/2026/10/1/focus-on-ai-as-product-experience-specialist-akeneo-announces-three-senior-executive-appointments)

### Syndigo — Updated

**Summary:** **Sept 28 Syndigo blog "AI Shopping, Tariffs & the Holiday Retail Challenge"** (Tarun Chandrasekhar, President & CPO) argues shoppers now ask AI first and never see a retailer's page if the product-data feed is stale — collapses tariff-driven supplier swaps and AI-assistant answers onto the same clock. **Oct 1–2 at DAM New York / PIM/PXM NYC**: Syndigo exhibiting Booth 38 and running an exclusive Oct 1 PIM / Digital Commerce Leaders dinner at TAO Uptown; **Oct 2 PIM/PXM NYC session with Vinny Maurici — "How PIM Gets Products Chosen Across AI, In-Store Experiences, and Online."** MCP-adjacent — reinforces governed PIM as prerequisite for AI assistants.

**Why it matters:** First US east-coast on-the-ground push into DAM / PIM leader audiences since GS1 Connect in June; keeps Syndigo in the "AI needs well-governed PIM" narrative without adding net new MCP capability.

**Source:**
- [AI Shopping, Tariffs & the Holiday Retail Challenge (Syndigo blog, Sept 28, 2026)](https://syndigo.com/blog/holiday-retail-ai-shopping-tariffs-product-data/)
- [Meet Syndigo at DAMNYC & PIM/PXM NYC (Oct 1–2, 2026)](https://syndigo.com/events/damnyc-pim-pxm-nyc-2026/)

### Salsify — Updated (minor)

**Summary:** **Sept 30, 2026 at 3 PM GMT**: Europe airing of **"AI in Salsify Part 3 — Powering Agentic Experiences"** — final session in the three-part agentic-commerce readiness series, focused on **federating product data to AI agents and shopping bots** so brands are understood and recommended at the moment of agent-driven purchase. No net new MCP capability disclosed on the webinar page; extends the MCP-adjacent positioning anchored on Salsify's first-party remote MCP server.

**Why it matters:** Closes Salsify's three-part agentic-commerce campaign; sets up the "What's New at Salsify? Q3" roadmap push expected later in October.

**Source:**
- [AI in Salsify Part 3 — Europe (Sept 30, 2026)](https://www.salsify.com/resources/webinar/ai-in-salsify-a-practical-playbook-for-agentic-commerce-readiness-europe)

## 3. Notable Patterns

- **SAP's two-SKU MDM story is now explicit:** MDG at the SAP source + Reltio for cross-system unification, with the BTP-based MDG cloud edition retired — pairs cleanly with Reltio's new SAP-branded Velocity Packs the same week.
- **"Final" / "GA" MCP milestones are starting to appear in product releases without any 2026-07-28 compatibility statement:** Pimcore's Datahub Simple REST MCP reaching "final" is the second such GA event in a month (after SAP CAP MCP Adapter GA in September). Nine weeks post-spec, the tracked set still has zero explicit MCP 2026-07-28 compatibility statements.
- **Native OAuth 2.0 as the AI-agent authentication layer is now a competitive feature:** Pimcore 2026.3 explicitly builds OAuth 2.0 server capability on top of existing user accounts for MCP and third-party AI agents, mirroring SAP Integration Suite MCP Gateway's OAuth 2.0 / OIDC posture — vendor-side consensus that identity is the real gating control for agent access to master data.

## 4. No Relevant Updates

- Profisee — only promotion of the virtual Data Hero Summit on Oct 8, 2026; no new product / MCP news this week.
- Inriver — Sept 25 incremental community release notes cover import UX / mapping bugfixes only; no new MCP endpoints or agent capabilities.

## 5. Suggested Follow-Up

- Monitor the SAP MDG discontinuation announcement for customer-communications fallout and watch whether SAP / Reltio publish a joint migration or "legacy MDG BTP → Reltio" play — this is the week's most consequential competitive signal.
- Review Pimcore 2026.3 (final MCP + native OAuth 2.0 server + embeddings) alongside Stibo's MCP messaging; consider whether Stibo should emphasise its own identity / governance story for agent access more explicitly.
- Watch the Oct 16 Preview / Oct 23 GA of Reltio 2026.2 for a formal 26.2 announcement — likely the headline Reltio product milestone of Q4.
