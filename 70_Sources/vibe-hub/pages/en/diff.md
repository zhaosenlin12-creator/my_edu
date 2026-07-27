---
type: web_source
source_url: "https://vibe-hub.org/en/diff"
title: "Diff"
language: en
category: "diff"
fetched_at: 2026-07-27T10:05:39+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←.gitignoreGit→

# Diff

You might say

Show me exactly what changed this time—what lines were added and what lines were removed.

**See exactly what changed between two states**·A diff shows added, removed, and modified lines between the working tree, staged changes, commits, or branches. Read it before committing and reviewing so accidental edits, secrets, and unrelated changes are caught early.

Know first

[Git](/en/git)[Commit](/en/commit)

Before changesButton text***−* Click me**

→

After changesButton text***＋* Start now**

git diff

Diff is a list of changes: red minus signs indicate deleted content, and green plus signs indicate new content. Read it over before submitting to make sure there are no accidentally deleted, debugged content or keys.

### When to use it

- Review work before a commit

  **$** **git diff**- <button>Click me</button>+ <button class="btn btn-primary">Get started</button>Red means deleted and green means added; shows changes not yet added
- Compare two branches or commits

  **$** **git diff HEAD~1 HEAD** 2 files changed, 18 insertions(+), 4 deletions(-)Explicitly compare the two most recent commits
- Understand a pull request

  📄 index.html+18 −4

  - Click me+ Get started
- Find an accidental or missing change

  AI finished the changes→git diff for a line-by-line review→commit records a revision

### When NOT to use it

- Review only the filenames and skip the actual lines

  **$** **git add . && git commit -m "AI changes"**47 files changed, without reviewing each oneWhen something breaks, it is hard to identify the exact change
- Assume a small diff has a small product impact

  + console.log("test 123")+ // debugger;Temporary debugging code was committed tooUse diff to remove debugging code before committing
- Include formatting changes that hide the real edit

  3 files changedA file list alone cannot confirm the exact line changes
- Copy secrets into a diff shared outside the team

  - <nav>…entire navigation bar…</nav>- <footer>…</footer>+ <nav>New navigation</nav>The deletion includes the footer; confirm that is intended

Anatomy

📄 **index.html**
@@ -12,5 +12,5 @@
- <button>Click me</button>
+ <button class="btn btn-primary">Start now</button>

1File HeaderWhich file does this change belong to? One file and one section.

2Hunk @@@@ -12,5 +12,5 @@: Change near line 12

3- RemovedRed with - sign: lines that existed in the old version and deleted in the new version

4+ AddedGreen with a + sign: extra lines in the new version

Variants

git diff

git diff

Check what has been changed in the workspace relative to the staging area

git diff --staged

git diff --staged

Review after add and before commit

git diff commits

git diff HEAD~1 HEAD

Review specific changes from the most recent commit

git diff main..feat

git diff main..feat/dark-mode

Before merging, check how far ahead the branch is

Typical use cases

Pre-commit review

zsh — my-first-page

**$** **git diff**
diff --git a/index.html b/index.html
@@ -12,5 +12,5 @@
- <button>Click me</button>
+ <button class="btn btn-primary">Start now</button>
The red band - is deleted, the green band + is added

Pull request

zsh — my-first-page

**$** **git diff HEAD~1 HEAD --stat**
 index.html | 10 ++++++----
 style.css | 12 ++++++++++++
 2 files changed, 18 insertions(+), 4 deletions(-)
**$** **git diff HEAD~1 HEAD**
Check the line-by-line details again to confirm the content of this round of AI modifications

Bug investigation

ConversationCommits 3Checks ✓Files changed 2

**📄 index.html**
+18 −4

@@ -12,5 +12,5 @@

- <button>Click me</button>

+ <button class="btn btn-primary">Start now</button>

Release comparison

🤖 AI finishes a round of changes
→
🔍 review git diff line by line
→
✅ git commit record

Further reading

[Git - git-diff Documentationgit-scm ↗](https://git-scm.com/docs/git-diff)
