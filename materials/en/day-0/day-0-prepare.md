# Day 0. Course preparation (≈60-90 min, before Day 1)

> Status: DRAFT. Install commands (`winget`, `xcode-select`, `brew`, `nvm`, `apt`) are not yet verified on clean machines (see `mentor/en/day-0-checklist.md`). Language: [Українська](../../uk/day-0/day-0-prepare.md).

**Goal:** arrive on Day 1 with a working environment. Result: a verification screenshot sent to the mentor.

## 0. Prerequisites
- Windows 10/11, macOS or Linux computer, ≈5 GB free disk, internet.
- Permission to install software (if not, tell the mentor **in advance**).
- Accounts: GitHub (required), Cursor (free plan), Figma (required; if you have no account, the mentor will give you a link to the design and you will work with it, see Day 3).
- English reading level sufficient for the Cursor and Figma interfaces.

## 1. Install tools (≈40 min)
| Tool | Windows (PowerShell) | macOS (Terminal) |
|---|---|---|
| Git | `winget install --id Git.Git -e` | `xcode-select --install` |
| Node.js 22+ | `winget install OpenJS.NodeJS.LTS` | installer from https://nodejs.org |
| Cursor | https://cursor.com | https://cursor.com |

Linux: see [installation-guide](../setup/installation-guide.md). After installing, **close and reopen the terminal**.

Check:
```bash
git --version
node -v
```
Expected: Git 2.x, Node `v22` or newer.

Configure Git once (use the name on your GitHub account):
```bash
git config --global user.name "Ivan Petrenko"
git config --global user.email "you@example.com"
```

## 2. GitHub authentication (≈15 min)
Passwords are no longer accepted for `git push`. Simplest path for beginners:
1. Install **GitHub CLI**: Windows `winget install --id GitHub.cli -e`, macOS `brew install gh` (or https://cli.github.com).
2. Run `gh auth login`, choose **GitHub.com → HTTPS → Login with a web browser**, confirm the code in the browser.
3. Check: `gh auth status` shows "Logged in".

Fallback: Git Credential Manager (bundled with Git for Windows) opens a sign-in window on first `git push`. Docs: https://docs.github.com/en/get-started/git-basics/set-up-git

## 3. Readiness checklist
- [ ] `git --version` and `node -v` print versions
- [ ] `gh auth status` shows you are logged in (or Credential Manager is set up)
- [ ] Cursor starts and you are signed in
- [ ] You have a Figma account or you know you will use the mentor's link
- [ ] Screenshot of the first two items sent to the mentor

## 4. If something fails
Do not spend more than 20 min on one problem: write to the mentor with the error text and a screenshot. Common Windows/macOS issues: [installation-guide](../setup/installation-guide.md).

Next: [Glossary](glossary.md).
