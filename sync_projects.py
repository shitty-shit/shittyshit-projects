#!/usr/bin/env python3
"""
Simple project sync utility.
Syncs between PROJECTS_SPREADSHEET.md and project folders.

Usage:
  python sync_projects.py check      # Check for inconsistencies
  python sync_projects.py update     # Update spreadsheet from folders
  python sync_projects.py create     # Create missing project folders
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).parent
SPREADSHEET_FILE = BASE_DIR / "PROJECTS_SPREADSHEET.md"
ACTIVE_DIR = BASE_DIR / "_ACTIVE"
PARKED_DIR = BASE_DIR / "_PARKED"
MUDROOM_DIR = BASE_DIR / "_MUDROOM"

def parse_spreadsheet():
    """Parse PROJECTS_SPREADSHEET.md into list of projects"""
    if not SPREADSHEET_FILE.exists():
        print(f"Error: {SPREADSHEET_FILE} not found")
        return []
    
    with open(SPREADSHEET_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the table
    lines = content.split('\n')
    table_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith('|------'):
            table_start = i + 1
            break
    
    if table_start is None:
        print("Error: No table found in spreadsheet")
        return []
    
    projects = []
    for i in range(table_start, len(lines)):
        line = lines[i].strip()
        if not line.startswith('|'):
            continue
        if 'How to Add/Update' in line:
            break
        if '---' in line:
            continue
        
        cells = [c.strip() for c in line.split('|') if c.strip()]
        if len(cells) >= 9:
            projects.append({
                'name': cells[0],
                'codename': cells[1],
                'status': cells[2],
                'type': cells[3],
                'revenue': cells[4],
                'priority': cells[5],
                'tags': cells[6],
                'last_updated': cells[7],
                'next_action': cells[8],
                'line_number': i,
                'raw_line': line
            })
    
    return projects

def check_folders_exist(projects):
    """Check if project folders exist based on status"""
    missing_folders = []
    
    for project in projects:
        codename = project['codename']
        status = project['status']
        
        if status == 'ACTIVE':
            folder = ACTIVE_DIR / codename
        elif status == 'PARKED':
            folder = PARKED_DIR / codename
        elif status == 'MUDROOM':
            folder = MUDROOM_DIR / codename
        else:
            continue
        
        if not folder.exists():
            missing_folders.append({
                'project': project['name'],
                'codename': codename,
                'status': status,
                'expected': str(folder)
            })
    
    return missing_folders

def find_unregistered_folders():
    """Find folders not in spreadsheet"""
    registered = set()
    projects = parse_spreadsheet()
    for p in projects:
        registered.add(p['codename'])
    
    unregistered = []
    
    # Check all directory locations
    directories = [
        (ACTIVE_DIR, 'ACTIVE'),
        (PARKED_DIR, 'PARKED'),
        (MUDROOM_DIR, 'MUDROOM')
    ]
    
    for dir_path, status in directories:
        if dir_path.exists():
            for item in dir_path.iterdir():
                if item.is_dir():
                    codename = item.name
                    if codename not in registered and codename != '.keep':
                        unregistered.append({
                            'codename': codename,
                            'status': status,
                            'path': str(item),
                            'files': [f.name for f in item.iterdir() if f.is_file()]
                        })
    
    return unregistered

def update_spreadsheet():
    """Update spreadsheet with current folder state"""
    projects = parse_spreadsheet()
    unregistered = find_unregistered_folders()
    
    if not unregistered:
        print("No unregistered folders found.")
        return
    
    print(f"Found {len(unregistered)} unregistered folders:")
    for folder in unregistered:
        print(f"  - {folder['codename']} ({folder['status']})")
        print(f"    Files: {', '.join(folder['files'][:5])}")
        if len(folder['files']) > 5:
            print(f"    ... and {len(folder['files']) - 5} more")
    
    # Ask user what to do
    print("\nOptions:")
    print("  1. Add all to spreadsheet")
    print("  2. Add selected folders")
    print("  3. Skip for now")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == '1':
        add_all_to_spreadsheet(unregistered)
    elif choice == '2':
        add_selected_to_spreadsheet(unregistered)
    else:
        print("Skipping.")

def add_all_to_spreadsheet(folders):
    """Add all unregistered folders to spreadsheet"""
    with open(SPREADSHEET_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find where to insert (before "How to Add/Update")
    insert_line = None
    for i, line in enumerate(lines):
        if 'How to Add/Update' in line:
            insert_line = i
            break
    
    if insert_line is None:
        insert_line = len(lines) - 2
    
    new_lines = []
    today = datetime.now().strftime('%Y-%m-%d')
    
    for folder in folders:
        # Generate project name from codename
        name = folder['codename'].replace('_', ' ').title()
        
        # Guess type from files
        file_types = set(f.split('.')[-1].lower() for f in folder['files'])
        if any(ext in ['py', 'js', 'ts', 'java', 'cpp'] for ext in file_types):
            project_type = 'code'
        elif any(ext in ['md', 'txt', 'doc', 'pdf'] for ext in file_types):
            project_type = 'content'
        elif any(ext in ['jpg', 'png', 'gif', 'psd'] for ext in file_types):
            project_type = 'photo'
        else:
            project_type = 'infra'
        
        # Create new row
        new_row = f"| {name} | {folder['codename']} | {folder['status']} | {project_type} | NO | 3 | #{project_type} | {today} | Review folder contents |\n"
        new_lines.append(new_row)
    
    # Insert new lines
    lines[insert_line:insert_line] = new_lines
    
    # Write back
    with open(SPREADSHEET_FILE, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"Added {len(folders)} projects to spreadsheet.")

def add_selected_to_spreadsheet(folders):
    """Let user select which folders to add"""
    print("\nSelect folders to add (comma-separated numbers):")
    for i, folder in enumerate(folders, 1):
        print(f"  {i}. {folder['codename']} ({folder['status']})")
    
    selection = input("\nEnter numbers: ").strip()
    if not selection:
        print("No selection made.")
        return
    
    selected_indices = []
    for num in selection.split(','):
        try:
            idx = int(num.strip()) - 1
            if 0 <= idx < len(folders):
                selected_indices.append(idx)
        except ValueError:
            continue
    
    selected_folders = [folders[i] for i in selected_indices]
    add_all_to_spreadsheet(selected_folders)

def create_missing_folders():
    """Create folders for projects that don't have them"""
    projects = parse_spreadsheet()
    missing = check_folders_exist(projects)
    
    if not missing:
        print("All project folders exist.")
        return
    
    print(f"Found {len(missing)} missing folders:")
    for m in missing:
        print(f"  - {m['project']} ({m['status']}): {m['expected']}")
    
    confirm = input("\nCreate missing folders? (y/N): ").strip().lower()
    if confirm != 'y':
        print("Cancelled.")
        return
    
    for m in missing:
        folder_path = Path(m['expected'])
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Create basic project.md if doesn't exist
        project_md = folder_path / "project.md"
        if not project_md.exists():
            with open(project_md, 'w', encoding='utf-8') as f:
                f.write(f"""# {m['project']}

---

## IDENTITY BLOCK
```yaml
---
project_name:       {m['project']}
codename:           {m['codename']}
status:             {m['status'].lower()}
type:               {projects[0]['type'] if projects else 'infra'}
revenue:            false
gumroad_ready:      false
priority:           3
spun_up:            {datetime.now().strftime('%Y-%m-%d')}
last_updated:       {datetime.now().strftime('%Y-%m-%d')}
owner:              kevin
tags:               ['#{projects[0]['type'] if projects else 'infra'}]
blocker:            null
---
```

## WHAT THIS IS
*Describe the project here*

## CURRENT STATUS
Project folder created via sync script.

## NEXT ACTION
Review folder contents and update project details.

---

*Created by sync_projects.py on {datetime.now().strftime('%Y-%m-%d')}*
""")
        
        print(f"Created: {folder_path}")
    
    print(f"\nCreated {len(missing)} folders.")

def export_to_json():
    """Export projects to JSON for use in other tools"""
    projects = parse_spreadsheet()
    
    data = {
        'exported_at': datetime.now().isoformat(),
        'total_projects': len(projects),
        'projects': projects
    }
    
    output_file = BASE_DIR / "projects_export.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print(f"Exported {len(projects)} projects to {output_file}")

def main():
    import sys
    
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    command = sys.argv[1].lower()
    
    if command == 'check':
        print("Checking for inconsistencies...")
        missing = check_folders_exist(parse_spreadsheet())
        unregistered = find_unregistered_folders()
        
        if missing:
            print(f"\n❌ Missing {len(missing)} folders:")
            for m in missing:
                print(f"  - {m['project']} (should be in {m['expected']})")
        else:
            print("\n✅ All project folders exist.")
        
        if unregistered:
            print(f"\n⚠️  Found {len(unregistered)} unregistered folders:")
            for u in unregistered:
                print(f"  - {u['codename']} ({u['status']})")
        else:
            print("\n✅ All folders registered in spreadsheet.")
    
    elif command == 'update':
        update_spreadsheet()
    
    elif command == 'create':
        create_missing_folders()
    
    elif command == 'export':
        export_to_json()
    
    elif command == 'stats':
        projects = parse_spreadsheet()
        active = len([p for p in projects if p['status'] == 'ACTIVE'])
        parked = len([p for p in projects if p['status'] == 'PARKED'])
        mudroom = len([p for p in projects if p['status'] == 'MUDROOM'])
        revenue = len([p for p in projects if p['revenue'] == 'YES'])
        
        print(f"📊 Project Statistics")
        print(f"Total projects: {len(projects)}")
        print(f"  ACTIVE: {active}")
        print(f"  PARKED: {parked}")
        print(f"  MUDROOM: {mudroom}")
        print(f"  Revenue projects: {revenue}")
        
        # Type breakdown
        types = {}
        for p in projects:
            t = p['type']
            types[t] = types.get(t, 0) + 1
        
        print("\n📁 By type:")
        for t, count in sorted(types.items()):
            print(f"  {t}: {count}")
    
    else:
        print(f"Unknown command: {command}")
        print(__doc__)

if __name__ == '__main__':
    main()