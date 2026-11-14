# Mentor guide

> DRAFT v2. Language: [Українська](../uk/mentor-guide.md). Grading rules (threshold, deadlines, resubmission) are defined on the learning platform and are not repeated here. This document: **how to prepare, how to run the days, what to do when things go wrong, how to review submissions.** Separate files: [Day 0 checklist](day-0-checklist.md), [client simulation script (Day 2)](day-2-stakeholder-script.md).

## 1. Role and principles
- You teach **working with a specification as the source of truth**, using the analyst's strengths: asking "why", structuring, tracing, verifying. You do not teach programming.
- **Answer with a pointer, not a lecture.** Answer a student's question with a link to an instruction section, the [glossary](../../materials/en/day-0/glossary.md) or official documentation (question table in section 7). Detailed explanations "from scratch" eat the group's time.
- **20-minute rule:** a student stuck on a step for more than 20 min: fallback path, pair with a stronger student, or you show it on screen and the student continues with the files.
- Grade **what the student recorded and verified themself**, not a match with the reference. Experiment results differ between students.
- Two profiles, two tracks: **base** (everyone) and **fast** (stretch tasks at the end of each day).

## 2. Before the course (1-2 weeks ahead)
- [ ] Send [Day 0](../../materials/en/day-0/day-0-prepare.md), collect screenshots, chase the missing; go through the [Day 0 checklist](day-0-checklist.md).
- [ ] Do Days 1-4 yourself on a clean machine (Windows and macOS): verify the install commands, `npm install`, `npm run dev`, `npm test`.
- [ ] Check the student template: https://github.com/VovaD199/spec-driven-ba-workshop-template (**Use this template** button, running the app).
- [ ] **Figma:** find out who has an account; prepare the **mentor's canvas** with a ready mockup (view link, without the `?t=` token and without edit rights); walk through [Figma MCP](../../materials/en/day-4/figma-mcp-setup.md) on a clean machine.
- [ ] Prepare Humanizer (skill) and check its file for external links, `.env` access, shell commands. Hand students only the verified one.
- [ ] Verify the Spec Kit / OpenSpec / BMAD table (Day 4, block 1) against the documentation.
- [ ] Agree with the curator: submission channel, reply template, progress table.
- [ ] Fallback artifacts for each day: [`fallback/en/`](../../fallback/en/README.md) (examples in Ukrainian; update them per the "Known gaps" list in `fallback/uk/README.md`).
- [ ] Plan B in case Cursor/network is missing: you show on the projector, students work with files.

## 3. How submission works
- A student works in their own **public** repository created from the template (`sdd-workshop-<name>`) and for each day sends a Pull Request link (from branch `day-N` into `main` of their repository). On Day 2 also a link to the issue.
- **PR cycle:** the student submits, you leave feedback, the student revises **in the same branch** (a new commit updates the PR), after your OK the student clicks **Merge pull request** and starts the next day from an up-to-date `main`. Do not merge before feedback.
- Submission channel: `<given by the curator>`.

### General checklist for every PR (2 min)
In the **Files changed** tab:
- [ ] Only the day's expected files (table below).
- [ ] No `.env`, `node_modules`, `.cursor/mcp.json`, tokens, `docs/templates/`. **A token in the repository: tell the student immediately, revoke it (Git history keeps it).**
- [ ] PR into `main` of the student's own repository, not someone else's and not the template.
- [ ] Title `Day N: <short>`, description of 2-4 sentences (what was done, what was hard, what is unclear).

| Day | Required in the PR | Extra |
|---|---|---|
| 1 | `AGENTS.md`, `docs/architecture.md`, `docs/questions.md` | `.cursor/rules` (S1) |
| 2 | `docs/contact-form-feature.md`; **in the issue**: original, "Business context", AC, "Rules table:", impact analysis, questions | `docs-ba.mdc`, Humanizer, MCP |
| 3 | `docs/poc-notes.md`, `docs/poc-summary-<date>.md`, `docs/figma-contact-form-analysis.md`; **no code changes** | seed/label/flags |
| 4 | `docs/spec-contact-form.md`, `docs/ai-check-notes.md`, `docs/slice-contact-form.md`, `docs/handoff-contact-form.md`, `docs/rewrite-compare.md`, `docs/figma-contact-form-analysis.md` | `docs/ba-playbook.md` |

## 4. How to run each day
Minute-by-minute tables are at the end of each instruction ("For the mentor: timing"). Below is what they lack: risk points and plan B.

### Day 1 ([instruction](../../materials/en/day-1/day-1-instruction.md))
- **Risk points:** `git push` authentication (the most common blocker), long paths and SSL (Windows), `npm install` without network, terminal confusion (the server occupies the first one: a second is needed).
- **Demo:** 10 min Git/GitHub (analogy: a repository is a shared folder with history), then students.
- **Plan B:** Download ZIP; Codespaces (if allowed); you run the app on the projector, the student works with files (step 5 onward only needs files).
- **Time box:** if step 4 (running) takes over 20 min, do not wait for the group.
- **Review:** [rubric](#5-review-rubric-by-day), Day 1.

### Day 2 ([instruction](../../materials/en/day-2/day-2-instruction.md))
- **Risk points:** the densest day. Block 4 (code vs requirement) may stretch: cut the rules table to 8 rows. The agent invents line numbers.
- **Client simulation** (block 3): run it with the [script](day-2-stakeholder-script.md); assess whether the student recorded the goal, metric and ≥2 constraints and did not invent answers.
- **MCP** is optional (S2): do not let it eat the base track's time; revoke the token after class.
- **Plan B:** fallback `issue-texts.md`, `contact-form-feature.md`; a student without a Day 1 PR takes fallback artifacts.

### Day 3 ([instruction](../../materials/en/day-3/day-3-instruction.md))
- **Risk points:** probe results differ between students (normal: assess what was recorded); `git restore .` **before** committing the documents (repeat the order: commit first, then restore); Figma accounts and limits.
- **Before class:** check Figma accounts, have the mentor's canvas link.
- **Plan B:** without Figma Make: the student does B4-B5 on the mentor's canvas.

### Day 4 ([instruction](../../materials/en/day-4/day-4-instruction.md))
- **Risk points:** Figma MCP limit (20 calls/month), Cursor limit, block 5 time (cut NFR to 3 items), "Grounded" mislabeling (watch the 5-claim audit).
- **Template download** (block 0): check that the raw links open; fallback: an archive.
- **Figma MCP:** you demonstrate, students repeat; time box 15 min; without MCP: a description of the mockup in words.
- **Course feedback:** `<format given by the curator>`.

## 5. Review rubric by day
Rate each criterion **met / partly / not met** + one sentence to the student.

**Day 1.** (1) `AGENTS.md` and diagram in the PR, matching the real project (no invented pages). (2) ≥2 own corrections visible. (3) The diagram renders. (4) `docs/questions.md`: ≥4 open questions with "why" and "who", one about privacy. (5) No service files and secrets. *Typical mistakes:* invented pages, an unrendered diagram, `.env` in a commit, closed questions ("is there a form?").

**Day 2.** (1) The original issue is preserved; AC in the AC-NN + Given/When/Then + RULE-ID format, passed the linter. (2) The rules table matches the code, has three states, a client/server discrepancy found. (3) Questions Q-NN with owner and date, privacy among them. (4) "Business context" from the client conversation. (5) `docs/contact-form-feature.md` in the PR, ≥3 own edits. (6) No token. *Typical mistakes:* AC without `Then`; invented rows in the table; impact analysis mixed with AC; the original issue overwritten.

**Day 3.** (1) PoC summary: hypothesis, setup, changes, evidence (with test results), checklist, next step. (2) "Proven" only what is recorded in `poc-notes.md`; "developer needed" honest. (3) Duplicated validation noticed (client/server/tests/translations). (4) Only documents in the PR. (5) Figma analysis: own observations next to AI, ≥10 questions. (6) No secrets. *Typical mistakes:* facts and assumptions mixed; code ended up in the PR; summary written for techies.

**Day 4.** (1) Specification: 8 artifacts + NFR (≥4, with privacy) + a matrix without orphans; IDs kept from Day 2. (2) Rules match the code and the conversation; questions with owners and dates. (3) `ai-check-notes.md`: audit of 5 claims with quotes; gap closed without gaming the counter. (4) Slice: falsifiable hypothesis, OUT with reasons, two signals with thresholds, ≥2 parent IDs, Day 3 evidence. (5) Handoff pack: 9 sections, DoR, commit; Humanizer did not change IDs. (6) `rewrite-compare.md`. (7) Mockup analysis sections. (8) No secrets. *Typical mistakes:* long text instead of structure; IDs without links; a rule added only to remove Invented; technical solutions without a request.

## 6. Limits, spotting weak points, different levels

### Limits policy
| Resource | What to do |
|---|---|
| Cursor (free plan) | The cheapest model for routine work; a stronger one for blocks needing precision (Day 2 block 1, Day 4). Limit exhausted: you show on screen, the student works with files and fallback; do not buy plans for the course |
| Figma Make (150 credits/day on free) | One generation with the prompt; do not refine needlessly. Exhausted: the mentor's canvas |
| Figma MCP (20 calls/month on free) | One test request. Exhausted: description by link (method 3), description in words or a screenshot |
| GitHub PAT (Day 2, S2) | Fast track only; lifetime 7-30 days; revoke after class |

### Signs a student is falling behind (and what to do)
- Did not complete Day 0 or has no screenshot: seat them in a pair; fallback install paths.
- At minute 40 the app is still not running / no branch created: you show on screen, the student continues with files.
- The agent chat "writes for them" without edits: ask them to show 2 own edits; repeat the "your own first" rule.
- Many questions in a row: point to the [glossary](../../materials/en/day-0/glossary.md) and the FAQ below; collect group-level basic questions on the board and answer once.
- No PR by the end of the day: allow submission marked "no PR" (files by mail/platform), then fallback.

### Fast students
Give the **fast track**: stretch tasks at the end of each day (with criteria). Ask for a **peer review** (Day 4 S4) and a short talk "what I did not expect from AI". Do not answer them at length: a minimal hint "check against the source".

## 7. Typical student questions: pointer answers
Answer in one sentence and a link; do not explain from scratch.

| Question | Pointer answer |
|---|---|
| What is a repository / branch / commit / PR? | [Glossary](../../materials/en/day-0/glossary.md); https://docs.github.com/en/get-started/start-your-journey/about-github-and-git |
| `git push` asks for a password | `gh auth login`: [Day 0, section 2](../../materials/en/day-0/day-0-prepare.md) |
| `git`/`node` not found | Close and reopen the terminal; [installation-guide](../../materials/en/setup/installation-guide.md) |
| I cannot install (no rights) | Write to the mentor; fallback paths in the [installation-guide](../../materials/uk/setup/installation-guide.md) |
| Port 3000 is busy | Use the address from the terminal; Day 1, step 4 |
| How do I open a second terminal? | The `+` button in the terminal panel; Day 1, step 4 |
| Cursor chat does not answer / limit | [cursor-model-tips](../../materials/en/setup/cursor-model-tips.md); the limits policy above |
| The agent invented a file/line | Open the file and check; Day 2 block 1; [Cursor docs](https://docs.cursor.com) |
| Mermaid does not render | https://mermaid.live; Day 1, step 8 |
| What is AC / NFR / PoC? | [Glossary](../../materials/en/day-0/glossary.md); Day 4, vocabulary |
| What do I write in `docs/questions.md`? | Day 1, step 10 (quality criterion) |
| What is Given/When/Then? | Day 2, block 6 (AC linter) |
| MCP does not connect | Base track without MCP (Day 2); [github-mcp-setup](../../materials/en/day-2/github-mcp-setup.md); [MCP docs](https://modelcontextprotocol.io) |
| No Figma account / credits exhausted | The mentor's canvas: Day 3 part B; [figma-mcp-setup](../../materials/en/day-4/figma-mcp-setup.md) |
| No Open in canvas button | Names change; the mentor will show; [Figma docs](https://help.figma.com) |
| `git restore .` is scary: will I lose files? | Commit the documents first: Day 3, A8 |
| I got tangled in branches | Day 3, A8 "IF IT FAILED"; copy the documents outside the project and recreate `day-N` |
| I committed a token | Revoke the token immediately, the key is compromised; tell the mentor |
| What is "Grounded/Invented"? | Day 4, block 6 |
| Which template to choose: Spec Kit, OpenSpec or BMAD? | Day 4, block 1; [Spec Kit](https://github.com/github/spec-kit), [OpenSpec](https://github.com/Fission-AI/OpenSpec), [BMAD](https://github.com/bmad-code-org/BMAD-METHOD) |

## 8. Feedback
- First one thing that worked; then no more than three remarks by priority, each tied to a rubric criterion ("Day 2, criterion 2").
- Comments in the PR on GitHub; a summary to the submission channel.
- Do not rewrite for the student: point to the place and ask a question ("where does this number come from?").
- Take reply deadlines and credit statuses from the platform's rules.

## 9. Safety
- A token is a password: never in chat, in a commit or in a screenshot. Found one in a PR: tell the student, revoke it.
- Skills (Humanizer etc.): open the file and check for external links, `.env` access, shell commands.
- Public issue content is not private.

## 10. Open items for the curator
- [ ] Submission channel and reply template.
- [ ] Progress table (Excel as an aid).
- [ ] A rubric run on 2-3 trial submissions.
- [ ] Verification of all commands and Figma MCP on clean machines; pilot.
