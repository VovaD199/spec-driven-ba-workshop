# Day 1. Project start and context: step-by-step instruction

> DRAFT v2. Language: [Українська](../../uk/day-1/day-1-instruction.md). Prerequisite: [Day 0](../day-0/day-0-prepare.md) completed (Git, Node 22+, Cursor, GitHub login). If not, do it now and add ≈60 min to your schedule. `<…>` placeholders are filled in by the mentor before the course.

## Goal of the day
By the end you have:
- your own copy of the template repository on GitHub and locally, the app running in the browser;
- `AGENTS.md` and a Mermaid diagram submitted as a Pull Request;
- your first analyst document: a list of questions for the client (step 10).

## Two tracks
| | **Base** (everyone) | **Fast** (if you are ahead of schedule) |
|---|---|---|
| Steps | 1-9 + 10 | 1-10 + stretch tasks S1-S3 below |
| Support | Every step has CHECK and IF IT FAILED | Minimal hints, success criteria at the end |
| Time budget | 240 min | ≈150 min core + stretch |

**20-minute rule:** if you are stuck on one step for more than 20 min, use the fallback in "IF IT FAILED" or write to the mentor (error text + screenshot). Unknown term? See the [glossary](../day-0/glossary.md).

## Markers
| Marker | Meaning |
|---|---|
| **COPY** | Commands and texts to copy |
| **IN CURSOR CHAT** | Prompt for the Cursor agent chat |
| **CHECK** | Checkpoint |
| **IF IT FAILED** | Fallback path |

---

## Step 1. Your own repository from the template (≈10 min)
1. Sign in at https://github.com.
2. Open the template https://github.com/VovaD199/spec-driven-ba-workshop-template and click **Use this template → Create a new repository**.
3. Name: `sdd-workshop-<your-name>` in Latin letters. Visibility: **Public** (the mentor must see your PR). Do not put passwords or tokens in the repository. **Create repository**.

**CHECK:** your repository contains `README.md`, `package.json`, the `app/` folder.

## Step 2. Code on your computer (≈10 min)
Open a terminal. **COPY** (replace `<login>` and `<name>`):

macOS / Linux:
```bash
mkdir -p ~/Projects && cd ~/Projects
git clone https://github.com/<login>/sdd-workshop-<name>.git
cd sdd-workshop-<name>
```
Windows PowerShell (clone close to the disk root, paths are long):
```powershell
mkdir C:\Projects -Force; cd C:\Projects
git clone https://github.com/<login>/sdd-workshop-<name>.git
cd sdd-workshop-<name>
```

**CHECK:** `git status` says `On branch main`.

**IF IT FAILED:**
- Asks for login/password or `Authentication failed`: passwords no longer work. Run `gh auth login` (see [Day 0, section 2](../day-0/day-0-prepare.md)).
- Long paths (Windows): `git config --global core.longpaths true`.
- `SSL certificate problem` (Windows): `git config --global http.sslBackend schannel`, then retry.
- Git does not work at all: on the repository page **Code → Download ZIP**, unpack and work in the unpacked folder.

## Step 3. Open the project in Cursor (≈10 min)
1. **File → Open Folder** → the project folder. At "Trust this workspace?" choose **Yes, I trust the authors**.
2. Terminal in Cursor: menu **Terminal → New Terminal** (or `Ctrl+Shift+P` / `Cmd+Shift+P`, command `Terminal: Create New Terminal`).
3. Model: pick the cheapest one to preserve the free plan limit: [cursor-model-tips](../setup/cursor-model-tips.md).

**CHECK:** a terminal at the bottom, its path leads to the project folder; file tree on the left.

> The **agent chat** opens as a panel on the right. Shortcuts depend on the Cursor version (usually `Ctrl+L` / `Cmd+L`); check the menu or the [Cursor docs](https://docs.cursor.com). `<mentor confirms the current shortcut in class>`.

## Step 4. Run the app (≈20 min)
In the Cursor terminal, one by one:

```bash
cp .env.example .env         # Windows PowerShell: Copy-Item .env.example .env
npm install
npm run dev
```
- `.env` holds local settings; it does not go to Git (it is in `.gitignore`). Defaults are enough.
- `npm install` downloads libraries listed in `package.json`; the first run takes up to a few minutes and a `node_modules/` folder appears. npm warnings are normal, errors are not.
- `npm run dev` starts a local server and **occupies this terminal**. Open a **second terminal** for other commands: the `+` button in the terminal panel. Stop the server with `Ctrl+C`.

Open http://localhost:3000/en in the browser.

**CHECK:** the Liatoshynsky Foundation site opens. Browse "About" and "Contacts": which sections are real and which are placeholders?

**IF IT FAILED:**
- Port 3000 busy: use the address shown in the terminal.
- `npm install` fails: `node -v` must be 22+; retry without VPN.
- `running scripts is disabled` (Windows): `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
- Blank page after changes: `Ctrl+C` and `npm run dev` again.
- Not working after 20 min: the mentor shows the running app on screen and you continue (step 5 onward only needs files).

The database lives in memory and is refilled with demo data on every start, so nothing can be permanently broken.

**What is in the project (short):** `package.json` (dependencies and commands), `app/` (pages, API, services), `i18n/messages/` (uk/en texts), `scripts/` (demo data), `node_modules/` (libraries, appears after `npm install`).

> For Python developers: `npm install` ≈ `pip install -r requirements.txt`, `package.json` ≈ `requirements.txt`, `node_modules/` ≈ `.venv/`, `npm run dev` ≈ `python main.py`.

## Step 5. Get to know the project through the agent (≈15 min)
Open a new agent chat.

**IN CURSOR CHAT:**
```text
Read README.md and the top-level folder structure.
Explain what this project does, who it is for and how it is organized.
Answer in no more than 200 words.
```
**CHECK (your analyst work):** write three columns: what the answer **guessed right**, what it **missed**, what it **invented**. Compare with what you saw in the browser. We return to this on Days 2 and 4 (Grounded / Inferred / Invented labels).

## Step 6. Markdown in 5 minutes
Four constructs are enough:
```markdown
# Heading
## Subheading
- list item
| Column A | Column B |
|---|---|
| value | value |
```
Docs: [Markdown Guide](https://www.markdownguide.org/basic-syntax/), [basic formatting on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). Clarity matters more than volume.

## Step 7. Standing instructions for the agent: `AGENTS.md` (≈30 min)
Cursor reads `AGENTS.md` in the project root automatically. An analyst does not write code but writes instructions.

**IN CURSOR CHAT:**
```text
Based on what you know about this project, write a starter AGENTS.md file
for a new team member who is a business analyst.

Include:
- a one-paragraph project description
- the main pages and their business purpose (as a table)
- conventions: TypeScript, no default export, Ukrainian (uk) as the primary language
- a note that this is a training repository and the DB resets on every start
```
Review the result, **fix at least two inaccuracies** (this is your analytical part) and save it as `AGENTS.md` in the root. Conventions ("TypeScript, no default export") are hints for the agent, not business requirements; keep them but tell such things apart.

**CHECK:** open a **new** chat and ask: "What is this project? Answer as if I just joined the team." The agent should answer using terms from your `AGENTS.md`. If not: restart Cursor.

*Optional (fast track, see S1):* a rule for documents in `.cursor/rules/`.

## Step 8. Architecture diagram (Mermaid) (≈20 min)
**IN CURSOR CHAT:**
```text
Study the project structure, especially app/[lang]/, app/api/, app/services/,
app/infrastructure/ and app/di/.

Generate a Mermaid flowchart TD diagram showing:
- the main pages
- the API routes they call
- the services that use these routes
- the infrastructure (DB models/repositories) the services depend on

Label nodes with real folder or file names.

Create the file docs/architecture.md (create docs if missing) and write into it:
- a short introduction (2-3 sentences) on what the diagram shows;
- the diagram in a code block labelled mermaid.
```
**CHECK:** `docs/architecture.md` exists (if not: "Save the diagram to docs/architecture.md"). Preview: `Ctrl+Shift+V` / `Cmd+Shift+V` in Cursor or https://mermaid.live. If the diagram does not render, check that the block starts with ```` ```mermaid ```` or paste the code at mermaid.live.

**Discussion:** what is missing in the diagram? Where does your business knowledge matter?

## Step 9. Submission: Pull Request (≈25 min)
Run all commands in the terminal in the project folder (if the server is running, open a second terminal).

```bash
git checkout -b day-1
git status
```
`git status` must show `AGENTS.md` and `docs/architecture.md` (as new). If not, go back to steps 7-8.

```bash
git add AGENTS.md
git add docs/architecture.md
git status
git commit -m "docs: add AGENTS.md and architecture diagram (day 1)"
git push -u origin day-1
```
Authentication: see Day 0, section 2. Then on GitHub click **Compare & pull request → Create pull request** (from `day-1` into `main` of **your** repository). Send the PR link to the mentor (channel: `<given by the mentor>`).

**PR requirements:**
- from branch `day-1` into `main` of your repository (not the template), repository is public;
- title: `Day 1: <short what was done>`;
- description of 2-4 sentences: what you did, what was hard, what remains unclear;
- **Files changed** has only the day's files; no `.env`, `node_modules`, `.cursor/mcp.json`, tokens;
- after the mentor's feedback click **Merge pull request** so tomorrow starts from an up-to-date `main`. **Do not merge before the mentor's feedback.**

**CHECK before committing:** `git status` shows no `.env`, `node_modules`.

**IF IT FAILED (git push):** authentication error → `gh auth login`; `src refspec day-1 does not match` → you did not create the branch or commit anything: `git checkout -b day-1`, then `git add` and `git commit`. After 20 min: send the files to the mentor (screenshot / zip); this counts as a submission marked "no PR".

## Step 10. Analyst closing: questions for the client (≈15 min)
You already know the product from the code and the browser. Now look at it as an analyst.

**IN CURSOR CHAT:**
```text
Read AGENTS.md and docs/architecture.md. Compose a list of 5 questions for the client
(Liatoshynsky Foundation) whose answers are not in the code. For each question state:
why it matters (which decision depends on the answer) and who can answer it.
```
Edit the list and save it to `docs/questions.md` (another commit in the same PR). **Quality criterion:** questions are open ("why", "who", "what happens if…"), without a hinted answer; at least one concerns the privacy of visitor data. You will need this document on Day 2.

## Review criteria (for the mentor)
1. `AGENTS.md` and the diagram are in the PR and match the real project (no invented pages).
2. Own edits are visible (not only AI text), ≥2 corrections.
3. No service files or secrets.
4. `docs/questions.md`: ≥4 open questions with "why" and "who".

## Fast track: stretch tasks
- **S1.** Create a Cursor rule in `.cursor/rules/` for `docs/**/*.md` (one topic per file, a heading with a "why" explanation). *Criterion:* a new chat follows the rule; you corrected the generated text.
- **S2.** Ask the agent to find 3 business rules in the code that are not in the README and name the file for each. Verify manually. *Criterion:* 3 rules with file references, confirmed by you.
- **S3.** Add a second diagram to `docs/architecture.md` (sequence: what happens when a visitor submits the contact form). *Criterion:* the diagram matches the real behavior in the browser.

## For the mentor: timing (240 min)
| Min | Block |
|---|---|
| 0-20 | Introduction, format, 20-minute rule, grading rules (`<Moodle>`) |
| 20-60 | Steps 1-2 (Git/GitHub demo), authentication check in the room |
| 60-80 | Step 3 (Cursor) |
| 80-110 | Step 4 (run) |
| 110-125 | Break |
| 125-150 | Steps 5-6 |
| 150-185 | Step 7 (`AGENTS.md`) |
| 185-205 | Step 8 (diagram) |
| 205-230 | Steps 9-10 (PR, questions) |
| 230-240 | Wrap-up, pointer to Day 2 |

Risks and plan B: see `mentor/en/` (to be added in the mentor guide step).
