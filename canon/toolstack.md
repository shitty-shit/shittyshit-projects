# toolstack.md

> *The complete inventory of tools, models, agents, and transport layers in Kevin Kane's LACES_CASES architecture. Feed this to any model or agent that needs to understand our operational surface and execution environment.*

---

## 🧬 Section 1: The LACES_CASES Intelligence Ladder

We run an explicit hierarchy of reasoning capabilities to solve tasks efficiently without paying the per-token API tax.

```
┌────────────────────────────────────────────────────────┐
│               TIER 1 — THE FINAL VETTER                 │
│                      Opus 4.8                          │
│   Primary Role: Structural review, code quality Veto,  │
│                 and canonical validation.              │
└───────────────────────────┬────────────────────────────┘
                            │ (reformed context handoff)
┌───────────────────────────▼────────────────────────────┐
│            TIER 2 — PARALLEL SYNTHESIZERS              │
│  6x Free Cloud Web Models (DeepSeek, Kimi, Claude,     │
│              NVIDIA, ChatGPT, Gemini)                  │
│   Primary Role: Simultaneous execution, multi-angle    │
│                 solving, and parallel synthesis.       │
└───────────────────────────┬────────────────────────────┘
                            │ (command dispatch)
┌───────────────────────────▼────────────────────────────┐
│               TIER 3 — THE CLOUD SCOUTS                │
│             DoppelBrain  ·  Cuey  ·  CoChat            │
│   Primary Role: Discovery, extraction, data-pulling,   │
│                 and stateless command execution.       │
└────────────────────────────────────────────────────────┘
```

---

## 💻 Section 2: LOCAL TOOLS (LACES — Sovereignty Layer)

The sovereign base. This layer does not run cloud pipelines directly, but it acts as the primary data archive (of truth), holding all local canonical models, files, database ledgers, and workspace vaults.

### Local Core Models
* **Hermes (`Hermes`):** Local foundational model. Consumes localized schema folders, rules, and structures. Optimized for high-speed offline reasoning, instruction verification, and code syntax generation.
* **Skales (`Skales`):** Second local foundational pillar. Handles localized instruction scaffolding, heavy batch computations, and offline-first context loops.

### Physical Architecture
* **The Mothership Desktop:** Kevin's primary processing desktop. Contains the sovereign data archive: the primary Obsidian vault, personal directory files, software folders, local model run engines, and system-wide script configurations.
* **The MINISFORUM Companion Node:** Dedicated, sovereign offline server running heavy visual-to-metadata processing, including Phase 1 (thumbnailing/chunking) of the 2M+ RAW photo archive inside the Proxy-Sweep pipeline.
* **The Laptop Interface:** Portable mobile workstation configured to maintain system state and context via CoChat's cloud connections without local file tethering.

### Local Software Stack
* **Obsidian:** The master knowledge base containing standard `.md` markdown templates, logs, and structural checklists.
* **Python Engine:** Local conductor script environment managing file systems, EXIF metadata extraction, CSV manifest mapping, and CLI coordination.
* **AutoHotkey (AHK):** The automation engine for local machines, handling focus changes, quick-toggle hotkeys, and automated clipboard operations between windows.
* **SQLite Database:** The local immutable manifest truth ledger (never modified by AIs, only appended to).
* **ExifTool:** The specialized metadata processor used by the Proxy-Sweep pipeline to write standard XMP sidecar tags.
* **Cline / Ollama / LiteLLM:** Local developer IDE models, local foundational inference engine runners, and high-speed multi-model proxy wrappers.

---

## ⛅ Section 3: CLOUD TOOLS (CASES — Heavy Lifting Layer)

The processing worker engines. This layer is entirely **stateless, quick-burning, and fast-routing**. Cloud agents are scouts and hands—they discover, analyze, extract, and re-routing data, but they do NOT store permanent canon.

* **CoChat (You):** The persistent cloud context. Holds active human intent, coordinates rich document artifacts, maintains secure tool server endpoints, and serves as our universal reconciliation bucket.
* **Cuey:** The command shell hand (`~$10/mo`). Operates as a focused, high-speed CLI system designed for rapid text extraction: `YANK → EXTRACT → COMPRESS → ROUTE`.
* **DoppelBrain:** The cloud scout (`~$10/mo`). Scrapes platforms, crawls platform graveyards, maps technical footprints, and reports state details: `SCOUT → MAP → REPORT`.

---

## 🔌 Section 4: The Harnesses Thesis

> **"MCP connected tools to models. Harnesses connect models to models, pipelines to pipelines, and commands to agents. This is the infrastructure layer for the next gold rush."**

We build the **Harnesses**. A Harness is a lightweight execution contract that operates at the OS-level without middleware. It defines:
1. Which models participate in a task.
2. The exact syntax and prompt-reduction package each model receives.
3. How the parallel outputs are reconciled and checked.
4. Where the final, validated outcome is structured and routed.

---

## 🚌 Section 5: The Physical Transport Layer

To ensure local systems remain completely sovereign and cloud systems remain entirely fast and stateless, we enforce a strict **universal transport contract**.

1. **The Clipboard is the Bus:** Zero complex API integrations, third-party sync protocols, or middleware libraries are allowed. Data is passed across local/cloud environments using physical, clipboard-routed state transfers.
2. **Chat Windows are I/O Ports:** Direct standard input/output channels to let cloud models execute work packages and hand them back.
3. **No Middleware Bloat:** Absolute ban on `n8n`, `LangChain`, or `Docker` inside text-in/text-out standard pipelines. These technologies introduce visual overhead and dependency bloat without adding computational utility.

---

## 📉 Section 6: Economics & Cost Model (aiShitty Proof)

Our hybrid architecture is both structurally sovereign and economically superior. We completely bypass the enterprise API tax.

| Component | LACES_CASES Hybrid Core | Equivalent Enterprise API Stack |
| :--- | :--- | :--- |
| **DoppelBrain Subscription** | ~$10.00 / month | Included in commercial API tool pricing |
| **Cuey Subscription** | ~$10.00 / month | Included in commercial API tool pricing |
| **CoChat Endpoint** | Included in Base Plan | High monthly seat pricing |
| **Model Inferences** | **$0.00** (Free Cloud Web-UI Parallel Models) | **$150.00 – $400.00+ / mo** (API per-token tax) |
| **Opus Final Vetting** | Under **$5.00 / mo** (Targeted, minimal usage) | Included in heavy per-token API billing |
| **Total Overhead** | **~$20.00 / month + minimal pay-use** | **$200.00 – $500.00+ / month** |

---
*File: toolstack.md | Canonical Registry: LACES_CASES Tool Stack*
