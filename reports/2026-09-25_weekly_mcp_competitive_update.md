Subject: Weekly MCP Competitive Update – September 18 to September 25, 2026

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

## 1. Executive Summary

- **Informatica** used Dreamforce to launch a new **AI-Ready Data Intelligence** solution (7 factors, 21 measures) that runs via Claude and evaluates an organization's data estate for agent readiness — extending its MCP + Claude Plugin story from access to *diagnostics*.
- **SAP** (MDG-adjacent) published a fresh SAP News Center piece positioning the **Business Transformation Management** portfolio (Signavio, LeanIX, WalkMe, Cloud ALM) as the operational backbone for agents, with **SAP AI Agent Hub** (LeanIX-based) already governing **180,000+** discovered agents, LLMs and MCP servers pre-GA.
- **Reltio** got its first **SAP News Center author feature** (Sept 23, Manish Sood on agentic AI + trusted data), a joint **SAP-branded webinar on golden records + agents (Sept 23)**, and a Community Show demo of **AgentFlow + Intelligent 360 + zero-copy** pulling live contract/claims data into sales-call prep.
- **Akeneo** dropped a new **PX Pulse consumer survey** (Sept 23) explicitly citing "AI-powered shopping tools constantly comparing prices" — extending the agentic-commerce narrative into pricing, on the heels of its June PricingHUB deal.
- Cross-vendor: SAP's **CAP MCP Adapter (Node.js + Java) went GA in the September 2026 CAP release** — the first tier-1 SAP-native MCP server framework GA — while **no tracked vendor has yet published an MCP 2026-07-28 compatibility statement** (eight weeks post-spec).

## 2. Key Updates This Week

### Company: Informatica
**Status:** Updated
**Summary:** Sept 17 Informatica blog *"Informatica at Dreamforce 2026: The Engine Powering Salesforce's Enterprise AI Harness"* introduces **AI-Ready Data Intelligence**, a new solution accessible via Claude that scans metadata, access, lineage and other dimensions and returns a readiness score plus remediation steps across **seven factors** (discoverability, quality, context, accessibility, governance, trust, observability) and **21 underlying measures**. Same blog reiterates the Sept 16 **Informatica Plugin for Claude** on Claude's Plugin Marketplace and adds an "AI Governance" wrapper for the entire agentic lifecycle.
**Why it matters:** Moves Informatica's MCP story from *exposing* trusted data to *proving* AI-readiness on the customer's own estate — a differentiator Stibo Systems should track when framing governed MDM as prerequisite for agents.
**Sources:**
- [Informatica at Dreamforce 2026: The Engine Powering Salesforce's Enterprise AI Harness (Sept 17, 2026)](https://www.informatica.com/blogs/power-every-agent-with-ai-ready-data.html)
- [AI-Ready Data Intelligence – customer scorecard landing page](https://now.informatica.com/AI-ReadyAssessmentScorecard.html)

### Company: SAP MDG
**Status:** Updated
**Summary:** Sept 22 SAP News Center piece *"The Operational Backbone of the Autonomous Enterprise"* (Andre Wenz, from the SAP Transformation Excellence Summit in Atlanta) frames **SAP Signavio, SAP LeanIX, WalkMe, and SAP Cloud ALM** as the systems that deploy, govern and observe AI agents across the Business AI Platform. The **SAP AI Agent Hub** (built on LeanIX) is reportedly already tracking **~180,000 agents at 150–180 organisations pre-GA**, with Q3 2026 GA. Cloud ALM adds production agent monitoring; Signavio ships a Process Consulting Agent and AI Agent Excellence framework. Separately, the **SAP CAP September 2026 release notes** mark the **MCP Protocol Adapter (Node.js and Java) as GA**, with `describe` output streamlined, `query` now using CQL, and `@cap-js/ord@1.5.0` generating ORD resource definitions for MCP. The **SAP Reltio product page** was also updated to formalise the MDG-vs-Reltio complementary positioning ("MDG enforces governance at data creation in SAP ERP; Reltio unifies across systems").
**Why it matters:** SAP is codifying agent governance, observability and MCP tooling as a native BTP capability — a direct competitive frame for Stibo's MCP + governance messaging.
**Sources:**
- [The Operational Backbone of the Autonomous Enterprise (SAP News Center, Sept 22, 2026)](https://news.sap.com/2026/09/autonomous-enterprise-business-transformation-management-solutions-sap-ai-agents-work-at-scale/)
- [SAP CAP – September 2026 release: MCP Adapter GA](https://cap.cloud.sap/docs/releases/2026/sep26)
- [SAP Reltio in SAP Business Data Cloud – product page (updated)](https://www.sap.com/products/data-cloud/reltio.html)

### Company: Reltio
**Status:** Updated
**Summary:** Three signals this week. (1) **Sept 17 Reltio Community Show blog** *"Unlock Context Intelligence with Reltio Intelligent 360 & Zero Copy"* shows a live **AgentFlow query pulling a customer's contracts and claims history (via zero-copy from a cloud data warehouse) to auto-generate sales-call prep notes**; formal 26.2 announcement flagged for October. (2) **Sept 23 SAP News Center feature** *"Reltio CEO: Can Agentic AI Bridge the Gap with Enterprise Data?"* (Tim Clark) — first SAP-owned editorial spotlight on Manish Sood since the acquisition closed. (3) A **SAP-branded Sept 23 webinar** on the SAP Reltio product page ("How trusted golden records power agentic AI") ran the same day. (4) **Reltio 2026.1.11.0 rolled to PRD Sept 25** per the delivery-schedule page; specific release notes are not yet published.
**Why it matters:** Reltio is now visibly amplified through SAP's own editorial and marketing channels, tightening the SAP-anchored positioning that competes most directly with Stibo's SAP-adjacent story.
**Sources:**
- [Community Show: Unlock Context Intelligence with Reltio Intelligent 360 & Zero Copy (Sept 17, 2026)](https://community.reltio.com/blogs/sara-brams-miller/2026/09/17/reltio-intelligent-360-zero-copy)
- [Reltio CEO: Can Agentic AI Bridge the Gap with Trusted Enterprise Data? (SAP News Center, Sept 23, 2026)](https://news.sap.com/2026/09/can-agentic-ai-bridge-gap-with-trusted-enterprise-data/)
- [Reltio release cadence and delivery schedule (2026.1.11.0 PRD Sept 25)](https://docs.reltio.com/en/reltio/whats-new-and-notable/whats-new-at-a-glance/release-notes-at-a-glance/release-cadence-and-delivery-schedule)

### Company: Akeneo
**Status:** New
**Summary:** **Sept 23 primary-source press release** *"Akeneo Survey Finds Shoppers No Longer Take Prices at Face Value"* — new PX Pulse survey of 1,000 U.S. consumers (fielded by Dynata in August 2026) reports **79% delayed a purchase waiting for price drops, 77% spotted price discrepancies across retailers, and only 32% trust retailers to offer fair prices**. CEO Romain Fouache: *"Consumers, and increasingly AI-powered shopping tools, are constantly comparing products, prices, and offers across channels. Brands need trusted product and pricing information working together."* Positions the June 2026 **PricingHUB acquisition** and the Akeneo MCP Server as the joint answer.
**Why it matters:** Extends Akeneo's agentic-commerce narrative from product data to pricing — MCP-adjacent, but explicitly names AI shopping agents as a second audience for product-and-price data.
**Sources:**
- [Akeneo Survey Finds Shoppers No Longer Take Prices at Face Value (Akeneo press release, Sept 23, 2026)](https://www.akeneo.com/press-release/akeneo-survey-finds-shoppers-no-longer-take-prices-at-face-value/)

### Company: Inriver
**Status:** Updated
**Summary:** **AEO Masterclass Episode 2** *"AEO: How to Fix What AI Sees on Your Product Page"* delivered live Tuesday **Sept 22** (Steve Vink + Joakim Gavelin) as a 45-minute walkthrough **inside a real Inriver PIM environment** — covering the five-step structured-data plan, common patterns that break machine-readability, and what "AI-ready" product data requires at the data-model level. Attendees also receive a whitepaper on ERP/PLM feeds into PIM as the single source of trust for answer engines.
**Why it matters:** Inriver is turning its ACP/UCP/MCP protocol-stack thesis into a repeatable enablement funnel — the "operational playbook" competitive vendors so far only assert.
**Sources:**
- [Inriver Masterclass: Episode 2 – AEO: How to Fix What AI Sees on Your Product Page (Sept 22, 2026)](https://www.inriver.com/event/aeo-masterclass-structured-data/)

### Company: Pimcore
**Status:** Updated
**Summary:** **DMEXCO 2026 Masterclass Sept 23** *"Job Killer or Team Multiplier? The Truth About Agentic Data and Experience Management"* delivered by co-CEO **Dietmar Rietsch** (MC Commerce 7B, Hall 7.1 D025), with the recording being distributed by opt-in — session claim is that agentic AI already runs across Pimcore PIM/MDM/DAM/DXP end-to-end with human-in-the-loop. On the code side, **v2026.2.14 shipped on GitHub** this week (storage-queue and Doctrine DBAL 4 fixes, thumbnail null-safety) — no Agent Bundle or MCP-based Agent SDK changes.
**Why it matters:** First public post-Tenzing acquisition on-stage message; reinforces the open-core + governance thesis but no new MCP surface yet.
**Sources:**
- [Pimcore @ DMEXCO 2026 – Masterclass session page (Sept 23, 2026)](https://pimcore.com/dmexco-2026)
- [Pimcore v2026.2.14 GitHub release notes](https://newreleases.io/project/github/pimcore/pimcore/release/v2026.2.14)

### Company: Syndigo
**Status:** Updated
**Summary:** **Sept 22 InternetRetailing UK cut** of Syndigo's *State of Product Experience 2026 – UK Edition*: **43% of UK consumers recently abandoned a purchase due to insufficient product information**. The piece explicitly reframes product data as having "two audiences: the shopper and the machine helping the shopper," and argues that retail-media placements cannot rescue poor product records once AI agents start filtering. MCP-adjacent (no new MCP capability disclosed).
**Why it matters:** Continues the vendor-neutral trend of using primary consumer research to shift buyer language from "PIM/PXM" to "AI-verified product data."
**Sources:**
- [Retail media's missing link: Why better product data is becoming essential to conversion – InternetRetailing (Sept 22, 2026)](https://internetretailing.net/retail-medias-missing-link-why-better-product-data-is-becoming-essential-to-conversion/)

### Company: Salsify
**Status:** Updated (minor)
**Summary:** Salsify confirmed the **Sept 30, 2026 European webinar "AI in Salsify Part 3 – Powering Agentic Experiences"** (3:00 PM GMT) on its resources page — final session in the three-part agentic-commerce readiness series, explicitly covering how AI agents "condense the purchasing funnel from broad search pages with hundreds of listings down to three or four highly personalised recommendations." No new MCP capability disclosed.
**Why it matters:** Salsify continues to keep MCP visible in customer enablement even without new server-side news.
**Sources:**
- [AI in Salsify – A Practical Playbook for Agentic Commerce Readiness (Europe)](https://www.salsify.com/resources/webinar/ai-in-salsify-a-practical-playbook-for-agentic-commerce-readiness-europe)

## 3. Notable Patterns

- **From MCP access to MCP-driven diagnostics**: Informatica's new AI-Ready Data Intelligence is the first move in the tracked set that uses an MCP-connected chat surface (Claude) to *audit* customer data for agent-readiness — not just serve it.
- **Vendor-neutral consumer/enterprise research is the buyer message**: Akeneo (Sept 23 PX Pulse on pricing) and Syndigo (Sept 22 UK State of PX) both used primary research this week to reframe product-data quality as an AI-agent recommendation issue — deepening the "product data is now agent-facing" chorus.
- **SAP's agent-governance flywheel is materially widening**: MDG-adjacent BTM stack (LeanIX-hosted AI Agent Hub with 180K discovered agents), CAP MCP Adapter GA, Reltio featured on SAP News Center and in a SAP-branded webinar all landed in a single week. Eight weeks post-2026-07-28 spec, none of the nine tracked vendors has published a public MCP protocol-version compatibility statement.

## 4. No Relevant Updates

- **Profisee** — no new primary content this week; next milestone remains the 26R3 release (quarterly cadence).

## 5. Suggested Follow-Up

- Assess Informatica's *AI-Ready Data Intelligence* scoring model (7 factors, 21 measures) as a possible framing lens for Stibo's own AI-readiness discovery conversations.
- Track whether the Sept 22 SAP BTM messaging and the Sept 23 SAP-branded Reltio moves start to explicitly redraw the MDG-vs-Reltio-vs-partner-MDM boundary in SAP-influenced deals.
- Watch for the Reltio 2026.1.11.0 release notes (PRD Sept 25) and the 26.2 zero-copy formal announcement flagged for October — both may add MCP or observability surfaces relevant to Stibo positioning.
