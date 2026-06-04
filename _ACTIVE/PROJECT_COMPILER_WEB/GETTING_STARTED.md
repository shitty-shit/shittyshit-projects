# GETTING STARTED — PROJECT COMPILER WEB

Quick guide to start building the MVP.

---

## Prerequisites

- Node.js 18+ installed
- pnpm installed (`npm install -g pnpm`)
- OpenAI API key
- Anthropic API key
- Git

---

## Step 1: Initialize Project

```bash
# Create Next.js app
npx create-next-app@latest project-compiler-web \
  --typescript \
  --tailwind \
  --app \
  --no-src-dir \
  --import-alias "@/*"

cd project-compiler-web
```

---

## Step 2: Install Dependencies

```bash
# Core dependencies
pnpm install prisma @prisma/client
pnpm install openai @anthropic-ai/sdk
pnpm install zod react-hook-form @hookform/resolvers

# UI components
pnpm install @radix-ui/react-dialog
pnpm install @radix-ui/react-select
pnpm install @radix-ui/react-tabs
pnpm install @radix-ui/react-toast
pnpm install lucide-react

# Dev dependencies
pnpm install -D prisma
```

---

## Step 3: Set Up Database

```bash
# Initialize Prisma with SQLite
npx prisma init --datasource-provider sqlite
```

Edit `prisma/schema.prisma`:

```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "sqlite"
  url      = env("DATABASE_URL")
}

model Project {
  id          String   @id @default(uuid())
  name        String
  codename    String   @unique
  description String?
  status      String   @default("draft")
  priority    Int      @default(3)
  revenue     Boolean  @default(false)
  tags        String
  folderPath  String?
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
  
  artifacts   Artifact[]
  synthesis   Synthesis?
}

model Artifact {
  id              String   @id @default(uuid())
  projectId       String
  type            String
  originalName    String
  storagePath     String
  transcript      String?
  createdAt       DateTime @default(now())
  
  project         Project  @relation(fields: [projectId], references: [id], onDelete: Cascade)
}

model Synthesis {
  id          String   @id @default(uuid())
  projectId   String   @unique
  status      String   @default("pending")
  brief       String?
  prd         String?
  projectMd   String?
  error       String?
  createdAt   DateTime @default(now())
  completedAt DateTime?
  
  project     Project  @relation(fields: [projectId], references: [id], onDelete: Cascade)
}
```

Run migration:

```bash
npx prisma migrate dev --name init
```

---

## Step 4: Configure Environment

Create `.env.local`:

```bash
# Database
DATABASE_URL="file:./dev.db"

# OpenAI API
OPENAI_API_KEY="sk-..."

# Anthropic API
ANTHROPIC_API_KEY="sk-ant-..."

# File Storage
UPLOAD_DIR="C:/Users/idfk/Desktop/SHITTY_SYSTEM HARNESS/00_SHITTYSHIT_MASTER/.PROJECTS_SHITTYSHIT/_ACTIVE"
TEMP_UPLOAD_DIR="./public/uploads"

# App Config
NEXT_PUBLIC_APP_URL="http://localhost:3000"
```

---

## Step 5: Create Lib Files

### `lib/db.ts`

```typescript
import { PrismaClient } from '@prisma/client'

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined
}

export const prisma = globalForPrisma.prisma ?? new PrismaClient()

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma
```

### `lib/whisper.ts`

```typescript
import OpenAI from 'openai'
import fs from 'fs'

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
})

export async function transcribeAudio(filePath: string): Promise<string> {
  const audioFile = fs.createReadStream(filePath)
  
  const transcription = await openai.audio.transcriptions.create({
    file: audioFile,
    model: 'whisper-1',
    language: 'en',
  })
  
  return transcription.text
}
```

### `lib/claude.ts`

```typescript
import Anthropic from '@anthropic-ai/sdk'

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
})

export async function synthesizeProject(
  projectData: {
    name: string
    description?: string
    tags: string[]
    priority: number
    revenue: boolean
    artifacts: Array<{
      type: string
      originalName: string
      transcript?: string
    }>
  }
): Promise<{
  brief: string
  prd: string
  projectMd: string
}> {
  const prompt = buildSynthesisPrompt(projectData)
  
  const message = await anthropic.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 4096,
    messages: [
      {
        role: 'user',
        content: prompt,
      },
    ],
  })
  
  const content = message.content[0]
  if (content.type !== 'text') {
    throw new Error('Unexpected response type')
  }
  
  // Parse JSON response
  const result = JSON.parse(content.text)
  
  return {
    brief: result.brief,
    prd: result.prd,
    projectMd: result.projectMd,
  }
}

function buildSynthesisPrompt(projectData: any): string {
  // TODO: Build comprehensive prompt
  return `Synthesize project: ${projectData.name}`
}
```

### `lib/filesystem.ts`

```typescript
import fs from 'fs/promises'
import path from 'path'

export async function createProjectFolder(
  codename: string,
  files: {
    brief: string
    prd: string
    projectMd: string
  },
  artifacts: Array<{
    type: string
    originalName: string
    storagePath: string
  }>
): Promise<string> {
  const projectPath = path.join(
    process.env.UPLOAD_DIR!,
    codename
  )
  
  // Create folder structure
  await fs.mkdir(projectPath, { recursive: true })
  await fs.mkdir(path.join(projectPath, 'assets'), { recursive: true })
  await fs.mkdir(path.join(projectPath, 'assets', 'audio'), { recursive: true })
  await fs.mkdir(path.join(projectPath, 'assets', 'documents'), { recursive: true })
  await fs.mkdir(path.join(projectPath, 'assets', 'images'), { recursive: true })
  await fs.mkdir(path.join(projectPath, 'assets', 'video'), { recursive: true })
  
  // Write generated docs
  await fs.writeFile(path.join(projectPath, 'BRIEF.md'), files.brief)
  await fs.writeFile(path.join(projectPath, 'PRD.md'), files.prd)
  await fs.writeFile(path.join(projectPath, 'project.md'), files.projectMd)
  
  // Copy artifacts
  for (const artifact of artifacts) {
    const destDir = path.join(projectPath, 'assets', artifact.type)
    const destPath = path.join(destDir, artifact.originalName)
    await fs.copyFile(artifact.storagePath, destPath)
  }
  
  // Create session log
  const sessionLog = `# Session Log\n\n| Date | Agent | Summary | Files Changed |\n|------|-------|---------|---------------|\n| ${new Date().toISOString().split('T')[0]} | Project Compiler | Project created via web interface | All files |\n`
  await fs.writeFile(path.join(projectPath, 'session_log.md'), sessionLog)
  
  return projectPath
}
```

---

## Step 6: Create First API Route

### `app/api/project/create/route.ts`

```typescript
import { NextRequest, NextResponse } from 'next/server'
import { prisma } from '@/lib/db'
import { z } from 'zod'

const createProjectSchema = z.object({
  name: z.string().min(1),
  description: z.string().optional(),
  tags: z.array(z.string()),
  priority: z.number().min(1).max(5),
  revenue: z.boolean(),
})

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const data = createProjectSchema.parse(body)
    
    // Generate codename
    const codename = data.name
      .toUpperCase()
      .replace(/[^A-Z0-9]+/g, '_')
    
    // Create project in database
    const project = await prisma.project.create({
      data: {
        name: data.name,
        codename,
        description: data.description,
        tags: JSON.stringify(data.tags),
        priority: data.priority,
        revenue: data.revenue,
        status: 'draft',
      },
    })
    
    return NextResponse.json({
      id: project.id,
      codename: project.codename,
      status: project.status,
    })
  } catch (error) {
    console.error('Error creating project:', error)
    return NextResponse.json(
      { error: 'Failed to create project' },
      { status: 500 }
    )
  }
}
```

---

## Step 7: Create Basic UI

### `app/page.tsx`

```typescript
import Link from 'next/link'

export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-8">Project Compiler</h1>
        
        <div className="space-y-4">
          <Link
            href="/new"
            className="block p-6 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
          >
            <h2 className="text-2xl font-semibold">+ New Project</h2>
            <p className="mt-2">Create a new project from voice and documents</p>
          </Link>
          
          <div className="p-6 bg-gray-100 rounded-lg">
            <h2 className="text-2xl font-semibold mb-4">Recent Projects</h2>
            <p className="text-gray-600">No projects yet</p>
          </div>
        </div>
      </div>
    </main>
  )
}
```

### `app/new/page.tsx`

```typescript
'use client'

import { useState } from 'react'

export default function NewProject() {
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    const response = await fetch('/api/project/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name,
        description,
        tags: ['#infra'],
        priority: 3,
        revenue: false,
      }),
    })
    
    const data = await response.json()
    console.log('Project created:', data)
  }
  
  return (
    <main className="min-h-screen p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-8">New Project</h1>
        
        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block text-sm font-medium mb-2">
              Project Name
            </label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full p-3 border rounded-lg"
              required
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium mb-2">
              Description
            </label>
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full p-3 border rounded-lg"
              rows={4}
            />
          </div>
          
          <button
            type="submit"
            className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
          >
            Create Project
          </button>
        </form>
      </div>
    </main>
  )
}
```

---

## Step 8: Run Development Server

```bash
pnpm dev
```

Open http://localhost:3000

---

## Next Steps

1. **Test project creation** — Create a test project, verify database entry
2. **Add file upload** — Build FileUpload component
3. **Add audio recording** — Build AudioRecorder component
4. **Integrate Whisper** — Add transcription API route
5. **Build synthesis** — Complete Claude integration
6. **Test end-to-end** — Full workflow from voice to folder

---

## Troubleshooting

**Prisma errors:**
```bash
npx prisma generate
npx prisma migrate reset
```

**API key errors:**
- Check `.env.local` exists
- Verify API keys are valid
- Restart dev server after changing env vars

**File upload errors:**
- Check `UPLOAD_DIR` path exists
- Verify write permissions
- Check file size limits

---

*Getting Started Guide v0.1 | 2026-05-22*
