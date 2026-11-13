# Weekly MCP Competitive Update — November 6, 2026 to November 13, 2026

**To:** mjan@stibosystems.com
**Subject:** Weekly MCP Competitive Update – November 6, 2026 to November 13, 2026

---

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

## 1. Executive Summary

- **Informatica formalises a "Three Pillars + Gov/Trust Gateway" MCP architecture** at the Nov 10 Tech Tuesday — the MCP catalog is now backed by an explicit multi-tenant control plane with OAuth 2.0/2.1, prompt-injection and PII input safety, human-in-the-loop escalation and bulk circuit breakers. Pairs with a new Nov 6 demo video in which CDGC sensitivity classification plus the Omni Gateway blocks HIPAA-protected context from reaching AI agents in real time.
- **Syndigo turns the Microsoft deal into a governance narrative.** New Nov 10 blog by CPO Tarun Chandrasekar ("You're Not Deploying an Agent. You're Deploying a Liability.") positions agentic AI as an accountability and data-trust problem, cites Gartner's 40%+ agentic-project cancellation forecast and references Microsoft Frontier Tuning — the first strategic follow-through to the Nov 2 Microsoft Global ISV partnership.
- **Pimcore's MCP footprint gains a public reference implementation.** At Pimcore Community Dev Days 2026 (Nov 10 Frankfurt) Sebastian Bergmann keynoted on coding agents and CKEditor DevRel Ondřej Chrastina shipped the open-source "Pimcore AI Guidepost" — a Pimcore 2026.3 skeleton with 44 agent skills, an AGENTS.md map and the Datahub Simple REST MCP server wired in.
- **Pimcore v2026.3.5 (Nov 10–11) adds agent-relevant security hardening** — restricted `unserialize()` for document editables, signed WebDAV delete log, read-only stand-ins for stored expression evaluation, editable-password masking and view-permission enforcement on frontend previews. No Agent Bundle feature changes.
- **Sixteen weeks post-spec, still zero MCP 2026-07-28 compatibility statements** from any of the nine tracked vendors. SAP Enterprise AI Gateway remains "announced, no date" (Q1 2027 target); Reltio 2026.2.2.0's DEV/TEST deployment slipped from Nov 13 to Nov 16 with PRD still Nov 20.

## 2. Key Updates This Week

### Company: Informatica
**Status:** Updated
**Summary:** The **Nov 10, 2026 Tech Tuesday "Data You Can Trust: Building Enterprise-Grade Integration in the Cloud"** (Sreehari Desai, Dihitha Sai Nadella) formally documents the architecture under Informatica's MCP catalog as a **"Three Pillars"** framework — Headless Integration (API-first, 500+ connectors, Secure Agent hybrid runtime), Real-Time Data Quality (in-flight validation across Accuracy, Completeness, Consistency, Timeliness, Validity) and Enterprise Governance (lineage, policy-as-code for GDPR/HIPAA/CCPA, searchable catalog). The slide deck exposes a **multi-tenant "Gov/Trust Gateway"** sitting between engagement surfaces (AI agents, apps) and the IDMC MCP servers, enforcing OAuth 2.0/2.1 authentication, prompt-injection/PII input safety, human-in-the-loop escalation, and circuit breakers on bulk hard limits — with CDGC Metadata Search, CDGC Data Quality Score, Job Management and CLAIRE Orchestrator named as the agent-facing MCP servers. A companion **Nov 6 support video "Protecting Sensitive Data with MCP Trust Gates & CDGC Classification"** demonstrates CDGC free-text sensitivity classification combined with Omni Gateway route-ceiling policies blocking HIPAA-protected clinical visit reasons from reaching an AI agent without manual intervention.
**Why it matters:** This is the clearest public Informatica articulation yet of MCP as a *governed enterprise control plane*, not just a set of connectors — the Gov/Trust Gateway diagram is the first time Informatica has publicly described its own equivalent of SAP's AI Agent Hub verification layer and MuleSoft's Omni Gateway for its MCP catalog. Raises the bar on "enterprise-grade MCP" messaging for Stibo Systems.
**Source:**
- [Informatica Success Portal — Tech Tuesday "Data You Can Trust: Building Enterprise-Grade Integration in the Cloud" (Nov 10, 2026)](https://success.informatica.com/explore/tt-webinars/data-you-can-trust--building-enterprise-grade-integration-in-the.html)
- [Tech Tuesday slide deck (PDF) — "Data You Can Trust" with Informatica MCP Servers Technical Architecture](https://success.informatica.com/content/dam/informatica-cxp/techtuesdays-slides-pdf/Data%20You%20Can%20Trust%20Building%20Enterprise%20-%20Grade%20Integration%20in%20the%20Cloud.pdf)
- [Informatica Support — "Protecting Sensitive Data with MCP Trust Gates & CDGC Classification" (Nov 6, 2026)](https://success.informatica.com/videos/support-videos/Yi2mjassXWc.html)

### Company: Syndigo
**Status:** Updated
**Summary:** On **Nov 10, 2026** Syndigo Chief Product Officer Tarun Chandrasekar published **"You're Not Deploying an Agent. You're Deploying a Liability."** — the first strategic positioning piece after the Nov 2 Microsoft Global ISV partnership announcement. The post reframes the agentic-AI risk conversation as a *governance and accountability* problem (not a model problem), cites **Gartner's forecast that more than 40% of agentic-AI projects will be cancelled by the end of 2027**, and argues that leaders must answer two questions before deploying an agent — *who verifies the data the agent is grounded in, and who is accountable when a decision is wrong*. The piece references **Microsoft Frontier Tuning (private preview)** as an example of tuning small models on customer-specific workflows instead of relying on frontier models alone, tying Syndigo's PX Cloud + Microsoft Azure footprint to that direction.
**Why it matters:** This is Syndigo's post-partnership narrative: it is now positioning Synapse / PX Cloud explicitly as the *trusted-data accountability layer* under agentic commerce running on Microsoft Foundry and Agent 365. MCP-adjacent (no explicit MCP mention) but tightens the "governed data for agents" messaging that Stibo Systems, Profisee, Akeneo and Reltio are all competing on.
**Source:**
- [Syndigo blog — "You're Not Deploying an Agent. You're Deploying a Liability." (Tarun Chandrasekar, Nov 10, 2026)](https://syndigo.com/blog/agentic-ai-trusted-data-governance/)
- [Syndigo News — Nov 2, 2026 Microsoft Global ISV partnership (context)](https://syndigo.com/news/syndigo-microsoft-ai-commerce-partnership/)

### Company: Pimcore
**Status:** Updated
**Summary:** Two developments this week. (1) **Pimcore Community Dev Days 2026 (PCDD) delivered Nov 10, 2026 in Frankfurt** — the agenda centred on AI coding agents: **Sebastian Bergmann** (author of PHPUnit) keynoted "Development with Coding Agents" on using LLM tools safely with PHP/Symfony/PHPStan guardrails, and **Ondřej Chrastina** (Developer Advocate at CKEditor) presented "AI Best Practices for Your Product" and open-sourced the **Pimcore AI Guidepost** — a working Pimcore 2026.3 skeleton with **44 vendored agent skills**, an `AGENTS.md` map of Pimcore's AI resources, and the **Datahub Simple REST MCP server** wired in. The guidepost explicitly identifies the Agent Bundle's guardrails and the Datahub Simple REST MCP as the two MCP-facing doors into Pimcore today. (2) **Pimcore v2026.3.5 released Nov 10–11, 2026** — a maintenance release with ~5 GHSA security patches including restricted `unserialize()` for document editables (`pimcore.documents.editables.unserialize_allowed_classes`), a signed WebDAV delete log, read-only stand-ins for stored expression evaluation, editable-password masking and view-permission enforcement on frontend object preview. No Agent Bundle beta or Datahub Simple REST MCP feature changes.
**Why it matters:** The guidepost is the first public, runnable third-party reference implementation of Pimcore's MCP surface, and it adds narrative weight to Pimcore's Visionary PIM MQ positioning; the 2026.3.5 security patches continue Pimcore's pattern of pushing agent-relevant hardening (serialization, auth, expression evaluation) into maintenance releases.
**Source:**
- [PCDD 2026 agenda — Pimcore Community Dev Days, Frankfurt (Nov 10, 2026)](https://www.pluswerk.digital/en/about-us/pluswerk-at-events/pimcore-community-dev-days-2026)
- [Ondřej Chrastina — "AI Best Practices for Your Product" talk (Nov 10, 2026)](https://ondrej.chrastina.dev/talks/ai-best-practices-for-your-product-pcdd-2026/)
- [Pimcore AI Guidepost — GitHub repo (Simply007/pcdd26-pimcore-ai-guidepost)](https://github.com/Simply007/pcdd26-pimcore-ai-guidepost)
- [Pimcore v2026.3.5 release notes — GitHub (Nov 11, 2026)](https://github.com/pimcore/pimcore/releases)
- [Pimcore 2026.3.5 upgrade notes — security changes](https://docs.pimcore.com/platform/Pimcore/Upgrade_Notes/)

### Company: Salsify
**Status:** Updated
**Summary:** **Nov 12, 2026 blog "The Digital Shelf Is Evolving — Is Your Commercial Strategy?"** (Lisa Schrumpf, Salsify) recaps the "One Source of Truth" panel at the Digital Shelf Summit London with Revlon, Ansell and Lindt & Sprüngli. The post argues that AI-powered discovery (not keyword search) will increasingly determine which products get surfaced, considered and purchased, and that brands need governed, structured, trustworthy product data as the foundation for agentic commerce. Positions Salsify as the "single, trusted source of product information" layer that agentic shopping assistants depend on. No reference to the Model Context Protocol by name.
**Why it matters:** Salsify continues the AEO/GEO-focused agentic-commerce positioning it has used all autumn, and keeps steering around an explicit MCP statement. Reinforces the pattern we flagged last week — the Nov 18 "What's New at Salsify: Into 2027" webinar remains the next realistic catalyst for any first explicit Salsify MCP GA announcement. MCP-adjacent only.
**Source:**
- [Salsify blog — "The Digital Shelf Is Evolving — Is Your Commercial Strategy?" (Lisa Schrumpf, Nov 12, 2026)](https://www.salsify.com/blog/the-digital-shelf-is-evolving-is-your-commercial-strategy-salsify)
- [Salsify — "What's New at Salsify: Into 2027" webinar (Nov 18, 2026, upcoming)](https://www.salsify.com/resources/webinar/whats-new-at-salsify-q4-2026)

## 3. Notable Patterns

- **"Gov/Trust Gateway" is becoming the shared MCP reference architecture.** Informatica's Three Pillars deck (Nov 10) joins SAP Enterprise AI Gateway, SAP AI Agent Hub verification, Reltio's OAuth 2.0 MCP server, Pimcore's native OAuth 2.0 server and MuleSoft's Omni Gateway in a now-converged pattern: a dedicated control plane between AI agents and enterprise MCP tools enforcing auth, policy, PII/prompt-injection safety, HITL and circuit breakers. "MCP you plug in" is being quietly replaced by "MCP behind a gateway you govern."
- **CPO-level narrative shifts from product to accountability.** Syndigo's Nov 10 CPO post and Informatica's Gov/Trust Gateway framing both move the agentic-AI discussion up from capability to *liability and verification*, mirroring Reltio's and SAP's "autonomous agents under human oversight" positioning. The competitive battleground is shifting from feature lists to governance posture.
- **Community-driven agent evidence is now a competitive asset.** Last week Akeneo had DwyerOmega Part 2; this week Pimcore gains a public third-party AI Guidepost that makes its MCP surface explorable in minutes. Vendors whose MCP surface is only documented in release notes risk losing mindshare to those whose MCP surface has runnable community references.

## 4. No Relevant Updates

- **SAP MDG** — No new MCP-material primary content this week. SAP Enterprise AI Gateway status unchanged (Q1 2027 target); AI Governance Assistant Early Adopter Care window still November.
- **Reltio** — Nov 10 Community Show ("Fresh look, familiar workflows: UI Modernization in Reltio") is non-MCP. 2026.2.2.0 DEV/TEST deployment rescheduled from Nov 13 to Nov 16 with PRD still Nov 20 — next MCP-material delta expected then.
- **Profisee** — No new press, blog or release note. Profisee Anywhere remains on track for December 2026 GA.
- **Akeneo** — No new primary content after last week's DwyerOmega Part 2. Next scheduled catalyst is the Winter release cycle preview.
- **Inriver** — Nov 7–8 release notes (masked extension settings in audit log, REST API enhancements for Language Roles) and Nov 9 Inspire UI update (Enrich / Generate & translate workspace redesign) contain no MCP Server or AI-agent delta.

## 5. Suggested Follow-Up

- **Benchmark Informatica's "Gov/Trust Gateway" against Stibo Systems' own MCP control-plane messaging.** The Nov 10 slide deck is now a concrete reference competitors will point to in RFPs; our positioning on auth, PII/prompt-injection safety, HITL escalation and circuit breakers should answer the same seven checkboxes.
- **Pre-read Syndigo's "Deploying a Liability" blog before any customer conversation touching Microsoft Fabric / Agent 365.** Syndigo is explicitly positioning its data layer as the accountability layer for agentic commerce on Microsoft; Stibo Systems' MDM governance story should foreground the same "who verifies the data, who is accountable" framing.
- **Monitor Nov 18 Salsify "Into 2027" webinar and Nov 20 Reltio 2026.2.2.0 GA** — both are the next realistic MCP-material catalysts in the set.
