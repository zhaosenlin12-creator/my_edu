---
type: web_source
source_url: "https://vibe-hub.org/en/env-var"
title: "Env Var"
language: en
category: "env-var"
fetched_at: 2026-07-27T10:05:29+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←SEODeployment→

# Env Var

You might say

I know a secret key shouldn't go in the code. Where should I put it?

**Provide configuration outside the source code**·Environment variables supply values such as API endpoints, feature settings, and secret keys when a program starts. Public browser variables are visible to visitors, even if their names come from an environment file. Keep real secrets on the server and document the required variable names with safe examples.

Know first

[Terminal](/en/terminal)

.env · Local development configuration
**OPENAI\_API\_KEY**=*sk-proj-••••••*
**DATABASE\_URL**=*postgres://••••*

process.env.OPENAI\_API\_KEY
🛡 .gitignore rule has been matched; check git status before submitting

### When to use it

- Set different values for development and production

  .env  
  **OPENAI\_API\_KEY**=sk-••••••  
  **DATABASE\_URL**=postgres://••••Keep one local setting per line. Do not commit, screenshot, or forward sensitive values.
- Provide server-side credentials

  const key = **process.env.OPENAI\_API\_KEY**Code reads the variable name, so you can usually change the configuration value without changing code.
- Configure an API endpoint

  .gitignore  
  node\_modules  
  **.env**Untracked files that match the rule are skipped; tracked files need separate handling.
- Turn deployment-specific features on or off

  💻 Local .env☁️ Platform settings

### When NOT to use it

- Commit a file containing real secrets

  const key = "sk-proj-8fk2…"A secret committed to the repository may appear in history, clones, or build artifacts.
- Put private keys in variables exposed to browser code

  .env→ Forward to a teammate / share a screenshot in the group chat

  Sharing the file or a screenshot may expose sensitive values in it.
- Assume changing a value updates a running process automatically

  Right-click → View page source<script> key="sk-…" </script>Once written into frontend code, visitors may read it directly.
- Leave required variables undocumented

  Changed .env, then just refreshed the page…401 Unauthorized (still using the old key)

Anatomy

OPENAI\_API\_KEY=sk-proj-•••••• # For local development, please do not submit

1KeyIt is the convention to use all uppercase letters and underlines, so read this name in the code.

2ValueAfter the equal sign is the actual configuration value; when the key is included, it must be covered before taking the screenshot.

3CommentNotes starting with # will be ignored by the program.

Variants

.env

.env

For local development use, should usually be excluded by .gitignore

Platform Env

Vercel → Settings → Env

Add another copy to the deployment platform settings page.

.env.example

.env.example

Telling others what to wear is not true.

Typical use cases

Database connection

.env🔒 Do not submit

# For local development  
**OPENAI\_API\_KEY**=sk-proj-8fk2••••••  
**DATABASE\_URL**=postgres://localhost:5432

API credential

api.js

const key = **process.env.OPENAI\_API\_KEY**;  
const res = await askAI(prompt, key);

The code reads the variable name; changing the configuration value locally usually does not require modifying the code

Site URL

.gitignore

node\_modules  
dist  
**.env**

🛡 Untracked files that match the rules will be skipped by git add; you still need to check git status before committing

Feature setting

Environment Variables
+ Add

KEY

VALUE

Environment

OPENAI\_API\_KEY

••••••••

Production

DATABASE\_URL

••••••••

Production
