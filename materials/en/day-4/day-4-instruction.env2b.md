# Day 4. From design to specification (SDD) and wrap-up: step-by-step instruction

> DRAFT v3. Language: [Українська](../../uk/day-4/day-4-instruction.md). Prerequisite: the Day 3 PR is merged (you have `docs/contact-form-feature.md`, `docs/poc-summary-*.md`, `docs/figma-contact-form-analysis.md`). Templates: [`templates/en/`](../../../templates/en/README.md). Figma MCP connection: [figma-mcp-setup](figma-mcp-setup.md). Practical blocks follow **the mentor shows, you do**. `<…>` is filled in by the mentor.

## Goal of the day
You can:
- read a mockup via Figma MCP (read-only) and compare it with the code, patterns and accessibility;
- compare three specification approaches (Spec Kit, OpenSpec, BMAD) on one requirement;
- assemble a specification with IDs, NFR and a **traceability matrix** (request → rule → AC → design → test idea);
- work with AI within the specification and **verify its claims** instead of counting labels;
- extract a PoC/MVP slice and assemble a handoff pack with a Definition of Ready.

**Final result of the course: the handoff pack for development** (`docs/handoff-contact-form.md`).

**Submission (PR):** `docs/spec-contact-form.md` (with the matrix), `docs/ai-check-notes.md`, `docs/slice-contact-form.md`, `docs/handoff-contact-form.md`, `docs/rewrite-compare.md` and the updated `docs/figma-contact-form-analysis.md`.

## Time budget (240 min)
| Block | Min |
|---|---|
| 0. Branch, Figma MCP together with the mentor | 20 |
| 1. SDD theory | 15 |
| 2. Real SDD project walkthrough (demo) | 10 |
| 3. Design → code: components, patterns, accessibility | 30 |
| 4. Triple rewrite (new requirement) | 20 |
| 5. Specification, NFR, traceability matrix | 35 |
| 6. AI within the specification: claim audit | 20 |
| 7. PoC/MVP slice | 10 |
| 8. Handoff pack, Definition of Ready | 20 |
| 9. Submission and wrap-up | 15 |
| Break | 15 |
| Buffer | 30 |

The **20-minute rule** and **"your own first"** apply. Unknown terms: [glossary](../day-0/glossary.md) and the vocabulary below.

### Vocabulary
| Abbreviation | Meaning |
|---|---|
| **ID** | unique label of a row, e.g. `RULE-01` |
| **IN / OUT** | what is in the change and what is deliberately not |
| **RULE** | business rule: "if… then… else…" |
| **AC** | acceptance criterion (Given/When/Then) |
| **Q** | open question; **ASM** assumption; **NFR** non-functional requirement |
| **refinement** | a meeting where the team analyzes a requirement before development |
| **PRD / ADR** | product requirements document / architecture decision record |
| **capability** | a separate product capability with its own specification |
| **Blocker / Important / Minor** | finding severity |
| **MCP** | standard way to connect Cursor to external systems |
| **DoR** | Definition of Ready: when a requirement is ready for development |
| **handoff** | the pack handed over to development |

---

## Block 0. Preparation and Figma MCP (20 min)
```bash
git checkout main
git pull
git checkout -b day-4
```
**CHECK:** the Day 3 PR is merged (Day 2-3 files are in `docs/`). **IF IT FAILED:** the mentor gives fallback artifacts ([`fallback/en/`](../../../fallback/en/README.md), examples in Ukrainian).

**Download the templates** (needed in blocks 4, 5, 7). From your project root:

macOS / Linux:
```bash
mkdir -p docs/templates
B=https://raw.githubusercontent.com/VovaD199/spec-driven-ba-workshop/main/templates/en
for f in template-ba-story template-spec-kit template-openspec-bmad ba-refinement-template traceability-matrix-template mvp-poc-slice-template; do curl -sL -o docs/templates/$f.md $B/$f.md; done
ls docs/templates
```
Windows PowerShell:
```powershell
New-Item -ItemType Directory -Force docs/templates | Out-Null
$B = "https://raw.githubusercontent.com/VovaD199/spec-driven-ba-workshop/main/templates/en"
foreach ($f in "template-ba-story","template-spec-kit","template-openspec-bmad","ba-refinement-template","traceability-matrix-template","mvp-poc-slice-template") { Invoke-WebRequest "$B/$f.md" -OutFile "docs/templates/$f.md" }
dir docs/templates
```
**CHECK:** `docs/templates/` has six files. Do not commit them (`docs/templates/` is not submitted). **IF IT FAILED:** open the files in the course repository on GitHub and copy manually (**Copy raw file**), or ask the mentor for an archive.

**Figma MCP together with the mentor (≈10 min).** The mentor demonstrates the connection [per the guide](figma-mcp-setup.md), you repeat it; then **one** test request with the link to your mockup frame (the free plan has 20 calls per month: do not repeat it needlessly). No canvas mockup or no account: the mentor gives `<mentor's canvas link>`. Not working after 15 min: use a description of the mockup in words or a screenshot (fallback in block 3).

# Block 1. SDD theory (15 min)
Main thesis: **requirements are stronger when they are structured, traceable and verifiable, not when they are longer.**

**What SDD is for an analyst.** Spec-Driven Development: break business intent into named linked artifacts; make rules, scope and assumptions explicit; make the specification traceable (request → design → delivery → test); let AI help without losing human judgment. The analyst is the author and owner of the "source of truth" (business decisions); the code is just one of its reflections.

| Requirement gap | Consequence with AI |
|---|---|
| Ambiguous boundaries | AI invents features |
| Missing rules | AI picks arbitrary values |
| No IDs | Output cannot be matched to intent |
| No acceptance signals | AI's answer cannot be verified |

**Eight specification artifacts:** 1) problem statement, 2) scope and exclusions, 3) actors and flow, 4) business rules, 5) constraints and dependencies, 6) assumptions, 7) open questions, 8) acceptance signals. We add **NFR** (privacy, security, accessibility, localization, retention) and a **traceability matrix**.

**Three approaches.** They produce similar artifacts but differ in process. The table below is **a guide**: before using it with a group the mentor checks it against the documentation (links below).

| | GitHub Spec Kit | OpenSpec | BMAD |
|---|---|---|---|
| Idea | Sequence: principles (constitution) → specification → plan → tasks, in a GitHub flow | Module specs in the repository + **changes as deltas** (ADDED / MODIFIED / REMOVED) | Role-based agents and a process from idea to requirement packages |
| Where the analyst works | Specification and principles | Change descriptions and scenarios | Early phases: brief, PRD |
| Strength | Structured start of a new feature | Changes to existing code (brownfield) | Vague request, discovery |

For our application (existing code from someone else) the logical emphasis is on OpenSpec **deltas**. Choose by the team's process; the approaches can be mixed. Docs: [Spec Kit](https://github.com/github/spec-kit), [OpenSpec](https://github.com/Fission-AI/OpenSpec), [BMAD](https://github.com/bmad-code-org/BMAD-METHOD).

**Anti-patterns:** over-specification too early; pseudo-architecture (the specification dictates technology); a wall of IDs without a simple description; templates nobody verifies.

# Block 2. Real SDD project walkthrough (10 min, mentor demo)
**Weather Explorer** (DOU Day 2026, Next.js, OpenSpec; the developer's permission was obtained). The mentor shows, you open the same tabs: [app `/compare`](https://weather-explorer-lemon.vercel.app/compare), [`AGENTS.md`](https://github.com/koldovsky/weather-explorer/blob/master/AGENTS.md), [`docs/prd.md`](https://github.com/koldovsky/weather-explorer/blob/master/docs/prd.md) (IDs `FR-`, `NFR-`, `TC-`, `BC-`), [change folder `add-weekend-compare`](https://github.com/koldovsky/weather-explorer/tree/master/openspec/changes/archive/2026-05-12-add-weekend-compare) (`proposal.md`, `design.md`, `tasks.md`), [the change `spec.md`](https://github.com/koldovsky/weather-explorer/blob/master/openspec/changes/archive/2026-05-12-add-weekend-compare/specs/weekend-compare/spec.md), [traceability matrix](https://github.com/koldovsky/weather-explorer/blob/master/docs/qa/traceability-matrix.md), [evidence recording](https://github.com/koldovsky/weather-explorer/blob/master/docs/qa/recordings/weekend-compare.md).

**What to look for:** `FR-COMPARE-01` runs through the PRD, the matrix, the specification and the evidence: this is the traceability backbone, and **you will build the same one in block 5**. Explicit "Out of scope"; concrete scenarios; a matrix row points to a record of a real run.

**Finding (drift):** `FR-COMPARE-01..03` in the PRD describe city chips and a toggle, while the specification and the matrix speak of a `/compare` page. The PRD and the accepted specification diverged: a mistake or a deliberate decision? The files do not say, and this is exactly what an analyst catches.

# Block 3. Design → code (30 min)
Results accumulate in `docs/figma-contact-form-analysis.md`.

## 3.1. Components via Figma MCP, read-only (15 min)
The agent reads components, variants, styles and layers directly. Your role: **check that the translation is accurate**. Frame link: right-click the frame → **Copy link to selection**.

**IN CURSOR CHAT:**
```text
Using Figma MCP (read-only, change nothing in Figma), analyze the contact form mockup:
<link to your frame>
1. List the components (fields, buttons, checkbox, errors, file upload indicator).
2. For each, give variants and states.
3. Compare with existing UI patterns in the code: app/shared/components/ and app/[lang]/.
4. Mark: already exists / close (needs adaptation) / new.
Add the result to @docs/figma-contact-form-analysis.md, a new section "Components and reuse".
```
**CHECK:** the most important finding is **terminology mismatch** (a field name or error wording in the design versus `i18n/messages`). Write down at least one finding of your own **before** the agent answers.

**IF IT FAILED (no Figma MCP or limit exhausted):** describe the mockup in words (frames, components) or paste a screenshot and do the same tasks on the description, or use the mentor's canvas.

## 3.2. Application patterns and accessibility (15 min)
The mockup was generated from requirements and does not know the application's conventions.

**IN CURSOR CHAT:**
```text
Compare the contact form design (<frame link> or my description) with the existing application
patterns: 1) terminology mismatches 2) duplicated UI concepts 3) inconsistent interaction
patterns 4) typography and spacing 5) missing states that similar components have
6) patterns the design could reuse.
Classify each finding: Blocker, Important or Minor.
Add to @docs/figma-contact-form-analysis.md, section "Pattern comparison".
```
```text
Check the contact form mockup for accessibility risks: color contrast (errors, states),
screen readers for error messages, keyboard navigation (fields, file picker, button),
motion or animation, touch target sizes. Classify: Blocker/Important/Minor.
Write for a BA presenting the findings at refinement. Add to the section "Accessibility".
```
**CHECK:** both sections exist, every finding is classified. Blockers go into "Risks" of the handoff pack (block 8), Important into questions, Minor are just noted.

# Block 4. Triple rewrite (20 min)
Goal: rewrite **one vague requirement** in three forms and see which form exposes gaps fastest. To avoid repeating Day 2 we take a **new** requirement.

> "We want visitors to be able to subscribe to the Foundation's news by email. Unsubscribing must be easy."

| Min | Step |
|---|---|
| 0-3 | AI ambiguity scan |
| 3-12 | Three templates via AI |
| 12-17 | Star ★ where each format **first** exposed a gap |
| 17-20 | Discussion |

**Scan. IN CURSOR CHAT:**
```text
You are helping a business analyst. Do not solve the feature yet.
Read the requirement and list: 1) 10 ambiguities (actors, scope, rules, data, privacy,
dependencies); 2) 5 implicit stakeholder assumptions; 3) 5 questions for a 30-minute session.
Do not invent policy or numeric limits. Label each item: Explicit-in-text / Implied / Missing.

REQUIREMENT: "We want visitors to be able to subscribe to the Foundation's news by email.
Unsubscribing must be easy."
```
**Template A** (`@docs/templates/template-ba-story.md`), **B** (`template-spec-kit.md`), **C** (`template-openspec-bmad.md`): for each, a separate prompt:
```text
Using ONLY this requirement, fill in the template @docs/templates/<file>.
If information is missing write TBD and invent no metrics, limits or policy.
Mark Invented where you had to guess.
REQUIREMENT: <the same requirement>
```
**Save the result** in one file `docs/rewrite-compare.md`: table | Format | Where it first exposed a gap ★ | What it hid | What is hardest to trace | Who it suits (Product / engineers / AI) |. This is submitted to the mentor.

**The same requirement:** rewrite all three formats for the **same** requirement (the email news subscription from the text above), not different ones: otherwise comparing the formats is meaningless.

**Discussion:** which format "hid" the privacy rule? Where did scope appear unprompted? Which would you paste into an AI tool and why?

# Block 5. Specification, NFR, traceability matrix (35 min)
This is a **consolidation** of what already exists from Days 2-3: you **do not rewrite** the rules, AC and questions, you carry them over **keeping IDs** and add what is missing: NFR, design links and the matrix.

### Step 1. File from the template (≈3 min)
macOS/Linux: `cp docs/templates/ba-refinement-template.md docs/spec-contact-form.md`
PowerShell: `Copy-Item docs/templates/ba-refinement-template.md docs/spec-contact-form.md`

### Step 2. Carry over keeping IDs (≈12 min)
**IN CURSOR CHAT** (attach files with `@`):
```text
In @docs/spec-contact-form.md fill sections 1-9 from @docs/contact-form-feature.md and
@docs/figma-contact-form-analysis.md.
Requirements:
- Carry over IDs from the documents (RULE-NN, AC-NN, Q-NN) UNCHANGED; new IDs only for new items.
- Invent nothing: whatever is not in the documents goes in as Q-NN or ASM-NN.
- Propose no technical solutions (DB, libraries).
- Do not touch section 10.
```
**CHECK:** read it **in full**, fix inaccuracies, remove invented content, **and verify the IDs did not change** (compare with Day 2). If sections of `docs/figma-contact-form-analysis.md` from Day 3 are still empty, fill them **before submission**.

### Step 3. NFR (≈8 min)
For a form with a phone and a CV these are personal data. Do **not renumber** NFRs whose IDs you already had on Day 2: keep the same numbers and meaning; append new NFRs at the end with the next numbers. Add at least 4 requirements to the NFR section: privacy (what we collect, why, for how long), upload security (file type and content, malicious files), accessibility, localization. Take answers from the client conversation (Day 2); record what you did not hear as Q-NN with an owner.

### Step 4. Traceability matrix (≈10 min)
Add at the end of the specification a table following `docs/templates/traceability-matrix-template.md`:
```text
Build a matrix: Request (Source) | Requirement / RULE | AC | Design (Figma frame) | Test idea | Status.
Take Source from the original issue text of Day 2 (sentences). Status: Draft / Agreed / Open Q-NN.
Do NOT set Agreed without a record of who agreed and when. Flag orphans (RULE without Source, AC without RULE).
```
**CHECK (specification DoR check):**
- [ ] Every rule, question, assumption and AC has an ID kept from Day 2
- [ ] Every rule has a source (request, conversation, code or "needs clarification")
- [ ] Every AC has a RULE, every RULE has an AC; no orphans in the matrix
- [ ] Every question has an owner and a date
- [ ] NFR: ≥4, including privacy
- [ ] No technical solutions; nothing invented without Q or ASM

# Block 6. AI within the specification: claim audit (20 min)
AI "fills in gaps": if it does not know something it invents a plausible answer. We give it your specification and rules. The labels are set by AI, but **they cannot be trusted**: you verify.

| Label | Meaning |
|---|---|
| **Grounded** | follows directly from the specification (there is an ID) |
| **Inferred** | a logical conclusion |
| **Invented** | made up: the specification has no answer |

### Step 0. Notes file
Create `docs/ai-check-notes.md` and paste:
```markdown
# AI check notes

## Claim audit (5 random Grounded)
| AI claim | AI label | Quote from the specification (ID, section) | Confirmed? | My verdict |
|---|---|---|---|---|

## What turned out Invented and what the specification lacked:

## Which gap I closed and how:

## Result of the rerun:

## What surprised me:
```
### Step 1. Rules for the AI
Open a **new** chat (`@docs/spec-contact-form.md`):
```text
You are helping a business analyst. Use ONLY the specification @docs/spec-contact-form.md.
Rules: cite IDs (RULE-NN, OUT-NN, Q-NN, NFR-NN); if information is missing, ask clarifying
questions and DO NOT invent policy, legal rules or numeric limits; label each item
Grounded / Inferred / Invented; answer in tables. Confirm in one sentence.
```
### Step 2. Criteria and edge cases
```text
Write acceptance criteria from the specification: max 4 topics; Given/When/Then; rule IDs for each;
Invented for what you had to make up, and say what exactly the specification lacks.
Format: | AC ID | Criterion | Rule IDs | Label |
```
```text
List 8-15 edge cases (validation, time, data and state, privacy, notifications, language).
For each: trigger and expected behavior. If the specification is silent: "Specification is silent: question Q-NN".
```
### Step 3. Audit (the main part, 8 min)
Pick **5 claims labelled Grounded** and find a quote in the specification for each. Fill the table in `docs/ai-check-notes.md`. If there is no quote, the claim is **not Grounded**: AI dressed an invention up as a confirmed fact. This is the most common substitution. You fill in the "Confirmed?" and "My verdict" columns and all four sections of `docs/ai-check-notes.md` yourself; a file with empty sections is not accepted. Also verify all **numbers** (file size, retention terms) in the answer against the specification.

### Step 4. Close a gap
Take the worst invention and add to the specification **what closes it**: a rule you actually heard from the client, or a question `Q-NN`. **Do not add a rule just to get rid of Invented:** without business confirmation it is only a rewording of an invention. Repeat the request and record what changed.

**Human check:** every Invented has a Q or a confirmed rule; numbers are not from AI; AC do not contradict OUT; there is something to show in a demo.

# Block 7. PoC/MVP slice (10 min)
From Day 3 you know a PoC answers one question. Now derive a slice from the specification and **use the Day 3 evidence**.

`cp docs/templates/mvp-poc-slice-template.md docs/slice-contact-form.md` (PowerShell: `Copy-Item …`)
```text
In @docs/slice-contact-form.md fill the template: a 2-week PoC or MVP slice from the specification
@docs/spec-contact-form.md and the evidence in @docs/poc-summary-*.md (Day 3).
1. One falsifiable hypothesis H-01. 2. 3 SLICE-IN, 3 SLICE-OUT (reason). 3. PoC or MVP + 2 sentences.
4. SIG-P-01 and SIG-P-02: PoC threshold | production threshold. 5. Q-P-01..03 (blockers).
Label each row Grounded/Inferred/Invented; cite parent IDs; no invented policy.
```
**CHECK:** the slice is smaller than the feature; the hypothesis is falsifiable in 2 weeks; ≥2 parent IDs; the PoC evidence claims no more than was proven on Day 3.

# Block 8. Handoff pack and Definition of Ready (20 min)
The handoff pack is assembled from the specification and the mockup analysis.

### Step 1. Assemble
```text
Compose a refinement handoff pack using ONLY @docs/spec-contact-form.md,
@docs/figma-contact-form-analysis.md and @docs/slice-contact-form.md. Save docs/handoff-contact-form.md.
Sections: 1) short description (2 sentences, non-technical) 2) affected areas 3) dependencies
4) questions Q-NN 5) risks (Blocker/Important from block 3) 6) missing states 7) AC
8) evidence summary (what the PoC and prototype showed, and what they did not) 9) traceability matrix (link).
Keep IDs unchanged. Separate facts from assumptions.
```
### Step 2. Humanizer for the short description only
The skill is provided by the mentor (before connecting it, open it and check for external links, `.env` access and shell commands). Apply it to **section 1 only**. Then:
```bash
git diff docs/handoff-contact-form.md
```
Make sure **IDs, numbers and the words "must / must not" did not change**. If they did, revert.

### Step 3. Definition of Ready
```text
Assess @docs/handoff-contact-form.md against the Definition of Ready: section | ready / not ready | what is missing.
```
The pack is ready for refinement (**DoR**) when: the description is clear without context; all Blockers are addressed or flagged; every AC is verifiable; the matrix has no orphans; open questions have owners and dates; "Evidence" honestly says what was and was not proven. Fix blockers before submission. Record in the pack the commit (`git rev-parse --short HEAD`) for which it was DoR.

### Step 4 (optional, ≈15-20 min). Handoff into GitHub Issues
Your repository is public and you connected `gh` on Day 0, so you can hand the pack off the way a real tracker works: epic, stories, AC, labels. This practises the mechanics; for Jira or Azure DevOps they are the same. **Do not add** this step to the Day 4 PR, the result is the issues in your repository.

| What | In GitHub | Content |
|---|---|---|
| Epic | 1 issue with the `epic` label | link to the original request (the Day 2 issue), list of stories as a checklist `- [ ] #12`, goal and metric |
| Story | 1 issue per group of AC, `story` label | title "As a visitor, I want …, so that …"; body: RULE-ID, AC as checkboxes (Given/When/Then), NFR, test idea, link to the spec section |
| Open question | 1 issue, `question` label | Q-NN, owner (role), date, related AC |

Write IDs (RULE, AC, Q, NFR) in the title and body, for example `[RULE-03] …`, not in labels: only three labels (`epic`, `story`, `question`), GitHub searches by text.

**Limit:** 1 epic and 3-4 stories, otherwise the step drags on. The repository is public: fictional data only, no tokens or private contacts.

**Create them yourself with `gh`, not through AI with GitHub MCP.** It is a write to a public repository and a human must read every call. AI only prepares the text in chat:
```text
From @docs/handoff-contact-form.md and @docs/spec-contact-form.md prepare the text of 3-4 stories (title "As a visitor, I want …, so that …",
RULE-ID, AC as checkboxes, NFR, test idea), the epic text with the list of stories, and issue texts for the Q-NN questions.
Every AC from the specification must be in exactly one story. Create nothing, only show the text. Keep IDs unchanged, invent no new requirements.
```
Labels first, then stories, and the epic last (so you can paste the numbers into the checklist):
```bash
gh label create epic
gh label create story
gh label create question
gh issue create --title "[RULE-03] As a visitor, I want …, so that …" --body "<text>" --label story
gh issue create --title "Epic: contact form" --body "<text with a - [ ] #N list>" --label epic
```
You can create the first story manually on github.com.

**Criterion:** the epic links to all stories; every AC from the specification is in exactly one story; every story has a RULE-ID; issues for the Q-NN questions are created; no requirement that is absent from the specification. If you have Jira or Azure DevOps, you can make an import CSV as an extra task.

**Pre-submission checklist:** the DoR table is in the pack; the commit is recorded; all 9 sections of the pack are filled; there are no empty sections in `docs/ai-check-notes.md` and `docs/figma-contact-form-analysis.md`.

Record the commit in the pack (`git rev-parse --short HEAD`): this command shows the short number of the current commit (for example, `a1b2c3d`). The set of documents changes over time. A note "DoR passed at commit a1b2c3d" lets you know exactly, a month later, which version was ready and whether it was changed after the check.

# Block 9. Submission and wrap-up (15 min)
```bash
git status
git add docs/spec-contact-form.md
git add docs/ai-check-notes.md
git add docs/slice-contact-form.md
git add docs/handoff-contact-form.md
git add docs/rewrite-compare.md
git add docs/figma-contact-form-analysis.md
git commit -m "docs: add spec, AI check notes, slice, handoff pack (day 4)"
git push -u origin day-4
```
Do **not** add `docs/templates/`. On GitHub: **Compare & pull request → Create pull request** (from `day-4` into `main` of your repository), send the link to the mentor.

**PR requirements:** branch `day-4` → `main` of your (public) repository; title `Day 4: <short>`; description 2-4 sentences; only the day's files, no `.env`, `node_modules`, tokens, `docs/templates/`; merge after the mentor's feedback.

**What goes to whom.** The final deliverable is the handoff pack; the other files stay as learning materials for the mentor.

| File | For | Purpose |
|---|---|---|
| `docs/handoff-contact-form.md` | developers, QA, product owner | final result: the feature is clear at refinement without the other files |
| `docs/spec-contact-form.md` | developers, QA | source of truth: rules, AC, NFR |
| traceability matrix (in the spec) | QA, product owner | link request → rule → AC → design → test |
| `docs/ai-check-notes.md` | mentor | your audit of AI claims |
| `docs/rewrite-compare.md` | mentor | comparison of specification formats |
| `docs/slice-contact-form.md` | mentor (referenced by the pack) | PoC/MVP boundaries |
| `docs/figma-contact-form-analysis.md` | mentor (referenced by the pack) | mockup analysis: risks, states |

## Key takeaways
1. Structure exposes ambiguity earlier than beautiful text.
2. SDD is an analyst skill: traceability and verifiability, and the analyst owns the source of truth.
3. Spec Kit, OpenSpec, BMAD differ in process; choose by phase and project type.
4. AI strengthens a specification only with IDs, boundaries and **human verification of claims**.
5. Design, code and specification are connected by shared IDs, questions and evidence.
6. A PoC/MVP slice: a hypothesis, scope and signals tied to the parent specification.
7. Questions for the client with an owner and a date are part of the specification, not a sign of its weakness.

## Review criteria (for the mentor)
1. Specification: 8 artifacts + NFR (≥4, with privacy) + a matrix without orphans; **IDs kept from Day 2**.
2. Rules match the code and the client conversation; each has a source; questions have owners and dates.
3. `docs/ai-check-notes.md` filled in by the participant: audit of 5 claims with quotes, gap closed without "gaming the counter".
4. Slice: falsifiable hypothesis, OUT with reasons, two signals with PoC/production thresholds, ≥2 parent IDs, Day 3 evidence used.
5. Handoff pack: 9 sections, DoR passed, commit noted; Humanizer did not change IDs or numbers.
6. `docs/rewrite-compare.md` with the ★ table.
7. The mockup analysis has the sections "Components and reuse", "Pattern comparison", "Accessibility".
8. No secrets or service files.

## Fast track: stretch tasks
- **S1. Clickable prototype in Figma** (**Prototype** tab: form → success, error → form; present with `Ctrl+Alt+Enter` / `Cmd+Option+Enter`). *Criterion:* a "Prototype slice" section in the mockup analysis with assumptions as Q-NN.
- **S2. Double-check Spec Kit/OpenSpec/BMAD.** Verify the table in block 1 against the documentation and correct it. *Criterion:* 3 corrections with links.
- **S3. Playbook** `docs/ba-playbook.md`, one page: "from a vague requirement to a handoff pack" (when to start, steps with tools, artifacts, DoR, anti-patterns). *Criterion:* clear to a person who was not at the course.
- **S4. Peer review.** Swap specifications and find 3 "orphans" (RULE without source, AC without rule) or numbers not taken from the specification. *Criterion:* 3 findings with a line reference.

## For the mentor: timing (240 min)
| Min | Block |
|---|---|
| 0-20 | Block 0 (+Figma MCP demo) |
| 20-35 | Block 1 |
| 35-45 | Block 2 |
| 45-75 | Block 3 |
| 75-90 | Break |
| 90-110 | Block 4 |
| 110-145 | Block 5 |
| 145-165 | Block 6 |
| 165-175 | Block 7 |
| 175-195 | Block 8 |
| 195-210 | Block 9 |
| 210-240 | Buffer, course feedback `<format given by the mentor>`, wrap-up |

**Before class:** walk through Figma MCP on a clean machine, have your own canvas with a mockup, verify the Spec Kit/OpenSpec/BMAD table, have fallback artifacts, check that the raw template links open. **Risks:** Figma MCP limit (20/month), Cursor limit, block 5 time (cut NFR to 3 items), Grounded mislabeling.
