# OBSIDIAN INTEGRATION GUIDE
*How to connect your SHITTYSHIT projects to Obsidian*

---

## Quick Setup

### Option 1: Use Obsidian as Your Project Manager (Recommended)

1. **Open Obsidian**
2. **Open this folder as a vault:**
   - File → Open folder as vault
   - Select: `C:\Users\idfk\Desktop\SHITTY_SYSTEM HARNESS\00_SHITTYSHIT_MASTER\.PROJECTS_SHITTYSHIT`
3. **Install Dataview plugin:**
   - Settings → Community plugins → Browse
   - Search for "Dataview"
   - Install and enable
4. **Create project dashboard:**

Create a new note called `Projects Dashboard.md`:

````markdown
```dataview
TABLE status, type, revenue, priority, tags, lastUpdated, nextAction
FROM ""
WHERE contains(file.name, "project.md") OR file.name = "PROJECTS_SPREADSHEET.md"
SORT priority ASC, status ASC
```
````

### Option 2: Sync with Separate Obsidian Vault

1. **Create symlink to projects:**
   ```cmd
   mklink /D "C:\Users\idfk\Obsidian\SHITTYSHIT Projects" "C:\Users\idfk\Desktop\SHITTY_SYSTEM HARNESS\00_SHITTYSHIT_MASTER\.PROJECTS_SHITTYSHIT"
   ```
2. **Add to existing Obsidian vault**
3. **Use folder as reference**

---

## Obsidian Templates for Projects

### Project Note Template

Create `Templates/Project Note.md`:

```markdown
---
project: "{{Project Name}}"
codename: "{{CODENAME}}"
status: "active"
type: "infra"
revenue: false
priority: 3
tags: "#infra"
lastUpdated: {{date:YYYY-MM-DD}}
---

# {{Project Name}}

**Status:** `= this.status`  
**Priority:** `= this.priority`  
**Revenue:** `= this.revenue`  

---

## Project Details

**Codename:** `= this.codename`  
**Type:** `= this.type`  
**Tags:** `= this.tags`  

---

## Next Action
{{next action}}

---

## Project Folder
`= link("_ACTIVE/" + this.codename)`

---

## Related Files
```dataview
LIST
FROM "_ACTIVE/{{CODENAME}}"
```

---

*Created: {{date:YYYY-MM-DD}}*
```

---

## Daily Workflow with Obsidian

### Morning Review
1. Open `Projects Dashboard.md`
2. Filter for `status = ACTIVE` and `priority <= 2`
3. Click into project notes
4. Update status as needed

### During Work
1. Keep Obsidian open
2. Edit project `.md` files directly
3. Use quick switcher (Ctrl+O) to jump between projects
4. Link related projects with `[[ ]]`

### Evening Update
1. Update `lastUpdated` dates
2. Move completed projects to PARKED
3. Add notes to project logs
4. Review MUDROOM for new projects

---

## Advanced Obsidian Features

### 1. Kanban Boards
```markdown
---
kanban-plugin: board
---

## Backlog

## In Progress

## Done

%% kanban:settings
```
```
{"kanban-plugin":"board"}
```
%%
```

### 2. Calendar Integration
```markdown
```dataview
CALENDAR file.ctime
FROM "_ACTIVE"
WHERE file.name = "project.md"
```
```

### 3. Project Timeline
```markdown
```dataview
TABLE lastUpdated, priority
FROM "_ACTIVE"
WHERE file.name = "project.md"
SORT lastUpdated DESC
```
```

### 4. Revenue Tracker
```markdown
```dataview
TABLE sum(priority) AS TotalPriority
FROM "_ACTIVE"
WHERE file.name = "project.md" AND revenue = true
GROUP BY status
```
```

---

## Templates for Common Project Types

### Content Project Template
```markdown
---
project: "{{Project Name}}"
type: "content"
revenue: true
tags: "#content #revenue"
---

## Content Plan
- [ ] Outline
- [ ] Draft
- [ ] Edit
- [ ] Publish

## Distribution Channels
- [ ] Gumroad
- [ ] Newsletter
- [ ] Social media

## Metrics
- Target audience:
- Price point:
- Launch date:
```

### Code Project Template
```markdown
---
project: "{{Project Name}}"
type: "code"
tags: "#code"
---

## Tech Stack
- Frontend:
- Backend:
- Database:
- Deployment:

## Features
- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3

## Development Log
| Date | What | Hours |
|------|------|-------|
|      |      |       |
```

### Infrastructure Project Template
```markdown
---
project: "{{Project Name}}"
type: "infra"
tags: "#infra"
---

## Problem Statement
What problem does this solve?

## Solution Architecture
How does it work?

## Dependencies
What does this depend on?

## Impact
Who benefits? What projects does this enable?
```

---

## Automations with Obsidian

### 1. Auto-create Project Notes
Use Templater plugin to create project notes from `PROJECTS_SPREADSHEET.md`

### 2. Daily Standup Note
Create a template that pulls today's active projects:

```markdown
# Daily Standup {{date:YYYY-MM-DD}}

## Active Projects Today
```dataview
TABLE nextAction
FROM "_ACTIVE"
WHERE file.name = "project.md" AND status = "ACTIVE" AND priority <= 3
```

## Yesterday's Progress
- 

## Today's Focus
1. 
2. 
3. 

## Blockers
- 
```

### 3. Weekly Review
```markdown
# Weekly Review {{date:YYYY-MM-DD}}

## Projects Completed
```dataview
LIST
FROM "_ACTIVE"
WHERE file.name = "project.md" AND status = "PARKED" AND lastUpdated >= date({{date:YYYY-MM-DD}}) - dur(7 days)
```

## New Projects Added
```dataview
LIST
FROM "_ACTIVE"
WHERE file.name = "project.md" AND file.ctime >= date({{date:YYYY-MM-DD}}) - dur(7 days)
```

## Revenue Projects Status
```dataview
TABLE nextAction, lastUpdated
FROM "_ACTIVE"
WHERE file.name = "project.md" AND revenue = true
SORT lastUpdated DESC
```

## Next Week's Focus
1. 
2. 
3. 
```

---

## Integration with Cline

### Option 1: Share Project List
1. Export `PROJECTS_SPREADSHEET.md` to Cline
2. Use as reference in Cline Kanban
3. Sync updates manually

### Option 2: Use Obsidian as Source of Truth
1. Keep all project data in Obsidian
2. Cline reads from Obsidian vault
3. Single source of truth

### Option 3: Bidirectional Sync
1. Create sync script that updates both systems
2. Use GitHub as intermediary
3. More complex but fully automated

---

## Recommended Obsidian Plugins

| Plugin | Purpose | Why |
|--------|---------|-----|
| **Dataview** | Query projects | Essential for dashboards |
| **Templater** | Auto-create notes | Save time on project setup |
| **Calendar** | Track project dates | Visual timeline |
| **Kanban** | Project boards | Visual workflow |
| **QuickAdd** | Fast note creation | Quick project updates |
| **Various Complements** | Auto-complete | Faster typing |
| **Obsidian Git** | Version control | Backup projects |
| **Excalidraw** | Diagrams | Visual planning |

---

## Quick Start Commands

### Set up Obsidian vault:
```cmd
# Create vault in current folder
echo # Obsidian Vault > .obsidian/core-plugins.json
```

### Add to existing vault:
1. Copy `.PROJECTS_SHITTYSHIT` folder to vault
2. Or create symlink (recommended)

### First-time setup:
1. Install Dataview plugin
2. Create `Projects Dashboard.md`
3. Set up project templates
4. Create daily standup template

---

## Troubleshooting

### Projects not showing in Dataview?
- Check frontmatter formatting
- Ensure Dataview queries are in code blocks
- Verify file paths are correct

### Can't edit files?
- Check file permissions
- Ensure Obsidian has write access
- Try running as administrator

### Sync issues?
- Use Git for version control
- Set up automatic backups
- Consider cloud sync (Dropbox, etc.)

---

## Next Steps

1. **Today:** Open `.PROJECTS_SHITTYSHIT` as Obsidian vault
2. **Week 1:** Set up Dataview dashboard and templates
3. **Week 2:** Create automation scripts
4. **Week 3:** Integrate with Cline Kanban
5. **Week 4:** Set up Git backup system

---

*Obsidian is perfect for your workflow because it's Markdown-based, local-first, and highly customizable. Start with the Dataview dashboard today.*

