# Cursor model settings: how to save your limit

> DRAFT v1. Language: [Українська](../../uk/setup/cursor-model-tips.md). Based on Cursor's own answer and the author's observations. **Prices and plan terms change: check current data in Cursor.** Model names and menu locations may differ between versions.

## Why this matters
The free Cursor plan has a **limited usage quota**. When it runs out, the chat stops answering. Expensive models spend the quota faster, so on this course it is better **to pick the cheapest model from the start**.

**Exception:** in blocks where precision about files and code lines matters (Day 2 block 1) and on Day 4, if you have a choice, take a stronger model from those included in your plan. A non-cheap model more often gives accurate code references; keep the cheap one for routine work.

## What to do (before your first prompts, Day 1)

### 1. Turn off expensive models
1. In Cursor open **File → Settings → Cursor Settings** (on macOS **Cursor → Settings → Cursor Settings**).
2. On the left choose **Models**.
3. Turn off expensive models and leave the cheapest available one.

### 2. Pick a cheap model in the chat
- The model is changed with the **drop-down above the chat input**.
- On Windows models can also be switched with `Ctrl + /`.
- The new model applies from the **next message** in the same chat; no new chat is needed.

### 3. Which options count as cheap
According to Cursor's answer:
- **Composer** (Cursor's fast model) is designed to be economical: per the docs cheaper than Grok (input $0.50 and output $2.50 per million tokens vs $2 and $6 for Grok). These figures come from Cursor's answer and must be verified.
- **Auto → Cost**, if Auto is available on your plan. Individual plans usually have only the Cost mode: it uses models from the included weekly pool.
- **Avoid the Fast label** next to a model: it is a more expensive speed mode.

### 4. Make the cheap model the default
**Cursor Settings → Models**: set the default model so that every new chat starts with the cheap one.

## The message "Model unavailable on Free"
Cursor may show:

> Model unavailable on Free. Free includes Grok 4.7, Grok 4.6, and Auto with fixed settings. Switch to an included model to continue. [Switch to Auto] [Upgrade to Premium]

**What it means:** the model you chose is not available on the free plan. The free plan includes only **Grok 4.7, Grok 4.6 and Auto with fixed settings**.

**What to do:** click **Switch to Auto** (or choose Grok 4.6 or Grok 4.7 in the list). The **Upgrade to Premium** button is not required. So on the free plan a model such as Composer may be unavailable; go by the list in the message.

## If there is a lock next to the model
A lock next to a model (for example, Grok) means the model choice is **fixed**. This happens on the free plan without your own API key:
- `Ctrl + /` changes nothing because there is nothing to switch to: one model remains in the list;
- click the locked model's name: a card like "Upgrade to unlock more models" may open;
- while the lock is on, this conversation cannot be moved to Composer or another model;
- after unlocking (a paid plan) the cheaper option in the list is Composer.

## If the limit runs out
- The Cursor chat stops responding. This is not an error in your project.
- Talk to the mentor before or during class and agree on an option (the mentor can provide ready example results from the `fallback/` folder).
- Parts of the course that do not need the chat (Git, running the app, manual steps) can continue.

## How to save the limit
- Start with the cheapest model.
- Keep prompts short and specific.
- Do not open unnecessary files in the chat context.
- Use one chat per topic, but do not stretch a conversation forever.

## For the mentor
- Decision: we **recommend the cheapest model** to participants (this document), except in precision-critical blocks. We set no requirement for a paid plan.
- Fallback if the chat is unavailable: the `fallback/` folder of the course repository with ready example results (the mentor hands them out when needed).
- [ ] Add screenshots of the **Models** menu and the model drop-down.
- [ ] Check prices and model names are current before the course.
