# Weekly MCP Competitive Update — October 23, 2026 to October 30, 2026

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

## 1. Executive Summary

- **SAP TechEd Berlin (Oct 27–29) delivers the biggest MCP announcement of the quarter.** New **SAP Enterprise AI Gateway** (premium offering on SAP Business AI Platform) becomes the centralized control plane for AI traffic — MCPs, APIs, A2A and LLMs — with unified authentication, policy enforcement, routing, monitoring, usage tracking and auditing. Developers can discover and subscribe to MCP servers from any provider from one place. Joule Work gets agentic thinking + n8n workflow triggers; SAP Knowledge Graph extends to customer-specific SAP and non-SAP data; a new AI Governance Assistant addresses the EU AI Act.
- **SAP Reltio is now Generally Available inside SAP Business Data Cloud** (Oct 29 SAP News Center). Multi-domain MDM is now natively part of the SAP business data fabric alongside SAP MDG for S/4HANA — Reltio's AI-based entity resolution unifies SAP and non-SAP records into 360-degree profiles for Joule and third-party agents.
- **Informatica adds a second MCP distribution channel this week.** Its **Headless Data Management Catalog Discovery MCP is now available as a trusted semantic source directly within Oracle Select AI** (Oracle Database 26ai), showcased with Oracle at Oracle AI World Las Vegas (Oct 26–28). Same week, the Oct 27 Tech Tuesday delivered the **Customer Identification MCP Server for MDM SaaS** (with a new composite MDM-Provenance server adding `get_master_record_sources` / `get_master_field_provenance` / `get_source_record`) — bringing the Informatica native MCP catalog to **20 shared servers plus composite**.
- **Reltio 2026.2 continues to roll out post-GA.** The **Integrated Development Experience** (AI-powered VS Code + Cursor extension) GA'd Oct 30 with workflow and Life Cycle Action (LCA) authoring; the first bi-weekly 2026.2.1.0 (DEV/TEST Oct 30, PRD Nov 6) adds **Capacity Unit usage monitoring for autonomous agents provisioned through SAP BDC** and **APIs for managing long-running tasks**. Oct 29 Reltio Community Show walked customers through Unstructured search architecture (50 GB knowledge bases, 25 per tenant, S3 / Google Drive / Azure sources, playground tuning).
- **No MCP 2026-07-28 compatibility statements yet from the tracked nine** (thirteen weeks post-spec). "Autonomous enterprise" messaging continues to converge: SAP, Reltio, Profisee, Informatica all now use autonomous-agent language in their current product pages.

## 2. Key Updates This Week

### SAP MDG — New
**Summary:** SAP TechEd Berlin (Oct 27–29) delivered a dense MCP-focused week. The Oct 27 press release *"SAP Empowers AI Developers to Build What Matters and Turn Intent into Autonomous Execution"* introduces **SAP Enterprise AI Gateway** — a premium offering on SAP Business AI Platform that becomes the single control plane for AI traffic (MCPs, APIs, A2A, LLMs) with consolidated auth / policy / routing / monitoring / usage tracking / auditing. Developers get a consistent interface for discovering and subscribing to third-party MCP servers and reusing existing APIs/integration flows as agent-ready capabilities. Joule Work adds agentic thinking (multistep workflow planning) and the ability to trigger deterministic n8n workflows; **SAP Knowledge Graph** now ingests customer-specific SAP and non-SAP data for natural-language querying; a new **AI Governance Assistant** targets EU AI Act compliance. In parallel, the Oct 29 SAP News Center feature on SAP Lakehouse / Data Fabric innovations in SAP BDC announces **native Apache Iceberg + Apache Polaris catalog**, **Dremio-powered federated zero-copy querying** (across Databricks, Snowflake, Google, AWS, Microsoft, plus SQL Server / MongoDB / Oracle / Postgres), the new **BDC Ontology Manager** AI-native authoring experience, and the new **SAP-RPT-2.0** tabular foundation model.

**Why it matters:** SAP Enterprise AI Gateway is the first vendor-controlled governed MCP distribution layer in the tracked set that explicitly accepts third-party MCP servers on equal footing. Combined with Oct 27 confirmation that **SAP Reltio is GA inside SAP BDC**, SAP has now shipped both the governance control plane (Agent Hub + Enterprise AI Gateway) and the unification data plane (MDG + Reltio) for the autonomous enterprise narrative.

**Source:**
- [SAP News — "SAP Empowers AI Developers to Build What Matters and Turn Intent into Autonomous Execution" (Oct 27, 2026)](https://www.prnewswire.com/news-releases/sap-empowers-ai-developers-to-build-what-matters-and-turn-intent-into-autonomous-execution-302920376.html)
- [SAP News Center — "Advancing SAP Lakehouse and New Data Fabric Innovations in SAP BDC for the Autonomous Enterprise" (Oct 29, 2026)](https://news.sap.com/2026/10/sap-lakehouse-new-data-fabric-innovations-sap-bdc-autonomous-enterprise/)
- [SAP Community — "Introducing SAP Enterprise AI Gateway: Control and Visibility Across Agents" (SAP TechEd 2026)](https://community.sap.com/t5/technology-blog-posts-by-sap/introducing-sap-enterprise-ai-gateway-control-and-visibility-across-agents/ba-p/14510567)
- [SAP TechEd Innovation News Guide 2026](https://www.sap.com/topics/events/teched/innovation-news-guide-2026)
- [SiliconANGLE — "SAP advances its autonomous enterprise push with smarter, governed Joule agents" (Oct 27, 2026)](https://siliconangle.com/2026/10/27/sap-advances-its-autonomous-enterprise-push-with-smarter-governed-joule-agents/)

### Reltio — Updated
**Summary:** Three concurrent moves this week. First, **SAP Reltio is now Generally Available inside SAP BDC**, confirmed by the Oct 29 SAP News Center feature: Reltio brings AI-based entity resolution and multi-domain master data management natively into the business data fabric, complementing SAP MDG (MDG = central governance at the SAP source; Reltio = enterprise-wide unification across SAP and non-SAP). Second, the **Integrated Development Experience** — AI-powered VS Code + Cursor extension — **GA'd Oct 30** with support for **workflows (BPMN visualisation + live validation + deploy history)** and **Life Cycle Actions (LCA code generated from AI prompts, deployed to the customer's own AWS / GCP / Azure)**. Third, bi-weekly **2026.2.1.0** rolled to DEV/TEST Oct 30 (PRD Nov 6): **CU-usage monitoring for autonomous agents provisioned through SAP BDC** (so SAP BDC customers can track agent-run consumption in the shared SAP Capacity Unit pool), and **APIs for managing long-running tasks** (discover published agents, schedule recurring agent runs, trigger / monitor jobs, retrieve per-entity results at scale). The Oct 29 Reltio Community blog on **Unstructured search** fleshes out the Oct 23 GA with concrete architecture (ingest / index / retrieve / cite pipeline, S3 / Google Drive / Azure sources, PDF / Word / HTML / PowerPoint / Markdown / CSV formats, up to 50 GB per knowledge base and 25 per tenant, licensing via Reltio context intelligence + autonomous agentic licenses).

**Why it matters:** Reltio now has three live distribution channels — standalone, inside SAP BDC, and embeddable in third-party IDEs via the GA developer extension. SAP BDC CU-based consumption monitoring is the first vendor-grade enterprise-billing primitive built around MCP-driven autonomous agents in the tracked set.

**Source:**
- [SAP News Center — "Advancing SAP Lakehouse and New Data Fabric Innovations in SAP BDC" (Oct 29, 2026) — SAP Reltio GA in SAP BDC](https://news.sap.com/2026/10/sap-lakehouse-new-data-fabric-innovations-sap-bdc-autonomous-enterprise/)
- [Reltio Docs — 2026.2.1.0 Bi-weekly Release Notes (DEV/TEST Oct 30, PRD Nov 6, 2026)](https://docs.reltio.com/en/reltio/release-notes-at-a-glance/2026.2-release-notes/2026.2-bi-weekly-release-notes-rn)
- [Reltio Docs — 2026.2 Major Release Notes (Integrated development experience GA Oct 30, 2026)](https://docs.reltio.com/en/reltio/release-notes-at-a-glance/2026.2-release-notes/2026.2-major-release-notes)
- [Reltio Community — "Community Show: Unstructured search: Smarter data, smarter decisions" (Oct 29, 2026)](https://community.reltio.com/blogs/sara-brams-miller/2026/10/29/community-show-unstructured-search)

### Informatica — Updated
**Summary:** Two MCP-explicit moves inside one week. First, Oct 27 Informatica blog by Rob Cornell *"Informatica Headless + Oracle Select AI: Enterprise-Wide Business Context for Oracle Database Customers"* announces that Informatica's **Headless Data Management Catalog Discovery MCP is now a trusted semantic source directly inside Oracle Select AI** (built into Oracle Autonomous AI Database on Oracle Database 26ai). Select AI pulls governed CDGC glossary / term / asset definitions at prompt time, so natural-language queries resolve to consistent, auditable SQL with the catalog context exposed for human review. Showcased live with Oracle at Oracle AI World Las Vegas (Oct 26–28). Second, the Oct 27 Tech Tuesday *"Bridging AI Assistants with Verified Master Records"* (Ankit Tripathi) delivered the **Customer Identification MCP Server for MDM SaaS**, with two first-party tools (`search_master_record` fuzzy identity search; `get_master_record_details`) plus a new **composite MDM-Provenance server** adding `get_master_record_sources`, `get_master_field_provenance` and `get_source_record` — making the pattern "answer who it is + prove why to trust it". The webinar also confirms the native Informatica MCP catalog now numbers **20 shared / managed servers** across Customer & Data, Governance & Catalog, and Operate IDMC — plus customer-built composite servers.

**Why it matters:** This is the first week MCP shows up as both a *distribution* channel (Oracle Database 26ai) and as a *provenance* layer (Informatica composite MDM-Provenance server) — i.e. the vendor is answering buyer concerns about trust and auditability of agent answers at the same time it widens the install-base reach.

**Source:**
- [Informatica blog — "Informatica Headless + Oracle Select AI: Enterprise-Wide Business Context for Oracle Database Customers" (Rob Cornell, Oct 27, 2026)](https://www.informatica.com/blogs/informatica-headless-oracle-select-ai-enterprise-wide-business-context-for-oracle-database-customers.html)
- [Informatica Success Portal — Tech Tuesdays: "Bridging AI Assistants with Verified Master Records: Exploring the Customer Identification MCP Server for MDM SaaS" (Oct 27, 2026)](https://success.informatica.com/explore/tt-webinars/bridging-ai-assistants-with-verified-master-records--exploring-t.html)
- [Informatica Docs — Customer Identification MCP Server (shared server reference)](https://docs.informatica.com/claire/mcp-servers/current-version/getting-started-with-informatica-mcp-servers/shared-mcp-servers/customer-identification-server.html)
- [Informatica Tech Tuesday slides PDF — Customer Identification MCP + MDM-Provenance composite server (Oct 27, 2026)](https://success.informatica.com/content/dam/informatica-cxp/techtuesdays-slides-pdf/Bridging%20AI%20Assistants%20with%20Verified%20Master%20Records%20Exploring%20the%20Customer%20Identification%20MCP%20Server%20for%20MDM%20SaaS.pdf)

### Pimcore — Updated
**Summary:** **Oct 28 Pimcore blog by Ashley Laing (VP North America) — "Automated Cut Sheets for Building Products: Why the PDF Is Always Out of Date."** Positions PIM-driven, automatically-regenerated cut sheets as the core governance play for building-products manufacturers: the PDF rebuilds itself from the golden product record so finishes, dimensions, images and certifications can never drift from the live catalog. No new MCP, Agent Bundle or Datahub release in the Oct 23–30 window (last platform release was 2026.3.3.1 on Oct 22).

**Why it matters:** MCP-adjacent at most — governed-data-as-source-of-truth messaging without explicit MCP terminology. Noted mostly to confirm Pimcore stays on the "data must be clean before AI can act on it" narrative established by the Oct 19 Visionary blog, now pushed into a specific vertical (building products / cut sheets).

**Source:**
- [Pimcore blog — "Automated Cut Sheets for Building Products: Why the PDF Is Always Out of Date" (Ashley Laing, Oct 28, 2026)](https://pimcore.com/en/resources/blog/automated-cut-sheets-for-building-products-why-the-pdf-is-always-out-of-date)
- [Pimcore GitHub releases (no 2026.3.4 or 2026.3.3.2 yet in the Oct 23–30 window)](https://github.com/pimcore/pimcore/releases)

### Salsify — Updated
**Summary:** The **Oct 27 US Part 3 of "AI in Salsify: A Practical Playbook for Agentic Commerce Readiness" with Otterly.ai** was delivered (Nathan Teplow + Marisa Borek / Salsify; Thomas Peham + Rick Tousseyn / Otterly.ai) — joint live demo of Salsify's syndication workflows alongside Otterly.ai's agentic analytics, positioning Salsify as a "system of delivery" to publish product data to the agentic shelf. Separately, the Oct 27 Salsify blog *"AI Path to Purchase: Winning the New Rules of AEO for Ecommerce and GEO"* recaps the final installment of the Salsify + DetailPage three-part AI path to purchase webinar series: DetailPage CEO Spencer Millerberg notes ChatGPT is **moving away from scraping retailer PDPs and increasingly relying on structured retailer product feeds**, which materially raises the value of the data brands send to retailers via syndication (Walmart, Target, Home Depot). No MCP terminology in either artefact — remains the only tracked PIM Challenger in Gartner's Oct 12 MQ.

**Why it matters:** Salsify is doubling down on the "agentic commerce = retailer-side distribution problem" framing without touching MCP vocabulary. That keeps a widening gap between Salsify's AI positioning (first-party MCP server + Angie assistant for *configuration* workflows) and its field marketing (agentic *commerce* readiness without MCP references).

**Source:**
- [Salsify blog — "AI Path to Purchase: Winning the New Rules of AEO for Ecommerce and GEO" (Chris Caesar, Oct 27, 2026)](https://www.salsify.com/blog/winning-the-new-rules-of-aeo-for-ecommerce-and-geo)
- [Salsify / Otterly.ai — Oct 27 Part 3 webinar announcement (Salsify LinkedIn)](https://www.linkedin.com/posts/salsify_agenticcommerce-pxm-ecommerce-activity-7516860547078774785-eLhV)
- [Salsify — "AI in Salsify: A Practical Playbook for Agentic Commerce Readiness" (series page)](https://www.salsify.com/resources/webinar/ai-in-salsify-a-practical-playbook-for-agentic-commerce-readiness)

## 3. Notable Patterns

- **SAP has shipped a two-plane architecture for governed MCP.** SAP AI Agent Hub (Oct 1 GA) + the new SAP Enterprise AI Gateway (TechEd Oct 27) now provide a *governance / discovery* plane, while SAP MDG + SAP Reltio (GA in SAP BDC Oct 29) + SAP Knowledge Graph + Dremio-powered federated zero-copy query provide the *trusted-data* plane for agents. No other tracked vendor currently matches this control-plane breadth.
- **MCP-provenance (not just MCP-access) is the new differentiator.** Informatica's new composite **MDM-Provenance** server (3 tools: `get_master_record_sources` / `get_master_field_provenance` / `get_source_record`) is the first explicit "prove why to trust the agent's answer" MCP tool-set this quarter, directly answering the audit / hallucination objections buyers raise against agent-driven stewardship. Reltio's RBAC / masking / audit framing of its MCP server and Pimcore's chat-session bearer tokens point in the same direction.
- **Enterprise distribution channels for MCP widen quickly.** Informatica Headless MCP now plugged into Oracle Database 26ai Select AI; Reltio in SAP BDC with CU-based consumption metering and a GA'd Cursor/VS Code extension; SAP Enterprise AI Gateway exposing third-party MCP servers under governed subscription. Buyers no longer need a greenfield agent platform to consume a vendor's MCP — the install base they already own may ship it next.

## 4. No Relevant Updates

- **Profisee** — No new primary source content in the Oct 23–30 window; 2026 R3 is still the current message. Watching Profisee Anywhere GA in December 2026.
- **Akeneo** — No new primary source content this week. The DwyerOmega × Akeneo MCP **Part 2** promised by the Oct 14 Part 1 blog has still not been published; social amplification of Part 1 continues (Oct 19–20 LinkedIn by Andrew Simpson, Samira McDonald).
- **Inriver** — Oct 24–25 and Oct 29 (Media) release notes shipped incremental UI, syndication and media bug-fixes with no MCP delta. Last MCP Server (Query Manager) change remains the Oct 10–11 recursive-traversal + snapshot-tag updates.
- **Syndigo** — No new primary source content in this window. Last MCP-adjacent moves remain the Oct 15 PIM MQ Leader press release and the Aug 19 State of PX 2026 study.

## 5. Suggested Follow-Up

- **Treat SAP Enterprise AI Gateway as a competitive milestone, not just a messaging milestone.** The combination of free Agent Hub (up to 500 agents) + governed MCP subscription + Reltio GA in SAP BDC is a credible lock-in for SAP installed-base MDM buyers. Prepare a Stibo talking-track that compares the Stibo MCP governance posture to the Enterprise AI Gateway's auth / policy / routing / monitoring controls on a feature-level basis.
- **Match the "MCP-provenance" framing in Stibo messaging.** Informatica's composite MDM-Provenance server (and Reltio's "all actions routed through MCP server, allowlisted tools only, full audit" wording) sets a bar for how MDM vendors answer the agent-hallucination objection. Stibo should quote its own equivalent provenance guarantees in the same terminology.
- **Watch for an Informatica announcement of Oracle AI World follow-on in Nov** (post-event amplification + Headless MCP in Oracle Select AI case studies). The Oracle Database 26ai install base is the single biggest net-new MCP distribution channel the tracked vendors have opened this quarter.

---

Prepared for Mark Janssen, Stibo Systems. Sources link to publicly available pages. No speculative content included. "MCP-adjacent" is used where sources discuss AI agents, semantic layers or AI-ready data access without explicitly naming MCP.
