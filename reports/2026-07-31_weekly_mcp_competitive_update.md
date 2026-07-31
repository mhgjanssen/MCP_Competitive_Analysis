# Weekly MCP Competitive Update – July 24, 2026 to July 31, 2026

**To:** mjan@stibosystems.com
**Subject:** Weekly MCP Competitive Update – July 24, 2026 to July 31, 2026

---

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

## 1. Executive Summary

- The MCP `2026-07-28` specification (the largest revision since launch — stateless core, hardened OAuth 2.0/OIDC, versioned Apps/Tasks extensions) shipped on schedule on July 28 with Tier-1 SDKs GA, Anthropic + AWS AgentCore Gateway compatible on day one. None of the nine tracked vendors has yet published a public compatibility statement; Informatica's MCP docs still reference protocol `2025-06-18`.
- Informatica opened a **private preview of two new MCP servers** — Catalog Discovery and Catalog Enrichment — in the IDMC July 2026 release, extending the MCP surface further into governed metadata search and enrichment.
- SAP's Q2 2026 earnings call (July 28) re-anchored the entire AI narrative on the AI Agent Hub as "the command center to discover, manage and govern SAP and non-SAP agents, MCP servers and more" and confirmed value-based agent pricing plus oversubscribed Joule Work beta demand.
- Reltio's 2026.1.7.0 bi-weekly release (PRD July 31) adds an **AI-assisted Agent Blueprint** feature that generates initial agent configuration, system prompt and recommended MCP tools from natural language — a direct answer to Profisee's Aisey and Akeneo's Agentic Ziggy on ease-of-authoring.
- Salsify and Syndigo continued to push MCP-adjacent "agentic shelf" messaging (new 3-part Salsify webinar series; Novi–Syndigo AI-optimized content pipeline into Amazon/Walmart/Target) without adding explicit MCP capabilities.

## 2. Key Updates This Week

### Informatica — Updated
**Summary:** The IDMC July 2026 release "Important Notices" pages (published in the Data Governance & Catalog and Informatica MCP servers / AI Agent Engineering sections) confirm that two new MCP servers — **Catalog Discovery** and **Catalog Enrichment** — are now in private preview. This extends the previously announced GA MCP server set (metadata search, data quality, MDM, etc.) further into governed catalog discovery and enrichment workflows. Separately, Informatica's public MCP docs still reference protocol version `2025-06-18` as of July 31 — no public compatibility statement yet for the new `2026-07-28` spec.
**Why it matters:** Continues Informatica's "MCP everywhere" pace-setting; the catalog-side MCP surface is where semantic and governance context flow to agents, which is directly analogous to how Stibo Systems would expose MDM context via MCP.
**Source:**
- [Data Governance and Catalog — Important notices (July 2026)](https://docs.informatica.com/release-information/what-s-new-in-idmc/current-version/what-s-new/data-governance-and-catalog/important-notices.html)
- [Informatica MCP servers and AI Agent Engineering — Important notices (July 2026)](https://docs.informatica.com/release-information/what-s-new-in-idmc/current-version/what-s-new/informatica-mcp-servers-and-ai-agent-engineering/important-notices.html)
- [Introduction to Informatica MCP servers (still references protocol 2025-06-18)](https://docs.informatica.com/claire/mcp-servers/current-version/getting-started-with-informatica-mcp-servers/introduction-to-informatica-mcp-servers.html)

### SAP MDG — Updated
**Summary:** SAP's Q2 2026 earnings call on July 28 re-centered its AI story on the **AI Agent Hub** — CEO Christian Klein positioned it as "our command center to discover, manage and govern SAP and non-SAP agents, MCP servers and more" — and confirmed that agents will be priced "based on value." Beta programs for Joule Work and the new Suite were "immediately oversubscribed." A companion SAP Sapphire 2026 glossary published the same day fixes Q4 2026 GA for enhanced A2A in Joule, introduces a dedicated **ABAP MCP** in the ABAP development environment, and formalizes NVIDIA / Anthropic / n8n as first-class partners inside Joule Studio. Because MDG data reaches AI via SAP Business Data Cloud, MDG continues to inherit this MCP posture by default — but there is still no MDG-specific roadmap communication.
**Why it matters:** SAP is now explicitly using "MCP servers" in the CEO's earnings-call vocabulary — a signal that MCP has crossed from technical spec into commercial narrative, and that the Hub/Gateway/Joule Studio stack is the endorsed pathway for MDG-adjacent MCP tooling.
**Source:**
- [SAP AI Agents: Where Are the CX Wins? — CX Today (July 28, 2026)](https://www.cxtoday.com/ai-automation-in-cx/sap-ai-agents-customer-service-wins/)
- [SAP Sapphire 2026 Glossary: AI Agents & Joule (s-peers, July 28, 2026)](https://s-peers.com/en/wiki/sap-sapphire-2026-glossar/)
- [Model Context Protocol (MCP) — SAP BTP AI Best Practices](https://btp-ai-bp.docs.sap/docs/technical-view/agentic-ai/mcp)

### Reltio — Updated
**Summary:** Bi-weekly release **2026.1.7.0** rolled out to Production tenants on July 31, 2026. Two new capabilities land in the AgentFlow Agent Builder: (1) **Agent Blueprint** — an AI-assisted feature that takes a natural-language description of an agent's purpose, users, use cases and constraints and generates an initial agent configuration, a system prompt, and a recommended set of MCP tools; (2) admins can now update all published agents in a tenant, regardless of original author. The same release notes formally register the **Reltio Ontology Builder** as an agentic web experience on reltio.com (no tenant, no credentials, no cost) that translates legacy source schemas into a Reltio-ready canonical model in minutes.
**Why it matters:** Reduces the friction to author governed MCP-backed agents from "days" to "minutes" — a direct parity move against Profisee's Aisey and Akeneo's Agentic Ziggy, and a data point for how quickly MCP tool selection is being automated for non-developers.
**Source:**
- [Reltio 2026.1 bi-weekly Release Notes — 2026.1.7.0 (July 31, 2026)](https://docs.reltio.com/en/reltio/whats-new-and-notable/whats-new-at-a-glance/release-notes-at-a-glance/2026.1-release-notes/2026.1-bi-weekly-release-notes-rn)
- [Reltio Ontology Builder — product page](https://www.reltio.com/ontology-builder/)

### Salsify — Updated
**Summary:** Salsify kicked off a new three-part webinar series, **"AI in Salsify: A Practical Playbook for Agentic Commerce Readiness"**, with the first session on July 30, 2026 (foundational product-content requirements for AI agents; in-platform demo and customer story). Continuation sessions on AI-powered workflows and syndication to shopping bots follow in August–September. Companion whitepaper **"Mastering the Agentic Shelf: A PXM Playbook for AI-Fueled Growth"** is now published, and the co-authored Azoma / Digital Shelf Institute "5 C's of Agentic Commerce" framework is being positioned as the new industry standard. No new MCP capabilities announced.
**Why it matters:** MCP-adjacent. Salsify is now running a sustained multi-month go-to-market cadence around "agentic shelf" readiness rather than a single launch splash — indicative of a shift from product marketing to category-shaping.
**Source:**
- [AI in Salsify: A Practical Playbook for Agentic Commerce Readiness — webinar series](https://www.salsify.com/resources/webinar/ai-in-salsify-a-practical-playbook-for-agentic-commerce-readiness)
- [Mastering the Agentic Shelf: A PXM Playbook for AI-Fueled Growth — whitepaper](https://www.salsify.com/resources/whitepaper/-agentic-shelf-pxm-playbook-ai-growth)
- [A New Framework: The 5 C's of Agentic Commerce (Salsify blog)](https://www.salsify.com/blog/a-new-framework-the-5-cs-of-agentic-commerce-salsify)

### Syndigo — Updated
**Summary:** Novi (AI-visibility platform for ChatGPT / Gemini product discovery) announced a strategic integration with Syndigo on July 22, 2026, creating an automated pipeline that pushes Novi's AI-optimized product content directly into Syndigo's syndication engine for publication across Amazon, Walmart and Target — eliminating manual copy/paste while enforcing retailer-specific taxonomy and publishing guidelines. Positioned in third-party coverage as "infrastructure for the agent-driven economy." No explicit MCP messaging; extends Syndigo's Synapse / Conversion Framework agentic PXM narrative.
**Why it matters:** MCP-adjacent. Reinforces the emerging separation between "content optimized so LLMs can *find* products" (Novi) and "the syndication substrate that carries governed product data to endpoints" (Syndigo) — a useful frame for Stibo's own AI-ready product data messaging.
**Source:**
- [Novi Launches New Integration to Flow AI-Optimized Product Content Directly into Syndigo (MarTech Series, July 22, 2026)](https://martechseries.com/content/novi-launches-new-integration-to-flow-ai-optimized-product-content-directly-into-syndigo-helping-brands-accelerate-content-syndication/)
- [Novi & Syndigo Partner on AI Product Content (CMO First)](https://cmofirst.com/marketing/novi-partners-with-syndigo-to-directly-flow-ai-optimized-product-content/)

## 3. Notable Patterns

- **MCP `2026-07-28` spec ships — vendor compatibility is now a competitive proof-point.** With the biggest MCP revision since launch officially released and Tier-1 SDKs GA, the next 4–8 weeks will separate vendors who ship an explicit "we support 2026-07-28" statement from those who don't. Informatica's docs currently still reference `2025-06-18`.
- **Natural-language agent authoring is becoming table stakes on top of MCP.** Reltio's Agent Blueprint (recommends MCP tools from a plain-English brief) joins Profisee's Aisey re-architecture (Microsoft Agent Framework, ~10-minute environment configuration) and Akeneo's Agentic Ziggy — the value-add is shifting from "we expose MCP" to "we generate the agent, its prompt and its tool selection for you."
- **The narrative is bifurcating: MDM/PIM vendors emphasize governed MCP tool-calling, while PXM/syndication vendors emphasize AI-readable content pipelines (Salsify, Novi–Syndigo).** Both are MCP-adjacent, but they are converging on different halves of the agent stack — a useful lens for Stibo's dual MDM+PIM positioning.

## 4. No Relevant Updates

- **Profisee** — no new public news this week; 2026.R2 (July 8) with Aisey re-architected on Microsoft Agent Framework and expanded MCP surface remains current.
- **Akeneo** — no new public news this week; Summer 2026 "Agentic Ziggy" release (July 8) on top of the Akeneo MCP Server remains current (Deminar on July 29 is a marketing event on already-announced capabilities).
- **Inriver** — no new public news this week; Summer 2026 release (June 30) with enhanced MCP endpoints, MCP Code Writer and the Enrich Assistant remains current.
- **Pimcore** — no new public news this week; Platform 2026.2 GA (July 9) with continued expansion of the MCP-based Agent Bundle remains current (patch v2026.2.4 shipped July 21 is maintenance).

## 5. Suggested Follow-Up

- Track which of the nine vendors is first to publish an explicit **MCP `2026-07-28` compatibility statement** (Informatica, Reltio, SAP, Profisee, Akeneo are the most likely candidates given prior MCP investment). Timing here is a leading indicator of platform seriousness.
- Consider whether Stibo Systems' agent-authoring story should now include a **"generate an agent from a natural-language brief"** analogue to Reltio Agent Blueprint / Profisee Aisey / Akeneo Agentic Ziggy — the "just expose MCP" bar is being raised to include MCP tool auto-recommendation.
- Monitor SAP MDG-specific roadmap communications post-Q2 earnings; the AI Agent Hub / Joule Work / MCP Gateway commercial framing is now firmly in place at group level, but MDG-specific product signal remains thin and is a potential window for differentiated Stibo messaging.
