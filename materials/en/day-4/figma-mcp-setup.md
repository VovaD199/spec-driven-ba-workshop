# Connecting Figma MCP to Cursor

> DRAFT v2. Language: [Українська](../../uk/day-4/figma-mcp-setup.md) (the full version with limit tables). Built from the official Figma documentation (see "Sources"). **Method 3 was verified by the author; methods 1 and 2 (plugin, manual connection) were not verified in practice.** The connection is done **on Day 4 (block 0) together with the mentor**, not at home. The mentor walks through it on a clean machine (Windows and macOS) before the course.

## Limits (summary; limits change: check the sources before the course)
- **Figma Make spends AI credits.** Free plan (Starter): 500 credits per month and a **daily limit of 150**; that is roughly one or two mockup generations per day. Generate once with the Day 3 prompt, refine minimally.
- **Figma MCP calls (reading design data).** View/Collab seats: **20 calls per month** (also on Starter, per Figma staff; older material says 6, outdated). Full/Dev seats on paid plans: 200+ per day. The Day 4 exercise needs only a few calls: do not repeat it needlessly.
- **If the limit is exhausted:** tell the mentor and use method 3 below, the mentor's canvas link, or the fallback without Figma MCP.

## Why
Figma MCP lets the Cursor agent read the design directly: component names, variants, styles, layers. In Day 4 (part 3) we use it to read the contact form mockup and compare it with the code. **We only read the design**: writing into a designer's file via MCP is not used in this course.

## What you need
- Cursor (installed in Day 1).
- A Figma account (the desktop Figma app is **not** needed for the remote server).
- The contact form mockup from Day 3 on the canvas of your Figma file, **or** the mentor's canvas link if you have no account or no limit.

## Method 1 (recommended): Figma plugin for Cursor
1. Open the command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and find **Open chat**.
2. In the chat enter `/add-plugin figma`, press **Submit**, then **Add Plugin** (or install from Cursor Marketplace).
3. Command palette → **Cursor Settings** → **Tools & MCP**.
4. Under **Installed MCP Servers** click **Connect** next to Figma.
5. Sign in to Figma and click **Allow access**.

## Method 2: add the server manually
If the plugin is unavailable (Figma skills and rules are not installed). Add to `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "figma": { "url": "https://mcp.figma.com/mcp" }
  }
}
```
If you already have this file with GitHub MCP (Day 2, optional), add `"figma"` next to `"github"` inside `mcpServers`, do not replace the existing content. This config has no token (sign-in via browser), but if you did GitHub MCP in Day 2, `.cursor/mcp.json` is already in `.gitignore`: do not remove it. Save, then in **Cursor Settings → Tools & MCP** click **Connect** next to Figma and sign in.

## Method 3: describe a design by link (verified during course preparation)
Works when the design generated in Figma Make has been **moved to the canvas of a regular Figma design file**, so the frame has its own link. In Make click **Open in canvas** (top right, next to Publish and Share; the button name depends on the version), then copy the frame link (**Copy link to selection**) and ask the agent:

**IN CURSOR CHAT:**
```text
Describe the design of this page: <link to your frame in Figma>
```
**CHECK:** the agent returns the page structure: blocks, components, texts. This works only for a design moved to the canvas, not a prototype inside Make. Conditions (plan type, whether Figma MCP is required, limits) were not verified separately: if the request fails, use the fallback.

## Connection check
1. In **Cursor Settings → Tools & MCP** Figma is "connected".
2. In Figma right-click a frame → **Copy link to selection**.
3. **IN CURSOR CHAT:**
```text
Using Figma MCP, describe the structure of this frame: component names and states.
Do not change code.

<paste the copied link>
```
**CHECK:** the agent returns component and layer names of your mockup.

## Common problems
| Symptom | What to do |
|---|---|
| Connection error, browser sign-in does not complete | Remote OAuth MCP servers in Cursor are reported unstable (Cursor forum, April 2026; current status unknown). Update Cursor, retry **Connect**, restart Cursor |
| The agent does not see the mockup | Use a "Copy link to selection" link to a specific frame, not the whole file |
| No permission for the file | Check that you open your own file or have access |
| Limit error | Wait or reduce requests; limits depend on the plan |
| Nothing helps | **Fallback:** describe the mockup in words (frame and component names) and do the exercise on the description |

## Fallback without Figma MCP
The Day 4 part 3 exercises (component reuse, pattern comparison, accessibility) can be done without MCP: describe each frame in the chat (names, fields, states) or paste a screenshot. The result is less precise but useful.

## For the mentor (check before the course)
- [ ] Walk through methods 1 and 2 on clean Windows and macOS.
- [ ] Check behavior on the free Figma plan (access, limits) and with 2-3 requests in a row.
- [ ] Check whether the OAuth problem is still current in your Cursor version.
- [ ] Prepare screenshots of the steps.
- [ ] Prepare your own canvas link with a ready mockup for students without accounts or limits.

## Sources
- Figma: [Cursor and Figma: set up the MCP server](https://help.figma.com/hc/en-us/articles/39889260656407-Cursor-and-Figma-Set-up-the-MCP-server)
- Figma Developers: [Remote server installation](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- Cursor forum: [Failed to set up Figma remote MCP server in Cursor](https://forum.cursor.com/t/failed-to-set-up-figma-remote-mcp-server-in-cursor/157062)
- Figma: [Figma MCP server: rate limits and access](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/)
- Figma Help: [Figma AI credits](https://help.figma.com/hc/en-us/articles/33459875669015)
- Figma Make: https://www.figma.com/make/
