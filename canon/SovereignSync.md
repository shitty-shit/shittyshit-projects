# SovereignSync Protocol

> *The command contract that prevents state-loss. Every cloud agent is a worker; every local file is canon. This protocol governs the handoff.*

---

## The Problem

When agents work across multiple platforms (CoChat threads, local Hermes sessions, Base 44 instances), context drifts. Threads get truncated. Platforms die. Projects get orphaned. Without an explicit command contract, the synthesis between cloud and local becomes a graveyard of half-finished ideas and stale memory fragments.

**SovereignSync is the bridge.**

---

## The Three Phases

Every data transaction across the LACES_CASES boundary follows **Harvest → Meld → Canon**:

### 1. HARVEST (Cloud Agent Pulls)
The cloud agent (Cuey, DoppelBrain, or any external model) reaches into the cloud or receives a prompt, extracts raw data, and generates a structured output. This output is **never** considered canon. It is a transient working stem.

- **Rule:** Cloud agents produce drafts, not truth.
- **Rule:** No cloud agent writes directly to local storage.
- **Rule:** All outputs must be explicitly scoped with a `HARVEST` tag indicating source agent, timestamp, and confidence.

### 2. MELD (Human or Tier 1 Vetter Reconciles)
Harvested outputs are routed to the reconciliation layer — typically a human review, a parallel-model consensus, or an Opus 4.8 vetting pass. During meld, conflicts are resolved, hallucinations are purged, and the output is upgraded from draft to candidate.

- **Rule:** Meld requires at least two independent sources or a Tier 1 vetter.
- **Rule:** Stale data (like "BlinkChange" or "IDFK AI as education platform") is purged at this stage by explicit canon integrity rules.
- **Rule:** Meld outputs are tagged `MELD` with a reconciliation hash.

### 3. CANON (Local File Receives)
Only melded, vetted candidates are written to local canonical storage (Obsidian vault, projectstack.md, me.md, biz.md, toolstack.md). The local synthesizer-of-record appends or patches the canon file.

- **Rule:** The clipboard is the transport layer. No sync services, no auto-upload, no middleware.
- **Rule:** Canon files are append-only for history; patches require explicit ops.
- **Rule:** Every canon update increments a version note in the file footer.

---

## The Command Contract (YANK/EXTRACT/COMPRESS/ROUTE)

| Command | Function | Executor | Direction |
| :--- | :--- | :--- | :--- |
| **YANK** | Pull raw output from a cloud agent session | Cuey | Cloud → Local |
| **EXTRACT** | Parse structured data from raw agent output | Cuey / Python | Cloud → Local |
| **COMPRESS** | Minify context to fit transport window | Python / AHK | Local ↔ Cloud |
| **ROUTE** | Direct output to the correct local canon file | Human / AHK | Local |

**Transport discipline:**
- Clipboard is the universal bus.
- Chat windows are I/O ports, not storage.
- Python is the conductor; AutoHotkey is the focus manager.
- `.md` files are the canonical storage format.

**Never:**
- Upload vault contents to cloud sync.
- Auto-write cloud outputs to local files without meld.
- Trust a single agent's output as truth.
- Use n8n, LangChain, or Docker for text-in/text-out pipelines.

---

## State-Loss Prevention Checklist

Before terminating any agent session:
- [ ] Is there a `HARVEST` tag on all cloud-generated outputs?
- [ ] Has the output passed through `MELD` (multi-source vet or Opus review)?
- [ ] Is the final destination a local `.md` file with a version footer?
- [ ] Was transport via clipboard only — no middleware, no auto-sync?
- [ ] Did the human explicitly confirm the canon update with Post/Discard?

---

## Emergency Recovery

If context is lost mid-session:
1. **Re-bootstrap** from the latest local `.md` canon file (me.md → projectstack.md → toolstack.md → biz.md).
2. **Re-scan** the cloud thread for the last `HARVEST` tag and replay extraction.
3. **Re-meld** using parallel agents if the original output is ambiguous.
4. **Re-patch** the canon file with a reconciliation note.

---

*File: SovereignSync Protocol | Version: 1.0 (June 2026) | Bound to: LACES_CASES*
