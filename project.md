# PROJECT.MD — SHITTYSHIT GLOBAL PROJECT TEMPLATE
*Version 1.0 | Established 2026-05-07*
*This file is the intake form, the standing orders, and the session log for every project.*
*Agents read this first. Agents write back here. Kevin reviews.*

---

## IDENTITY BLOCK
```yaml
---
project_name:       # Full name
codename:           # Short slug, no spaces (e.g. KISS_DASH, IRISH_MYTH)
status:             # mudroom | active | parked | archive
type:               # content | code | infra | creative | photo | ai | product
revenue:            # true | false
gumroad_ready:      # true | false | pending
priority:           # 1 (highest) - 5 (lowest)
spun_up:            # YYYY-MM-DD
last_updated:       # YYYY-MM-DD (auto-update on every session)
owner:              # kevin | agent | shared
tags:               # array — use standard tags below
blocker:            # null | description of what's stopping progress
---
```

### Standard Tags
`#revenue` `#infra` `#content` `#creative` `#ai` `#photo` `#code`
`#audio` `#video` `#podcast` `#blog` `#product` `#parked` `#deprecated`

---

## WHAT THIS IS
*2-3 sentences max. What does this project produce? Who is it for? Why does it exist?*

> [FILL ON CREATION]

---

## ASSETS IN THIS FOLDER
*List every meaningful asset here so the next agent doesn't have to scan blindly.*
*Format: filename | type | status (raw | processed | final)*

| File | Type | Status | Notes |
|------|------|--------|-------|
|      |      |        |       |

---

## TOOLS — ALWAYS ON
*These fire on project folder creation. Minimal. Core only.*

- [ ] **Obsidian MCP** — vault read/write for this project
- [ ] **Filesystem** — project folder access

---

## TOOLS — ON DEMAND
*Available but not loaded at spin-up. Add/remove per project type.*
*Agent checks project `type` field and activates relevant set.*

### Universal (all project types)
- [ ] **Claude Code** — agentic execution
- [ ] **Linear** — issue tracking (team: Aishitty)
- [ ] **GitHub** — version control

### Content / Writing
- [ ] **NotebookLM** — synthesis pass (ShittyLoop)
- [ ] **Gumroad** — publish when ready

### Code / Infra
- [ ] **n8n** — workflow automation (LACES)
- [ ] **Qdrant** — vector storage / RAG
- [ ] **Ollama** — local inference (LACES)
- [ ] **Supabase** — database if needed

### Audio / Video / Podcast
- [ ] **[TBD — Whisper/Parakeet]** — transcription (Handy fork)
- [ ] **[TBD — video pipeline]** — export workflow

### Photo
- [ ] **BIGSHOT workflow** — see .BIGSHOTNYC project

---

## SKILLS AVAILABLE
*Reusable instruction sets this project can invoke.*
*Skills live in tools_skills/ — reference by name.*

- [ ] **intake-classification** — how to process mudroom drops
- [ ] **spec-writing** — Specshitty five-artifact discipline
- [ ] **token-reduction** — manifest-first, metadata-before-content
- [ ] **competitive-sweep** — scan landscape for similar projects

*[Add project-specific skills as they develop]*

---

## CURRENT STATUS
*What is the actual state right now? Written by agent at session end.*
*One paragraph. Factual. No fluff.*

> [AGENT WRITES HERE]

---

## NEXT ACTION
*Single next step. Not a roadmap. One thing. Owned by someone.*

| What | Who | By when |
|------|-----|---------|
|      |     |         |

---

## OPEN QUESTIONS
*Decisions unmade. Blockers unresolved. Things that need Kevin.*

- [ ] [question]

---

## MUDROOM LOG
*Raw intake that arrived but hasn't been fully processed yet.*
*Utility agent clears this as items get classified and filed.*

| Date | Item | Source | Status |
|------|------|--------|--------|
|      |      |        | pending |

---

## SESSION LOG
*Agent writes a one-line entry at the end of every session.*
*Date | Agent | What happened | What changed*

| Date | Agent | Summary | Files Changed |
|------|-------|---------|---------------|
|      |       |         |               |

---

## GOVERNANCE NOTES
*Standing rules specific to this project. Override global CLAUDE.md only when necessary.*

> [FILL IF NEEDED — otherwise global CLAUDE.md governs]

---
*Global template v1.0 — born from .PROJECTS_SHITTYSHIT/CLAUDE.md*
*Do not add Spinner references to this file. Spinner has its own folder.*
*Export pipeline, SEO, social media workflows are downstream — not here.*
