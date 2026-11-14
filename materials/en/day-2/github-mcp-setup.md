# Optional (fast track S2): GitHub MCP in Cursor

> DRAFT. Optional. MCP is the standard way Cursor talks to external systems. Official docs: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server

**A token is a password.** Risks: (1) leaks: the token lives in `.cursor/mcp.json`; add that file to `.gitignore` before the first commit, never paste the token in chat, run `git status` before every commit; (2) your organization may forbid creating tokens: then work without MCP; (3) connection errors: a space in the token, an expired token, a file not at `.cursor/mcp.json`.

## 1. Token (fine-grained PAT)
https://github.com/settings/personal-access-tokens/new

| Field | Value |
|---|---|
| Token name | `cursor-mcp-course` |
| Expiration | 7-30 days |
| Repository access | **Only select repositories**: your repository only |
| Contents | Read-only |
| Issues | Read and write |
| Metadata | Read-only |
| Pull requests | Read-only (optional) |

Copy the token immediately; GitHub shows it once.

## 2. Cursor
1. At the end of `.gitignore`:
```text
# Cursor MCP config — contains a Personal Access Token
.cursor/mcp.json
```
2. Create `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": { "Authorization": "Bearer YOUR_GITHUB_PAT" }
    }
  }
}
```
3. Fully quit and reopen Cursor. **Settings → Cursor Settings → Tools & MCP**: the `github` server must show a green indicator. Not working after 20 min: continue without MCP.

**CHECK:** `git status` does not show `.cursor/mcp.json`. Chat prompt: "Using GitHub MCP, show open issues in my repository <name>".

## Safe-use rules
- Before approving a write, read the tool call: are `owner` and `repo` correct; for a comment it must be `add_issue_comment`, not `update_issue`/`create_issue`.
- Public issue content is not private and is input data for the AI.
- After class **revoke the token** in GitHub settings.
