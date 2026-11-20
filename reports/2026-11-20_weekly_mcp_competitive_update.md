# Weekly MCP Competitive Update — November 13, 2026 to November 20, 2026

**To:** mjan@stibosystems.com
**Subject:** Weekly MCP Competitive Update – November 13, 2026 to November 20, 2026

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

## 1. Executive Summary

- **Microsoft Ignite 2026 (Nov 17–21, San Francisco) was the dominant catalyst.** In five days, Informatica, Syndigo, Profisee, Reltio and SAP all pushed Microsoft-centric MCP / agent announcements — making Microsoft Foundry and Copilot the most visible shared surface for MDM/PIM MCP servers this quarter.
- **Syndigo MCP crossed from read-only to full write.** Microsoft Copilot (or any MCP assistant) can now create, update and enrich products in Syndigo PX Cloud, PIM, MDM and Syndication, validate against ~4,000 retailer requirements, and route every change through human approval — the first explicit write-capable MCP server in the PIM/PXM set beyond Reltio.
- **Informatica Headless MCP servers are GA in Microsoft Foundry** (Foundry Tools Catalog) with new governance, identity and administrative capabilities, and Informatica is now also reachable from Microsoft Copilot and Teams in natural language — the Microsoft counterpart to Informatica's Oracle Select AI integration announced in October.
- **Reltio 2026.2.2.0 went to production Nov 20** with the Data Explorer autonomous agent embedded directly inside Hub (floating / sidebar / full-screen) and task-level credit metering for long-running autonomous-agent jobs — continuing Reltio's move from "MCP you plug in" to "MCP you can audit, meter and schedule."
- **Profisee reframed its December GA around Microsoft's data-governance pivot**, positioning Profisee Anywhere's OneLake-native MDM as the master-data layer of Microsoft's newly-strategic OneLake catalog (following the retirement of Purview Data Governance) — effectively re-staking the Microsoft-Fabric-governed-MDM battleground against Syndigo's fresh Global ISV alliance.

## 2. Key Updates This Week

### Company: Informatica
**Status:** New
**Summary:** On Nov 17, 2026 Salesforce and Informatica jointly announced an expanded Microsoft collaboration: Informatica Headless MCP servers are now **generally available in Microsoft Foundry** (listed in the Foundry Tools Catalog) with new governance, identity and administrative capabilities for Foundry agents; a new integration brings Informatica catalog, data quality, governance and lineage into **Microsoft Copilot and Teams** via natural language for business users; Fabric scanning and lineage now cover notebooks and pipelines; and a new U.S. East Coast Azure POD expands deployment choice. A technical walkthrough blog by Ajay Gollapalli details which Informatica MCP servers (CDGC Metadata Search, CDQ, CDI, Address Verification, Customer Identification MDM, Job Management, Data Provisioning, CLAIRE Data Exploration) are exposed as Foundry tools, with Entra app registration and group-based access as the admin pattern.
**Why it matters:** Puts Informatica on both of the two dominant hyperscaler MCP surfaces (Microsoft Foundry + Oracle Select AI) in under a month and raises the governance/identity bar — Foundry-side admin + Entra-group access is the pattern Stibo's own MCP positioning will increasingly be measured against.
**Source:**
- [Informatica from Salesforce brings Trusted Enterprise Data into Microsoft Copilot, Microsoft Foundry, and Microsoft Fabric (Salesforce newsroom, Nov 17, 2026)](https://www.salesforce.com/news/stories/informatica-trusted-enterprise-data-microsoft-collaboration/)
- [Informatica MCP for Microsoft Copilot and Foundry — Ajay Gollapalli (Informatica blog, Nov 17, 2026)](https://www.informatica.com/blogs/informatica-mcp-copilot-foundry.html)

### Company: Syndigo
**Status:** New
**Summary:** At Microsoft Ignite on Nov 18, 2026, Syndigo announced **expanded Syndigo MCP server capabilities** that let Microsoft Copilot (or any MCP-compatible assistant) create, update and enrich products in Syndigo PX Cloud, PIM, MDM and Syndication by conversation — explicitly moving beyond read-only. The agent can build a product record end-to-end, write marketing copy, validate the product against ~4,000 retailer-specific requirements, fix what's missing and show per-retailer readiness; every proposed change is shown next to the current data and nothing is saved until a human approves it. The Syndigo MCP acts as the signed-in user with that user's existing permissions and tenant isolation. CPO Tarun Chandrasekar's Nov 19 companion blog frames this as "agentic PXM with human ambition," positioning Syndigo as the "trusted data accountability layer" under Microsoft Frontier Commerce.
**Why it matters:** First explicit write-capable MCP server in the broader PIM/PXM set besides Reltio, operationalises the Nov 2 Microsoft Global ISV alliance in under three weeks, and directly reframes the Syndigo ↔ Profisee Microsoft-Fabric battleground around end-to-end agentic syndication, not just Fabric placement.
**Source:**
- [Syndigo Helps Brands and Retailers Get Products to Market Faster with Microsoft Copilot (GlobeNewswire, Nov 18, 2026)](https://www.globenewswire.com/news-release/2026/11/18/3405735/0/en/syndigo-helps-brands-and-retailers-get-products-to-market-faster-with-microsoft-copilot.html)
- [The Most Important Ingredient in AI Commerce Is Human Ambition — Tarun Chandrasekar (Syndigo blog, Nov 19, 2026)](https://syndigo.com/blog/human-ambition-ai-commerce/)

### Company: Profisee
**Status:** New
**Summary:** On Nov 18, 2026 at Microsoft Ignite, Profisee issued a new Profisee Anywhere press release that reaffirms December 2026 GA and adds fresh Microsoft-governance framing: following Microsoft's announcement that it will retire Purview Data Governance and make **OneLake catalog its strategic foundation for data governance**, master data mastered with Profisee Anywhere is automatically part of OneLake catalog. Profisee is "working with Microsoft to deepen its OneLake catalog integration." Golden records live in a Fabric SQL database inside the customer's own tenant; Fabric IQ and Fabric ontologies can consume them directly; stewards can work in the Profisee portal or Profisee's Fabric-native workload. The Profisee MCP Server for Copilot / Claude / ChatGPT is unchanged.
**Why it matters:** Re-anchors Profisee's December GA to Microsoft's post-Purview governance pivot — a positioning counter-move against Syndigo's new Microsoft alliance and a reminder that the Microsoft-Fabric-governed-MDM surface now has two serious MDM vendors competing for the same control plane.
**Source:**
- [Profisee Brings Real-Time Master Data Management Natively to Microsoft Fabric with Profisee Anywhere (Profisee press release, Nov 18, 2026)](https://profisee.com/press-release/profisee-brings-real-time-master-data-management-natively-to-microsoft-fabric-with-profisee-anywhere/)

### Company: Reltio
**Status:** New
**Summary:** Reltio **2026.2.2.0 shipped to production on Nov 20, 2026** (DEV/TEST Nov 17). Two MCP-material additions: (1) the **Data Explorer autonomous agent is now embedded inside Hub** as a floating window, right-side panel or full-screen workspace, so stewards can query master-data context without leaving a record or dashboard; (2) **task-level credit usage monitoring for autonomous agents** adds per-long-running-task and per-job credit consumption to the Usage billing dashboard, filterable by agent and tenant. Access-control plumbing also tightens: interaction types now require READ permission to be returned by the Configuration API. At Microsoft Ignite session ODSP2207, Reltio demonstrated a Microsoft Foundry agent workflow calling the Reltio MCP server for master-data context on top of a Contoso Manufacturing duplicate-record case.
**Why it matters:** Reltio keeps extending the programmable control plane around its MCP server (after Nov 6's CU/LRT/custom-instructions APIs) and ships one of the first embedded MCP-backed steward agents directly inside an MDM workbench — raising the bar for in-context, governed master-data agents and giving SAP BDC customers a visible Microsoft-Foundry proof point.
**Source:**
- [2026.2 Bi-weekly Release Notes — 2026.2.2.0 (Reltio docs)](https://docs.reltio.com/en/reltio/release-notes-at-a-glance/2026.2-release-notes/2026.2-bi-weekly-release-notes-rn)
- [Give AI Agents Data They Can Trust — ODSP2207 (Microsoft Ignite 2026 session, Reltio × Microsoft Foundry MCP demo)](https://tech.hub.ms/ml/videos/give-ai-agents-data-they-can-trust-odsp2207)

### Company: Inriver
**Status:** New
**Summary:** The **Inriver November 2026 Product Release** (published Nov 18, 2026) introduces the new **Inspire Review Agent** — an AI agent that checks selected PIM fields against guidelines the customer defines (brand voice, compliance, quality, translation accuracy, fact-checking or a custom review type) and returns a percentage score, a Pass / Needs Review / Fail verdict, a summary, and a ranked list of issues plus recommendations. Results are stored in PIM fields so the next workflow step can route the record to an Inspire Agent for automatic fixing or to a human reviewer. Review Agent runs on Inriver's visual workflow builder and requires Inspire plus Inriver Workflows. The release also adds automated content-gap research from manufacturer websites and public PDFs, AI mapping suggestions in Syndicate Advance, and EU AI Act preparation (AI watermarking, content credentials, automatic marking of AI-generated content).
**Why it matters:** First productised, workflow-triggered quality agent in the PIM set with an explicit verdict-and-trace output shape — MCP-adjacent (no MCP terminology), but it is the clearest "agent returns an auditable judgement that another agent or human acts on" pattern to appear in Inriver's platform and the first vendor in the set to pre-stage EU AI Act transparency features.
**Source:**
- [November 2026 Product Release: Faster, Smoother Everyday Work, and AI That Applies Your Rules (Inriver Community, Nov 18, 2026)](https://community.inriver.com/hc/en-us/articles/31859162701468-November-2026-Product-Release-Faster-Smoother-Everyday-Work-and-AI-That-Applies-Your-Rules)

### Company: SAP MDG
**Status:** Updated
**Summary:** The Nov 17, 2026 Microsoft Community Hub blog "Microsoft and SAP at Ignite 2026" clarifies the operational state of the SAP ↔ Microsoft agent surface: **SAP AI Agent Hub and Microsoft Agent 365 are moving toward agents that can be discovered, registered, governed and observed across both environments** through SAP's agent gateway capabilities and Microsoft Copilot Studio. SAP tabular foundation predictive models (TabFM) are available in Microsoft Foundry. Customers without Joule can connect Microsoft 365 Copilot to SAP ERP, RISE with SAP, S/4HANA and ECC via **MCP servers and Copilot skills**, hosted either on SAP BTP or Azure API Management, aligned with SAP's API policy. Azure Workload Center for SAP enters limited preview with an Azure Copilot Run SAP Agent. A separate Nov 11 SAP Community TechEd debrief (Rene Pfeufer) confirms that **SAP MDG + SAP Reltio as a native MDM component of SAP Business Data Cloud is on track for Q1 2027 GA**, with capacity-unit procurement between MDG and Reltio inside BDC.
**Why it matters:** Confirms a two-way governance bridge between SAP's and Microsoft's agent control planes without SAP conceding exclusivity — and makes clear that the SAP-native MCP path for MDG master data now runs through either SAP BTP or Azure API Management, not just Joule.
**Source:**
- [Microsoft and SAP at Ignite 2026: Connecting SAP customers to AI agents, data, and security (Microsoft Community Hub, Nov 17, 2026)](https://techcommunity.microsoft.com/blog/sapapplications/microsoft-and-sap-at-ignite-2026-connecting-sap-customers-to-ai-agents-data-and-/4573931)
- [SAP TechEd 2026: The MDM and Data Governance Conversation (SAP Community, Rene Pfeufer)](https://community.sap.com/t5/data-and-ai-professionals-blog-posts/sap-teched-2026-the-mdm-and-data-governance-conversation/ba-p/14520021)

### Company: Salsify
**Status:** Updated
**Summary:** On Nov 18, 2026 Salsify published **"Product Data Is the Bottleneck: How Manufacturers Clear It to Grow"** (Mandy Earle + Peter Crosby), introducing a **four-component intelligent-PIM architecture** — System of Record (governed product data), System of Action (AI-powered enrichment at scale), System of Delivery (distribution plus "access for any agent"), and System of Intelligence (continuous learning). The paper cites Deloitte ("nearly 40% of B2B buyers already use agentic AI to make purchasing decisions, while only 24% of suppliers have agents on the sell side to meet them"), Distribution Strategy Group (industry-wide product-data completeness 51.3%), and Gartner (30% of routine sales negotiations handled by AI agents by 2028). The same day Salsify delivered its Q4 "What's New at Salsify: Into 2027" webinar previewing early-2027 roadmap.
**Why it matters:** Salsify is anchoring its B2B / industrial-manufacturer narrative (the segment Gartner flagged as its Caution) to agent-accessible product data — MCP-adjacent (no explicit MCP mention in this paper), but the "access for any agent" positioning is the clearest signal yet that Salsify intends to catch up on the write-side MCP surface Syndigo just extended.
**Source:**
- [New Salsify Research: Product Data Is the Bottleneck. Machine Speed Is the Fix. (Salsify / GlobeNewswire, Nov 18, 2026)](https://www.globenewswire.com/news-release/2026/11/18/3405572/0/en/new-salsify-research-product-data-is-the-bottleneck-machine-speed-is-the-fix.html)
- [What's New at Salsify: Into 2027 — Q4 2026 webinar (Nov 18, 2026)](https://www.salsify.com/resources/webinar/whats-new-at-salsify-q4-2026)

### Company: Akeneo
**Status:** Updated
**Summary:** A new Akeneo whitepaper **"The Agentic PIM Playbook"** (coverage first surfaced Nov 16, 2026 via ChannelX) argues that "your first agent is a use case; your tenth is an operating model," and identifies ten agents across the product lifecycle (modelling, supplier data, enrichment, content creation, localisation, asset intelligence, quality/compliance, activation, market intelligence, insights). Five required foundations: trusted product data, business context and repeatable intelligence, human expertise in the loop, channel intelligence, and trust/traceability/authority. Four shared capabilities: agents work from the same governed product record, tasks and approvals follow the correct sequence, taxonomies and policies are governed by shared rules, and every change is traceable. The companion Autumn Release 2026 live walkthrough webinar was delivered on Nov 18.
**Why it matters:** Positions Akeneo as the PIM vendor framing multi-agent governance ("ten agents, one operating model") as the real differentiator over single-agent demos — MCP-adjacent and directly relevant to how Stibo's own MCP messaging treats fleets of agents rather than a single assistant.
**Source:**
- [The AI agent boom is creating a new product data challenge for retailers — Akeneo "Agentic PIM Playbook" (ChannelX, Nov 16, 2026)](https://channelx.world/2026/11/the-ai-agent-boom-is-creating-a-new-product-data-challenge-for-retailers/)
- [Akeneo Autumn Release 2026 webinar (live walkthrough, Nov 18, 2026)](https://pages.akeneo.com/akeneo-autumn-release-2026-webinar-registration.html)

### Company: Pimcore
**Status:** Updated
**Summary:** **Pimcore Platform v2026.3.6 shipped Nov 17, 2026** — a maintenance release (DataObject lazy-relation performance, admin-translation scan, system-settings caching, EPS asset dimensions, video-thumbnail tmp-file race, workflow support strategy, PHPStan 2.3.5). The Pimcore Agent Bundle and Datahub Simple REST MCP server shipped no new features this week, although the underlying `Pimcore\Contracts\PimcoreAgent` namespace (introduced earlier in 2026.3) plus the `InitiatorMcpServerResolverInterface` resolver pattern continue to stabilise so downstream bundles can depend on the agent-task facade without coupling to the Agent Bundle implementation. No Pimcore-authored MCP blog or release note this week.
**Why it matters:** Pure platform-hardening week; no fresh MCP messaging. Keeps Pimcore's agent surface (released as "final" Datahub Simple REST MCP + beta Agent Bundle in 2026.3 Sept 30) stable while competitors push new Microsoft-Foundry announcements — worth monitoring whether Pimcore produces a response to the Ignite wave.
**Source:**
- [Pimcore v2026.3.6 release notes (GitHub, Nov 17, 2026)](https://github.com/pimcore/pimcore/releases/tag/v2026.3.6)

## 3. Notable Patterns

- **Microsoft Ignite is now the single biggest MCP-launch surface for enterprise MDM/PIM vendors.** In one week Informatica (Foundry GA + Copilot/Teams), Syndigo (write-capable MCP via Foundry), Profisee (OneLake-catalog-native MDM), Reltio (Foundry agent demo), and SAP (dual-control-plane with Agent 365 via MCP servers on BTP or Azure API Management) all shipped Microsoft-centric MCP/agent announcements — a stronger collective moment than SAP TechEd.
- **MCP writes are becoming the new table-stakes.** Syndigo's shift from read-only to full create/update/enrich with HITL joins Reltio's autonomous agents in writing to master data through MCP, and Informatica's Foundry MCP includes Data Provisioning and Job Management. Read-only MCP is beginning to look like a lagging capability rather than a safe default.
- **Microsoft's data-governance pivot (Purview Data Governance retirement, OneLake catalog as strategic foundation) is reshaping the governed-MDM battleground.** Profisee Anywhere's OneLake-catalog integration and Syndigo's Microsoft Global ISV alliance now compete on the same control plane, and Informatica's Fabric scanning/lineage expansion to notebooks + pipelines lands in the same week — a three-way Microsoft-Fabric contest Stibo should expect to intensify into NRF 2027.

## 4. No Relevant Updates

- No companies in the covered set had zero relevant activity this week — Microsoft Ignite drew every vendor into at least an "Updated" entry.

## 5. Suggested Follow-Up

- Pressure-test Stibo Systems' MCP positioning against the **"write-capable, HITL-approved, retailer-rule-aware"** standard Syndigo just set on the Microsoft Foundry + Copilot surface, and against Informatica's Foundry-admin + Entra-group-access pattern.
- Review whether Stibo Systems should publish an explicit position on the **Microsoft OneLake catalog + Fabric-governed-MDM** surface before NRF 2027, now that Profisee has re-anchored its December GA to Microsoft's post-Purview governance pivot and Syndigo has taken the Microsoft Global ISV slot.
- Track Reltio 2026.2.3.0 (next bi-weekly, mid-December), Profisee Anywhere GA (December 2026), and Informatica's Dec 1 Tech Tuesday "Context and Trust in Any UI: Augmenting Your Data and AI with Informatica MCP" + Dec 15 "A Deep Dive into Governance & Data Quality MCPs" — three near-term catalysts that may extend this quarter's MCP write-plane / governance-plane expansion.

*Automated weekly MCP competitive intelligence digest. Sources are cited inline; classifications (New / Updated) are computed against the previous baseline.*
