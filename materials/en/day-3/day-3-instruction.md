# Day 3. Hypotheses and prototypes: step-by-step instruction

> DRAFT v2. Language: [Українська](../../uk/day-3/day-3-instruction.md). Prerequisite: the Day 2 PR is merged (you have `docs/contact-form-feature.md` with RULE-IDs, AC-NN, Q-NN). Code values (`MESSAGE_MIN_LENGTH = 10`, phone optional) were checked against the lf-client template; a student's experiment results may differ: **record what you see yourself**. `<…>` is filled in by the mentor.

## Goal of the day
You can:
- test a business hypothesis with disposable changes without risking shared code, and close the loop "requirement → code → test";
- explain a diff in plain language and honestly split "proven / not proven / developer needed";
- generate (or get from the mentor) a contact form mockup in Figma Make and analyze it as an analyst.

**Submission (PR):** `docs/poc-notes.md`, `docs/poc-summary-<date>.md`, `docs/figma-contact-form-analysis.md`. The PR has **no code changes**.

> The file `docs/contact-form-feature.md` is already in `main` after Day 2. On Day 3 you only **read** it (the source of RULE-IDs, AC and the Q-NN numbering) and **do not commit or change** it: the new Day 3 questions go into `docs/figma-contact-form-analysis.md`. If `git status` shows `docs/contact-form-feature.md` as modified, revert it: `git restore docs/contact-form-feature.md`.

## Two tracks and time budget (240 min)
| Block | Min | Base | Fast (extra) |
|---|---|---|---|
| 0. Day 2 review, branch | 15 | ✓ | |
| A1-A2. What a PoC is, preparation | 15 | ✓ | |
| A3. Probe 1: mandatory phone | 30 | ✓ | |
| A4. Probe 2: minimum message length | 25 | ✓ | |
| A5. Diff in plain language | 10 | ✓ | |
| A6. "Proven / not proven" checklist | 15 | ✓ | |
| A7. PoC summary | 15 | ✓ | |
| A8. Submit PoC (discard code) | 10 | ✓ | |
| Break | 15 | | |
| B. Mockup in Figma Make | 45 | ✓ (generate or mentor link) | |
| C. Add Figma analysis to the PR | 10 | ✓ | |
| Wrap-up | 15 | | |
| Stretch | | | S1 seed, S2 label, S3 feature flags |

The **20-minute rule** and **"your own first"** apply. Unknown terms: [glossary](../day-0/glossary.md).

---

## Block 0. Preparation (15 min)
The app runs in the **first** terminal (`npm run dev`); run git in the **second** (`+` in the terminal panel).

```bash
git checkout main
git pull
git checkout -b day-3
git branch --show-current
```
**CHECK:** prints `day-3`. **IF IT FAILED:** `already exists` → `git checkout day-3`.

# Part A. Sandbox PoC

## A1. What a PoC is for an analyst
A PoC (proof of concept) for a BA is **a disposable experiment that answers one question**: "If the rule worked like this, would the system behave the way stakeholders expect?"

| A BA PoC… | A BA PoC is NOT… |
|---|---|
| Tests one hypothesis | An implementation of the feature |
| Changes code only temporarily | Something that lands in `main` |
| Produces evidence (diff, screenshot, test results) | A replacement for developer estimates |
| Surfaces unknowns before refinement | An answer to "which solution is technically right" |

The day's result is **documents**, not code: we discard the code, the evidence stays. A PoC is inappropriate when it needs a real API call, real data or changes to more than 2-3 files: mark it "developer needed".

**Our hypothesis (from Day 2):** *"If we make the phone mandatory and reduce the minimum message length, the system behaves consistently on client and server."* You will test it with two probes.

## A2. Preparation: notes file
Create `docs/poc-notes.md` (in Cursor: right-click `docs` → **New File**; or `touch docs/poc-notes.md`; PowerShell: `New-Item docs/poc-notes.md -ItemType File`) and paste:

**COPY:**
```markdown
# PoC notes: what I saw in the running app

## Probe 1: mandatory phone
What I changed:
What I saw in the browser:
What the tests showed:

## Probe 2: minimum message length
What I changed:
What I saw in the browser:
What the tests showed:
```
The agent cannot see your browser, so "proven" is only what you wrote here. If you did not check, write "not checked".

## A3. Probe 1: mandatory phone (30 min)
**Scenario.** The client wants the phone mandatory (your RULE from Day 2). Let us see what this touches.

**Your own first:** in `docs/poc-notes.md` write which places in the code you think must change (use the rules table and impact analysis from Day 2).

**IN CURSOR CHAT:**
```text
Find all places where the phone in the contact form is declared optional (client, server,
tests, translations). Show file and line for each. Then show a diff that makes the phone
mandatory in all these places. Do not apply yet.
```
Review the diff: does it cover both the client form (`ContactForm.tsx`) and the server validator (`validateContactData.ts`)? If so, apply:
```text
Apply the change.
```
**Browser check.** Restart the server (`Ctrl+C`, `npm run dev`), open http://localhost:3000/en/contacts and try submitting the form **without a phone**. Note: what did the form show? Is there a "required" mark?

**Test check** (second terminal, takes seconds):
```bash
npx jest app/lib/utils/validateContactData.test.ts --coverage=false
```
Note which tests are **red** and why. A red test here is not a mistake but a finding: it shows which behavior the client is changing.

**Record in `docs/poc-notes.md`** the "Probe 1" section. Do not paste chat answers: only what you saw yourself.

> A safe change for the sandbox: touches ≤3 files, can be undone (`git restore`), calls no external API and writes to no shared DB. Bad candidates: authentication, payments.

## A4. Probe 2: minimum message length (25 min)
**Scenario.** Can we lower the message minimum from 10 to 5 characters?
```text
Find where the minimum message length is validated (client, server, tests, translations).
Show the current value, file and line. Then show a diff changing the minimum to 5. Do not apply yet.
```
**Your own first:** how many places do you expect? Then compare. Ask: "Are there other places you missed?"

<details><summary>Reference (open after your own attempt)</summary>

The value lives in at least three places: `MESSAGE_MIN_LENGTH` in `app/constants/validation.ts` (server), the `.min(...)` number in `ContactForm.tsx` (client) and the error text "at least 10 characters" in `i18n/messages` (en and uk). If you change only the constant, the API accepts 5 characters while the form still demands 10.
</details>

Apply the change **everywhere** found. Check a 6-character message in the browser on `/en/contacts`. Run tests:
```bash
npx jest app/lib/utils --coverage=false
```
**Record** in "Probe 2": what you changed, what you saw, which tests are red.

**Discussion:** this is the first step of a closed loop *requirement → code → test*: changing a rule in one place produced red tests elsewhere. How many places must change to change the rule? Is this a finding for the specification?

## A5. Diff in plain language (10 min)
```bash
git diff --stat
git --no-pager diff
```
(If the output switches to a pager, exit with `q`.)

**IN CURSOR CHAT:**
```text
Here is the git diff of my branch:
<paste git diff output>

Explain every change in plain business language: which rule or behavior the file controls,
what the change did, and whether there is a risk the BA should flag before handing over to a developer.
```
**CHECK:** no unexplained abbreviations.

## A6. Checklist "proven / not proven / developer needed" (15 min)
**Rule:** "proven" is only what you **saw yourself** and wrote in `docs/poc-notes.md`.
```text
Based on the git diff of my branch (run it yourself) and my notes @docs/poc-notes.md
help me fill in the checklist. For each change:
1. Proven: only what I recorded as seen.
2. Not proven: plausible, but no observation in the notes.
3. Developer needed: questions that cannot be answered from the code alone.
If there is no observation, write "not recorded" instead of assuming.
```
"Developer needed" rows may stay open: that is an honest state. Example questions: is this change consistent with the Day 2 AC? Which minimum value is right under the client's requirements?

## A7. PoC summary (15 min)
```text
Write a PoC summary from the git diff of my branch (run it yourself) and notes @docs/poc-notes.md.
Fill "Evidence" and "Proven" only from my notes. Take statistics from git diff --stat.
Save as docs/poc-summary-<date>.md. Sections:
1. Hypothesis. 2. Setup (branch, how data was controlled). 3. Changes (one sentence each).
4. Evidence (from notes, screenshots, statistics, test results). 5. Checklist.
6. Recommended next step (one sentence).
Write for a non-technical stakeholder.
```
**CHECK:** read it through a stakeholder's eyes. **Edit** at least 2 places (your own edit).

## A8. Submit the PoC: keep documents, discard code (10 min)
One branch, no switching. **Order matters:** commit the documents first, then discard the code.
```bash
git add docs/poc-notes.md
git add docs/poc-summary-<date>.md
git commit -m "docs: add PoC notes and summary (day 3)"
git restore .
git status
```
- `git restore .` discards **uncommitted** changes of tracked files (the PoC code). The documents are already committed and safe. If you have not yet committed the documents, **do not run** `git restore .` (edits to already tracked files would be lost).
- **CHECK:** `git status` says `nothing to commit, working tree clean`; `git diff main --stat` shows only files in `docs/`.

```bash
git push -u origin day-3
```
**IF IT FAILED:** copy the documents to a safe place outside the project, reset (`git restore .`, `git checkout main`), recreate `day-3` and put the documents back.

> Never push PoC code to a shared repository without discussion. The value is what the PoC proved, not the code.

*Break 15 min.*

---

# Part B. Mockup in Figma Make (45 min)
**Figma is mandatory for the course.** If you have no account or the limit is exhausted, the mentor gives you **a link to a ready mockup** `<link from the mentor>`: skip generation (B3) and do B4-B5 on it.

## B1. Prototype mindset
A prototype for a BA is **an analytical tool**, not a design: it exposes missing states, unclear behavior, contradictory flows, terminology mismatches. The question is "does it behave the way stakeholders expect?", not "is it pretty?".

## B2. Analysis file
Create `docs/figma-contact-form-analysis.md` (as `poc-notes.md`) and paste:

**COPY:**
```markdown
# Contact form mockup analysis

## My assumption before generation

## My observations before AI (2-3)

## Hidden assumptions (from AI analysis)

## Missing states (from AI analysis)

## Risks (from AI analysis)

## Questions by category (from AI analysis)
```
In "My assumption" write one that the requirements leave open.

## B3. Generate the mockup (15 min)
Open https://www.figma.com/make/ and paste the prompt **as is** (the level of detail is intentional). Pick the cheapest model in the list (look for a savings label): Figma Make spends credits and the free plan has daily and monthly limits.

**IN FIGMA MAKE:**
```text
Create a clean, modern contact form page for a cultural foundation website
(the Liatoshynsky Foundation).

Requirements:
- Fields: Name, Email, Phone number (required, international format starting with +),
  Message, and an optional file attachment (PDF only, max 5 MB).
- A required privacy policy checkbox before submit.
- A Submit button that is disabled until the required fields are valid.
- Show these states: empty form, filled valid form, invalid phone number,
  file too large, wrong file type (not PDF), uploading, success, and error.
- Show the form in both English and Ukrainian.
- Keep the styling calm, accessible, and consistent with a cultural-heritage site.
- Use plain, user-friendly language. Avoid technical jargon.
- Avoid excessive visual complexity.
```
Wait for the result without interrupting. Generate **once**, refine minimally (credits are limited). If states are missing: "Also show the error, success and validation states." Figma button names change (for example "Preview a state"): go by meaning. This is a **state demonstration**, not working validation.

## B4. Your own analyst review (5 min, no AI)
Which states are shown? Which are missing (network drop during upload, removing a file)? Who sees the form? Do the terminology and error texts match the site's `i18n/messages`? Write 2-3 observations into "My observations before AI" **before** turning to AI.

## B5. Analysis with AI (20 min)
**IN CURSOR CHAT** (describe the frames and states in words or paste their names):
```text
Analyze the contact form mockup for the Liatoshynsky Foundation website.
The mockup: fields Name, Email, Phone (required), Message, optional PDF attachment;
states: empty, valid, errors, uploading, success.
Generate: clarifying questions for refinement; hidden assumptions; missing states;
risks visible from the design; discussion points. No implementation recommendations.
Add the result to @docs/figma-contact-form-analysis.md under "Hidden assumptions",
"Missing states", "Risks". Do not change my sections.
```
Then:
```text
Build structured questions by category: Business rules; UI behavior; Data model;
Integration; Edge cases. Format: Q-NN | [Category] question | who answers.
Add to the "Questions by category" section. Continue numbering after Q-NN in
@docs/contact-form-feature.md, do not duplicate existing ones.
```
**CHECK:** ≥10 questions by category; your own observations stand next to the AI analysis; invented content removed. `docs/contact-form-feature.md` is unchanged (it is only the numbering source).

## B6. Preparation for Day 4 (5 min)
Figma MCP sees only a design **on the canvas of a regular Figma file**. In Figma Make click **Open in canvas**, paste the design into a new file, right-click the main frame → **Copy link to selection** and save the link. (The button name depends on the interface version.) We connect Figma MCP **on Day 4 with the mentor** (block 0): nothing is needed at home. No account: the mentor gives you the canvas link.

# Part C. Submission (10 min)
You are on branch `day-3`:
```bash
git status
git add docs/figma-contact-form-analysis.md
git commit -m "docs: add Figma mockup analysis (day 3)"
git push -u origin day-3
```
On GitHub: **Compare & pull request → Create pull request** (from `day-3` into `main` of your repository). Send the PR link to the mentor.

**PR requirements:** branch `day-3` → `main` of your (public) repository; title `Day 3: <short>`; description 2-4 sentences (what you did, what was hard, what remains unclear); **documents only**, no code changes; no `.env`, `node_modules`, tokens; merge after the mentor's feedback.

## Review criteria (for the mentor)
1. The PoC summary has hypothesis, setup, changes, evidence (including test results), checklist, next step.
2. "Proven" is only what was observed and recorded in `docs/poc-notes.md`; "developer needed" is filled honestly.
3. Duplicated validation (client/server/tests/translations) noticed, or honestly marked as unclear.
4. Only documents in the PR.
5. `docs/figma-contact-form-analysis.md`: own observations next to AI, ≥10 questions, own edits visible.
6. No secrets or service files.

## Fast track: stretch tasks
- **S1. Seed probe.** Find where the seed is defined (`scripts/seed-memory-mongo.js`), remove the `OurMission` block of the about-us page, restart the server, record what you see (error or graceful degradation). *Criterion:* a "what I saw" record + a question for developers about production.
- **S2. Button label.** "Support the Foundation" → "Become a patron" on `/en/support-us`; find **all** keys in `i18n/messages` (en and uk). *Criterion:* a list of keys and whether the Ukrainian translation must change.
- **S3. Feature flags.** Does the code have environment-variable toggles? Describe where you would add a simple boolean flag for a page. *Criterion:* a list of files it touches, confirmed manually.

All stretch changes are also discarded by `git restore .` before submission.

## For the mentor: timing (240 min)
| Min | Block |
|---|---|
| 0-15 | Day 2 PR review, Block 0 |
| 15-30 | A1-A2 |
| 30-60 | A3 (probe 1) |
| 60-85 | A4 (probe 2) |
| 85-110 | A5-A6 |
| 110-125 | A7 |
| 125-135 | A8 |
| 135-150 | Break |
| 150-195 | Part B (Figma) |
| 195-205 | Part C (submission) |
| 205-240 | Buffer, wrap-up, questions; **before class**: check Figma accounts, have a link to a ready mockup |

**Risks:** Figma accounts and limits (mentor link is plan B); `git restore .` before committing the documents (repeat the order rule); different probe results across students (normal: assess what was recorded, not a match with the reference); Figma Make availability in the organization.
