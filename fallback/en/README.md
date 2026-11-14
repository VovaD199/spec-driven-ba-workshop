# Fallback: example results of Days 1–4

> DRAFT v2. Language: English (Ukrainian version: [`../uk/README.md`](../uk/README.md)). For mentors; given to participants only when needed (see "When to use").

## Why this folder exists

The Cursor chat may be unavailable (free plan limit reached, an outage, restrictions). Then a participant cannot do the exercises with the AI agent. This folder contains **ready example results**: they can be read, checked against the code, edited with your own understanding and submitted.

## When to use

- The Cursor chat does not respond and cannot be restored (see [cursor-model-tips](../../materials/en/setup/cursor-model-tips.md)).
- A participant has fallen behind and wants to catch up on the day.
- A mentor shows what a good result looks like.

Always **try the normal path first** (cheapest model, restarting Cursor). The examples are a fallback.

## How to work with an example

1. Read the example.
2. **Check it against the template code** (open the file it mentions and compare): the example may contain inaccuracies, and the code in your version may differ.
3. **Edit it:** fix an error, add your own observation or question, delete the unnecessary. Without your own edit the submission does not meet the "own analysis" criterion.
4. In the PR description write: "A fallback example was used (chat unavailable)" and what exactly you changed.

> Mentor: grade the participant's own edits, not the example itself. A submission without edits does not meet the "own edit is visible" criterion.

## What is in the folder

| Day | File | What it is |
|---|---|---|
| 1 | `day-1/AGENTS.md` | Example `AGENTS.md` file for the project |
| 1 | `day-1/docs/architecture.md` | Example Mermaid architecture diagrams |
| 1 | `day-1/docs/questions.md` | 5 open questions about the project (step 10) |
| 2 | `day-2/contact-form-feature.md` | Feature document: original request, business context, RULE-NN (three states), AC-NN, Q-NN with owners |
| 2 | `day-2/issue-texts.md` | Issue texts (body and comments) for manual pasting |
| 3 | `day-3/poc-summary-example.md` | PoC summary (the Day 3 hypothesis, probes with `npx jest` results), checklist |
| 3 | `day-3/poc-notes-example.md` | PoC notes: two probes, what the tests showed, what was not checked |
| 3 | `day-3/figma-make/` | Three Figma Make screenshots: start screen, the "Open in canvas" button, the expected result (contact form with states) |
| 3 | `day-3/figma-analysis-example.md` | Mockup analysis: observations and questions (from the requirement, not from a real Figma; questions Q-11…Q-16) |
| 4 | `day-4/spec-contact-form.md` | Specification: 8 artefacts, NFR, matrix; IDs from Day 2 |
| 4 | `day-4/slice-contact-form.md` | PoC slice from the specification |
| 4 | `day-4/ai-check-notes-example.md` | Audit of 5 claims with quotes (structure example) |
| 4 | `day-4/handoff-example.md` | Handoff pack with Definition of Ready (mockup sections are illustrative) |

## Where the examples come from

- `day-1/*`: result of a real attempt in Cursor on the template; file paths in the diagrams were checked against the code.
- `day-2/*`: compiled from the template code (files and values checked manually).
- `day-3/poc-*`: both probes were applied on the template and the `npx jest` results are real; there are no checks in the browser, and this is stated in the examples.
- `day-1/docs/questions.md`, `day-4/*` (IDs, NFR, matrix, audit): compiled per the current instructions; the audit and the matrix illustrate the structure, not a real AI run.

## Limitations

- The examples are not a reference of the "only correct" answer: your participant may get a different one.
- The Day 1 diagrams and the `AGENTS.md` example may partly differ from what your own agent produces: that is acceptable.

## Alignment with the current instructions

The Day 1–4 examples are aligned with the current instructions: the RULE/AC/Q/NFR IDs run through all days and match (Day 2 → Day 3 → Day 4); `questions.md`, three-state rules, questions with owners, NFR, the traceability matrix, the claim audit and Definition of Ready are included.

What was **not verified**: the examples have not been run through the full course with a new person, and paths and names in them are checked only against the template code. The Day 3 `jest` results were taken on Linux (Node 22); student results on Windows/macOS may differ, and the probes were not checked in the browser. Figma frame names in the Day 4 matrix are illustrative.

The student still **adds their own corrections**: it is part of the submission criteria.
