# Weekly MCP Competitive Update – October 16, 2026 to October 23, 2026

**To:** mjan@stibosystems.com
**Subject:** Weekly MCP Competitive Update – October 16, 2026 to October 23, 2026

---

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

## 1. Executive Summary

- **Reltio 2026.2 reaches General Availability today (Oct 23).** The release renames **Reltio AgentFlow to "Autonomous agents"** across the product, ships **Long Running Tasks** (background jobs on large record sets, isolated per-tenant runtime) and **Unstructured search** (document knowledge bases that ground custom agents) as GA, and documents Autonomous agents as built on the Reltio MCP Server. Capability rename matrix: AgentFlow Unstructured → Unstructured augmentation, Agent Builder → Custom agents, Agent Marketplace → Discover agents.
- **Pimcore finally positioned on the Oct 12 Gartner PIM MQ: Visionary** (Oct 19 blog by CEO Dietmar Rietsch). Pimcore is now across **three** Gartner MQs — DXP, MDM and PIM — with an explicit "AI needs clean, governed data" message framed around the Data Spine. This also **corrects an inference in last week's report**: per the Gartner MQ document and independent analysis, **Salsify is the only Challenger** in the 2026 PIM MQ (not a Leader as inferred from Salsify's Oct 13 LinkedIn post). Confirmed 2026 PIM MQ Leaders among the tracked set: **Akeneo, Inriver, Salesforce (Informatica), Stibo Systems, Syndigo**.
- **SAP scales partner agents into the AI Agent Hub ahead of TechEd Berlin (Oct 27–29).** Oct 19 SAP News Center: SAP has moved from a 680-agent Sapphire milestone to a **1,000-partner-agent target for TechEd**; 300+ partner agents forecast on SAP Discovery Center by year-end; SAP AI Agent Hub is **free for customers managing up to 500 AI agents** and now hosts partner agents alongside SAP's own as "one marketplace." TechEd agenda confirms new hands-on MCP sessions (IN202 MCP Gateway, IN261 lab, AD161/AD262 CAP-based MCP servers, BT160/BT161 LeanIX MCP governance).
- **Inriver's October product release ships agentic translation review + AI image adaptation**, with its MCP Server (Query Manager) also extended Oct 10–11 for **recursive entity retrieval across channel-node descendants and snapshot-version data access**. Framed explicitly as validation of the Oct 12 PIM MQ Leader placement.
- **Informatica's Oct 2026 MDM release documents MCP-based stewardship inside Slack**, plus two new PXM Agent skills (classify-and-enrich products via AI agent; update product records by chatting with an AI agent) and golden-record publishing into Databricks. Oct 20 Tech Tuesday on Data 360 + MDM delivered; Oct 27 Customer Identification MCP Server for MDM SaaS is next.

## 2. Key Updates This Week

### Company: Reltio
**Status:** New
**Summary:**
Reltio 2026.2 reaches GA on Oct 23, 2026 (per the official release-cadence page). The marquee change: **Reltio AgentFlow is renamed "Autonomous agents"**, with capability-level renames (AgentFlow Unstructured → Unstructured augmentation, Agent Builder → Custom agents, Agent Marketplace → Discover agents). **Long Running Tasks** (GA) let autonomous and custom agents work through large record sets in the background on an isolated per-tenant runtime, with per-record status, confidence score, reason, trace and CSV/JSONL export. **Unstructured search** (GA, part of Unstructured augmentation) turns documents into AI-searchable knowledge bases, grounding custom-agent answers in enterprise content. Reltio's Autonomous agents overview docs explicitly state the capability is "built on the Model Context Protocol (MCP) server," enforcing RBAC, data masking and audit policies. The Oct 19 Gartner IT Symposium session with Pfizer (Nishith Trivedi, Enterprise Data Governance / Global MDM Lead) was delivered: Pfizer projects an **80–90% cut in due-diligence time and a 30–40% cut in stewardship backlog** from the agentic AI + MDM approach.
**Why it matters:** The rename from "AgentFlow" to "Autonomous agents" normalises Reltio's naming with the SAP + enterprise category (SAP AI Agent Hub, Autonomous Suite) and positions "autonomous master data governance" as a shipping product category, not a slide. The MCP Server is still the plumbing, now with explicit customer-grade benchmarks via Pfizer.
**Source:**
- [Reltio 2026.2 Major Release Notes (Reltio Docs)](https://docs.reltio.com/en/reltio/release-notes-at-a-glance/2026.2-release-notes/2026.2-major-release-notes)
- [Autonomous agents overview — "Built on the Model Context Protocol (MCP) server" (Reltio Docs)](https://docs.reltio.com/en/products/autonomous-agents/autonomous-agents-overview)
- [Release cadence and delivery schedule — 2026.2 GA Oct 23, 2026 (Reltio Docs)](https://docs.reltio.com/en/reltio/release-notes-at-a-glance/release-cadence-and-delivery-schedule)
- [Reltio: Scaling Agentic AI at Pfizer — Gartner IT Symposium session detail (Oct 19, 2026)](https://www.gartner.com/en/conferences/na/symposium-us/sessions/detail/6187712-Scaling-Agentic-AI-at-Pfizer-Key-Lessons-in-Trust-Governance-and-Innovation)

### Company: Pimcore
**Status:** New
**Summary:**
**Oct 19, 2026 — Pimcore blog "We bring together what belongs together. Pimcore recognized in the 2026 Gartner® Magic Quadrant™ for PIM"** by CEO/co-founder Dietmar Rietsch finally takes a position on the Oct 12 Gartner PIM MQ: **Pimcore is placed as a Visionary**, alongside Bluestone PIM and Viamedici. The blog uses the recognition to make an explicit agent-governance argument: "An agent that enriches product content, answers a buyer, or updates a catalogue does not care how impressive your model is. It cares whether the data it touches is correct, complete, and governed. … Data management is no longer plumbing. It is the infrastructure that lets agents work." Pimcore also launches a dedicated [`/gartner-mq-2026-pim`](https://pimcore.com/gartner-mq-2026-pim) landing page, noting the company now appears in **three Gartner MQs — DXP, MDM and PIM** — all on one platform. Separately, **Pimcore v2026.3.3 shipped Oct 20** (bugfixes + two security fixes: GHSA-6r57-mhj4-5gmr Custom Reports SQL validator LOAD_FILE denylist bypass; GHSA-8xfm-m7j7-4mr5 PHP Object Injection via tmp_store session data) and **v2026.3.3.1 Oct 22** (Twig sandbox restriction). No new Agent Bundle / Datahub MCP changes.
**Why it matters:** Corrects an inference in last week's report (which implied Pimcore and Salsify were among six Leaders): per the Gartner document, the tracked-set Leaders are **Akeneo, Inriver, Salesforce (Informatica), Stibo Systems, Syndigo**, with **Salsify the only Challenger** and **Pimcore a Visionary**. Pimcore's agent-governance framing is sharper than most of the Leader cohort's quadrant announcements and worth watching.
**Source:**
- [Pimcore blog — "We bring together what belongs together" (Dietmar Rietsch, Oct 19, 2026)](https://pimcore.com/en/resources/blog/we-bring-together-what-belongs-together.-now-recognised-in-three-gartner-magic-quadrants)
- [Pimcore MQ landing page — "Recognized in the 2026 Gartner® Magic Quadrant™ for PIM"](https://pimcore.com/gartner-mq-2026-pim)
- [Pimcore v2026.3.3 release (GitHub, Oct 20, 2026)](https://github.com/pimcore/pimcore/releases)
- [Gartner Magic Quadrant for Product Information Management Solutions (Oct 12, 2026)](https://www.gartner.com/en/documents/8496777)

### Company: SAP MDG
**Status:** Updated
**Summary:**
**Oct 19, 2026 SAP News Center — "1k AI Agents by SAP TechEd: Accelerating with Partners"** (Andrea Diederichs): partners delivered 680+ agents by Sapphire (vs. a 200-agent target); SAP has now set a **1,000-partner-agent target for SAP TechEd Berlin (Oct 27–29)** and forecasts 300+ partner agents published on SAP Discovery Center by year-end. **Partner agents are now embedded directly in the SAP AI Agent Hub** on equal footing with SAP-native agents. SAP AI Agent Hub is **free of charge for customers managing up to 500 AI agents**. The TechEd Berlin program confirms new hands-on MCP sessions: **IN202 "Model Context Protocol (MCP) Unlocked: Enable governed access to AI agents," IN261 MCP Gateway hands-on lab, AD161 "Agentic CAP: Build MCP servers and enterprise AI agents," AD262 CAP-based MCP + A2A, BT160/BT161 LeanIX MCP governance workshops** (with Claude Code connected via the LeanIX MCP server). Independent corroboration: **Oct 16 nl2sql.ai analysis** of the Joule Work rollout confirms AI Agent Hub + SAP Reltio as GA together, with Joule Studio imminent.
**Why it matters:** SAP is now shipping the economic layer (free Agent Hub up to 500 agents, €100M partner fund) and the discovery/marketplace layer (partner agents in a single Hub) on top of the Oct 1 governance GA. For MDG, this is the direct distribution path to buyers already shortlisting around "verified MCP servers only."
**Source:**
- [SAP News Center — 1k AI Agents by SAP TechEd (Oct 19, 2026)](https://news.sap.com/2026/10/1k-ai-agents-by-sap-teched-sap-and-partners-accelerate-together/)
- [SAP TechEd Berlin — IN261 Model Context Protocol (MCP) Unlocked: Enabling Governed Access to Agents](https://www.masteringsap.events/collaborate-sap-teched-on-tour/session/4546684/in261-model-context-protocol-mcp-unlocked-enabling-governed-access-to-agents)
- [SAP TechEd Berlin BT160 + BT161 — LeanIX MCP governance workshops (SAP Community)](https://community.sap.com/t5/sap-teched-blog-posts/sap-teched-berlin-bt161-bt160-two-workshops-one-goal-put-ai-under-control/ba-p/14501636)
- [SAP TechEd Berlin tracks (Oct 27–29, 2026)](https://www.sap.com/events/teched/berlin/tracks.html)

### Company: Inriver
**Status:** New
**Summary:**
**Oct 20, 2026 — "October 2026 Product Release: AI-adapted images, agentic review of translations, and improved performance for even the largest data sets"** (Beccy Johnston, Inriver Community). Headline features: (a) **AI image adaptation** per market/channel — natural-language prompts, up to three reference images, in-PIM edit history, usage billed from the existing AI credits balance for Inspire licensees; (b) **agentic critique loop for translations** on OpenAI's latest model; (c) performance improvements for large data sets (richer completeness rules, Table View language selector); (d) print & publish document-status insights; (e) Shopify adapter configuration UI. Inriver frames the release as validation of its **Oct 12 Gartner PIM MQ Leader** placement. Separately, **Oct 10–11 community release notes** extended the Inriver **MCP Server (Query Manager)**: `recursive retrieval of all entities of a specified type from a channel node and its descendants` (channel-content validation, business-unit exports, missing-product identification, reporting integration) and **snapshot-version data access** via the `get_entity_data` tool (new snapshot-tag argument).
**Why it matters:** The agentic translation critique loop and the AI image adaptation move Inriver's Inspire AI agent fabric into the "work-doing agent" bracket populated by Reltio Autonomous agents and Profisee Aisey. The MCP Query Manager extensions make Inriver's MCP server noticeably more useful to agents operating across catalog hierarchies — the first MCP-level product change from Inriver since the September 2025 launch.
**Source:**
- [Inriver — October 2026 Product Release (Oct 20, 2026, Inriver community)](https://community.inriver.com/hc/en-us/articles/31147870813980-October-2026-Product-Release-AI-adapted-images-agentic-review-of-translations-and-improved-performance-for-even-the-largest-data-sets)
- [Inriver — Release notes: Oct 10th–Oct 11th, 2026 (MCP Server / Query Manager updates)](https://community.inriver.com/hc/en-us/articles/30973041531292-Release-notes-Oct-10th-Oct-11th-2026)
- [Inriver Brand Store release notes (Oct 20, 2026)](https://community.inriver.com/hc/en-us/articles/31095949479580-Release-notes-October-20th-2026-Brand-Store)

### Company: Informatica
**Status:** Updated
**Summary:**
Two primary items this week. **Oct 20, 2026 Tech Tuesday webinar "From Golden Record to Agentic Action: Unlocking Data 360 with Trusted Context — MDM"** (Kamal Abrol, Senior Success Architect) was delivered and is now on-demand on the Informatica Success Portal. The session positions **Informatica MDM + Salesforce Data 360 as the "Stop AI hallucinations" story**: publishing MDM golden records into Data 360 via the Ingestion API, identity-resolution reuse from Customer 360 SaaS match outcomes, and AI-driven personalisation grounded in trusted master data. **The Oct 2026 Informatica MDM release deck (Tech Tuesday slides)** documents several AI-agent capabilities that overlap directly with the MCP story: **"Steward data through AI agents in tools like Slack"** (MCP servers let agents read metadata, search trusted data, write back, monitor jobs and anomalies, with validation + rollback — preview Nov 2026), **"Update product records by chatting with an AI agent"** (PXM Agent in CoPilot extracts data from English PDFs, plan preview before execution), and **"Classify and enrich products with an AI agent"** (two new PXM Agent skills, auto-classify or confidence-recommended against UNSPSC / GPC / NAICS / custom hierarchies, world-knowledge enrichment, draft proposals). Also newly published: **"Publish trusted master data into Databricks."** Next: **Oct 27 Tech Tuesday** on the **Customer Identification MCP Server for MDM SaaS**.
**Why it matters:** Informatica is now explicitly productising MCP into day-to-day MDM stewardship surfaces (Slack, chat-driven product updates) — not just agent-platform tooling. The Oct 2026 release deck confirms a Nov preview for MCP-based stewardship.
**Source:**
- [Tech Tuesdays — "From Golden Record to Agentic Action: Unlocking Data 360 with Trusted Context — MDM" (Oct 20, 2026)](https://success.informatica.com/explore/tt-webinars/from-golden-record-to-agentic-action--unlocking-data-360-with-tr.html)
- [Informatica MDM October 2026 Release Highlights (Tech Tuesday slides, PDF)](https://success.informatica.com/content/dam/informatica-cxp/techtuesdays-slides-pdf/Informatica%20MDM%20October%202026%20Release%20Highlights.pdf)
- [Tech Tuesdays — "Bridging AI Assistants with Verified Master Records: Customer Identification MCP Server for MDM SaaS" (Oct 27, 2026)](https://success.informatica.com/explore/tt-webinars/bridging-ai-assistants-with-verified-master-records--exploring-t.html)

### Company: Akeneo
**Status:** Updated
**Summary:**
**Oct 20, 2026 Unite.AI op-ed by Akeneo CTO Benoit Jacquemont — "Scaling AI Shouldn't Mean Rebuilding Data Foundations Every Time"** reframes Akeneo's PIM MQ Leader messaging around AI-infrastructure reuse, with primary-source Akeneo survey data: **93% of IT decision-makers report productivity gains from AI; 36% spend >50% of total AI-project effort on data preparation; 53% spend 26–50%**. Argues the next-gen opportunity is making the data-prep work reusable across deployments. Akeneo also published the **Italian localisation of the Oct 15 Leader announcement** (Agentic Ziggy and the "tectake 200 automation rules in minutes" example). **DwyerOmega × Akeneo MCP Part 1** was amplified Oct 19 by Alexandra Coman and Akeneo's own LinkedIn ("MCP removes the borders between systems"); **Part 2 explicitly promised** by the Oct 14 blog but not yet published.
**Why it matters:** The CTO's Unite.AI op-ed is the first serious attempt by a tracked vendor to put empirical numbers on "data prep is the AI bottleneck," which is exactly the opening for MCP + governed data arguments. Combined with the DwyerOmega production case, Akeneo is building a two-sided — vendor evidence and customer evidence — MCP story faster than the rest of the Leader cohort.
**Source:**
- [Unite.AI — "Scaling AI Shouldn't Mean Rebuilding Data Foundations Every Time" (Benoit Jacquemont, Akeneo CTO, Oct 20, 2026)](https://www.unite.ai/making-enterprise-ai-infrastructure-reusable/)
- [Akeneo — "How DwyerOmega Uses Akeneo MCP to Unlock Operational Excellence (Part 1)" (Oct 14, 2026)](https://www.akeneo.com/blog/dwyeromega-akeneo-mcp-part-1/)
- [Akeneo — Italian localisation of the Leader announcement (Oct 15, 2026)](https://www.akeneo.com/it/blog/gartner-magic-quadrant-pim-akeneo-leader-2026/)

### Company: Salsify
**Status:** Updated
**Summary:**
Two items. **Correction to last week's report**: per the Gartner MQ document and independent analysis, **Salsify was placed as the only Challenger in the 2026 PIM MQ**, not a Leader. The Oct 13 Salsify LinkedIn post referenced "Ability to Execute and Completeness of Vision"; the actual quadrant position is Challenger. **Oct 22, 2026 Salsify × Shoppers Drug Mart webinar** launched a new **Shoppers Drug Mart vendor-portal partnership**: suppliers submit required attributes through Salsify's vendor portal with automated validation, review/approval and live PDP updates — **zero cost to suppliers**; PXM Activation customers can also syndicate through Salsify. The US Part 3 of "AI in Salsify: A Practical Playbook for Agentic Commerce Readiness" with Otterly.ai remains Oct 27.
**Why it matters:** The Challenger placement sharpens the competitive picture: Salsify's PIM MQ Caution is explicitly its B2B/industrial-manufacturing footprint (per independent analysis), and its MCP is still described as "in pilot." The Shoppers Drug Mart deal is classic Salsify execution — retailer-side syndication partnerships at zero cost to suppliers — but is MCP-adjacent at most.
**Source:**
- [Salsify × Shoppers Drug Mart: Exploring the Salsify Vendor Portal (Webinar, Oct 22, 2026)](https://www.salsify.com/resources/webinar-salsify-shoppers-drug-mart-vendor-portal)
- [Salsify — Syndicate to Shoppers Drug Mart (retailer landing page)](https://www.salsify.com/retailers/shoppersdrugmart)
- [Gartner Magic Quadrant for Product Information Management Solutions (Oct 12, 2026)](https://www.gartner.com/en/documents/8496777)

## 3. Notable Patterns

- **"Autonomous" is this quarter's category label.** Reltio formally renames AgentFlow to **Autonomous agents** and ships Long Running Tasks + Unstructured search as GA; SAP's TechEd track is titled "Become the autonomous enterprise"; Profisee's 2026 R3 Aisey already configures FastApps and matching strategies in-conversation; Inriver adds an agentic critique loop for translations. The category has moved past "AI assistant" wording in two quarters.
- **MCP continues to show up as the plumbing beneath "autonomous" products** — Reltio's Autonomous agents docs explicitly state the capability is "built on the MCP server"; Informatica's Oct 2026 MDM release ties Slack-based stewardship directly to MCP servers; Inriver's Query Manager MCP gains recursive channel traversal and snapshot-version access. Still **zero MCP 2026-07-28 compatibility statements** from the tracked nine (twelve weeks post-spec).
- **The Gartner PIM MQ picture is clearer than last week.** Confirmed tracked-set positions (per the Gartner document): Leaders — Akeneo, Inriver, Salesforce (Informatica), Stibo Systems, Syndigo; Challenger — Salsify (only one); Visionary — Pimcore (now with a positioning statement). This replaces last week's inference that six of nine tracked vendors were Leaders.

## 4. No Relevant Updates

- **Profisee** — This week's items (Oct 15 LinkedIn R3 recap) restate the Oct 12 R3 story already covered. Watching Profisee Anywhere GA December.
- **Syndigo** — Oct 15 Leader press release already covered; Item Management 8.78 October release notes posted in the customer community but no public agent/MCP delta.

## 5. Suggested Follow-Up

- **Request the Gartner PIM MQ via one of the Leader pages (Akeneo, Inriver, Informatica, Syndigo, Stibo).** The "Strengths and Cautions" sections will clarify why Salsify is a Challenger and Pimcore a Visionary — useful ammunition for Stibo's own Leader position and worth comparing against Stibo's own entry.
- **Prepare a response posture to the Reltio 2026.2 "Autonomous agents" rename for internal AR and sales enablement.** The capability renames (Autonomous agents / Unstructured augmentation / Custom agents / Discover agents) are likely to become the de facto category vocabulary in SAP + enterprise RFPs by Q1 2027; align Stibo messaging where appropriate without copying it.
- **Review the SAP TechEd Berlin MCP sessions (IN202 / IN261 / AD161 / BT160–161)** for live-event signals the week of Oct 27–31. SAP's Oct 27 content will set the ceiling for how aggressively MDM/MDG vendors should talk about "verified MCP servers only" in competitive deals.
