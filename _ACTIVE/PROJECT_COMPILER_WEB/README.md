# PROJECT COMPILER WEB

Agent-guided web interface for multi-modal project intake and synthesis.

---

## What This Does

Converts Kevin's voice notes, handwritten transcriptions, documents, images, and videos into structured project folders with AI-generated briefs and PRDs.

**Input:** Voice recording + supporting docs  
**Output:** Complete project folder in `_ACTIVE/` with SHITTYSHIT template

---

## Quick Start

```bash
# Initialize project
npx create-next-app@latest project-compiler-web --typescript --tailwind --app
cd project-compiler-web

# Install dependencies
pnpm install prisma @prisma/client
pnpm install @radix-ui/react-dialog @radix-ui/react-select
pnpm install openai @anthropic-ai/sdk

# Set up database
npx prisma init --datasource-provider sqlite
npx prisma migrate dev --name init

# Configure environment
cp .env.example .env.local
# Add API keys: OPENAI_API_KEY, ANTHROPIC_API_KEY

# Run dev server
pnpm dev
```

---

## Tech Stack

- **Frontend:** Next.js 14 + TypeScript + Tailwind CSS
- **Backend:** Next.js API Routes + Prisma + SQLite
- **Transcription:** OpenAI Whisper API
- **TTS:** OpenAI TTS API
- **Synthesis:** Anthropic Claude API

---

## Core Workflow

1. **Create project** → Enter name, description, tags
2. **Add artifacts** → Upload files, record audio, paste text
3. **Transcribe audio** → Automatic via Whisper API
4. **Review transcripts** → Edit if needed
5. **Synthesize** → Claude generates BRIEF.md, PRD.md, project.md
6. **Review output** → Edit or regenerate
7. **Finalize** → Project folder created in `_ACTIVE/`

---

## Project Structure

```
_ACTIVE/[PROJECT_CODENAME]/
├── project.md              # SHITTYSHIT template
├── BRIEF.md                # 1-page summary
├── PRD.md                  # detailed requirements
├── assets/
│   ├── audio/              # recordings + transcripts
│   ├── documents/          # PDFs, docs, text files
│   ├── images/             # photos, sketches
│   └── video/              # video files
└── session_log.md          # creation history
```

---

## Key Features

- **Multi-modal input:** Audio, video, images, documents, text
- **Real-time transcription:** See transcript as you speak
- **TTS playback:** Listen to any text field
- **AI synthesis:** Claude generates project docs
- **Editable output:** Review and refine before finalizing
- **Preserves originals:** All source artifacts kept in assets/

---

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/project/create` | POST | Create new project |
| `/api/upload/file` | POST | Upload document/image |
| `/api/upload/audio` | POST | Upload audio recording |
| `/api/transcribe` | POST | Transcribe audio file |
| `/api/tts` | POST | Generate speech from text |
| `/api/synthesize` | POST | Trigger AI synthesis |
| `/api/project/:id` | GET | Get project details |

---

## Environment Variables

```bash
# .env.local

OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
DATABASE_URL=file:./dev.db
UPLOAD_DIR=/path/to/.PROJECTS_SHITTYSHIT/_ACTIVE
TEMP_UPLOAD_DIR=/path/to/project-compiler-web/public/uploads
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

---

## Development Roadmap

### Week 1: MVP
- [x] Architecture defined
- [x] PRD written
- [ ] Next.js project initialized
- [ ] File upload working
- [ ] Audio recording working
- [ ] Transcription integrated
- [ ] Synthesis working
- [ ] Project folder creation
- [ ] End-to-end test

### Week 2: Polish
- [ ] Real-time transcription display
- [ ] TTS integration
- [ ] Transcript editing
- [ ] Review interface
- [ ] Regeneration with instructions

### Week 3: Project Management
- [ ] Master project list
- [ ] Search and filter
- [ ] Re-open existing projects
- [ ] Add to existing projects

---

## Deployment (LACES)

```bash
# On LACES UM890
git clone <repo-url> /home/kevin/project-compiler-web
cd /home/kevin/project-compiler-web
pnpm install
npx prisma migrate deploy
pnpm build
pm2 start npm --name "project-compiler" -- start
pm2 save

# Access at http://laces.local:3000
```

---

## Documentation

- **ARCHITECTURE.md** — System design and component breakdown
- **PRD.md** — Detailed product requirements
- **ROADMAP.md** — Week-by-week implementation plan
- **project.md** — SHITTYSHIT project card

---

## Status

**Current:** Fully specified, ready for implementation  
**Next:** Initialize Next.js project and build file upload UI  
**Target:** Working MVP in 1 week

---

*Project Compiler Web v0.1 | 2026-05-22*
