# PROJECT COMPILER WEB — ARCHITECTURE

---

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     WEB INTERFACE                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Upload  │  │  Audio   │  │   Text   │  │  Video   │   │
│  │  Files   │  │  Record  │  │  Input   │  │  Upload  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   PROCESSING LAYER                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Transcription│  │     TTS      │  │   Storage    │     │
│  │   Service    │  │   Service    │  │   Handler    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   AGENT SYNTHESIS                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Claude API / n8n Workflow                            │  │
│  │  - Read all artifacts                                 │  │
│  │  - Generate project brief                             │  │
│  │  - Generate PRD                                       │  │
│  │  - Create project.md                                  │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   OUTPUT LAYER                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Project Folder Created                               │  │
│  │  ├── project.md                                       │  │
│  │  ├── BRIEF.md                                         │  │
│  │  ├── PRD.md                                           │  │
│  │  ├── assets/                                          │  │
│  │  │   ├── original_audio.mp3                          │  │
│  │  │   ├── transcript.txt                              │  │
│  │  │   ├── uploaded_doc.pdf                            │  │
│  │  │   └── images/                                     │  │
│  │  └── session_log.md                                  │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Component Breakdown

### 1. Web Interface (Frontend)

**Purpose:** Multi-modal input collection with real-time feedback

**Features:**
- File upload (drag-drop + browse)
- Audio recording (browser MediaRecorder API)
- Text input (rich text editor)
- Video upload with preview
- Real-time transcription display
- TTS playback controls
- Project metadata form (name, description, tags)

**Tech Options:**
- **React + Next.js** — familiar, good ecosystem, API routes built-in
- **Svelte + SvelteKit** — lighter, simpler, faster
- **Vue + Nuxt** — middle ground

**Recommendation:** Next.js for rapid prototyping, built-in API routes, and Kevin's existing familiarity.

---

### 2. Backend API

**Purpose:** Handle uploads, coordinate services, trigger agent synthesis

**Endpoints:**
```
POST   /api/project/create          # Initialize new project
POST   /api/upload/file             # Upload document/image
POST   /api/upload/audio            # Upload or stream audio
POST   /api/upload/video            # Upload video
POST   /api/transcribe              # Trigger transcription
POST   /api/tts                     # Generate speech from text
POST   /api/synthesize              # Trigger agent synthesis
GET    /api/project/:id             # Get project status
GET    /api/project/:id/artifacts   # List all artifacts
```

**Tech Options:**
- **Next.js API routes** — same codebase as frontend
- **Express.js** — separate Node backend
- **FastAPI (Python)** — if heavy AI integration needed

**Recommendation:** Next.js API routes for single-codebase simplicity.

---

### 3. Transcription Service

**Purpose:** Convert audio to text (lightweight, not frontier AI)

**Options:**

| Service | Pros | Cons | Cost |
|---------|------|------|------|
| **Whisper API (OpenAI)** | Accurate, simple API | Cloud dependency, usage cost | $0.006/min |
| **Deepgram** | Fast, streaming support | Usage cost | $0.0043/min |
| **AssemblyAI** | Good accuracy, speaker labels | Usage cost | $0.00025/sec |
| **Local Whisper (Parakeet)** | Free, private, LACES-hosted | Setup complexity, slower | Free |
| **Whisper.cpp** | Fast local inference | C++ integration | Free |

**Recommendation:** Start with **Whisper API** for speed, migrate to local Whisper on LACES if usage grows.

---

### 4. TTS Service

**Purpose:** Read back content for Kevin's workflow

**Options:**

| Service | Pros | Cons | Cost |
|---------|------|------|------|
| **ElevenLabs** | Best quality, voice cloning | Expensive | $0.30/1K chars |
| **OpenAI TTS** | Good quality, simple API | Less natural | $15/1M chars |
| **Google Cloud TTS** | Cheap, many voices | Setup overhead | $4/1M chars |
| **Local Piper** | Free, fast, LACES-hosted | Lower quality | Free |

**Recommendation:** **OpenAI TTS** for balance of quality and cost.

---

### 5. File Storage

**Purpose:** Store uploaded artifacts and generated outputs

**Options:**

| Storage | Pros | Cons | Cost |
|---------|------|------|------|
| **Local filesystem** | Simple, fast, no cost | Not scalable, backup needed | Free |
| **Cloudflare R2** | S3-compatible, no egress fees | Setup overhead | $0.015/GB |
| **Supabase Storage** | Integrated with DB, simple API | Vendor lock-in | Free tier generous |
| **LACES NAS** | Private, unlimited | Network dependency | Free |

**Recommendation:** **Local filesystem** for MVP, **Supabase Storage** for production.

---

### 6. Agent Synthesis Engine

**Purpose:** Read all artifacts, generate project brief + PRD + project.md

**Workflow:**
1. Collect all artifacts (transcripts, docs, images, metadata)
2. Build context package
3. Send to Claude API with synthesis prompt
4. Generate:
   - `BRIEF.md` — 1-page project summary
   - `PRD.md` — detailed requirements doc
   - `project.md` — SHITTYSHIT template filled out
5. Write files to project folder
6. Update master project index

**Integration Options:**
- **Direct Claude API** — simple, synchronous
- **n8n workflow** — orchestrated, can add steps
- **MCP server** — reusable, composable

**Recommendation:** **Direct Claude API** for MVP, **n8n** for production orchestration.

---

### 7. Database

**Purpose:** Track projects, artifacts, synthesis status

**Schema:**
```sql
projects
  - id (uuid)
  - name (text)
  - codename (text)
  - status (enum: draft, synthesizing, complete)
  - created_at (timestamp)
  - folder_path (text)

artifacts
  - id (uuid)
  - project_id (fk)
  - type (enum: audio, video, image, document, text)
  - original_filename (text)
  - storage_path (text)
  - transcript (text, nullable)
  - created_at (timestamp)

synthesis_jobs
  - id (uuid)
  - project_id (fk)
  - status (enum: pending, running, complete, failed)
  - output_brief (text, nullable)
  - output_prd (text, nullable)
  - output_project_md (text, nullable)
  - created_at (timestamp)
  - completed_at (timestamp, nullable)
```

**Tech Options:**
- **SQLite** — simple, local, no setup
- **PostgreSQL (Supabase)** — production-ready, hosted
- **PostgreSQL (local)** — self-hosted on LACES

**Recommendation:** **SQLite** for MVP, **Supabase PostgreSQL** for production.

---

## Data Flow

### Scenario: Kevin creates a new project via voice

1. **Kevin opens web interface**
   - Clicks "New Project"
   - Enters project name: "Irish Mythology Serial"

2. **Kevin records audio notes**
   - Clicks record button
   - Speaks for 5 minutes about project concept
   - Stops recording

3. **System transcribes audio**
   - Audio sent to Whisper API
   - Transcript appears in real-time
   - Kevin reviews, edits if needed

4. **Kevin uploads supporting docs**
   - Drags in PDF of research notes
   - Uploads 3 reference images
   - Pastes chat transcript from previous brainstorm

5. **Kevin triggers synthesis**
   - Clicks "Generate Project Brief"
   - System sends all artifacts to Claude API
   - Agent reads everything, generates:
     - BRIEF.md
     - PRD.md
     - project.md (SHITTYSHIT template)

6. **System creates project folder**
   - Creates `_ACTIVE/IRISH_MYTHOLOGY_SERIAL/`
   - Copies all original artifacts to `assets/`
   - Writes generated docs
   - Updates master project index

7. **Kevin reviews output**
   - Sees generated brief
   - Can edit, regenerate, or approve
   - Clicks "Finalize" → project is ready

---

## Deployment Strategy

### Phase 1: Local MVP (LACES)
- Next.js app running on LACES UM890
- SQLite database
- Local filesystem storage
- Whisper API for transcription
- OpenAI TTS for playback
- Direct Claude API for synthesis
- Accessible on local network

### Phase 2: Cloud Production
- Deploy to Vercel/Railway
- Migrate to Supabase (DB + Storage)
- Add authentication (single-user)
- Keep transcription/TTS services
- Add n8n orchestration layer

### Phase 3: Advanced Features
- Multi-project batch processing
- Vector search across all projects
- Auto-tagging and classification
- Integration with Linear for task creation
- Gumroad export for revenue projects

---

## Security Considerations

- **Single-user initially:** No auth needed for MVP
- **File upload validation:** Check file types, size limits
- **API rate limiting:** Prevent abuse of transcription/TTS
- **Secrets management:** Environment variables for API keys
- **CORS:** Restrict to known origins

---

## Performance Targets

- **Audio transcription:** < 30 seconds for 5-minute audio
- **TTS generation:** < 5 seconds for 1000 characters
- **Agent synthesis:** < 60 seconds for typical project
- **File upload:** Support up to 100MB per file
- **Concurrent projects:** Handle 10+ projects in draft state

---

## Next Steps

1. **Choose stack:** Confirm Next.js + SQLite + Whisper API + OpenAI TTS
2. **Set up dev environment:** Initialize Next.js project
3. **Build file upload UI:** Drag-drop + preview
4. **Integrate Whisper API:** Audio → transcript pipeline
5. **Build synthesis prompt:** Claude API integration
6. **Test end-to-end:** One complete project creation flow
7. **Deploy to LACES:** Local network access

---

*Architecture v0.1 | 2026-05-22*
