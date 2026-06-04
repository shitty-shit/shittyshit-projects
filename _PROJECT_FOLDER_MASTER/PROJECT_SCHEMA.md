# Project Schema

Version: 0.1
Created: 2026-05-10

## Purpose

This file defines the minimum fields every project should eventually expose, either in `project.md`, a project-named `.md` file, or `PROJECT.yaml`.

## Required Identity Fields

```yaml
project_name:
codename:
observed_folder_name:
status: mudroom
type:
priority:
owner:
tags: []
confidence: unknown
```

## Required Date Fields

```yaml
dates:
  original_date:
  captured_date:
  imported_date:
  processed_date:
  last_reviewed_date:
  target_publish_date:
```

Rules:

- `original_date` means when the idea/event/content actually came from.
- `captured_date` means when it was written, recorded, dictated, saved, or exported.
- `imported_date` means when it entered this project system.
- `processed_date` means when an agent classified or summarized it.
- `last_reviewed_date` means when a human or agent last judged it.
- Do not replace one date with another.

## Required Human Sections

- What this is
- Assets in this folder
- Tools for this project
- Current status
- Next action
- Open questions
- Session log

## Confidence Rule

Agents must mark uncertain claims as uncertain. Use:

```yaml
confidence: observed | inferred | proposed | unknown
```

## Naming Rule

Keep the observed folder name. Add a cleaned project name only after review.
