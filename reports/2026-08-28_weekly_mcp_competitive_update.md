Subject: Weekly MCP Competitive Update – August 21, 2026 to August 28, 2026

Hi Mark,

Here is this week's concise MCP competitive intelligence update.

1. Executive Summary
- Pimcore announced a change of control on August 27 — London-based Tenzing Private Equity acquired the majority stake from Nordwind Growth, with co-founders remaining and an explicit commitment to preserve open core plus the Data Spine and MCP-based Agent SDK roadmap.
- Reltio 2026.1.9.0 hit production on August 28, adding Reltio Docs for You (AI-personalized documentation) and Git integration in Reltio IDE — extending the AgentFlow/MCP developer surface into version-controlled DevOps workflows.
- Salesforce Q2 FY27 earnings (August 26) reported a $456M Informatica revenue contribution and folded Informatica into a new "Data 360, Headless Platform, and Other" reporting segment; CEO Marc Benioff introduced "AIforce" as the "trusted enterprise harness" for agents. MCP docs still reference protocol 2025-06-18.
- Inriver added OrigoVero as a technology partner (August 27) to feed governed PIM data into unit-level Digital Product Passports — repositioning governed PIM as the source of truth for EU DPP compliance and, by extension, agent verification.
- One month after MCP 2026-07-28 shipped, none of the nine tracked vendors has yet issued a public compatibility statement.

2. Key Updates This Week

Company: Pimcore
Status: New
Summary: Tenzing acquired the controlling stake in Pimcore from Nordwind Growth (announced August 27, subject to antitrust clearance). Co-CEOs Dietmar Rietsch and Matthias Blauth stay in role. Pimcore's own announcement explicitly commits to keeping the platform open-core and preserving the Data Spine + AI-native roadmap and the MCP-based Agent SDK. Legal advisor Dechert confirmed the deal in a same-day release, and Tech Times framed it as a PE bet that "enterprise AI fails without governed data."
Why it matters: A PE thesis built explicitly around governed data as the bottleneck for enterprise AI — validating the MCP-and-governance category Stibo Systems competes in. Roadmap continuity of the MCP Agent SDK means the "agents as first-party governed participants" narrative accelerates rather than pauses.
Source:
- We built the layer enterprise AI is about to crash into. Now we scale it. (Pimcore, Aug 27) — https://pimcore.com/en/resources/blog/pimcore-tenzing-next-chapter
- Dechert Advises Tenzing on Its Investment in Pimcore (Aug 27) — https://www.dechert.com/knowledge/news/2026/8/dechert-advises-tenzing-on-its-investment-in-pimcore.html
- Pimcore Sold to Tenzing as PE Bets That Enterprise AI Fails Without Governed Data (Tech Times, Aug 27) — https://www.techtimes.com/articles/325825/20260827/pimcore-sold-tenzing-pe-bets-that-enterprise-ai-fails-without-governed-data.htm

Company: Reltio
Status: Updated
Summary: 2026.1.9.0 reached PRD on August 28. Two agent/MCP-adjacent additions: Reltio Docs for You, an AI-powered application that generates personalized guides from official Reltio documentation, and Reltio IDE + Git integration, letting VS Code/Cursor users manage Reltio business configuration in a shared Git repo with CI/CD-style review before applying to a tenant. RDM Autopilot also expanded to auto-resolve unmapped source values by similarity and frequency.
Why it matters: Reltio is widening the "AI-assisted implementation" surface around AgentFlow/MCP — from configuration authoring (IDE) into DevOps (Git) and self-service enablement (personalized docs). Sharpens the pitch that a governed MDM/MCP platform can be operated as code.
Source:
- 2026.1.9.0 bi-weekly Release Notes (Reltio Docs, Aug 28) — https://docs.reltio.com/en/reltio/whats-new-and-notable/whats-new-at-a-glance/release-notes-at-a-glance/2026.1-release-notes/2026.1-bi-weekly-release-notes-rn
- Reltio IDE overview (Reltio Docs, updated Aug 13) — https://docs.reltio.com/en/developer-resources/ai-integrations/reltio-ide-overview
- reltio-ai/reltio-ide v1.0.17 release (GitHub, Aug 28) — https://github.com/reltio-ai/reltio-ide/releases

Company: Informatica
Status: Updated
Summary: Salesforce reported record Q2 FY27 results on August 26 with a $456M Informatica revenue contribution ($440M subscription); FY27 guidance raised. Informatica now sits inside a new "Data 360, Headless Platform, and Other" reporting segment alongside Agentforce MuleSoft and Tableau. CEO Marc Benioff introduced "AIforce" as "our trusted enterprise harness" that exposes Salesforce data, workflows, business logic, actions, and governance to "every agent, model, and interface." Informatica's public MCP docs still reference protocol 2025-06-18.
Why it matters: Informatica is being productized as the governed data plane behind Salesforce's agent runtime, and the AIforce naming makes the "trusted harness" positioning explicit. Reinforces the strategic case for MDM/MCP as the enterprise governance layer beneath any agent surface.
Source:
- Salesforce Delivers Record Second Quarter Fiscal 2027 Results (Aug 26) — https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/
- Introduction to Informatica MCP Servers (Updated Aug 2026) — https://docs.informatica.com/claire/mcp-servers/current-version/getting-started-with-informatica-mcp-servers/introduction-to-informatica-mcp-servers.html

Company: Inriver
Status: Updated
Summary: Inriver announced a technology partnership with OrigoVero on August 27 to connect governed PIM data into unit-level Digital Product Passports (dual-factor QR + NFC, blockchain-anchored, GS1 Digital Link and EPCIS 2.0-aligned). Positioned against the EU ESPR / DPP registry deadlines. Separately, an Aug 26 Inriver resource, "5 Signs your traditional SaaS isn't built for AI agents," continues the three-protocol (ACP / UCP / MCP) framing introduced on Aug 17.
Why it matters: Reframes governed PIM as the upstream source of truth for both AI agents (MCP) and unit-level compliance (DPP) — a "one trusted record, verifiable end to end" pitch that raises the bar for what "trusted data for AI" means. MCP-adjacent for the ACP/UCP/MCP messaging; directly relevant to Stibo's Digital Product Passport positioning.
Source:
- Inriver and OrigoVero connect governed PIM data to unit-level Digital Product Passports (SAPinsider, Aug 27) — https://sapinsider.org/blogs/inriver-and-origovero-connect-governed-pim-data-to-unit-level-digital-product-passports-for-product-verification-traceability-and-compliance/
- OrigoVero × Inriver — from product data to a verifiable passport — https://www.origovero.com/partners/inriver
- 5 Signs your traditional SaaS isn't built for AI agents (Inriver, Aug 26) — https://www.inriver.com/resources/signs-your-traditional-saas-isnt-built-for-ai-agents/

3. Notable Patterns
- Investors are pricing "governed data for AI" as the enterprise thesis: Tenzing's Pimcore acquisition explicitly justifies the deal on governance being the bottleneck for enterprise AI production — mirroring the language already in use at Informatica, Reltio, Profisee, and Syndigo.
- The MCP surface is quietly extending into DevOps and Digital Product Passport territory: Reltio adds Git-based configuration lifecycle to its MCP-adjacent IDE, while Inriver pushes governed PIM into unit-level DPPs. In both cases the MDM/PIM platform is being positioned upstream of any protocol layer.
- Silence on MCP 2026-07-28 compatibility persists across the vendor set one month after the spec shipped; Informatica's docs, re-stamped "Updated: August 2026," still cite protocol version 2025-06-18 while Salesforce's Aug 26 earnings materials introduce AIforce as the trust harness without naming a spec version.

4. No Relevant Updates
- SAP MDG — no MDG-specific news in the window; Aug 21 SAP News Center piece on "Agentic AI Could Rewrite the Economics of SAP Transformation" covers ECC-to-S/4HANA migration agents, not MDG.
- Profisee — no new public news; 2026.R2 (July 8) remains current.
- Akeneo — no primary-source news in the window. Ecommerce-times.com published a fourth contradictory Adobe-acquires-Akeneo article this week (Aug 25, $200M/closed Aug 8) with no corroboration from Adobe, Akeneo, PR Newswire, BusinessWire, or Akeneo's own leadership page; excluded from the main body per the source rule.
- Salsify — no new product/MCP capabilities; Aug 19 workflow-library republish and Aug 20 "SOS: The Signals for AI Visibility" blog continue the agentic-commerce thought-leadership cadence only.
- Syndigo — no new news; Aug 19 "State of Product Experience 2026" remains the current headline asset.

5. Suggested Follow-Up
- Watch Tenzing's operational cadence at Pimcore (Sherpa Programme, bolt-on M&A) — a PE roll-up of governance-adjacent open-source assets would materially shift the MDM/PIM landscape.
- Read Salesforce's "AIforce" positioning in full and consider whether Stibo Systems should sharpen the "trusted governance harness for agents" framing before the term becomes market vocabulary.
- Monitor Inriver's DPP + MCP framing — if governed PIM becomes the default DPP source, Stibo Systems' MDM heritage plus MCP posture is a differentiator worth codifying.
