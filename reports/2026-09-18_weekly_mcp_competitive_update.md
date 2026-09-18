Subject: Weekly MCP Competitive Update – September 11, 2026 to September 18, 2026

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

## 1. Executive Summary

- Dreamforce 2026 (Sept 15–17) is the single biggest MCP news event of the year so far — Salesforce launched AIforce with Data 360 MCP Server (GA), Headless 360 MCP Server (open beta, GA November), Slackbot MCP Server and 100+ Agent Skills, all built on Informatica-grounded Data 360.
- Informatica's own Sept 16 announcement went live — a Plugin for the Claude Enterprise Platform on Claude's Plugin Marketplace that connects Claude to Informatica via a new "Secure MCP Gateway" fronting the Catalog Discovery MCP and CLAIRE Data Exploration Agent MCP.
- Reltio kicked off a book-length "system of context" campaign — Manish Sood + Venkat Venkatraman published "Agentic Intelligence: Strategy at the Speed of Data" (Forbes Books, Sept 15), the first mass-market vehicle for the SAP-owned Reltio narrative.
- Akeneo, Salsify and Inriver produced MCP-adjacent thought leadership only (UK cut of the Reality Check survey; "AI Workforce" and DetailPage Part 3; a "distribute-and-forget is dead" feedback-loop piece).
- Seven weeks post-spec, Salesforce/Informatica still did not publish a spec-version compatibility statement for MCP 2026-07-28; Salesforce's own MCP servers ship without a stated protocol version.

## 2. Key Updates This Week

### Informatica — New

Summary: At Dreamforce 2026 (Sept 15–17) Salesforce unveiled AIforce, a "live interface layer" bringing Data 360 and Informatica data services to any AI interface via MCP. The Data 360 MCP Server (GA), Headless 360 MCP Server (open beta, GA November), Slackbot MCP Server and 100+ Agent Skills were introduced. Informatica followed on Sept 16 with a dedicated blog announcing the Informatica Plugin for the Claude Enterprise Platform on Claude's Plugin Marketplace, connecting Claude CoWork and Claude Code to Informatica through a newly named **Secure MCP Gateway** fronting the Catalog Discovery MCP and CLAIRE Data Exploration Agent MCP.

Why it matters: This is the first time Informatica's MCP servers reach an end-user chat surface (Claude) via a first-party, publicly listed plugin — moving Informatica from developer plumbing to buyer-visible MCP delivery. AIforce also formalises Informatica as the trusted data foundation under Salesforce's Enterprise AI Harness.

Source:
- [Salesforce Unveils AIforce (Salesforce, Sept 15, 2026)](https://www.salesforce.com/news/stories/aiforce-announcement/)
- [From Model Intelligence to Enterprise Intelligence: Introducing the Informatica Plugin for the Claude Enterprise (Informatica, Sept 16, 2026)](https://www.informatica.com/blogs/introducing-the-informatica-plugin-for-claude-platform.html)
- [Salesforce Introduces the Trusted Enterprise AI Harness (Salesforce, Sept 11, 2026)](https://www.salesforce.com/ap/news/press-releases/2026/09/11/ph-salesforce-introduces-the-trusted-enterprise-ai-harness/)

### Reltio — Updated

Summary: Reltio's Sept 12 blog announced "Agentic Intelligence: Strategy at the Speed of Data," a Forbes Books title co-authored by Reltio founder/CEO Manish Sood and Boston University's Venkat Venkatraman, published Sept 15. The book positions data foundations, enterprise architecture and operating-model change as the prerequisites for agentic AI — a book-length extension of the "system of context" thesis Sood used in the Sept 2–3 WSJ Custom Content wave.

Why it matters: First mass-market thought-leadership vehicle for Reltio under the "an SAP company" umbrella, giving SAP a durable outbound counterweight to Salesforce's Dreamforce narrative. No new product surface, but a clear signal of sustained brand investment.

Source:
- [A New Playbook for the Agentic AI Era — Introducing Manish Sood's New Book (Reltio blog, Sept 12, 2026)](https://www.reltio.com/resources/blog/a-new-playbook-for-the-agentic-ai-era-introducing-manish-soods-new-book-agentic-intelligence/)

### Akeneo — Updated

Summary: On Sept 16 Akeneo issued UK-specific findings from its Agentic Commerce Reality Check Report through Modern Retail: 87% of UK organisations using AI already see measurable returns and connect AI investment particularly closely to efficiency, productivity and revenue growth. Extends the Sept 9 primary press release into local-market amplification.

Why it matters: MCP-adjacent. Regional cut positions Akeneo as the source of primary buyer data on agentic-commerce readiness in the UK — a natural pull surface for its MCP Server + Agentic Ziggy stack in that market.

Source:
- [AI Delivers Measurable Returns for 87% of UK Businesses (Modern Retail, Sept 16, 2026)](https://modernretail.co.uk/ai-delivers-measurable-returns-for-87-of-uk-businesses/)

### Salsify — Updated

Summary: Two content assets landed in the window. Sept 16 blog "The AI Workforce: Giving Your Ecommerce Team a Promotion" argues Salsify agents run natively inside the same platform as the product data (not bolted on) and pulls the "system of record and the system doing the work are the same system" framing forward. Same day, the DetailPage co-branded webinar "AI Path to Purchase — Putting It All Together" (Part 3) aired at 11 a.m. ET. The AI in Salsify Part 3 "Powering Agentic Experiences" session (US date still TBD; Europe Sept 30) will cover federating product data to AI platforms via MCP-adjacent patterns.

Why it matters: MCP-adjacent. Salsify continues to differentiate on native-vs-bolted-on agent execution rather than adding MCP endpoints.

Source:
- [The AI Workforce: Giving Your Ecommerce Team a Promotion (Salsify blog, Sept 16, 2026)](https://www.salsify.com/blog/the-ai-workforce-giving-your-ecommerce-team-a-promotion)
- [Executing Your AEO and GEO Strategy with DetailPage — Part 3 Sept 16 (Salsify)](https://www.salsify.com/resources/webinar/executing-your-aeo-and-geo-strategy-with-detailpage-webinar-series)
- [AI in Salsify: Part 3 "Powering Agentic Experiences" (Salsify)](https://www.salsify.com/resources/webinar/ai-in-salsify-a-practical-playbook-for-agentic-commerce-readiness)

### Inriver — Updated

Summary: Sept 18 resource "Distribute-and-forget is dead: Why product content needs a feedback loop" argues rank-tracking alone misses ~48% of queries surfaced by AI Overviews (BrightEdge) and positions Inriver Digital Shelf Analytics + flexible data model + agentic orchestration as the "single-platform feedback loop" between publish, monitor, diagnose and correct.

Why it matters: MCP-adjacent. Extends Inriver's protocol-agnostic verification-layer positioning from the Aug 17 ACP/UCP/MCP stack piece into an operational feedback-loop pitch — the closest any PIM vendor has come this week to naming AI-Overview-driven drift as a PIM problem to solve.

Source:
- [Distribute-and-forget is dead: Why product content needs a feedback loop (Inriver, Sept 18, 2026)](https://www.inriver.com/resources/distribute-and-forget-product-content-feedback-loop/)

## 3. Notable Patterns

- **First hyperscaler-hosted MCP servers backed by governed enterprise data ship** — Salesforce's Data 360 MCP Server (GA) and Headless 360 MCP Server (open beta) at Dreamforce, with Informatica reaching Claude's Plugin Marketplace on Sept 16 via a Secure MCP Gateway. The "put your MCP servers on the buyer's chat surface" phase has started.
- **Vendor outbound is now book-length and multi-quarter**. Reltio's Sept 15 Forbes Books release and Salesforce's Dreamforce AIforce narrative both frame governed enterprise data as *the* AI-readiness gap — matching Akeneo (Sept 9), Syndigo (Aug 19) and Inriver (Aug 5) primary-research plays. This is now a consensus buyer message.
- **Seven weeks post-spec, still zero MCP 2026-07-28 compatibility statements** across the nine tracked vendors and Salesforce. The new Salesforce-hosted MCP servers do not publish a protocol version; Informatica MCP docs still cite 2025-06-18. Compatibility remains a latent risk buyers can start asking about.

## 4. No Relevant Updates

- SAP MDG — No new MDG-specific news; SAP Business Data Cloud release cadence continues (Reltio and MDG remain listed as core BDC components).
- Profisee — No new news; next release cadence is 26R3 (quarterly).
- Pimcore — v2026.2.12 (Sept 8) and v2026.2.13 (Sept 15) bugfix/security releases only; no Agent Bundle or MCP-based Agent SDK changes. DMEXCO 2026 (Sept 23–24) session "Job Killer or Team Multiplier? The Truth About Agentic Data and Experience Management" (Rietsch, Wed Sept 23) confirmed.
- Syndigo — Only continued on-demand webinar recap content (Sept 4 DPP/2D-barcodes piece); on the ground at ECR iN MOTiON 2026 (Bonn, Sept 16–17). No product news.

## 5. Suggested Follow-Up

- Treat the Dreamforce AIforce launch as the trigger to sharpen Stibo Systems' MCP messaging vs Salesforce/Informatica — specifically the "Secure MCP Gateway" pattern (governed protocol edge + published skills + hosted MCP servers on partner chat surfaces such as Claude).
- Consider whether Stibo Systems should now be first among the nine tracked vendors to publish an explicit MCP 2026-07-28 compatibility statement — a differentiator becomes available as long as Informatica, SAP and the PIM/PXM set stay silent on protocol versioning.
- Use the Reltio book and the Akeneo/Syndigo/Inriver primary-research plays as third-party corroboration in Stibo's own materials — the "governance is the AI-readiness gap" narrative is now vendor-neutral consensus.
