# Day 2. From requirement to code: step-by-step instruction

> DRAFT v2. Language: [Українська](../../uk/day-2/day-2-instruction.md). Prerequisite: the Day 1 PR is submitted and merged (you have `AGENTS.md`, `docs/architecture.md`, `docs/questions.md`). Code file paths were verified against the lf-client template; the agent finds line numbers itself. `<…>` placeholders are filled in by the mentor.

## Goal of the day
You can:
- trace a feature from page to database and find hidden business logic;
- find out **why** is behind a requirement (a conversation with the client), not only what it says;
- compare a vague requirement with the code, build a rules table and assess the impact of a change;
- write verifiable acceptance criteria (AC) with identifiers and questions for the client with owners.

**Submission (PR):** `docs/contact-form-feature.md` + link to the issue (original request, AC, rules table, impact, questions).

## Two tracks and time budget (240 min)
| Block | Min | Base | Fast (extra) |
|---|---|---|---|
| 0. Day 1 review, branch | 15 | ✓ | |
| 1. Trace "About the Foundation" | 30 | 3 prompts | + prompt 4, own path for comparison |
| 2. Rule for feature documents | 15 | ✓ | + Humanizer (S1) |
| 3. Client and issue | 25 | ✓ (manually on github.com) | + GitHub MCP (S2) |
| 4. Code vs requirement + rules table | 40 | ✓ | |
| 5. Impact analysis | 25 | ✓ | + S3 |
| 6. AC and questions | 35 | ✓ | |
| 7. Feature document, PR | 25 | ✓ | |
| Break | 15 | | |
| Wrap-up | 15 | | |

The **20-minute rule** applies: stuck → fallback or ask the mentor. **GitHub MCP is optional today** (it needs a token and often eats 30-40 min): the whole base track works without it. Unknown terms: [glossary](../day-0/glossary.md).

**"Your own first" rule:** reference answers are in collapsed "Reference" blocks. First write your own answer (at least 2-3 points), then open the reference and compare.

## Markers
**COPY**: commands and texts. **IN CURSOR CHAT**: prompt. **CHECK**: checkpoint. **IF IT FAILED**: fallback.

---

## Block 0. Preparation (15 min)
The Day 1 app runs (`npm run dev` in the **first** terminal, http://localhost:3000/en). Run git commands in a **second** terminal.

```bash
git checkout main
git pull
git checkout -b day-2
```
**IF IT FAILED:** `branch 'day-2' already exists` → `git checkout day-2`. We create `day-2` only here; Block 7 does not create it again.

## Block 1. Trace "About the Foundation" from page to database (30 min)
Open http://localhost:3000/en/about-us. The page passes all layers: page → service → repository → database. In **one** chat run the prompts in order.

> Model: for accuracy with files and lines do **not** pick the cheapest model in this block (see [cursor-model-tips](../setup/cursor-model-tips.md)). The agent may be wrong about line numbers: verify by opening the file.

**Prompt 1. Big picture.** **IN CURSOR CHAT:**
```text
Explain how the "About the Foundation" feature works now, including key business rules,
validations and the data flow.
```
**Prompt 2. Service.**
```text
@app/services/pages-data Which main business rules are implemented here?
For each rule give the file and line.
```
**Prompt 3. Hidden logic.**
```text
@app/services/pages-data Are there hidden dependencies, implicit logic or hard-coded
values that are not described anywhere? Consider environment variables and configs.
```
**CHECK:** write down 3 things that surprised you. Then open the reference.

<details><summary>Reference (open after your own attempt)</summary>

- Prompt 1: expect `app/[lang]/about-us/page.tsx`, `resolvePageData`, `pagesDataService`; in production mode an "Under development" placeholder may be returned.
- Prompt 2: draft mode, in which the container substitutes another service.
- Prompt 3: slug check in `schema-factory.ts`, `isProductionMode()`, environment-dependent branches.
- Data path: Browser → `middleware.ts` → `app/[lang]/about-us/page.tsx` → `resolvePageData("about-us","en")` → DI container `app/di/container.ts` → `pagesDataService.getPageData` → repository → in-memory MongoDB.
</details>

*Fast track:* **Prompt 4** ("Trace the full data flow… from the page route to the database, with transformations, validations and service calls") and compare with your Day 1 diagram: what did it miss?

## Block 2. Rule for feature documents (15 min)
A rule in `.cursor/rules/` is attached automatically for files matching its glob.

**IN CURSOR CHAT:**
```text
Create a Cursor rule file: .cursor/rules/docs-ba.mdc
Apply it only to files matching docs/**/*-feature.md
The rule must require the agent to:
- write user stories as: "As a [role], I want [goal], so that [benefit]"
- give Acceptance Criteria with identifiers AC-01, AC-02… in Given/When/Then format
- show data flows as Mermaid sequence diagrams
- write in plain language for non-technical stakeholders; explain jargon in brackets
- use the structure: short description, user stories, flow diagram, rules table,
  AC, key files table, open questions (with IDs Q-01…)
- invent nothing: whatever it does not know goes into open questions
```
**CHECK** the frontmatter of the created file:
```yaml
---
description: BA documentation standards for feature spec files in docs/
globs: docs/**/*-feature.md
alwaysApply: false
---
```
Why not `docs/**`: a broad glob would force the user-story structure on glossaries and notes.

**IF IT FAILED:** the rule is not picked up → open the file in Cursor and make sure the glob matches the file name; restart the chat.

## Block 3. Client and a vague requirement (25 min)
Real requirements start as one line. But an analyst does not touch code until they understand **why**.

**Step 3.1. Conversation with the client (10 min, in pairs or with the mentor).** The mentor plays a Foundation representative. The client's request: *"Contact form: make phone mandatory, let visitors attach a file (CV or portfolio), notifications must reflect the new field."* Ask 5-6 questions from your `docs/questions.md` (Day 1) and from these categories: why (what problem?), who is the user, how do we measure success, privacy (phone and CV are personal data), what happens if we do nothing.
Note down: the **goal**, the **success metric** and **at least 2 constraints** (NFR). Without a mentor: ask these questions to an agent playing the client and label the answers "Invented, not confirmed".

**Step 3.2. Issue.** On github.com in **your** repository create an issue:

- Title: `Contact form — update validation and notifications`
- Body (**do not change** the original until the end of the day; it is your baseline for traceability):
```text
## Original request
We want to tighten up the contact form. Phone number should be mandatory.
We should also let visitors attach a document (CV or portfolio) when they write
to us. Notifications need to reflect the new field.
```
Add a separate comment "Business context": goal, metric, constraints from step 3.1. Note the issue number (`#<number>`).

**CHECK:** the issue is in your repository, not the template.

*Fast track S2: GitHub MCP.* Setup (fine-grained PAT, `.cursor/mcp.json` in `.gitignore`, revoking the token): [github-mcp-setup](github-mcp-setup.md). A token is a password: the base track loses nothing without it.

## Block 4. Code vs requirement, rules table (40 min)
**IN CURSOR CHAT** (paste the issue text from github.com instead of `<issue text>`):
```text
Here is the requirement:
<issue text>

Compare it with the current implementation. Relevant files:
- @app/api/contact/route.ts
- @app/lib/utils/validateContactData.ts
- @app/shared/components/forms/contact-form/ContactForm.tsx
- @app/services/email/
- @app/api/collaboration/route.ts
- @app/shared/components/forms/offer-collaboration-form/

For each statement in the requirement say:
1. Is it already implemented? Where?
2. Partially implemented? What is missing?
3. Does it contradict the current code? How?
```
Write your own hypotheses (what you think already exists), then open the reference.

<details><summary>Reference</summary>

- Phone is currently optional (`if (phoneNumber)`, `.optional()`).
- Attachments are supported neither by the form, the API nor the mail.
- The mail service is a stub: it returns `{ success: true }` and sends nothing; `emailService` is never called.
- The "Contacts" form (`OfferCollaborationForm`) posts to `/api/collaboration`, not `/api/contact`; no page calls `/api/contact`. `GetNotesModal` uses the same form but makes no API call.
</details>

**Hidden rules and assumptions.**
```text
@app/lib/utils @app/shared/components/forms/contact-form/ContactForm.tsx
Which scenarios does the code handle that the requirement does not mention? Name the file for each.
What implicit assumptions does the implementation make (defaults, locales,
what happens to data after the API responds, environment variables, what changes with a real DB)?
```

**Rules table (three states).** Goal: tell what is in the code apart from what the business decided.
```text
For the contact form feature build a table with columns:
ID (RULE-01…) | Rule in plain language | File | Source of truth (constant, regexp, schema,
literal) | Layer (UI/API/shared/external) | Is now | Should be | Who decided
Leave "Should be" and "Who decided" empty when they are not known from the code or the
conversation with the client: do NOT invent.
Cover validation, error messages, defaults, the privacy-policy checkbox and the email side effect.
```
Ask: "What did you miss?" Typical misses: `maxLength` on fields, no rate limit on `POST /api/contact`, the auto-hide message hook, phone normalization.

<details><summary>Reference: rules and discrepancies</summary>

| Rule | Where it lives |
|---|---|
| Name 2-50 chars | `app/constants/validation.ts` + both validators |
| Message 10-1000 chars | `app/constants/validation.ts` + both validators |
| Phone: starts with `+`, digits only, 11-16 chars | `PHONE_NUMBER_PATTERN` |
| Email on the server | custom regexp |
| Email on the client | `z.string().email()` in `ContactForm.tsx` |
| Privacy-policy checkbox | client only |

Discrepancies: email rules differ between client and server; the policy checkbox is checked only in the browser. These go to open questions, not silently into "fixes".
</details>

Publish the table as a comment on the issue (on github.com), starting with the line `Rules table:`.

**Discussion:** how many places change if the maximum message length changes? Which table rows are a business requirement and which are just code behavior?

## Block 5. Impact analysis (25 min)
**IN CURSOR CHAT:**
```text
We will implement this change:
1. Make phone mandatory in the contact form.
2. Add an optional file field (PDF only, up to 5 MB).
3. Include the attachment as a link or upload in the notification email.

Analyze the impact on the codebase. List every file or area that needs changes,
grouped: UI and form components; API routes; validation (client and server);
services (mail, upload); tests; i18n; DB models and repositories; configuration.
Does the change contradict current rules (RULE-IDs from our table)? Also check
app/services/upload/ and existing size or MIME limits.
```
Then:
```text
Summarize the analysis as a Markdown table: Affected area | Change type (new/changed/removed) |
Risk (high/medium/low) | Recommended action | Regression test idea | Related RULE-IDs.
```
**CHECK:** the agent mentioned `app/services/upload/`. It is a reuse opportunity, but in the training code `upload.ts` is only a demo stub the app does not call. Publish the table as a comment on the issue (on github.com).

*Fast track S3:* endpoints. Ask the agent to find all API endpoints related to contacts, mail, upload (method, path, body, what it really does, whether the frontend calls it). Verify two manually.

## Block 6. Acceptance criteria and questions (35 min)
**IN CURSOR CHAT:**
```text
Based on: the current contact form implementation, app/constants/validation.ts,
the tests app/lib/utils/validateContactData.test.ts and
app/shared/components/forms/contact-form/ContactForm.test.tsx,
the rules table and impact analysis, and the business context (goal, metric, constraints)
write acceptance criteria for the change in the issue.

Format of each: AC-NN | Given … When … Then … | RULE-IDs it relates to.
Cover: mandatory phone (empty and invalid format); attachment (success, too large,
wrong MIME, no file); privacy policy; button states; notification content;
error texts (EN and UK); privacy and file retention.
```
**AC linter (check each manually, 5 min):**
1. Atomic: one behavior per AC.
2. One outcome in `Then`.
3. No implementation ("use Zod", "add a column").
4. No vague words ("fast", "convenient", "properly").
5. Describes **new** behavior, not the current one ("now the button…").
6. Testable: you can write a yes/no check.
Fix at least two AC that fail the linter.

**Questions for the client.**
```text
List open questions to answer before development starts. Each:
Q-NN | question | why it blocks | who answers (role) | by when | related AC/RULE.
Categories: numeric limits; locales; failure modes; storage (disk, blob, email only);
privacy and retention; discrepancies from the rules table.
```
**Publish to the issue (on github.com):** **do not overwrite** the original request. Add a comment `Acceptance criteria:` with the AC list and a separate comment `Open questions for the stakeholder:`.

## Block 7. Feature document and submission (25 min)
File `docs/contact-form-feature.md` (the `-feature.md` suffix attaches the rule from Block 2).

**IN CURSOR CHAT:**
```text
Create the file docs/contact-form-feature.md from our conversation and issue #<number>.
Sections: 1. Short description and original request (quote the issue original verbatim)
2. Business context (goal, metric, constraints) 3. User stories 4. Sequence diagram (Mermaid)
5. Rules table (RULE-ID, three states) 6. Acceptance criteria AC-NN
7. Key files table 8. Open questions Q-NN.
Use only what was found in the conversation and code. Whatever you do not know goes into open questions.
```
**CHECK:** the file is in `docs/`, 8 sections. Read and **edit** it: fix inaccuracies, remove invented content. Mark at least 3 places of your own edits in the file (`<!-- edited -->`).

**Submission:**
```bash
git status
git add docs/contact-form-feature.md
git commit -m "docs: add contact form feature analysis (day 2)"
git push -u origin day-2
```
Optionally, with separate commands: `.cursor/rules/docs-ba.mdc`, `docs/about-us-feature.md`. Read each file before adding. On GitHub: **Compare & pull request → Create pull request** (from `day-2` into `main` of your repository). Send the mentor the link to the PR **and to the issue**.

**PR requirements:** branch `day-2` → `main` of your (public) repository; title `Day 2: <short>`; description 2-4 sentences + `Related to #<number>`; only the day's files (**Files changed**), no `.env`, `node_modules`, `.cursor/mcp.json`, tokens; merge **after** the mentor's feedback.

## Review criteria (for the mentor)
Items 1-4 in the issue, 5-6 in the PR.
1. Original request preserved; AC in the AC-NN + Given/When/Then + RULE-ID format; passed the linter.
2. Rules table matches the code; client/server discrepancy found; three states present.
3. Open questions Q-NN with owner and date; privacy among them.
4. "Business context" (goal, metric, constraints) from the conversation exists.
5. `docs/contact-form-feature.md` in the PR, ≥3 own edits visible; PR meets the requirements.
6. No token or service files.

## Fast track: stretch tasks
- **S1. Humanizer** (skill provided by the mentor; before connecting, open it and check for external links, `.env` access and shell commands). Apply it to `docs/about-us-feature.md`. *Criterion:* you can name 3 style changes and object to one.
- **S2. GitHub MCP.** *Criterion:* issue and comments created via chat, and you checked owner/repo before each write; token revoked after class.
- **S3. Endpoints** (see Block 5). *Criterion:* a table with 2 manually confirmed endpoints.
- **S4. Cursor modes.** Ask only reads (safe reconnaissance), Plan drafts a plan before changes. Build the impact-analysis plan in Plan. *Criterion:* you adjusted the plan.

## For the mentor: timing (240 min)
| Min | Block |
|---|---|
| 0-15 | Day 1 PR review, Block 0 |
| 15-45 | Block 1 |
| 45-60 | Block 2 |
| 60-85 | Block 3 (client simulation, script: `mentor/en/day-2-stakeholder-script.md`) |
| 85-125 | Block 4 |
| 125-140 | Break |
| 140-165 | Block 5 |
| 165-200 | Block 6 |
| 200-225 | Block 7 |
| 225-240 | Wrap-up, pointer to Day 3 |

**Risks:** the agent invents line numbers (verify manually); Block 4 time (keep the pace, the table can be cut to 8 rules); a student with an empty Day 1 PR (give them the Day 1 artifacts from `fallback/`, `<to be added>`).
