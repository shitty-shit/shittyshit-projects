# PROJECT COMPILER WEB — PRODUCT REQUIREMENTS DOCUMENT

---

## Product Vision

A web-based project intake system that converts Kevin's multi-modal working style (voice notes, handwritten transcriptions, scattered documents, images, videos) into structured, agent-ready project folders that follow the SHITTYSHIT project system.

**Core insight:** Kevin works voice-first and often reads from handwritten notes. He doesn't need frontier AI for simple transcription — he needs a fast, reliable pipeline that captures everything, synthesizes it intelligently, and outputs clean project folders.

---

## Success Criteria

1. **Kevin can create a complete project folder in under 10 minutes** from voice input + supporting docs
2. **Generated project.md files follow SHITTYSHIT template exactly** and are immediately usable by other agents
3. **Original artifacts are always preserved** alongside synthesized outputs
4. **Transcription is fast enough** that Kevin doesn't context-switch while waiting
5. **System builds master project list incrementally** without manual index maintenance

---

## User Stories

### Primary User: Kevin

**As Kevin, I want to:**

1. **Record voice notes about a new project idea** so I can capture thoughts without typing
2. **Upload handwritten notes (as images)** so I don't lose original context
3. **Drag in supporting documents** (PDFs, Word docs, chat transcripts) without file format hassles
4. **See transcription happen in real-time** so I can verify accuracy as I speak
5. **Edit transcripts before synthesis** so errors don't propagate into the brief
6. **Trigger AI synthesis with one click** and get back a complete project folder
7. **Review generated brief and PRD** before finalizing the project
8. **Have all original files preserved** in the project folder for future reference
9. **See a master list of all projects** I've created through this system
10. **Re-open and add to existing projects** without starting from scratch

---

## Core Features

### 1. Multi-Modal Input Collection

**File Upload**
- Drag-and-drop interface
- Support: PDF, DOCX, TXT, MD, PNG, JPG, MP4, MOV, MP3, WAV
- Max file size: 100MB per file
- Preview uploaded files before processing
- Remove files before synthesis

**Audio Recording**
- Browser-based recording (no app install)
- Visual waveform during recording
- Pause/resume capability
- Max recording length: 30 minutes
- Save recording as artifact

**Text Input**
- Rich text editor for typed notes
- Markdown support
- Paste from clipboard (preserves formatting)
- Auto-save drafts

**Video Upload**
- Support MP4, MOV, AVI
- Extract audio for transcription
- Store original video in assets

**Project Metadata**
- Project name (required)
- Short description (optional)
- Tags (multi-select from standard tags)
- Priority (1-5)
- Revenue flag (yes/no)

---

### 2. Real-Time Transcription

**Audio → Text Pipeline**
- Transcribe as user speaks (streaming if possible)
- Display transcript in editable text area
- Highlight confidence scores (if available)
- Speaker diarization (if multiple voices)
- Timestamp markers every 30 seconds

**Transcript Editing**
- Inline editing of transcribed text
- Undo/redo support
- Save edited version
- Keep original transcript for reference

**Supported Languages**
- English (primary)
- Spanish (future)

---

### 3. Text-to-Speech Playback

**Read Back Content**
- Play any text field (transcript, brief, PRD)
- Adjustable speed (0.5x - 2x)
- Pause/resume controls
- Skip forward/back 10 seconds

**Voice Selection**
- Default: OpenAI TTS "alloy" voice
- Future: Multiple voice options

---

### 4. Agent Synthesis

**Synthesis Trigger**
- "Generate Project Brief" button
- Shows progress indicator
- Estimated time: 30-60 seconds

**Synthesis Process**
1. Collect all artifacts (transcripts, docs, images, metadata)
2. Build context package for Claude
3. Send to Claude API with synthesis prompt
4. Generate three outputs:
   - **BRIEF.md** — 1-page project summary
   - **PRD.md** — detailed requirements document
   - **project.md** — SHITTYSHIT template filled out

**Synthesis Prompt Structure**
```
You are synthesizing a project from the following artifacts:

PROJECT METADATA:
- Name: [name]
- Description: [description]
- Tags: [tags]
- Priority: [priority]
- Revenue: [yes/no]

TRANSCRIPTS:
[all audio transcripts]

DOCUMENTS:
[extracted text from PDFs/docs]

IMAGES:
[image descriptions if OCR available]

CHAT TRANSCRIPTS:
[pasted conversations]

YOUR TASK:
1. Read all materials carefully
2. Identify the core project concept
3. Extract key requirements and goals
4. Generate three documents:
   - BRIEF.md (1 page, executive summary)
   - PRD.md (detailed requirements)
   - project.md (SHITTYSHIT template format)

Follow the SHITTYSHIT project.md template exactly.
Preserve all dates, names, and specific details.
Flag any ambiguities or missing information.
```

---

### 5. Project Folder Creation

**Folder Structure**
```
_ACTIVE/[PROJECT_CODENAME]/
├── project.md              # SHITTYSHIT template
├── BRIEF.md                # 1-page summary
├── PRD.md                  # detailed requirements
├── assets/
│   ├── audio/
│   │   ├── recording_001.mp3
│   │   └── transcript_001.txt
│   ├── documents/
│   │   ├── research_notes.pdf
│   │   └── chat_transcript.txt
│   ├── images/
│   │   ├── sketch_001.jpg
│   │   └── reference_002.png
│   └── video/
│       └── demo_001.mp4
└── session_log.md          # creation history
```

**Automatic Actions**
- Create folder in `_ACTIVE/`
- Copy all original artifacts to `assets/`
- Write generated docs (BRIEF, PRD, project.md)
- Create session_log.md with creation timestamp
- Update master project index
- Generate codename from project name (uppercase, underscores)

---

### 6. Review and Edit

**Post-Synthesis Review**
- Display generated BRIEF.md
- Display generated PRD.md
- Display generated project.md
- Side-by-side view with original artifacts

**Edit Options**
- Edit any generated document inline
- Regenerate with additional instructions
- Approve and finalize
- Save as draft (don't create folder yet)

**Regeneration**
- "Regenerate with changes" button
- Add additional instructions (e.g., "focus more on technical requirements")
- Re-run synthesis with updated prompt

---

### 7. Master Project List

**Project Index View**
- Table of all projects created
- Columns: Name, Status, Priority, Revenue, Created Date, Last Updated
- Sort by any column
- Filter by status, tags, revenue flag
- Search by name or description

**Project Actions**
- Click to view project details
- Re-open for editing
- Add more artifacts to existing project
- Change status (active → parked, etc.)
- Export project folder as ZIP

---

## Non-Functional Requirements

### Performance
- Transcription: < 30 seconds for 5-minute audio
- TTS generation: < 5 seconds for 1000 characters
- Synthesis: < 60 seconds for typical project
- File upload: < 10 seconds for 50MB file
- Page load: < 2 seconds

### Reliability
- Auto-save drafts every 30 seconds
- Retry failed API calls (3 attempts)
- Graceful degradation if transcription service down
- Error messages are clear and actionable

### Usability
- Mobile-responsive (tablet minimum)
- Keyboard shortcuts for common actions
- Accessible (WCAG 2.1 AA)
- No page refreshes during workflow

### Security
- API keys stored in environment variables
- File upload validation (type, size)
- Rate limiting on API endpoints
- CORS restrictions

---

## User Interface Mockup

### Main Screen: New Project

```
┌─────────────────────────────────────────────────────────────┐
│  PROJECT COMPILER                                    [Kevin] │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  New Project                                                  │
│                                                               │
│  Project Name: [_________________________________]            │
│  Description:  [_________________________________]            │
│  Tags:         [#infra] [#ai] [+]                            │
│  Priority:     [●●●○○]  Revenue: [✓]                        │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  ARTIFACTS                                           │    │
│  │                                                       │    │
│  │  [🎤 Record Audio]  [📁 Upload Files]  [✍️ Add Text] │    │
│  │                                                       │    │
│  │  📄 research_notes.pdf                    [×]        │    │
│  │  🎵 voice_memo_001.mp3 → transcribing... 45%        │    │
│  │  🖼️ sketch_001.jpg                        [×]        │    │
│  │                                                       │    │
│  │  [+ Add More]                                        │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  TRANSCRIPT                                          │    │
│  │                                                       │    │
│  │  [00:00] So this project is about building a...     │    │
│  │  [00:15] The core idea is to create a system that...│    │
│  │  [00:30] I want it to handle multiple input types...│    │
│  │                                                       │    │
│  │  [▶️ Play]  [Edit]                                   │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  [Save Draft]              [Generate Project Brief →]        │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Synthesis Screen

```
┌─────────────────────────────────────────────────────────────┐
│  PROJECT COMPILER                                    [Kevin] │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Generating Project: Irish Mythology Serial                  │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  ⚙️ Synthesizing project brief...                   │    │
│  │                                                       │    │
│  │  ✓ Collected 5 artifacts                            │    │
│  │  ✓ Transcribed audio (3 files)                      │    │
│  │  ⏳ Generating BRIEF.md...                          │    │
│  │  ⏳ Generating PRD.md...                            │    │
│  │  ⏳ Generating project.md...                        │    │
│  │                                                       │    │
│  │  Estimated time remaining: 30 seconds                │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Review Screen

```
┌─────────────────────────────────────────────────────────────┐
│  PROJECT COMPILER                                    [Kevin] │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Review: Irish Mythology Serial                              │
│                                                               │
│  [BRIEF] [PRD] [project.md] [Artifacts]                      │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  # IRISH MYTHOLOGY SERIAL                            │    │
│  │                                                       │    │
│  │  A serialized storytelling project exploring Irish   │    │
│  │  mythology through modern narrative techniques...    │    │
│  │                                                       │    │
│  │  ## Core Concept                                     │    │
│  │  This project aims to...                             │    │
│  │                                                       │    │
│  │  [Edit] [▶️ Read Aloud]                              │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  [← Back]  [Regenerate]  [Finalize Project →]               │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Technical Constraints

- Must run on LACES UM890 (AMD Ryzen 9, 24GB RAM)
- Must work on local network initially
- Must integrate with existing SHITTYSHIT folder structure
- Must follow project.md template exactly
- Must preserve all original artifacts
- Must not require manual index maintenance

---

## Out of Scope (v1)

- Multi-user support
- Real-time collaboration
- Mobile app (web only)
- Bulk project import
- Integration with Linear/GitHub (future)
- Gumroad export (future)
- Vector search across projects (future)
- Auto-tagging via AI (future)

---

## Success Metrics

**Usage Metrics**
- Projects created per week
- Average time to create project
- Transcription accuracy (manual review)
- Synthesis regeneration rate (lower is better)

**Quality Metrics**
- Generated project.md passes validation
- Kevin approves brief without edits (target: 80%)
- Original artifacts successfully preserved (target: 100%)

**System Metrics**
- Transcription latency (target: < 30s for 5min audio)
- Synthesis latency (target: < 60s)
- Uptime (target: 99% on local network)

---

## Implementation Phases

### Phase 1: Core Pipeline (Week 1-2)
- [ ] Next.js project setup
- [ ] File upload UI
- [ ] Audio recording
- [ ] Whisper API integration
- [ ] Basic synthesis (Claude API)
- [ ] Project folder creation
- [ ] Local deployment on LACES

### Phase 2: Polish (Week 3)
- [ ] Real-time transcription display
- [ ] TTS integration
- [ ] Transcript editing
- [ ] Review/edit interface
- [ ] Regeneration with instructions

### Phase 3: Project Management (Week 4)
- [ ] Master project list view
- [ ] Project search/filter
- [ ] Re-open existing projects
- [ ] Add artifacts to existing projects
- [ ] Export project as ZIP

### Phase 4: Production (Week 5+)
- [ ] Cloud deployment (optional)
- [ ] Authentication
- [ ] n8n orchestration
- [ ] Advanced features (vector search, auto-tagging)

---

## Open Questions

1. **Should transcription be streaming or batch?** Streaming is better UX but more complex.
2. **How to handle very long audio (>30 min)?** Split into chunks? Warn user?
3. **Should we support video transcription?** Extract audio first, then transcribe?
4. **How to handle images with text (OCR)?** Use Tesseract or Claude vision?
5. **Should synthesis be synchronous or async?** Async with polling is more scalable.
6. **How to version project.md if regenerated?** Keep history or overwrite?
7. **Should we support project templates?** (e.g., "Content Project", "Code Project")
8. **How to handle duplicate project names?** Auto-append number or warn user?

---

*PRD v0.1 | 2026-05-22*
