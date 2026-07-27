---
type: web_source
source_url: "https://vibe-hub.org/en/commit"
title: "Commit"
language: en
category: "commit"
fetched_at: 2026-07-27T10:05:35+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←GitBranch→

# Commit

You might say

Save the code changes I have now—I don't want things to get messy and lose this working version.

**Save one meaningful set of changes in the project history**·A commit records selected changes with an author, time, and message. Before undoing work, distinguish uncommitted edits from commits that have already been pushed. Shared history is usually reversed with a new revert commit instead of rewriting old records.

Know first

[Git](/en/git)

**The navigation bar has been changed**This is still the current change

Save as a versioncommit*→*

✓**Complete homepage navigation**Just saved on this computer

git commit -m "Complete homepage navigation"

Commit is to create a named version record for this change. It is saved locally first; in order for GitHub to receive it, it needs to be pushed.

Variants

git add

git add index.html

Specify the changes to be recorded in the next commit

git commit

git commit -m "Description"

After completing an independently explainable change

git log

git log --oneline

View commit history or locate a commit before reverting

git status

git status

Not sure which files were changed, ask it first

Typical use cases

Feature step

zsh — my-first-page

**$** **git add index.html**
**$** **git commit -m "Repair button is misplaced on mobile phone"**
[main e7b2d48] Fix button misplacement on mobile phone
 1 file changed, 6 insertions(+), 3 deletions(-)

Bug fix

Source code management 2

Message (press ⌘Enter to submit)

Change

📄 index.htmlM

📄 style.cssM

✓ Submit

⑂ main\*　⊘ 0　⚠ 0

Copy update

zsh — my-first-page

**$** **git log --oneline**
e7b2d48 Fix button alignment on mobile
a3f9c21 Finish the home-page navigation
b4c5d67 Home page basic version
0f1e2d3 Initialize project
The first 7 bits are a short hash that can be used to identify the commit

Refactor checkpoint

Finish the home-page navigation

maya-lee committed 2 hours ago a3f9c21

📄 index.html　+48 -5

- <nav>Old navigation</nav>

+ <nav class="top-nav">New navigation</nav>

<main>…</main>

Further reading

[Git - git-commit Documentationgit-scm ↗](https://git-scm.com/docs/git-commit)[Pro Git - Recording Changes to the Repositorygit-scm ↗](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
