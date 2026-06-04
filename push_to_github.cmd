@echo off
REM Push SHITTYSHIT Projects to GitHub
REM Run this after creating your GitHub repository

echo ===================================
echo SHITTYSHIT Projects - GitHub Push
echo ===================================
echo.

REM Check if Git is initialized
git rev-parse --git-dir >nul 2>&1
if %errorlevel% neq 0 (
    echo Initializing Git repository...
    git init
)

REM Show current status
echo Current status:
git status --short
echo.

REM Add documentation and system files
echo Adding core files...
git add AGENTS.md CLAUDE.md ME.md project.md
git add PROJECTS_KANBAN.md PROJECTS_SPREADSHEET.md
git add project-manager.html sync_projects.py
git add OBSIDIAN_INTEGRATION.md PROJECT_MANAGEMENT_SYSTEM.md
git add PROJECT_MANAGER_UI.md AGENT_HANDOFF.md
git add README.md .gitignore
git add push_to_github.sh push_to_github.cmd

REM Add master documentation
echo Adding master documentation...
git add _PROJECT_FOLDER_MASTER/

REM Add tools
echo Adding tools...
git add tools_skills/

REM Add active projects
echo Adding PROJECT_COMPILER_WEB...
git add _ACTIVE/PROJECT_COMPILER_WEB/

echo.
echo Files staged. Review before committing:
git status
echo.

set /p CONFIRM="Commit these files? (y/n): "
if /i "%CONFIRM%"=="y" (
    git commit -m "Initial commit: SHITTYSHIT project management system" -m "- 34 projects cataloged in PROJECTS_SPREADSHEET.md" -m "- Interactive dashboard (project-manager.html)" -m "- Python sync utility (sync_projects.py)" -m "- Complete documentation (AGENTS.md, CLAUDE.md, ME.md)" -m "- PROJECT_COMPILER_WEB fully specified" -m "- SIMPLE_PROJECT_MANAGER tools built" -m "- Ready for multi-account collaboration" -m "" -m "Company: Shittyshit.co" -m "Session: 2026-06-03"
    
    echo.
    echo Commit created!
    echo.
    echo Next steps:
    echo 1. Create GitHub repository (public or private)
    echo 2. Copy the repository URL
    echo 3. Run:
    echo    git remote add origin https://github.com/[your-org]/shittyshit-projects.git
    echo    git branch -M main
    echo    git push -u origin main
    echo.
) else (
    echo Commit cancelled. Files remain staged.
)

pause
