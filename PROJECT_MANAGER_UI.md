# PROJECT MANAGER UI
*Simple web interface to view, organize, and edit projects*

---

## Concept

A lightweight web interface that:
1. Shows all projects in a spreadsheet-like table
2. Lets you click into any project to view/edit its docs
3. Provides quick actions (create, update, move status)
4. Works with existing SHITTYSHIT folder structure
5. Can be opened in browser on LACES

---

## Minimal MVP Features

### 1. Project List View (Spreadsheet)
- Table view of all projects (from PROJECTS_SPREADSHEET.md)
- Sort by: Status, Priority, Last Updated
- Filter by: Tags, Revenue, Type
- Search by name or description

### 2. Project Detail View
- Show project folder contents
- Display project.md, BRIEF.md, PRD.md
- Edit any Markdown file in-place
- View assets (images, docs, audio)

### 3. Quick Actions
- Create new project (creates folder + project.md)
- Update project status (ACTIVE → PARKED, etc.)
- Add tag
- Update next action
- Refresh from filesystem

### 4. File Operations
- Create new Markdown file in project folder
- Upload file to assets/
- Delete file (with confirmation)
- Rename file

---

## Tech Stack (Super Simple)

**Option A: Python Flask (Easiest)**
```python
# project_manager.py
from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)
PROJECTS_ROOT = "/path/to/.PROJECTS_SHITTYSHIT"

@app.route('/')
def index():
    # Read PROJECTS_SPREADSHEET.md and parse table
    projects = parse_projects_spreadsheet()
    return render_template('index.html', projects=projects)

@app.route('/project/<codename>')
def project_detail(codename):
    # List files in project folder
    folder_path = os.path.join(PROJECTS_ROOT, '_ACTIVE', codename)
    files = os.listdir(folder_path)
    return render_template('project.html', codename=codename, files=files)

@app.route('/edit/<codename>/<filename>')
def edit_file(codename, filename):
    # Load file content for editing
    file_path = os.path.join(PROJECTS_ROOT, '_ACTIVE', codename, filename)
    with open(file_path, 'r') as f:
        content = f.read()
    return render_template('editor.html', codename=codename, filename=filename, content=content)
```

**Option B: Node.js + Express (More features)**
```javascript
// server.js
const express = require('express');
const fs = require('fs').promises;
const path = require('path');

const app = express();
const PROJECTS_ROOT = '/path/to/.PROJECTS_SHITTYSHIT';

app.get('/api/projects', async (req, res) => {
  const spreadsheet = await fs.readFile(
    path.join(PROJECTS_ROOT, 'PROJECTS_SPREADSHEET.md'),
    'utf8'
  );
  const projects = parseSpreadsheet(spreadsheet);
  res.json(projects);
});

app.get('/api/project/:codename', async (req, res) => {
  const folderPath = path.join(PROJECTS_ROOT, '_ACTIVE', req.params.codename);
  const files = await fs.readdir(folderPath);
  const fileContents = {};
  
  for (const file of files) {
    if (file.endsWith('.md')) {
      fileContents[file] = await fs.readFile(
        path.join(folderPath, file),
        'utf8'
      );
    }
  }
  
  res.json({ files, fileContents });
});
```

**Option C: Single HTML File (Simplest)**
```html
<!-- project-manager.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Project Manager</title>
  <style>
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
    .active { background-color: #e8f5e8; }
    .parked { background-color: #f5f5f5; }
    .mudroom { background-color: #fff3cd; }
  </style>
</head>
<body>
  <h1>Project Manager</h1>
  <div id="projects"></div>
  
  <script>
    // Load PROJECTS_SPREADSHEET.md via fetch
    fetch('PROJECTS_SPREADSHEET.md')
      .then(r => r.text())
      .then(parseTable)
      .then(renderTable);
    
    function parseTable(markdown) {
      // Parse the Markdown table
      // Simple regex to extract table rows
      const rows = markdown.match(/\|.*\|/g);
      return rows.slice(2).map(row => {
        const cells = row.split('|').filter(c => c.trim());
        return {
          name: cells[0],
          codename: cells[1],
          status: cells[2],
          type: cells[3],
          revenue: cells[4],
          priority: cells[5],
          tags: cells[6],
          lastUpdated: cells[7],
          nextAction: cells[8]
        };
      });
    }
    
    function renderTable(projects) {
      const html = `
        <table>
          <thead>
            <tr>
              <th>Name</th><th>Status</th><th>Priority</th><th>Tags</th><th>Next Action</th>
            </tr>
          </thead>
          <tbody>
            ${projects.map(p => `
              <tr class="${p.status.toLowerCase()}">
                <td><a href="#project-${p.codename}">${p.name}</a></td>
                <td>${p.status}</td>
                <td>${'★'.repeat(p.priority)}</td>
                <td>${p.tags}</td>
                <td>${p.nextAction}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      `;
      document.getElementById('projects').innerHTML = html;
    }
  </script>
</body>
</html>
```

---

## Implementation Phases

### Phase 1: Read-Only Viewer (Today)
- Single HTML file that reads PROJECTS_SPREADSHEET.md
- Display table with basic styling
- Click project name to show folder contents (text list)
- No editing, just viewing

### Phase 2: Simple Editor (Week 1)
- Add edit button for .md files
- Load file content into textarea
- Save button writes back to file
- Basic error handling

### Phase 3: Project Actions (Week 2)
- Create new project form
- Update status dropdown
- Add tag input
- Refresh from filesystem button

### Phase 4: File Operations (Week 3)
- Upload file to assets/
- Create new .md file
- Delete file (with trash folder)
- Rename file

---

## Folder Structure for UI

```
project-manager-ui/
├── index.html              # Main page (Phase 1)
├── styles.css             # Basic styling
├── app.js                 # JavaScript logic
├── server.py              # Python backend (if needed)
├── templates/             # HTML templates
│   ├── project.html
│   └── editor.html
└── README.md              # Setup instructions
```

---

## Quick Start (Phase 1 - Read Only)

### Option A: Pure HTML/JS (Easiest)

1. Create `project-manager.html` in your workspace root:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Project Manager - SHITTYSHIT</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; padding: 20px; }
    h1 { margin-bottom: 20px; color: #333; }
    .controls { margin-bottom: 20px; }
    .filter-input { padding: 8px; margin-right: 10px; }
    .status-badge { padding: 2px 6px; border-radius: 3px; font-size: 12px; }
    .active { background: #d4edda; color: #155724; }
    .parked { background: #f8f9fa; color: #6c757d; }
    .mudroom { background: #fff3cd; color: #856404; }
    table { width: 100%; border-collapse: collapse; }
    th, td { padding: 12px 8px; text-align: left; border-bottom: 1px solid #ddd; }
    th { background: #f8f9fa; font-weight: 600; }
    tr:hover { background: #f8f9fa; }
    .priority-1 { color: #dc3545; font-weight: bold; }
    .priority-2 { color: #fd7e14; }
    .priority-3 { color: #ffc107; }
    .priority-4 { color: #28a745; }
    .priority-5 { color: #6c757d; }
    .revenue-yes::before { content: "💰 "; }
    a { color: #007bff; text-decoration: none; }
    a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <h1>🏗️ SHITTYSHIT Project Manager</h1>
  
  <div class="controls">
    <input type="text" id="search" placeholder="Search projects..." class="filter-input">
    <select id="statusFilter" class="filter-input">
      <option value="">All Status</option>
      <option value="ACTIVE">ACTIVE</option>
      <option value="PARKED">PARKED</option>
      <option value="MUDROOM">MUDROOM</option>
    </select>
    <select id="tagFilter" class="filter-input">
      <option value="">All Tags</option>
      <option value="#revenue">#revenue</option>
      <option value="#infra">#infra</option>
      <option value="#content">#content</option>
      <option value="#creative">#creative</option>
    </select>
    <button onclick="refresh()">🔄 Refresh</button>
    <button onclick="createNew()">➕ New Project</button>
  </div>
  
  <div id="stats" style="margin-bottom: 20px; color: #666; font-size: 14px;">
    Loading projects...
  </div>
  
  <table id="projectsTable">
    <thead>
      <tr>
        <th width="25%">Project</th>
        <th width="10%">Status</th>
        <th width="5%">Pri</th>
        <th width="15%">Tags</th>
        <th width="15%">Type</th>
        <th width="10%">Revenue</th>
        <th width="20%">Next Action</th>
      </tr>
    </thead>
    <tbody id="projectsBody">
      <tr><td colspan="7">Loading...</td></tr>
    </tbody>
  </table>
  
  <script>
    let allProjects = [];
    
    async function loadProjects() {
      try {
        // Try to load from local file
        const response = await fetch('PROJECTS_SPREADSHEET.md');
        const text = await response.text();
        
        // Parse the Markdown table
        const lines = text.split('\n');
        const tableStart = lines.findIndex(l => l.startsWith('|------'));
        if (tableStart === -1) throw new Error('No table found');
        
        const projects = [];
        for (let i = tableStart + 2; i < lines.length; i++) {
          const line = lines[i].trim();
          if (!line.startsWith('|') || line.includes('---')) continue;
          if (line.includes('How to Add/Update')) break;
          
          const cells = line.split('|').map(c => c.trim()).filter(c => c);
          if (cells.length >= 9) {
            projects.push({
              name: cells[0],
              codename: cells[1],
              status: cells[2],
              type: cells[3],
              revenue: cells[4],
              priority: parseInt(cells[5]) || 3,
              tags: cells[6],
              lastUpdated: cells[7],
              nextAction: cells[8]
            });
          }
        }
        
        allProjects = projects;
        renderProjects(projects);
        updateStats(projects);
      } catch (error) {
        console.error('Error loading projects:', error);
        document.getElementById('projectsBody').innerHTML = `
          <tr><td colspan="7" style="color: red;">
            Error loading projects: ${error.message}<br>
            Make sure PROJECTS_SPREADSHEET.md exists in the same folder.
          </td></tr>
        `;
      }
    }
    
    function renderProjects(projects) {
      const tbody = document.getElementById('projectsBody');
      if (projects.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7">No projects found</td></tr>';
        return;
      }
      
      tbody.innerHTML = projects.map(p => `
        <tr>
          <td>
            <strong>${p.name}</strong><br>
            <small style="color: #666;">${p.codename}</small>
          </td>
          <td><span class="status-badge ${p.status.toLowerCase()}">${p.status}</span></td>
          <td class="priority-${p.priority}">${p.priority}</td>
          <td><small>${p.tags}</small></td>
          <td>${p.type}</td>
          <td class="${p.revenue === 'YES' ? 'revenue-yes' : ''}">${p.revenue}</td>
          <td><small>${p.nextAction}</small></td>
        </tr>
      `).join('');
    }
    
    function updateStats(projects) {
      const active = projects.filter(p => p.status === 'ACTIVE').length;
      const parked = projects.filter(p => p.status === 'PARKED').length;
      const mudroom = projects.filter(p => p.status === 'MUDROOM').length;
      const revenue = projects.filter(p => p.revenue === 'YES').length;
      
      document.getElementById('stats').innerHTML = `
        📊 <strong>${projects.length}</strong> total projects • 
        <span class="active">${active} ACTIVE</span> • 
        <span class="parked">${parked} PARKED</span> • 
        <span class="mudroom">${mudroom} MUDROOM</span> • 
        💰 ${revenue} revenue projects
      `;
    }
    
    function refresh() {
      loadProjects();
    }
    
    function createNew() {
      alert('Creating new project...\n\nFor now, add to PROJECTS_SPREADSHEET.md manually.\n\nPhase 2 will include a proper form.');
    }
    
    // Add filter functionality
    document.getElementById('search').addEventListener('input', filterProjects);
    document.getElementById('statusFilter').addEventListener('change', filterProjects);
    document.getElementById('tagFilter').addEventListener('change', filterProjects);
    
    function filterProjects() {
      const search = document.getElementById('search').value.toLowerCase();
      const status = document.getElementById('statusFilter').value;
      const tag = document.getElementById('tagFilter').value;
      
      const filtered = allProjects.filter(p => {
        if (search && !p.name.toLowerCase().includes(search) && 
            !p.codename.toLowerCase().includes(search) &&
            !p.tags.toLowerCase().includes(search)) {
          return false;
        }
        if (status && p.status !== status) return false;
        if (tag && !p.tags.includes(tag)) return false;
        return true;
      });
      
      renderProjects(filtered);
    }
    
    // Load projects on page load
    window.addEventListener('DOMContentLoaded', loadProjects);
  </script>
  
  <div style="margin-top: 40px; padding: 20px; background: #f8f9fa; border-radius: 5px;">
    <h3>Quick Actions</h3>
    <p>
      <strong>For Phase 2 (Editing):</strong><br>
      1. Create <code>server.py</code> to handle file operations<br>
      2. Add edit buttons to each project row<br>
      3. Create file editor modal<br>
      4. Add project creation form
    </p>
    <p>
      <strong>Current Limitations:</strong><br>
      • Read-only view<br>
      • No file editing<br>
      • No project creation<br>
      • Requires PROJECTS_SPREADSHEET.md in same folder
    </p>
  </div>
</body>
</html>
```

2. Save this as `project-manager.html` in your workspace root
3. Open it in browser (drag file to browser or use `file:///` URL)

### Option B: Python Flask (More Features)

Create `project-manager.py`:

```python
#!/usr/bin/env python3
"""
Simple Project Manager UI for SHITTYSHIT
Run: python project-manager.py
Open: http://localhost:5000
"""

import os
import json
from flask import Flask, render_template, request, jsonify, send_file
import markdown
import re

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def parse_projects_spreadsheet():
    """Parse PROJECTS_SPREADSHEET.md into structured data"""
    try:
        with open(os.path.join(BASE_DIR, 'PROJECTS_SPREADSHEET.md'), 'r') as f:
            content = f.read()
        
        # Find the table
        lines = content.split('\n')
        table_start = None
        for i, line in enumerate(lines):
            if line.startswith('|------'):
                table_start = i + 1
                break
        
        if table_start is None:
            return []
        
        projects = []
        for line in lines[table_start:]:
            line = line.strip()
            if not line.startswith('|') or '---' in line:
                continue
            if 'How to Add/Update' in line:
                break
            
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if len(cells) >= 9:
                projects.append({
                    'name': cells[0],
                    'codename': cells[1],
                    'status': cells[2],
                    'type': cells[3],
                    'revenue': cells[4],
                    'priority': int(cells[5]) if cells[5].isdigit() else 3,
                    'tags': cells[6],
                    'last_updated': cells[7],
                    'next_action': cells[8]
                })
        
        return projects
    except Exception as e:
        print(f"Error parsing spreadsheet: {e}")
        return []

@app.route('/')
def index():
    projects = parse_projects_spreadsheet()
    return render_template('index.html', projects=projects)

@app.route('/api/projects')
def api_projects():
    projects = parse_projects_spreadsheet()
    return jsonify(projects)

@app.route('/api/project/<codename>')
def api_project(codename):
    """Get project folder contents"""
    # Try _ACTIVE first, then other locations
    folders_to_check = ['_ACTIVE', '_PARKED', '_MUDROOM']
    
    for folder in folders_to_check:
        folder_path = os.path.join(BASE_DIR, folder, codename)
        if os.path.exists(folder_path):
            files = []
            for root, dirs, filenames in os.walk(folder_path):
                for f in filenames:
                    rel_path = os.path.relpath(os.path.join(root, f), folder_path)
                    files.append({
                        'name': f,
                        'path': rel_path,
                        'size': os.path.getsize(os.path.join(root, f))
                    })
            return jsonify({
                'codename': codename,
                'folder': folder,
                'files': files
            })
    
    return jsonify({'error': 'Project not found'}), 404

@app.route('/view/<codename>/<path:filename>')
def view_file(codename, filename):
    """View a file from project folder"""
    # Find the project folder
    folders_to_check = ['_ACTIVE', '_PARKED', '_MUDROOM']
    
    for folder in folders_to_check:
        file_path = os.path.join(BASE_DIR, folder, codename, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            
            if filename.endswith('.md'):
                # Convert Markdown to HTML
                html = markdown.markdown(content, extensions=['tables', 'fenced_code'])
                return f'<html><body style="padding:20px;"><pre>{content}</pre></body></html>'
            else:
                # Plain text
                return f'<html><body style="padding:20px;"><pre>{content}</pre></body></html>'
    
    return 'File not found', 404

if __name__ == '__main__':
    print("Starting Project Manager UI...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
```

Then create `templates/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Project Manager</title>
    <style>
        /* Same CSS as Option A */
    </style>
</head>
<body>
    <h1>Project Manager</h1>
    <div id="projects">
        {% for project in projects %}
        <div class="project-card">
            <h3>{{ project.name }}</h3>
            <p><strong>Status:</strong> {{ project.status }}</p>
            <p><strong>Next:</strong> {{ project.next_action }}</p>
            <a href="/view/{{ project.codename }}/project.md">View Files</a>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

---

## Which Option to Choose?

### Option A (HTML/JS) - **RECOMMENDED**
- **Pros:** Single file, no setup, works immediately
- **Cons:** Read-only, no editing
- **Best for:** Quick viewing TODAY

### Option B (Python Flask)
- **Pros:** Can edit files, more features
- **Cons:** Requires Python, setup time
- **Best for:** Full-featured editor next week

### Option C (Node.js/Express)
- **Pros:** JavaScript throughout, can reuse code from Project Compiler
- **Cons:** More setup
- **Best for:** If building Project Compiler anyway

---

## Next Steps

**Today:**
1. Create `project-manager.html` (Option A)
2. Open in browser to view all projects
3. Use as dashboard while working

**This Week:**
1. Add Python Flask backend (Option B)
2. Enable file editing
3. Add project creation form
4. Add file upload

**Next Week:**
1. Integrate with Cline Kanban
2. Add drag-drop reordering
3. Add Obsidian sync
4. Add advanced filters/views

---

## Integration Points

### With Cline Kanban
- Export projects to Cline Kanban format
- Import Cline updates back to spreadsheet
- Sync status between systems

### With Obsidian
- Watch project folders for changes
- Sync Markdown edits
- Use Obsidian as rich editor

### With Project Compiler Web
- Use same database
- Share project creation logic
- Unified interface

---

Start with **Option A** today to get immediate visibility, then build up features as needed.

