# Project Folder Master
Version: 0.1
Created: 2026-05-10
Scope: `.PROJECTS_SHITTYSHIT`

## What This Is

This folder is the control layer for the project folders in `.PROJECTS_SHITTYSHIT`.

It does not replace the project folders. It tracks them, names them, records dates, and gives agents a shared place to understand how the whole project folder system fits together.

## Ground Rules

- Evidence first. Use observed folder names, file names, dates, and existing templates before inventing labels.
- Keep local and global memory separate.
- Do not overwrite original dates. Add new time fields when the system imports, processes, or reviews something.
- Each project should eventually have its own local project file based on the existing `project.md` / `STANDARD_PROJECT_TEMPLATE.md`.
- The master layer tracks the whole system, not every detail inside every project.

## Local vs Global

Local project memory lives inside an individual project folder:

- `project.md` or a project-named `.md` file
- optional `PROJECT.yaml`
- assets, notes, links, and logs specific to that project

Global system memory lives here:

- `PROJECT_INDEX.yaml`
- `PROJECT_SCHEMA.md`
- `PROGRAMS.md`
- `TIMELINE.md`

## Current Source Folder

Observed project root:

`C:\Users\idfk\Desktop\SHITTY_SYSTEM HARNESS\00_SHITTYSHIT_MASTER\.PROJECTS_SHITTYSHIT`

## Current Objective

Create a reliable master layer so agents can:

- list all project folders
- preserve each folder's observed name and date
- classify folders without pretending certainty
- create or update per-project markdown files later
- connect projects into a larger communication/story/product system

## Status

This is the first baseline. It is intentionally plain and factual.
