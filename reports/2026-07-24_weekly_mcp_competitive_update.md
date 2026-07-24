Subject: Weekly MCP Competitive Update – July 17, 2026 to July 24, 2026

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

1. Executive Summary
- SAP Integration Suite MCP Gateway went generally available in July 2026 and SAP's Architecture Center now publishes MCP as governed integration surface — an enterprise-grade OAuth/OIDC-scoped, rate-limited, audited "front door" for any AI agent (Joule, Claude, Copilot, ChatGPT) to reach SAP APIs, iFlows and RFCs. This directly upgrades the MCP path into SAP MDG-in-BDC.
- SAP's new Architecture Center guidance formalises the split: MCP for governed tool exposure (via the Integration Suite Gateway) and A2A (via the SAP Agent Gateway, not yet GA) for multi-agent, vendor-to-vendor interoperability — a clearer, more prescriptive protocol posture than any other MDM vendor has published.
- Reltio fast-tracked a new AI-for-Implementation-Teams wave outside its normal major release (July 20 community show): Reltio Ontology Builder, natural-language Reltio IDE, AgentFlow Mobile and AI-ready markdown docs from docs.reltio.com — extending its agentic story from runtime agents into build-time / implementation productivity.
- No new MCP-specific product announcements from Informatica, Profisee, Akeneo, Salsify, Inriver, Pimcore or Syndigo this week; regional trade-press and community coverage of prior launches continues.
- Broader context: the MCP 2026-07-28 specification release candidate — the biggest revision of MCP since launch, with a stateless-core redesign and breaking changes — is set to ship next week and will apply to every vendor MCP server discussed in this report; expect vendors to start publishing compatibility statements after July 28.

2. Key Updates This Week

Company: SAP MDG
Status: Updated
Summary: The SAP Integration Suite MCP Gateway is now generally available in July 2026 (Help Portal "What's New" entry + SAP Developer News), rolling out in Integration Suite Enhanced and Premium editions and available on BTP Trial. It exposes SAP APIs, non-SAP APIs, iFlows, data sources and external MCP servers as governed, MCP-compliant tools with OAuth 2.0/OIDC authentication, scoped tokens, rate limiting, payload protection, monitoring and audit — a single "authorization boundary before execution" that any MCP client (Joule, Claude, Copilot, ChatGPT, custom agents) can consume. Alongside the GA, SAP has published two new Architecture Center reference pages that codify SAP's protocol posture: "A2A and MCP for Interoperability" positions Joule as the internal MCP consumer of SAP Knowledge Graph + business capabilities and A2A (via the not-yet-GA SAP Agent Gateway) as the preferred cross-vendor path, and "Third-Party MCP Access to SAP Solutions" flags the security/lifecycle risks of home-grown MCP servers and directs customers to the Gateway as the "endorsed pathway" for agents reaching SAP APIs. A companion "Integration Cell Runtime" is now available as the cloud-native runtime for designing, deploying and operating APIs and MCP servers, framed by SAP as the foundation for the agentic phase of Integration Suite. Because SAP MDG is delivered as data products through SAP Business Data Cloud, MDG data now inherits this governed MCP exposure path by default.
Why it matters: Turns SAP's earlier "MCP everywhere in BDC" narrative into shipped, governed product with a customer-managed control plane — a stronger governance story than any pure-play MDM vendor's MCP Server. The A2A-preferred / MCP-only-through-the-Gateway posture is also a policy signal: SAP is trying to prevent an "MCP sprawl" (ungoverned point-to-point servers) that most PIM/MDM vendors are still shipping. Raises the governance bar Stibo Systems' MCP messaging is measured against, especially for joint SAP accounts.
Source:
- SAP released the MCP Gateway in SAP Integration Suite (Jan Penninkhof, LinkedIn, July 16, 2026) — https://www.linkedin.com/posts/jpenninkhof_sap-released-the-mcp-gateway-in-sap-integration-activity-7483596359124766720-Qnx0
- MCP becomes governed infrastructure inside SAP Integration Suite and SAP BTP AI Best Practices Official Reference Hub launched (Gaurav Singh, LinkedIn Pulse, July 2026) — https://www.linkedin.com/pulse/mcp-becomes-governed-infrastructure-inside-sap-suite-btp-gaurav-singh-kk96e
- A2A and MCP for Interoperability (SAP Architecture Center reference architecture) — https://architecture.learning.sap.com/docs/ref-arch/76ec36
- Third-Party MCP Access to SAP Solutions (SAP Architecture Center reference architecture) — https://architecture.learning.sap.com/docs/ref-arch/137800
- SAP CPI / Integration Suite — Mid-2026 Update (Sai Prakash Sangam, LinkedIn, July 13, 2026) — https://www.linkedin.com/posts/sai-prakash-sangam-6aa9382a3_sap-sapcpi-integrationsuite-activity-7482341474836262912-eUnQ

Company: Reltio
Status: Updated
Summary: On July 20, 2026 the Reltio Community held a customer-and-partner webinar, "Build Faster on Reltio: AI for Implementation Teams", introducing four new AI-powered capabilities fast-tracked outside the normal Reltio major release cadence: (1) Reltio Ontology Builder, (2) a new Reltio IDE that lets developers/configurators use natural-language prompts (e.g. "create an employee entity type with the relevant attributes and a reference attribute to Organization") to generate entity types, attributes and even implied relationship types, with ontology comparison, version control and configuration promotion into a live tenant; (3) AgentFlow Mobile (iOS/Android access to AgentFlow); and (4) AI-ready markdown documentation from docs.reltio.com, plus AI assistance embedded in the official documentation. Reltio's release-cadence page also confirms bi-weekly release 2026.1.7.0 (DEV/TEST July 24, PRD July 31); the next major release, 2026.2, is scheduled for October 23, 2026.
Why it matters: Extends Reltio's agentic story upstream from runtime AgentFlow agents into build-time productivity, an area no other MDM vendor has publicly staked out. Combined with AgentFlow, Agent Builder and the Reltio MCP Server, this positions Reltio as the vendor most aggressively bundling AI into every phase of the MDM lifecycle — including partner/implementer enablement. Something to benchmark Stibo's own partner-implementation and modelling tools against.
Source:
- Customer and Partner Webinar: Build Faster on Reltio — AI for Implementation Teams Webinar (Sara Brams-Miller, Reltio Community, July 20, 2026) — https://community.reltio.com/blogs/sara-brams-miller/2026/07/20/build-faster-on-reltio-ai-for-implementation-teams
- Release cadence and delivery schedule (Reltio docs, updated July 10, 2026) — https://docs.reltio.com/en/reltio/whats-new-and-notable/whats-new-at-a-glance/release-notes-at-a-glance/release-cadence-and-delivery-schedule

3. Notable Patterns
- Governance is where competitive differentiation is going next: SAP now positions its MCP Gateway as an "authorization boundary before execution" with OAuth 2.0/OIDC, scoped tokens, rate limits and audit; Reltio, Profisee and Pimcore continue to lean on RBAC, audit trails, SBOM and human-in-the-loop as the trust story around MCP. Simply having an MCP server is no longer differentiating — how it is authenticated, scoped and audited is.
- MCP + A2A dual-protocol messaging is emerging as the "grown-up" agent architecture: SAP explicitly separates MCP (tools) from A2A (agent-to-agent) and prefers A2A for vendor-to-vendor interop, mirroring Informatica's already-announced A2A support in the Fall 2026 release. Vendors that only talk about MCP will look one step behind.
- The vendors are moving upstream from "agents at runtime" to "AI for the implementation lifecycle": Reltio's Ontology Builder / natural-language IDE, Profisee 2026.R2's "Word document to configured MDM in 10 minutes" and Pimcore's Agent SDK all point to AI accelerating configuration, modelling and onboarding — not just business execution.

4. No Relevant Updates
- Informatica — no new MCP-specific news this week; the July 2026 IDMC monthly release (docs published July 10) and the Informatica World 2026 cross-cloud MCP + Agent Fabric Context Catalog narrative remain current.
- Profisee — no new news this week; Profisee 2026.R2 (July 8) with re-architected Aisey on the Microsoft Agent Framework and expanded MCP Server (Matching, Connect, FastApps, Forms, Presentation Views) remains current.
- Akeneo — no new product news this week; Agentic Ziggy (July 8) and continued analyst pickup (Sentinel July 13, Help Center Ziggy Workspace page) remain current.
- Salsify — no new news this week; SalsifyIQ + MCP layer (May 5) and the July 6 Azoma/Mars "Decision Shelf" webinar and "Mastering the Agentic Shelf" whitepaper remain current.
- Inriver — no new news this week; Summer 2026 release (June 30) with enhanced MCP endpoints, MCP Code Writer and Enrich Assistant remains current.
- Pimcore — no new news this week; Pimcore Platform 2026.2 (July 9) with Agent Bundle expansion into Documents/Templates, Entity Ownership Management and per-release SBOM remains current.
- Syndigo — no new news this week; Synapse Agentic PXM (March 24), SynapseGo (April 15), Blue Yonder partnership (May 19), Conversion Framework (June 22) and GS1 Connect showcase (June 9–11) remain current.

5. Suggested Follow-Up
- Position Stibo Systems' MCP surface as governance-forward now that SAP has raised the bar: highlight authentication scope, tenancy-level policy enforcement, audit trail and rate limiting — not just "we have an MCP Server." A "governed MCP + A2A-ready" narrative will read most convincingly to joint SAP prospects.
- Prepare a compatibility statement for the MCP 2026-07-28 specification (shipping next week, stateless-core redesign, breaking changes). Being an early public voice on "our MCP server is 2026-07-28-compatible" is a low-effort, high-signal move as competitors go quiet during their SDK migrations.
- Monitor Reltio's Ontology Builder / natural-language IDE rollout across July–August (fast-tracked outside 2026.2). It is the first credible "AI for implementation partners" play in MDM and could become a lever Reltio (and by extension, SAP) uses in partner-driven deals.
