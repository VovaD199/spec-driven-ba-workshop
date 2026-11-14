# Clean-machine verification and pilot

> DRAFT v1. Language: [Українська](../uk/verification-and-pilot.md). For the curator or mentor. Goal: replace the assumption "the commands work" with facts before the first session. Fill in the "Result" and "Min" columns; write everything that failed under "Findings", fix it in the sources (`materials/`), then regenerate the PDFs.

## What is already verified and what is not

| What | Status |
|---|---|
| Day 3 `npx jest …` commands (two probes) and the full `npx jest --coverage=false` on the template | Run on Linux, Node 22 (all 1434 tests green) |
| PDF build from Markdown (`tools/build_materials.py`) | Run on Linux, headless Chromium |
| Links between repository files (`tools/check_links.py`) | Checked automatically |
| Raw links to the Day 4 templates | Opened (HTTP 200) when created |
| Installing Git, Node, Cursor, `gh` on Windows and macOS | **Not verified** |
| `npm install` and `npm run dev` on Windows and macOS | **Not verified** |
| Cursor: chat shortcuts, `.cursor/rules`, GitHub MCP, Figma MCP, Figma Make | **Not verified** |
| Uploading PDFs to Moodle, "Assignment" settings | **Not verified** |
| A full course run by a new person | **Not done** |

## Part 1. Clean machine (one run per OS)

You need: a computer or virtual machine without Git, Node and Cursor; a GitHub account that is not your main one (or a temporary one). Time it: the Day 0 budget is about 60 min.

### 1.1 Day 0 (`materials/en/day-0/day-0-prepare.md`, `materials/en/setup/installation-guide.md`)

| # | Step | Command or action | Expected | Result (OK / no) | Min |
|---|---|---|---|---|---|
| 1 | Install Git | Windows: `winget install --id Git.Git -e`; macOS: `xcode-select --install` | `git --version` shows 2.x | | |
| 2 | Install Node | Windows: `winget install OpenJS.NodeJS`; macOS: `brew install node@22` or the installer | `node -v` v22 or newer, `npm -v` | | |
| 3 | Configure Git | `git config --global user.name "…"` and `user.email` | no errors | | |
| 4 | Install `gh` and log in | Windows: `winget install --id GitHub.cli -e`; macOS: `brew install gh`; then `gh auth login` (HTTPS, browser) | `gh auth status`: Logged in | | |
| 5 | Install Cursor, sign in | from https://cursor.com | opens, the agent chat is there | | |
| 6 | Find the agent chat shortcut | check in the Cursor menu | matches the instruction (`Ctrl+L` / `Cmd+L`) or note the current one | | |

### 1.2 Day 1 (`materials/en/day-1/day-1-instruction.md`)

| # | Step | Command or action | Expected | Result | Min |
|---|---|---|---|---|---|
| 7 | Repository from the template | **Use this template** at https://github.com/VovaD199/spec-driven-ba-workshop-template, name `sdd-workshop-<name>`, public | repository created | | |
| 8 | Clone | Windows: `mkdir C:\Projects -Force; cd C:\Projects`; `git clone …`; macOS: `mkdir -p ~/Projects && cd ~/Projects` | folder with files; **no** password prompt | | |
| 9 | Dependencies | `cp .env.example .env` (PowerShell: `Copy-Item`), `npm install` | finishes without an error; record the time | | |
| 10 | Run | `npm run dev` | http://localhost:3000 opens (uk and en) | | |
| 11 | Second terminal | open a new terminal without stopping the server | the server keeps running | | |
| 12 | Tests | `npx jest --coverage=false` | all pass (on Linux: 290 suites, 1434 tests, all green, ≈30 s). The full `npm test` turns coverage on and **did not finish in 250 s** on Linux: do not give it to students, only `--coverage=false`; record the time on your OS | | |
| 13 | Branch and push | `git checkout -b day-1`, commit, `git push -u origin day-1` | push without a password prompt; a PR can be opened | | |

### 1.3 Days 2-4 (technical points)

| # | Step | Command or action | Expected | Result | Min |
|---|---|---|---|---|---|
| 14 | Cursor rule | create `.cursor/rules/docs-ba.mdc` per Day 2 | a new conversation follows the rule | | |
| 15 | GitHub MCP (optional) | per `github-mcp-setup.md` | tools visible in Cursor; token revoked | | |
| 16 | Day 3 probes | `npx jest app/lib/utils/validateContactData.test.ts --coverage=false`, `npx jest app/lib/utils --coverage=false` | one red test each after the changes (as in `fallback/`); on your OS record what you see | | |
| 17 | Order "documents first, then `git restore .`" | per Day 3, part C | code discarded, documents committed | | |
| 18 | Figma Make and **Open in canvas** | per Day 3, B1-B6 | design on the canvas, link copied | | |
| 19 | Figma MCP | per `figma-mcp-setup.md`, Day 4 block 0 | Cursor reads the canvas; record the call limit | | |
| 20 | Downloading the Day 4 templates | the `curl` (macOS) or `Invoke-WebRequest` (Windows) command from block 0 | six files in `docs/templates/` | | |
| 21 | Humanizer | skill per Day 4, block 8 | does not change IDs and numbers | | |

### Findings of Part 1

| Step # | What is wrong | Fix (file) | Status |
|---|---|---|---|
| | | | |

## Part 2. Pilot (1-2 people, preferably non-technical)

Goal: verify **time** and **clarity**, not knowledge. One person with no Git experience (the beginner profile), one with experience (the fast-track profile).

### Preparation

- [ ] Give the pilots only the PDFs (`python3 tools/build_materials.py --all --pdf`) and the template link; **do not hint**.
- [ ] Agree on a channel where the pilot writes when stuck; record **after how many minutes** they wrote.
- [ ] Prepare a Figma account or the mentor link for Figma.
- [ ] A mentor plays the stakeholder in Day 2 per `mentor/en/day-2-stakeholder-script.md`.
- [ ] One observer keeps the table below.

### Observation table (per day)

| Day | Block | Planned, min | Actual, min | Where stuck | What was unclear | What to fix |
|---|---|---|---|---|---|---|
| | | | | | | |

### Pilot success criteria

1. The beginner profile completes every day within 240 min of the **base track** (with the 30-minute buffer of Day 4) and submits a PR.
2. No step where a pilot was stuck for more than 20 min without a fallback.
3. All commands worked or were fixed in the sources.
4. The fast-track profile fits the day with or without stretch tasks; record how many stretch tasks were done.
5. The pilot can answer "what did you do yourself" (own edits are visible in the PR).

### After the pilot

- [ ] Move the findings into the "Findings" table above and fix the sources (`materials/`, `templates/`, `fallback/`).
- [ ] Update the timing in the "For the mentor" blocks.
- [ ] Record the pilot conclusions (what changed and why) in `docs/plan.md` or a new `docs/decisions.md`.
- [ ] Regenerate the PDFs and update the Moodle sandbox course.

## What I cannot do on my own

Installation on Windows and macOS, Cursor with its chat, Figma Make and Figma MCP, Moodle, and the pilot with people: these need you or a mentor. Everything else (fixing texts, regenerating PDFs, updating the examples from the findings) can be handed over once the tables are filled in.
