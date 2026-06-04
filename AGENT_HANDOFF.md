# AGENT HANDOFF DOCUMENTATION
*Complete context for any agent picking up this project*

---

## Company Information

**Company Name:** Shittyshit.co (or "The Shittyshit")  
**Operator:** Kevin Kane  
**Location:** Brooklyn, NYC  
**Working Style:** Voice-first, fast, direct execution  

---

## What This Repository Is

This is `.PROJECTS_SHITTYSHIT` - the master project management system for Shittyshit.co.

It contains:
1. **34+ active and parked projects** organized in `_ACTIVE/`, `_PARKED/`, `_MUDROOM/`
2. **Project management tools** (spreadsheet, dashboard, sync scripts)
3. **Project intake system** (PROJECT_COMPILER_WEB) - future web app for multi-modal project creation
4. **Master documentation** in `_PROJECT_FOLDER_MASTER/`
5. **Tools and skills roster** in `tools_skills/`

---

## Repository Structure

```
.PROJECTS_SHITTYSHIT/
├── AGENTS.md                           # Agent entrypoint - READ THIS FIRST
├── CLAUDE.md                           # Dispatcher rules
├── ME.md                               # Kevin's working preferences
├── project.md                          # Project template
├── PROJECTS_KANBAN.md                  # Kanban board view
├── PROJECTS_SPREADSHEET.md             # Master project list (34 projects)
├── project-manager.html                # Interactive dashboard (open in browser)
├── sync_projects.py                    # Python sync utility
├── OBSIDIAN_INTEGRATION.md             # Obsidian setup guide
├── PROJECT_MANAGEMENT_SYSTEM.md        # System overview
├── PROJECT_MANAGER_UI.md               # Future features spec
├── AGENT_HANDOFF.md                    # This file
│
├── _ACTIVE/                            # Projects currently in motion
│   ├── PROJECT_COMPILER_WEB/           # Web app for project intake
│   └── SIMPLE_PROJECT_MANAGER/         # Project management tools
│
├── _PARKED/                            # Projects not currently moving
├── _MUDROOM/                           # Raw intake, needs classification
├── _PROJECT_FOLDER_MASTER/             # Master index and schemas
│   ├── MASTER.md
│   └── PROJECT_INDEX.yaml
│
└── tools_skills/                       # Tool and skill roster
    └── TOOLS_ROSTER.md
```

---

## Current State (As of 2026-06-03)

### ✅ Completed in This Session

1. **PROJECT_COMPILER_WEB** - Fully specified web app for multi-modal project intake
   - Architecture documented
   - PRD written (5K words)
   - Roadmap created
   - Tech stack: Next.js + TypeScript + SQLite + Whisper API + Claude API
   - Status: Ready for implementation

2. **SIMPLE_PROJECT_MANAGER** - Lightweight project management tools
   - PROJECTS_SPREADSHEET.md created (34 projects cataloged)
   - project-manager.html dashboard built (interactive, works in browser)
   - sync_projects.py utility created
   - OBSIDIAN_INTEGRATION.md guide written
   - Status: Working and ready to use

### 📊 Project Inventory

- **Total Projects:** 34
- **ACTIVE:** 11 (including PROJECT_COMPILER_WEB)
- **PARKED:** 12
- **MUDROOM:** 11 (needs classification)

### 🔥 High Priority Projects

1. **PROJECT_COMPILER_WEB** - Priority 2, Infrastructure
2. **Irish Mythology Serial** - Priority 1, Revenue
3. **SpecKit** - Priority 2, Revenue
4. **SHITTY_BOOKS** - Priority 2, Revenue
5. **BIGSHOT NYC** - Priority 2, Revenue

---

## How to Use This Repository

### For Any Agent (Including You)

1. **First Action:** Read `AGENTS.md` - it's the roadblock on purpose
2. **Then Read:** `CLAUDE.md`, `ME.md`, `project.md`, `MASTER.md`
3. **Understand:** Kevin works voice-first, fast, direct. Assume compressed input.
4. **Rule:** Search before creating. Do not duplicate folders or project cards.
5. **Pattern:** Identify → Classify → Route → Prepare → Update project card

### Daily Workflow

1. **Morning:** Open `project-manager.html` to see active projects
2. **Working:** Update `PROJECTS_SPREADSHEET.md` as status changes
3. **Evening:** Run `python sync_projects.py check` to verify consistency

### Working on a Project

1. Navigate to `_ACTIVE/[PROJECT_CODENAME]/`
2. Read `project.md` first - it's the project card
3. Check "Next Action" section
4. Update session log when you make changes
5. Keep project memory local to project folder

---

## Git Repository Setup

### Current Status

This folder is already a Git repository.

### Remote Setup (Do This)

```bash
# Check current remotes
git remote -v

# If no remote exists, add GitHub remote:
git remote add origin https://github.com/[your-org]/.PROJECTS_SHITTYSHIT.git

# Or use SSH:
git remote add origin git@github.com:[your-org]/.PROJECTS_SHITTYSHIT.git
```

### Recommended GitHub Repo Name

- **Option 1:** `.PROJECTS_SHITTYSHIT` (matches folder name)
- **Option 2:** `shittyshit-projects` (cleaner public name)
- **Option 3:** `shittyshit-master` (indicates master system)

### Branch Strategy

- **main** - stable, documented projects
- **active-work** - day-to-day updates
- **experiments** - testing new tools/approaches

---

## Files to Commit (Initial Push)

### ✅ Include These

```
AGENTS.md
CLAUDE.md
ME.md
project.md
PROJECTS_KANBAN.md
PROJECTS_SPREADSHEET.md
project-manager.html
sync_projects.py
OBSIDIAN_INTEGRATION.md
PROJECT_MANAGEMENT_SYSTEM.md
PROJECT_MANAGER_UI.md
AGENT_HANDOFF.md
README.md (to be created)
.gitignore (to be created)

_PROJECT_FOLDER_MASTER/
tools_skills/
_ACTIVE/PROJECT_COMPILER_WEB/
_ACTIVE/SIMPLE_PROJECT_MANAGER/ (to be created)
```

### ⚠️ Review Before Committing

```
_ACTIVE/ (other projects - may contain private info)
_PARKED/ (legacy projects - review first)
_MUDROOM/ (raw intake - likely has private data)
```

### ❌ Do Not Commit

```
.env
.env.local
*.log
node_modules/
__pycache__/
*.pyc
.DS_Store
Thumbs.db
*.mp3
*.mp4
*.wav
*.mov
large_media_files/
```

---

## .gitignore Template

Create `.gitignore`:

```gitignore
# Environment files
.env
.env.local
.env*.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
desktop.ini

# Media files (too large for Git)
*.mp3
*.mp4
*.wav
*.mov
*.avi
*.flv
*.wmv
*.m4a

# Large assets
*.zip
*.tar.gz
*.rar
*.7z

# Sensitive data
secrets/
credentials/
private/
*.key
*.pem

# Build outputs
dist/
build/
*.egg-info/
.next/
out/

# Databases
*.db
*.sqlite
*.sqlite3

# Logs
*.log
logs/

# Temporary files
tmp/
temp/
*.tmp
*.bak
*.swp
```

---

## README for GitHub

Create `README.md`:

```markdown
# SHITTYSHIT Projects

Master project management system for Shittyshit.co

## What This Is

A structured project management system for managing 34+ projects including:
- Web applications and infrastructure
- Content projects and publications
- Creative works and photography
- AI tooling and automation

## Quick Start

1. **View Projects:** Open `project-manager.html` in browser
2. **Update Status:** Edit `PROJECTS_SPREADSHEET.md`
3. **Check Consistency:** Run `python sync_projects.py check`

## For Agents

Read `AGENTS.md` first - it explains how to work with this system.

## Structure

- `_ACTIVE/` - Projects in motion
- `_PARKED/` - Projects not currently moving
- `_MUDROOM/` - Raw intake, needs classification
- `_PROJECT_FOLDER_MASTER/` - Master documentation

## Company

**Shittyshit.co** - Brooklyn-based product and content studio

## License

Private repository - © 2026 Shittyshit.co
```

---

## Commands to Push Repository

```bash
# 1. Create .gitignore
# (Copy content from .gitignore template above)

# 2. Add files
git add AGENTS.md CLAUDE.md ME.md project.md
git add PROJECTS_KANBAN.md PROJECTS_SPREADSHEET.md
git add project-manager.html sync_projects.py
git add OBSIDIAN_INTEGRATION.md PROJECT_MANAGEMENT_SYSTEM.md
git add PROJECT_MANAGER_UI.md AGENT_HANDOFF.md
git add README.md .gitignore
git add _PROJECT_FOLDER_MASTER/
git add tools_skills/
git add _ACTIVE/PROJECT_COMPILER_WEB/

# 3. Initial commit
git commit -m "Initial commit: SHITTYSHIT project management system

- 34 projects cataloged in PROJECTS_SPREADSHEET.md
- Interactive dashboard (project-manager.html)
- Python sync utility (sync_projects.py)
- Complete documentation (AGENTS.md, CLAUDE.md, ME.md)
- PROJECT_COMPILER_WEB fully specified
- Ready for multi-account collaboration"

# 4. Set up remote (replace with your actual repo URL)
git remote add origin https://github.com/[your-org]/shittyshit-projects.git

# 5. Push to GitHub
git branch -M main
git push -u origin main
```

---

## For Your Other Kiro Pro Account

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/[your-org]/shittyshit-projects.git
   cd shittyshit-projects
   ```

2. **Read the entrypoint:**
   ```bash
   # In Kiro, ask: "Read AGENT_HANDOFF.md and AGENTS.md"
   ```

3. **Open the dashboard:**
   ```bash
   # Double-click project-manager.html
   # Or: start project-manager.html
   ```

4. **Understand context:**
   - 34 projects are cataloged
   - PROJECT_COMPILER_WEB is next to build
   - Simple project manager is working now
   - Kevin works voice-first, fast execution

5. **Continue work:**
   - Check `project.md` files for "Next Action"
   - Update session logs when you make changes
   - Push changes back to GitHub regularly

---

## Context Preservation Strategy

### What's Preserved in Git

- ✅ All documentation
- ✅ Project cards (project.md files)
- ✅ System rules (AGENTS.md, CLAUDE.md, ME.md)
- ✅ Tools (dashboard, sync scripts)
- ✅ Master index and schemas

### What's Not in Git (Privacy)

- ❌ Large media files
- ❌ Private notes in MUDROOM
- ❌ Credentials or API keys
- ❌ Work-in-progress in legacy folders

### Session Context Transfer

**This Session Created:**
1. PROJECT_COMPILER_WEB (full spec, ~15K words)
2. SIMPLE_PROJECT_MANAGER (working tools)
3. PROJECTS_SPREADSHEET.md (34 projects)
4. project-manager.html (dashboard)
5. sync_projects.py (sync utility)
6. Integration guides (Obsidian, Cline)
7. This handoff document

**Next Session Should:**
1. Review what was built
2. Test the dashboard
3. Initialize PROJECT_COMPILER_WEB (Next.js setup)
4. Or continue with other priority projects

---

## Agent Instructions for Next Session

```markdown
You are continuing work on the SHITTYSHIT project management system.

FIRST ACTIONS:
1. Read AGENT_HANDOFF.md (this file) - you are here
2. Read AGENTS.md for system rules
3. Read CLAUDE.md for dispatcher role
4. Read ME.md for Kevin's working style
5. Check PROJECTS_SPREADSHEET.md for current project status

CURRENT CONTEXT:
- 34 projects cataloged
- Simple project manager tools working (dashboard + scripts)
- PROJECT_COMPILER_WEB fully specified, ready to build
- Kevin has another Kiro Pro account and wants seamless handoff

YOUR ROLE:
- Continue building PROJECT_COMPILER_WEB, OR
- Work on other priority projects as Kevin directs
- Keep project.md files updated
- Push changes to Git regularly
- Maintain the spreadsheet as source of truth

KEVIN'S STYLE:
- Voice-first input (may be compressed or nonlinear)
- Fast execution (do the work, don't just describe)
- Revenue projects matter most
- Infrastructure matters when it unblocks revenue

RULES:
- Search before creating (no duplicates)
- Keep project memory local to project folders
- Update session logs when you change things
- Follow the SHITTYSHIT project.md template exactly
```

---

## Technical Handoff

### Dependencies Installed
- None yet (this is documentation only)

### To Install for PROJECT_COMPILER_WEB
```bash
# When ready to start building:
cd _ACTIVE/PROJECT_COMPILER_WEB
npx create-next-app@latest project-compiler-web --typescript --tailwind --app
cd project-compiler-web
pnpm install prisma @prisma/client openai @anthropic-ai/sdk
# See GETTING_STARTED.md for full instructions
```

### Python Environment
```bash
# For sync_projects.py:
python --version  # Should be 3.8+
# No additional packages needed (uses stdlib only)
```

---

## FAQ for Next Agent

**Q: Where do I start?**  
A: Read this file, then AGENTS.md, then check "Next Action" in project.md files.

**Q: What's the priority?**  
A: Check with Kevin, but likely PROJECT_COMPILER_WEB (Priority 2, infrastructure).

**Q: Can I change the structure?**  
A: Discuss with Kevin first. He has a system that works.

**Q: How do I add a new project?**  
A: Add to PROJECTS_SPREADSHEET.md, run `python sync_projects.py create`.

**Q: What if I find inconsistencies?**  
A: Run `python sync_projects.py check` to identify issues.

**Q: How do I know what was done in the last session?**  
A: Read session logs in project.md files, check Git commit messages.

---

## Contact & Company Info

**Company:** Shittyshit.co (The Shittyshit)  
**GitHub:** [your-org]/shittyshit-projects (to be set up)  
**Primary Storefront:** Gumroad  
**Operator:** Kevin Kane, Brooklyn  

**Working Hours:** Kevin works at all hours, voice-first  
**Response Style:** Direct, fast, builder-focused  

---

## Version History

- **v1.0** (2026-06-03) - Initial handoff documentation created
  - 34 projects cataloged
  - Simple project manager tools built
  - PROJECT_COMPILER_WEB fully specified
  - Ready for Git push and multi-account work

---

*This handoff document ensures zero context loss when switching between Kiro Pro accounts or bringing in new agents. Everything needed to continue is documented.*

**Next Step:** Push to GitHub, clone in other account, read this file again.

