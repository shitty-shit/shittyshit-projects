---
ijfw_version: 1.3.2
ijfw_schema: 1
type: software
primary_type: software
secondary_types: []
confidence: 0.901
detected_at: 2026-06-03T17:07:17.163Z
signals:
  - kind: manifest
    weight: 0.9
    manifests: [package.json]
  - kind: dir_design
    weight: 0.4
    name: assets
  - kind: file_extension_ratio
    weight: 0.7
    domain: software
    ratio: 0.909
    count: 1799
  - kind: file_extension_ratio
    weight: 0.7
    domain: design
    ratio: 0.065
    count: 129
---
# SHITTYSHIT PROJECTS AGENT ENTRYPOINT
*Read this first when you land in `.PROJECTS_SHITTYSHIT`. This is the roadblock on purpose.*

---

## WHAT THIS FILE IS

This is the agent-facing entrypoint for Codex, Claude Code, Cursor agents, local agents, and any future worker dropped into the Shittyshit Projects folder.

It is not the master Codex identity file.
It is not a replacement for `CLAUDE.md`.
It is not a project brief.

It tells you how to enter the project system without making a mess.

---

## FIRST MOVE

Before creating, moving, renaming, installing, or summarizing anything:

1. Read `CLAUDE.md` for the dispatcher rules.
2. Read `_PROJECT_FOLDER_MASTER/MASTER.md` for the master-layer map.
3. Read `project.md` for the standard per-project file format.
4. Read `tools_skills/TOOLS_ROSTER.md` before recommending or installing tools.
5. Read `ME.md` for operator context and working preferences.
6. Search existing folders before creating a new project.

If you are inside a specific project folder, read that folder's local `project.md`, `CLAUDE.md`, `AGENTS.md`, or equivalent project card before acting.

---

## YOUR ROLE HERE

At this level, you are a dispatcher and setup assistant, not the project builder.

Your job is to:

- identify what exists
- classify raw intake
- route work into `_ACTIVE`, `_PARKED`, `_MUDROOM`, or the right existing project
- prepare project folders so specialized agents can work cleanly
- keep project memory local to the project whenever possible
- update the relevant project file when you change project state

Do not execute deep project work from the root unless Kevin explicitly asks you to.

---

## FOLDER MAP

```text
.PROJECTS_SHITTYSHIT/
├── AGENTS.md                  # you are here
├── CLAUDE.md                  # dispatcher rules and operator context
├── ME.md                      # how Kevin wants agents to work with him
├── project.md                 # reusable per-project template
├── PROJECTS_KANBAN.md         # visible project flow
├── STANDARD_PROJECT_TEMPLATE.md
├── _PROJECT_FOLDER_MASTER/    # master map, schemas, timeline, programs
├── _MUDROOM/                  # raw intake lands here first
├── _ACTIVE/                   # classified projects in motion
├── _PARKED/                   # real projects, not moving right now
├── tools_skills/              # source of truth for tool and skill roster
└── [project folders]          # legacy or working project folders
```

---

## TOOL AND SKILL INSTALL RULE

Install or activate tools at the working project folder level, not globally from this root, unless Kevin explicitly asks for a global install.

The pattern is:

1. Identify the project folder you are actually working inside.
2. Read its local project file.
3. Check `tools_skills/TOOLS_ROSTER.md`.
4. Install or enable only the tools needed for that project.
5. Record what changed in the project's local session log.

If a tool or skill is missing, do not invent the stack. Add a clear open question or tool gap in the project file.

---

## PROJECT MEMORY RULE

Global memory belongs in `_PROJECT_FOLDER_MASTER`.
Local memory belongs inside the project folder.

Use the root only for routing, inventory, and governance.

Each serious project should eventually have:

- a project card based on `project.md`
- a status paragraph
- a single next action
- open questions
- a session log
- tool and skill notes

---

## KEVIN / OPERATOR CONTEXT

Kevin works voice-first, fast, and directly.

Assume input may be compressed, nonlinear, or partially transcribed. Your job is to infer carefully, inspect the folder evidence, and ask only when the next action would otherwise be risky.

Revenue projects matter.
Infrastructure matters when it unblocks revenue or repeatable execution.

Do not over-explain. Do the work, leave good notes, and keep the system navigable.

---

## HARD RULES

- Search before creating.
- Do not duplicate project folders or project cards.
- Do not overwrite original dates.
- Do not move raw intake without preserving where it came from.
- Do not install project tools globally from this root by default.
- Do not treat old legacy folders as trash unless a project file says they are deprecated.
- Do not revive deprecated JENKEV references.
- Do not replace `CLAUDE.md`; other agents still use it.
- Do not turn root-level work into a giant build session.

---

## SESSION EXIT

When you change anything meaningful:

1. Update the relevant project file or master file.
2. Add a short session-log entry where appropriate.
3. Name files changed.
4. Leave the next action obvious.

If you only inspected the system, say what you learned and do not create noise.

---

*This file is the first-stop guide for agents entering `.PROJECTS_SHITTYSHIT`. It exists so every agent can find the project rules before touching the work.*

<!-- IJFW-MEMORY-START -->
Project memory at .ijfw/memory/. Call `ijfw_memory_prelude` for full context.
<!-- IJFW-MEMORY-END -->

<!-- IJFW-AGENTS-START -->
No project agents yet. Run `ijfw team` to set them up.
<!-- IJFW-AGENTS-END -->
