# PROJECT COMPILER WEB
*Agent-guided web interface for multi-modal project intake and synthesis*

---

## IDENTITY BLOCK
```yaml
---
project_name:       Project Compiler Web Interface
codename:           PROJECT_COMPILER_WEB
status:             active
type:               infra | ai | product
revenue:            false
gumroad_ready:      false
priority:           2
spun_up:            2026-05-22
last_updated:       2026-05-22
owner:              kevin
tags:               ['#infra', '#ai', '#product', '#audio', '#video']
blocker:            null
---
```

---

## WHAT THIS IS

A web-based project intake portal that accepts multi-modal input (text, audio, video, images, documents, chat transcripts) and synthesizes them into structured project folders with generated briefs and PRDs.

**Core workflow:**
1. User uploads/inputs project artifacts (docs, audio notes, images, videos, transcripts)
2. Lightweight transcription service handles voice input (not frontier AI)
3. Real-time TTS for reading back content
4. Agent synthesizes all materials into coherent project brief + PRD
5. System creates project folder with original assets + synthesized documents
6. Builds master project list incrementally, one project at a time

**Why it exists:** Kevin works voice-first with handwritten notes and scattered artifacts. This tool converts messy multi-modal intake into clean, agent-ready project folders that follow the SHITTYSHIT project system structure.

---

## ASSETS IN THIS FOLDER

| File | Type | Status | Notes |
|------|------|--------|-------|
| project.md | project card | active | this file |
| ARCHITECTURE.md | technical spec | complete | system design, 4K words |
| PRD.md | product requirements | complete | detailed requirements, 5K words |
| ROADMAP.md | implementation plan | complete | week-by-week roadmap, 2.5K words |
| GETTING_STARTED.md | setup guide | complete | step-by-step with code, 2K words |
| README.md | quick reference | complete | overview, 800 words |
| SUMMARY.md | executive summary | complete | project overview |

---

## TOOLS — ALWAYS ON

- [x] **Claude Code** — agentic execution
- [x] **Filesystem MCP** — project folder access
- [x] **Obsidian MCP** — vault integration

---

## TOOLS — ON DEMAND

### Core Infrastructure
- [ ] **n8n** — workflow orchestration (LACES)
- [ ] **Ollama** — local inference for synthesis (LACES)
- [ ] **Qdrant** — vector storage for project memory

### Web Stack (TBD)
- [ ] **Frontend framework** — React/Next.js/Svelte (decision needed)
- [ ] **Backend** — Node/Python/Go (decision needed)
- [ ] **Database** — Supabase/PostgreSQL (decision needed)
- [ ] **File storage** — S3/Cloudflare R2/local (decision needed)

### Audio/Video Pipeline
- [ ] **Whisper API / Parakeet** — transcription service (lightweight)
- [ ] **TTS service** — ElevenLabs/OpenAI/local (decision needed)
- [ ] **FFmpeg** — video processing

### AI Synthesis
- [ ] **Claude API** — project brief + PRD generation
- [ ] **NotebookLM** — optional synthesis pass

---

## SKILLS AVAILABLE

- [ ] **intake-classification** — process multi-modal drops
- [ ] **project-card-writer** — generate project.md from artifacts
- [ ] **spec-writing** — Specshitty discipline for PRD generation
- [ ] **token-reduction** — efficient context management

---

## CURRENT STATUS

Project fully specified. Architecture, PRD, and roadmap complete. Tech stack confirmed: Next.js + TypeScript + SQLite + Whisper API + Claude API. Ready for implementation.

MVP target: 1 week to working end-to-end flow (voice input → project folder).

This is infrastructure that enables the entire project intake pipeline. Priority 2 because it unblocks systematic project creation.

---

## NEXT ACTION

| What | Who | By when |
|------|-----|---------|
| Initialize Next.js project and set up dev environment | kevin | 2026-05-23 |

---

## OPEN QUESTIONS

- [ ] **Streaming transcription?** Real-time display vs batch processing after recording?
- [ ] **Long audio handling?** How to handle recordings >30 minutes?
- [ ] **Video transcription?** Extract audio first or use specialized service?
- [ ] **OCR for images?** Use Tesseract, Claude vision, or skip for MVP?
- [ ] **Synthesis async?** Synchronous with loading spinner or async with polling?
- [ ] **Project versioning?** Keep history when regenerating or overwrite?
- [ ] **Project templates?** Pre-configured templates for common project types?
- [ ] **Duplicate names?** Auto-append number or warn user?

---

## MUDROOM LOG

| Date | Item | Source | Status |
|------|------|--------|--------|
| 2026-05-22 | Initial voice spec from Kevin | voice input | processed |

---

## SESSION LOG

| Date | Agent | Summary | Files Changed |
|------|-------|---------|---------------|
| 2026-05-22 | Claude Sonnet 4.5 | Project created from voice spec. Defined core workflow and open questions. | project.md (created) |
| 2026-05-22 | Claude Sonnet 4.5 | Complete architecture, PRD, roadmap, getting started guide, README, and summary written. Tech stack confirmed. ~15K words of documentation. Ready for implementation. | ARCHITECTURE.md, PRD.md, ROADMAP.md, GETTING_STARTED.md, README.md, SUMMARY.md (created); project.md (updated); PROJECT_INDEX.yaml (updated) |

---

## GOVERNANCE NOTES

**Single-user first:** Build for Kevin's workflow initially. Multi-user can come later.

**Voice-first design:** Audio input should be as frictionless as possible. Kevin often works from handwritten notes read aloud.

**Preserve originals:** Always keep source artifacts alongside synthesized outputs. Never destructive.

**Agent-readable output:** Generated project folders must follow SHITTYSHIT project.md template exactly.

**Incremental build:** One project at a time, one artifact at a time. Not a bulk import tool.

---
*Created 2026-05-22 | Project Compiler Web Interface v0.1*
