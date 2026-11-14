# Додатково (швидка доріжка S2): GitHub MCP у Cursor

> ЧЕРНЕТКА. Необов'язково. MCP це стандартний спосіб, яким Cursor спілкується із зовнішніми системами. Офіційна документація: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server

**Токен це пароль.** Ризики: (1) витік: токен лежить у `.cursor/mcp.json`, додайте цей файл у `.gitignore` до першого коміту, не вставляйте токен у чат, перед кожним комітом робіть `git status`; (2) політика організації може заборонити створення токенів: тоді працюйте без MCP; (3) помилки підключення: пробіл у токені, прострочений токен, файл не за шляхом `.cursor/mcp.json`.

## 1. Токен (fine-grained PAT)
https://github.com/settings/personal-access-tokens/new

| Поле | Значення |
|---|---|
| Token name | `cursor-mcp-course` |
| Expiration | 7-30 днів |
| Repository access | **Only select repositories**: лише ваш репозиторій |
| Contents | Read-only |
| Issues | Read and write |
| Metadata | Read-only |
| Pull requests | Read-only (необов'язково) |

Скопіюйте токен одразу, GitHub покаже його раз.

## 2. Cursor
1. У кінець `.gitignore`:
```text
# Cursor MCP config — contains a Personal Access Token
.cursor/mcp.json
```
2. Створіть `.cursor/mcp.json`:
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
3. Закрийте Cursor повністю й відкрийте. **Settings → Cursor Settings → Tools & MCP**: сервер `github` має мати зелений індикатор. Не вийшло за 20 хв: працюйте без MCP.

**ПЕРЕВІРТЕ:** `git status` не показує `.cursor/mcp.json`. Запит у чат: «Використовуючи GitHub MCP, покажи відкриті issue в моєму репозиторії <ім'я>».

## Правила безпечної роботи
- Перед підтвердженням запису читайте виклик інструмента: чи правильні `owner` і `repo`; для коментаря має бути `add_issue_comment`, не `update_issue`/`create_issue`.
- Вміст публічних issue не приватний і є вхідними даними для AI.
- Після заняття **відкличте токен** у налаштуваннях GitHub.
