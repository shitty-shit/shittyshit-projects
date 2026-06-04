#!/bin/bash
# Push SHITTYSHIT Projects to GitHub
# Run this after creating your GitHub repository

echo "==================================="
echo "SHITTYSHIT Projects - GitHub Push"
echo "==================================="
echo ""

# Check if Git is initialized
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Initializing Git repository..."
    git init
fi

# Show current status
echo "Current status:"
git status --short
echo ""

# Add documentation and system files
echo "Adding core files..."
git add AGENTS.md CLAUDE.md ME.md project.md
git add PROJECTS_KANBAN.md PROJECTS_SPREADSHEET.md
git add project-manager.html sync_projects.py
git add OBSIDIAN_INTEGRATION.md PROJECT_MANAGEMENT_SYSTEM.md
git add PROJECT_MANAGER_UI.md AGENT_HANDOFF.md
git add README.md .gitignore
git add push_to_github.sh

# Add master documentation
echo "Adding master documentation..."
git add _PROJECT_FOLDER_MASTER/

# Add tools
echo "Adding tools..."
git add tools_skills/

# Add active projects
echo "Adding PROJECT_COMPILER_WEB..."
git add _ACTIVE/PROJECT_COMPILER_WEB/

echo ""
echo "Files staged. Review before committing:"
git status
echo ""

read -p "Commit these files? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git commit -m "Initial commit: SHITTYSHIT project management system

- 34 projects cataloged in PROJECTS_SPREADSHEET.md
- Interactive dashboard (project-manager.html)
- Python sync utility (sync_projects.py)
- Complete documentation (AGENTS.md, CLAUDE.md, ME.md)
- PROJECT_COMPILER_WEB fully specified
- SIMPLE_PROJECT_MANAGER tools built
- Ready for multi-account collaboration

Company: Shittyshit.co
Session: 2026-06-03"
    
    echo ""
    echo "Commit created!"
    echo ""
    echo "Next steps:"
    echo "1. Create GitHub repository (public or private)"
    echo "2. Copy the repository URL"
    echo "3. Run:"
    echo "   git remote add origin https://github.com/[your-org]/shittyshit-projects.git"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo ""
else
    echo "Commit cancelled. Files remain staged."
fi
