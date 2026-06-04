# TOOLS & SKILLS ROSTER
*Version 1.0 | Established 2026-05-07*
*Source of truth for what's available in the SHITTYSHIT system.*
*Agents read this before recommending tools. Update when stack changes.*

---

## HOW TO READ THIS FILE
- **Status**: `active` | `evaluating` | `parked` | `planned`
- **Where**: `cloud` | `laces` | `local` | `both`
- **Cost**: free | api-usage | subscription | % of sales
- **Load**: `always` | `on-demand` — whether to include at project spin-up

---

## CORE INFRASTRUCTURE

| Tool | What it does | Where | Cost | Load | Status |
|------|-------------|-------|------|------|--------|
| **Claude / Claude Code** | Primary inference + agentic coding | cloud + cli | api-usage | always | active |
| **Obsidian + MCP plugin** | Vault-per-project knowledge layer, MCP bridge | local | free | always | active |
| **n8n** | Workflow automation, agent orchestration | laces (docker) | free | on-demand | active |
| **Ollama** | Local model inference | laces (UM890) | free | on-demand | active |
| **Qdrant** | Vector DB, RAG pipelines | laces (docker) | free | on-demand | active |
| **Filesystem MCP** | Direct file read/write access | local | free | always | active |

---

## PROJECT MANAGEMENT

| Tool | What it does | Where | Cost | Load | Status |
|------|-------------|-------|------|------|--------|
| **Linear** | Issue tracking (team: Aishitty, AIS-*) | cloud | subscription | on-demand | active |
| **GitHub** | Version control (shitty-shit org + idfkai org) | cloud | free/paid | on-demand | active |
| **Notion** | Docs, PRDs, project specs | cloud | subscription | on-demand | active |

---

## REVENUE / DISTRIBUTION

| Tool | What it does | Where | Cost | Load | Status |
|------|-------------|-------|------|------|--------|
| **Gumroad** | Primary storefront — all product revenue | cloud | % of sales | on-demand | active |

---

## AI MODELS

| Tool | What it does | Where | Cost | Load | Status |
|------|-------------|-------|------|------|--------|
| **Claude (Sonnet/Opus)** | Primary | cloud | api-usage | always | active |
| **DeepSeek v4** | Multi-model routing, Obsidian integration | cloud | api-usage | on-demand | evaluating |
| **Gemini** | Multi-model routing via n8n | cloud | api-usage | on-demand | evaluating |
| **Ollama models** | Local inference, LACES stack | local | free | on-demand | active |
| **NotebookLM** | Synthesis pass (ShittyLoop) | cloud | free | on-demand | active |

---

## VOICE / INPUT

| Tool | What it does | Where | Cost | Load | Status |
|------|-------------|-------|------|------|--------|
| **Whisper / Parakeet (Handy fork)** | Local voice capture → prompt pipeline | local | free | on-demand | planned |

---

## EVALUATING / WATCHING

| Tool | What it does | Where | Cost | Load | Status |
|------|-------------|-------|------|------|--------|
| **Superpower** | [Needs repo link — Kevin to provide] | TBD | TBD | on-demand | evaluating |
| **GSD (Get Shit Done)** | [Needs repo link — Kevin to provide] | TBD | TBD | on-demand | evaluating |
| **AnythingLLM** | Local vector DB + RAG + transcription | local | free | on-demand | evaluating |
| **Perplexity** | Research pass | cloud | subscription | on-demand | parked |

---

## SKILLS ROSTER
*Skills are instruction sets — what Claude knows how to DO, not external tools.*
*Stored as .md files in this folder when built out.*

| Skill | What it does | Status |
|-------|-------------|--------|
| **intake-classification** | Process mudroom drops — read, classify, route | planned |
| **spec-writing** | Specshitty five-artifact build discipline | planned |
| **token-reduction** | Manifest-first, metadata-before-content approach | planned |
| **competitive-sweep** | Scan web for similar projects, tools, Gumroad products | planned |
| **project-card-writer** | Generate a filled project.md from raw assets | planned |
| **session-logger** | Write session summary to project.md session log | planned |
| **tool-gap-analysis** | Compare project needs vs available tool roster | planned |

---

## HARDWARE
*The LACES stack — local AI infrastructure.*

| Hardware | Specs | Role |
|----------|-------|------|
| **MINISFORUM UM890 Pro** | AMD Ryzen 9 8945HS, 24GB RAM | Local AI inference, n8n, Docker host |

---

## PENDING
*Tools Kevin mentioned — need repo links or more info before classifying.*

- [ ] **Superpower** — get repo URL
- [ ] **GSD** — get repo URL
- [ ] **Antigravity** — what is this exactly? Project or tool?
- [ ] **Spinners** — separate project folder, not a tool
- [ ] **ShitBird** — agentic browser agent, recon-then-execute model (planned)

---
*Roster v1.0 — maintained by dispatcher Claude in .PROJECTS_SHITTYSHIT*
*When a tool changes status, update this file and relevant project.md files*
