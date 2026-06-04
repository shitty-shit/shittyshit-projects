# SHITTYSHIT Projects

Master project management system for **Shittyshit.co**

---

## What This Is

A structured project management system for managing 34+ projects across:
- 🚀 Web applications and infrastructure
- 📝 Content projects and publications  
- 🎨 Creative works and photography
- 🤖 AI tooling and automation

---

## Quick Start

### View All Projects
```bash
# Open interactive dashboard in browser
start project-manager.html
```

### Update Project Status
```bash
# Edit the master spreadsheet
code PROJECTS_SPREADSHEET.md
```

### Check Consistency
```bash
# Verify folders match spreadsheet
python sync_projects.py check

# View statistics
python sync_projects.py stats
```

---

## Project Statistics

- **Total Projects:** 34
- **Active:** 11 projects in motion
- **Parked:** 12 projects on hold
- **Mudroom:** 11 projects needing classification

---

## Key Features

### 📊 Interactive Dashboard
- **project-manager.html** - Browser-based project viewer
- Filter by status, tags, priority
- Search by name or description
- Live statistics panel

### 📋 Project Spreadsheet
- **PROJECTS_SPREADSHEET.md** - Single source of truth
- Markdown table (opens in any editor)
- Works with Obsidian and Cline Kanban
- Easy to update and version control

### 🔧 Sync Utility
- **sync_projects.py** - Python automation
- Check for inconsistencies
- Update spreadsheet from folders
- Create missing project folders

### 📚 Documentation
- **AGENTS.md** - Agent entrypoint (read this first!)
- **CLAUDE.md** - Dispatcher rules
- **ME.md** - Operator context and preferences
- **project.md** - Project template

---

## Structure

```
.PROJECTS_SHITTYSHIT/
├── project-manager.html           # Interactive dashboard
├── PROJECTS_SPREADSHEET.md        # Master project list
├── sync_projects.py               # Sync utility
│
├── _ACTIVE/                       # Projects in motion
│   ├── PROJECT_COMPILER_WEB/      # Multi-modal project intake app
│   └── [other active projects]
│
├── _PARKED/                       # Projects not moving
├── _MUDROOM/                      # Raw intake
├── _PROJECT_FOLDER_MASTER/        # Master docs & schemas
└── tools_skills/                  # Tool & skill roster
```

---

## For AI Agents

**Important:** Read `AGENTS.md` first - it's the entrypoint on purpose.

Then read:
1. `AGENT_HANDOFF.md` - Complete context and handoff info
2. `CLAUDE.md` - Dispatcher role and rules
3. `ME.md` - How Kevin likes to work
4. `project.md` - Project template format

### Agent Role
- **Dispatcher** at root level - classify, route, prepare
- **Builder** inside project folders - execute and document
- **Updater** - keep project.md files current
- **Never** duplicate folders or project cards

---

## Current Active Projects

### 🔥 Priority 1-2 (Revenue & Infrastructure)

1. **PROJECT_COMPILER_WEB** - Web app for multi-modal project intake
   - Status: Fully specified, ready to build
   - Tech: Next.js + TypeScript + SQLite + Whisper API
   - Priority: 2 (Infrastructure)

2. **Irish Mythology Serial** - Serialized storytelling on Gumroad
   - Priority: 1 (Revenue)
   - Next: Ship Issue 01

3. **SpecKit** - Downloadable spec framework
   - Priority: 2 (Revenue)
   - Next: Define product scope

4. **BIGSHOT NYC** - Executive headshots & photography
   - Priority: 2 (Revenue)
   - Next: Spin up dedicated vault

---

## Getting Started (New Agent/Account)

1. **Clone this repository:**
   ```bash
   git clone [repo-url]
   cd shittyshit-projects
   ```

2. **Read the handoff docs:**
   - `AGENT_HANDOFF.md` - Start here
   - `AGENTS.md` - System rules
   - `ME.md` - Kevin's workflow

3. **Open the dashboard:**
   ```bash
   start project-manager.html
   ```

4. **Check project status:**
   ```bash
   python sync_projects.py stats
   ```

5. **Continue where we left off:**
   - Check "Next Action" in project.md files
   - Update session logs when making changes
   - Push to GitHub regularly

---

## Integration

### With Obsidian
See `OBSIDIAN_INTEGRATION.md` for:
- Vault setup
- Dataview dashboards
- Project templates
- Daily/weekly review templates

### With Cline Kanban
- Use spreadsheet as project reference
- Export filtered projects to Cline format
- Keep Cline for tasks, this for projects

---

## Company

**Shittyshit.co** (The Shittyshit)  
Brooklyn-based product and content studio  

**Operator:** Kevin Kane  
**Primary Storefront:** Gumroad  
**Working Style:** Voice-first, fast, direct execution

---

## Tools & Tech Stack

### Current Tools
- **Browser** - Interactive dashboard
- **Python 3.8+** - Sync utility (stdlib only)
- **Text Editor** - Markdown editing
- **Git** - Version control

### Optional Integrations
- **Obsidian** - Rich project editor
- **Cline** - Kanban boards
- **VS Code** - Development

### Planned (PROJECT_COMPILER_WEB)
- **Next.js** - Web framework
- **OpenAI Whisper API** - Transcription
- **Anthropic Claude API** - AI synthesis
- **SQLite/Supabase** - Database

---

## Contributing

This is a private repository for Shittyshit.co internal project management.

### If you're an agent:
1. Read `AGENTS.md` and `AGENT_HANDOFF.md`
2. Follow the project.md template exactly
3. Update session logs when making changes
4. Search before creating (no duplicates)

### If you're Kevin:
1. Update the spreadsheet as you work
2. Use the dashboard for quick views
3. Run sync utility to check consistency
4. Push changes regularly

---

## Session History

### 2026-06-03 - Initial System Build
- ✅ Created PROJECTS_SPREADSHEET.md (34 projects)
- ✅ Built project-manager.html dashboard
- ✅ Created sync_projects.py utility
- ✅ Wrote OBSIDIAN_INTEGRATION.md guide
- ✅ Fully specified PROJECT_COMPILER_WEB
- ✅ Created complete handoff documentation
- ✅ Ready for multi-account collaboration

---

## License

Private repository - © 2026 Shittyshit.co

All rights reserved.

---

## Quick Commands

```bash
# View dashboard
start project-manager.html

# Update projects
code PROJECTS_SPREADSHEET.md

# Check consistency
python sync_projects.py check

# View stats
python sync_projects.py stats

# Create missing folders
python sync_projects.py create

# Export to JSON
python sync_projects.py export

# Git workflow
git add .
git commit -m "Update: [description]"
git push
```

---

**Ready to ship. Ready to scale. Ready for your other Kiro Pro account.**

Start with `AGENT_HANDOFF.md` for complete context.
