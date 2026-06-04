# PROJECT COMPILER WEB — IMPLEMENTATION ROADMAP

---

## Quick Start: MVP in 1 Week

**Goal:** Get Kevin from voice input to generated project folder in one working flow.

### Day 1: Foundation
- [ ] Initialize Next.js project with TypeScript
- [ ] Set up SQLite database with Prisma
- [ ] Create basic UI layout (header, main area, sidebar)
- [ ] Set up environment variables for API keys

### Day 2: File Upload
- [ ] Build drag-drop file upload component
- [ ] Implement file validation (type, size)
- [ ] Store uploaded files in local filesystem
- [ ] Display uploaded files with preview

### Day 3: Audio Recording + Transcription
- [ ] Implement browser audio recording (MediaRecorder API)
- [ ] Save recorded audio as file
- [ ] Integrate Whisper API for transcription
- [ ] Display transcript in editable text area

### Day 4: Synthesis Engine
- [ ] Build Claude API integration
- [ ] Create synthesis prompt template
- [ ] Implement artifact collection logic
- [ ] Generate BRIEF.md, PRD.md, project.md

### Day 5: Project Folder Creation
- [ ] Implement folder structure creation
- [ ] Copy artifacts to assets/ subdirectories
- [ ] Write generated documents to folder
- [ ] Create session_log.md

### Day 6: Review Interface
- [ ] Build review screen with tabs
- [ ] Display generated documents
- [ ] Add edit capability
- [ ] Implement "Finalize" action

### Day 7: Testing + Deployment
- [ ] End-to-end test with real project
- [ ] Fix bugs and edge cases
- [ ] Deploy to LACES
- [ ] Document setup and usage

---

## Tech Stack (Confirmed)

### Frontend
- **Next.js 14** (App Router)
- **TypeScript**
- **Tailwind CSS** for styling
- **Radix UI** for components
- **React Hook Form** for forms

### Backend
- **Next.js API Routes**
- **Prisma** (ORM)
- **SQLite** (database)
- **Node.js filesystem** (file storage)

### External Services
- **OpenAI Whisper API** (transcription)
- **OpenAI TTS API** (text-to-speech)
- **Anthropic Claude API** (synthesis)

### Development
- **pnpm** (package manager)
- **ESLint + Prettier** (code quality)
- **Git** (version control)

---

## File Structure

```
project-compiler-web/
├── src/
│   ├── app/
│   │   ├── page.tsx                 # Home / project list
│   │   ├── new/
│   │   │   └── page.tsx             # New project form
│   │   ├── project/
│   │   │   └── [id]/
│   │   │       ├── page.tsx         # Project detail
│   │   │       └── review/
│   │   │           └── page.tsx     # Review generated docs
│   │   └── api/
│   │       ├── upload/
│   │       │   ├── file/route.ts
│   │       │   └── audio/route.ts
│   │       ├── transcribe/route.ts
│   │       ├── tts/route.ts
│   │       └── synthesize/route.ts
│   ├── components/
│   │   ├── FileUpload.tsx
│   │   ├── AudioRecorder.tsx
│   │   ├── TranscriptEditor.tsx
│   │   ├── ProjectForm.tsx
│   │   └── ReviewPanel.tsx
│   ├── lib/
│   │   ├── db.ts                    # Prisma client
│   │   ├── whisper.ts               # Whisper API wrapper
│   │   ├── claude.ts                # Claude API wrapper
│   │   ├── tts.ts                   # TTS API wrapper
│   │   └── filesystem.ts            # File operations
│   └── types/
│       └── index.ts                 # TypeScript types
├── prisma/
│   └── schema.prisma                # Database schema
├── public/
│   └── uploads/                     # Temporary upload storage
├── .env.local                       # API keys (not committed)
├── package.json
├── tsconfig.json
└── next.config.js
```

---

## Database Schema (Prisma)

```prisma
// prisma/schema.prisma

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "sqlite"
  url      = "file:./dev.db"
}

model Project {
  id          String   @id @default(uuid())
  name        String
  codename    String   @unique
  description String?
  status      String   @default("draft") // draft, synthesizing, complete
  priority    Int      @default(3)
  revenue     Boolean  @default(false)
  tags        String   // JSON array as string
  folderPath  String?
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
  
  artifacts   Artifact[]
  synthesis   Synthesis?
}

model Artifact {
  id              String   @id @default(uuid())
  projectId       String
  type            String   // audio, video, image, document, text
  originalName    String
  storagePath     String
  transcript      String?
  createdAt       DateTime @default(now())
  
  project         Project  @relation(fields: [projectId], references: [id], onDelete: Cascade)
}

model Synthesis {
  id          String   @id @default(uuid())
  projectId   String   @unique
  status      String   @default("pending") // pending, running, complete, failed
  brief       String?
  prd         String?
  projectMd   String?
  error       String?
  createdAt   DateTime @default(now())
  completedAt DateTime?
  
  project     Project  @relation(fields: [projectId], references: [id], onDelete: Cascade)
}
```

---

## API Endpoints

### POST /api/project/create
Create new project record.

**Request:**
```json
{
  "name": "Irish Mythology Serial",
  "description": "A serialized storytelling project",
  "tags": ["#content", "#creative"],
  "priority": 2,
  "revenue": true
}
```

**Response:**
```json
{
  "id": "uuid",
  "codename": "IRISH_MYTHOLOGY_SERIAL",
  "status": "draft"
}
```

---

### POST /api/upload/file
Upload document, image, or video.

**Request:** `multipart/form-data`
- `projectId`: string
- `file`: File

**Response:**
```json
{
  "artifactId": "uuid",
  "type": "document",
  "originalName": "research_notes.pdf",
  "storagePath": "/uploads/uuid/research_notes.pdf"
}
```

---

### POST /api/upload/audio
Upload or stream audio recording.

**Request:** `multipart/form-data`
- `projectId`: string
- `audio`: File (mp3, wav, webm)

**Response:**
```json
{
  "artifactId": "uuid",
  "type": "audio",
  "storagePath": "/uploads/uuid/recording.mp3"
}
```

---

### POST /api/transcribe
Transcribe audio file.

**Request:**
```json
{
  "artifactId": "uuid"
}
```

**Response:**
```json
{
  "transcript": "So this project is about...",
  "duration": 300,
  "language": "en"
}
```

---

### POST /api/tts
Generate speech from text.

**Request:**
```json
{
  "text": "This is the project brief...",
  "voice": "alloy"
}
```

**Response:**
```json
{
  "audioUrl": "/api/tts/uuid.mp3"
}
```

---

### POST /api/synthesize
Trigger project synthesis.

**Request:**
```json
{
  "projectId": "uuid",
  "instructions": "Focus on technical requirements" // optional
}
```

**Response:**
```json
{
  "synthesisId": "uuid",
  "status": "running"
}
```

---

### GET /api/project/:id
Get project details and status.

**Response:**
```json
{
  "id": "uuid",
  "name": "Irish Mythology Serial",
  "codename": "IRISH_MYTHOLOGY_SERIAL",
  "status": "complete",
  "folderPath": "_ACTIVE/IRISH_MYTHOLOGY_SERIAL",
  "artifacts": [
    {
      "id": "uuid",
      "type": "audio",
      "originalName": "recording_001.mp3",
      "transcript": "..."
    }
  ],
  "synthesis": {
    "status": "complete",
    "brief": "...",
    "prd": "...",
    "projectMd": "..."
  }
}
```

---

## Environment Variables

```bash
# .env.local

# OpenAI API
OPENAI_API_KEY=sk-...

# Anthropic API
ANTHROPIC_API_KEY=sk-ant-...

# Database
DATABASE_URL=file:./dev.db

# File Storage
UPLOAD_DIR=/path/to/.PROJECTS_SHITTYSHIT/_ACTIVE
TEMP_UPLOAD_DIR=/path/to/project-compiler-web/public/uploads

# App Config
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

---

## Synthesis Prompt Template

```typescript
// src/lib/prompts.ts

export const SYNTHESIS_PROMPT = `
You are synthesizing a project from multi-modal artifacts.

PROJECT METADATA:
Name: {name}
Description: {description}
Tags: {tags}
Priority: {priority}
Revenue: {revenue}

ARTIFACTS:
{artifacts}

YOUR TASK:
Generate three documents following these exact formats:

1. BRIEF.md - One-page executive summary
2. PRD.md - Detailed product requirements document
3. project.md - SHITTYSHIT project template (see below)

SHITTYSHIT PROJECT TEMPLATE:
{projectTemplate}

RULES:
- Follow the project.md template exactly
- Preserve all dates, names, and specific details
- Flag any ambiguities or missing information in "Open Questions"
- Be concise but complete
- Use Kevin's voice (direct, builder-focused)

OUTPUT FORMAT:
Return a JSON object with three keys:
{
  "brief": "markdown content",
  "prd": "markdown content",
  "projectMd": "markdown content"
}
`;
```

---

## Next Steps

1. **Initialize project:**
   ```bash
   npx create-next-app@latest project-compiler-web --typescript --tailwind --app
   cd project-compiler-web
   pnpm install prisma @prisma/client
   pnpm install @radix-ui/react-dialog @radix-ui/react-select
   pnpm install openai @anthropic-ai/sdk
   ```

2. **Set up database:**
   ```bash
   npx prisma init --datasource-provider sqlite
   # Edit prisma/schema.prisma with schema above
   npx prisma migrate dev --name init
   ```

3. **Create API wrappers:**
   - `src/lib/whisper.ts` - Whisper API client
   - `src/lib/claude.ts` - Claude API client
   - `src/lib/tts.ts` - TTS API client

4. **Build UI components:**
   - Start with `FileUpload.tsx`
   - Then `AudioRecorder.tsx`
   - Then `TranscriptEditor.tsx`

5. **Test end-to-end:**
   - Create test project
   - Upload test files
   - Record test audio
   - Verify synthesis output
   - Check project folder structure

---

## Deployment to LACES

```bash
# On LACES UM890

# Clone repo
git clone <repo-url> /home/kevin/project-compiler-web
cd /home/kevin/project-compiler-web

# Install dependencies
pnpm install

# Set up environment
cp .env.example .env.local
# Edit .env.local with API keys

# Run database migrations
npx prisma migrate deploy

# Build for production
pnpm build

# Start with PM2
pm2 start npm --name "project-compiler" -- start
pm2 save

# Access at http://laces.local:3000
```

---

## Future Enhancements

### Phase 2: Advanced Features
- [ ] Streaming transcription (real-time)
- [ ] Video transcription (extract audio first)
- [ ] OCR for images with text
- [ ] Speaker diarization
- [ ] Multi-language support

### Phase 3: Integration
- [ ] n8n workflow orchestration
- [ ] Linear issue creation
- [ ] GitHub repo initialization
- [ ] Gumroad product export

### Phase 4: Intelligence
- [ ] Vector search across all projects
- [ ] Auto-tagging via AI
- [ ] Project similarity detection
- [ ] Smart artifact suggestions

---

*Roadmap v0.1 | 2026-05-22*
