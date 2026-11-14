# Analyst specification template (refinement)

Copy this file per feature/epic. Keep IDs stable across Jira/ADO/wiki links.

---

## Header
| Field | Value |
|-------|-------|
| Feature ID | FEAT-____ |
| Name | |
| Author | |
| Status | Discovery / Refinement / Ready |
| Stakeholders | |
| Last updated | |

---

## 1. Problem statement
**Who** is affected? **What** pain or opportunity? **Why now** (trigger, metric, risk)?

**Desired outcome (one sentence):**

---

## 2. Scope
### In scope
| ID | Item | Notes |
|----|------|-------|
| IN-01 | | |

### Exclusions
| ID | Exclusion | Reason |
|----|-----------|--------|
| OUT-01 | | |

**Enough for refinement:** every Must-have requirement maps to an IN item.

---

## 3. Actors and flow
| Actor | Description |
|-------|-------------|
| | |

**Main flow (happy path):**
```text
1.
2.
3.
```
**Alternative / exception flows:**
- 

---

## 4. Business rules
| ID | When (condition) | Then (result) | Else | Source |
|----|------------------|---------------|------|--------|
| RULE-01 | | | | Policy / Legal / Expert / Request #__ |

**Enough for refinement:** rules are verifiable, no wording like "handle appropriately".

---

## 5. Constraints and dependencies
| ID | Type | Description | Consequence if unresolved |
|----|------|-------------|---------------------------|
| CON-01 | Legal / Technical / Data / Vendor | | |
| DEP-01 | External system / team | | |

---

## 6. Assumptions
| ID | Assumption | How to verify | Owner |
|----|------------|---------------|-------|
| ASM-01 | | | |

---

## 7. Open questions
| ID | Question | Blocks | Owner | Due |
|----|----------|--------|-------|-----|
| Q-01 | | | | |

**Enough for refinement:** no open **blocker** without a dated decision or spike.

---

## 8. Acceptance signals
| ID | Signal | How we verify |
|----|--------|---------------|
| AC-01 | Observable behavior or metric | Demo / analytics / audit |

---

## 9. Traceability
Full matrix: see `traceability-matrix-template.md` (Request → RULE → AC → Design → Test idea → Status). Keep a link to it here.

| Rule / scope ID | AC | Test note |
|-----------------|----|-----------|
| RULE-01 | AC-01 | |

---

## 10. MVP / PoC planning (optional, before full development)
Use when the team needs a **validated slice** before committing to full delivery. Details in `mvp-poc-slice-template.md`.

| Field | Value |
|-------|-------|
| Slice type | PoC / MVP / Spike |
| Hypothesis (1 sentence) | |
| Smallest testable slice | |
| Target window | e.g. 2 weeks |

---

## Non-functional requirements (NFR)
| ID | Category (privacy / security / accessibility / localization / retention) | Requirement | Source |
|----|---------------------------------------------------------------------------|-------------|--------|
| NFR-01 | | | |

---

## Refinement checklist
- [ ] Problem and outcome agreed with the client
- [ ] Exclusions reviewed by affected teams
- [ ] Rules have sources or are marked draft
- [ ] Acceptance signals can be shown in a demo
- [ ] Open blockers have owners and dates

---

## Anti-patterns (remove before sharing if not needed)
- Do not paste a DB schema here unless it is a constraint
- Do not write pixel-level UI specs: link to the design when ready
- Do not close open questions with guesses: mark them ASM-##
