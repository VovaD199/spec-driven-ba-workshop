# Installing the tools: Windows, macOS, Linux

> DRAFT v1 (carried over from the earlier repository; needs verification). Language: [Українська](../../uk/setup/installation-guide.md). Core commands and GitHub authentication: [Day 0](../day-0/day-0-prepare.md). **The install commands (`winget`, `xcode-select`, `brew`, `nvm`, `apt`) have not been run or verified on Windows, macOS or Linux.** Only the fact that the training app starts on Windows with Node 24 was verified. The mentor verifies Windows, students and the mentor verify macOS (see "For the mentor"). Screenshots are not added yet.

## What to install
| Tool | What for | When needed |
|---|---|---|
| Git | Working with the repository | Day 1 |
| Node.js 22 or newer | Running the training app | Day 1 |
| Cursor | Editor with an AI agent | Day 1 |
| GitHub account | Repository, PR | Day 1 |
| Cursor model settings | Saving the free plan limit | Day 1 (see [cursor-model-tips](cursor-model-tips.md)) |
| Figma account (mandatory; if you have none, the mentor gives you a link to the mockup) | Mockup and Figma MCP | Days 3-4 |
| GitHub CLI (`gh`) | Signing in to GitHub for `git push` | Day 0 |

**Before the course:** install Git and Node.js and send the mentor a screenshot of:
```bash
git --version
node -v
```
Expected: Git 2.x and Node `v22.x` or newer (`v24.x` also works; the training app was verified to start on Node 24).

---

## Windows 10/11
### Git
Open PowerShell (Start → type "PowerShell").
```powershell
winget install --id Git.Git -e
```
If `winget` is unavailable, download the installer from https://git-scm.com/download/win and accept the defaults. Close and reopen PowerShell:
```powershell
git --version
```
### Node.js
```powershell
winget install OpenJS.NodeJS
```
Or the installer from https://nodejs.org/en/download (version 22 or newer). Close and reopen PowerShell:
```powershell
node -v
npm -v
```
### Cursor
Download from https://cursor.com and install. Sign in.
### Git setup (once)
```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
### Common problems (Windows)
| Symptom | What to do |
|---|---|
| `git` or `node` not found after installing | Close and reopen PowerShell; restart the computer |
| `npm install` complains about the script execution policy (`running scripts is disabled`) | In PowerShell run: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (allows local scripts for your user) |
| No administrator rights | Write to the mentor before class; use portable versions or the fallback path (Download ZIP + Codespaces, if allowed) |
| `SSL certificate problem` during `git clone` / `git push` | Run once `git config --global http.sslBackend schannel` (Git uses the Windows certificate store; helps behind a corporate proxy or certificate substitution) |
| Long-path error during `git clone` or `npm install` | Clone closer to the disk root, for example `C:\Projects`, and run once `git config --global core.longpaths true` |

---

## macOS
### Git
Open Terminal (Spotlight → "Terminal").
```bash
xcode-select --install
```
The Apple command line tools installation window appears: confirm. Or, if you have Homebrew:
```bash
brew install git
```
Check:
```bash
git --version
```
### Node.js
The installer from https://nodejs.org/en/download (version 22 or newer), or via Homebrew:
```bash
brew install node@22
```
Check:
```bash
node -v
npm -v
```
### Cursor
Download from https://cursor.com, drag to Applications and launch. If macOS blocks it, open **System Settings → Privacy & Security** and confirm.
### Git setup (once)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
### Common problems (macOS)
| Symptom | What to do |
|---|---|
| `xcode-select` downloads for a long time | This is normal, wait; internet is required |
| `node` not found after `brew install node@22` | Follow Homebrew's hint to add `node@22` to `PATH`, restart the terminal |
| Gatekeeper blocks the app | Allow it in "Privacy & Security" |

---

## Linux (Debian / Ubuntu, example)
### Git
```bash
sudo apt update && sudo apt install -y git
git --version
```
(Fedora: `sudo dnf install -y git`.)
### Node.js 22 via nvm
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```
Close and reopen the terminal, then:
```bash
nvm install 22
node -v
npm -v
```
> Before running a script from the Internet, read it (or install Node.js another way, for example from your distribution's package manager).
### Cursor
Download from https://cursor.com (AppImage or `.deb`, depending on the distribution) and follow the site's instructions.
### Git setup (once)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## Fallback paths (any OS)
1. **Without Git:** on your repository page on GitHub click **Code → Download ZIP**, unpack and open the unpacked folder in Cursor. You can connect Git later.
2. **No installation rights:** write to the mentor before class.
3. **GitHub Codespaces:** run in the browser without local tools. *Availability for external participants must be confirmed before the course.*

## Readiness checklist
- [ ] `git --version` shows a version
- [ ] `node -v` shows 22 or newer
- [ ] Cursor starts and you are signed in
- [ ] You have a GitHub account
- [ ] The check screenshot was sent to the mentor

## For the mentor
- [ ] Walk through the Windows section on a clean machine (the `winget` commands are not verified yet).
- [ ] macOS: students/mentor verify; collect feedback on `xcode-select`, `brew`, `node@22`.
- [ ] Linux: confirm which distributions we support (now only an example for Debian/Ubuntu and Fedora for Git).
- [ ] Check the nvm script version (v0.40.1) is current.
- [ ] Add screenshots and make separate PDFs per OS.
- [ ] Prepare an "installing without administrator rights" guide.
- [ ] Check whether Codespaces is allowed for external participants.
