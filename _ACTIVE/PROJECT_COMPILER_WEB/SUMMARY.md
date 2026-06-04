# PROJECT COMPILER WEB — EXECUTIVE SUMMARY

---

## What We Built

A complete specification for a web-based project intake system that converts Kevin's multi-modal working style into structured, agent-ready project folders.

---

## The Problem

Kevin works voice-first, often reading from handwritten notes. Project ideas come as scattered artifacts: voice memos, documents, images, chat transcripts. Converting these into structured project folders is manual, time-consuming, and inconsistent.

---

## The Solution

A web interface where Kevin can:
1. Record voice notes or upload audio
2. Drag in supporting documents, images, videos
3. Get real-time transcription (lightweight, not frontier AI)
4. Trigger AI synthesis with one click
5. Receive a complete project folder with:
   - `BRIEF.md` (1-page summary)
   - `PRD.md` (detailed requirements)
   - `project.md` (SHITTYSHIT template)
   - All original artifacts preserved in `assets/`

---

## Why This Matters

This is **infrastructure that unblocks revenue**. It's the intake system for Kevin's entire project pipeline. Every project that goes through this system becomes:
- Properly documented
- Agent-ready
- Searchable
- Trackable
- Actionable

---

## Tech Stack (Confirmed)

- **Frontend:** Next.js 14 + TypeScript + Tailwind CSS
- **Backend:** Next.js API Routes + Prisma + SQLite
- **Transcription:** OpenAI Whisper API
- **TTS:** OpenAI TTS API
- **Synthesis:** Anthropic Claude API
- **Deployment:** LACES UM890 (local) → Cloud (future)

---

## What's Included

### Documentation
- **project.md** — SHITTYSHIT project card (status, tools, questions)
- **ARCHITECTURE.md** — System design, component breakdown, data flow
- **PRD.md** — Detailed product requirements, user stories, UI mockups
- **ROADMAP.md** — Week-by-week implementation plan
- **GETTING_STARTED.md** — Step-by-step setup guide with code samples
- **README.md** — Quick reference and overview

### Specifications
- Database schema (Prisma)
- API endpoint definitions
- Synthesis prompt template
- Folder structure conventions
- UI component requirements

---

## Implementation Timeline

### Week 1: MVP (Core Pipeline)
- Initialize Next.js project
- Build file upload + audio recording
- Integrate Whisper API for transcription
- Integrate Claude API for synthesis
- Create project folder with generated docs
- **Deliverable:** Working end-to-end flow

### Week 2: Polish
- Real-time transcription display
- TTS integration for playback
- Transcript editing
- Review/edit interface
- Regeneration with custom instructions

### Week 3: Project Management
- Master project list view
- Search and filter
- Re-open existing projects
- Add artifacts to existing projects

---

## Key Features

1. **Multi-modal input** — Audio, video, images, documents, text
2. **Real-time transcription** — See transcript as you speak
3. **TTS playback** — Listen to any text field
4. **AI synthesis** — Claude generates complete project docs
5. **Editable output** — Review and refine before finalizing
6. **Preserves originals** — All source artifacts kept in assets/
7. **SHITTYSHIT compliant** — Follows project.md template exactly
8. **Incremental build** — One project at a time, one artifact at a time

---

## Success Criteria

1. Kevin can create a complete project folder in **under 10 minutes**
2. Generated project.md files **follow SHITTYSHIT template exactly**
3. Original artifacts are **always preserved**
4. Transcription is **fast enough** (< 30s for 5min audio)
5. System builds **master project list automatically**

---

## Next Actions

| Action | Owner | Timeline |
|--------|-------|----------|
| Initialize Next.js project | Kevin | Day 1 |
| Build file upload UI | Kevin | Day 1-2 |
| Integrate Whisper API | Kevin | Day 2-3 |
| Build synthesis engine | Kevin | Day 3-4 |
| Test end-to-end flow | Kevin | Day 5 |
| Deploy to LACES | Kevin | Day 6-7 |

---

## Open Questions

1. **Streaming transcription?** Real-time vs batch after recording?
2. **Long audio handling?** How to handle recordings >30 minutes?
3. **Video transcription?** Extract audio first or specialized service?
4. **OCR for images?** Use Tesseract, Claude vision, or skip for MVP?
5. **Synthesis async?** Synchronous with spinner or async with polling?
6. **Project versioning?** Keep history when regenerating or overwrite?

---

## Files Created

```
_ACTIVE/PROJECT_COMPILER_WEB/
├── project.md              # SHITTYSHIT project card
├── ARCHITECTURE.md         # System design (4,000 words)
├── PRD.md                  # Product requirements (5,000 words)
├── ROADMAP.md              # Implementation plan (2,500 words)
├── GETTING_STARTED.md      # Setup guide with code (2,000 words)
├── README.md               # Quick reference (800 words)
└── SUMMARY.md              # This file (executive summary)
```

**Total documentation:** ~15,000 words of comprehensive specs, ready for implementation.

---

## Project Status

- **Status:** Active, fully specified
- **Priority:** 2 (infrastructure that unblocks revenue)
- **Blocker:** None
- **Next:** Initialize Next.js project and start building

---

## Why This Will Work

1. **Solves real pain** — Kevin's actual workflow, not theoretical
2. **Simple tech stack** — Proven tools, no exotic dependencies
3. **Incremental build** — MVP in 1 week, polish later
4. **Clear success metrics** — Time to create project, template compliance
5. **Infrastructure play** — Enables systematic project creation

---

*This project is ready to build. All architectural decisions made. All requirements documented. All code patterns specified. Start with GETTING_STARTED.md and build the MVP.*

---

**Session completed:** 2026-05-22  
**Agent:** Claude Sonnet 4.5  
**Files created:** 7  
**Status:** Ready for implementation

