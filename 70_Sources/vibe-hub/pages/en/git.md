---
type: web_source
source_url: "https://vibe-hub.org/en/git"
title: "Git"
language: en
category: "git"
fetched_at: 2026-07-27T10:05:28+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←DiffCommit→

# Git

You might say

AI broke my code. I want to get back to the last version that worked.

**Keep a history of code changes so work can be compared and restored**·Git records snapshots of a project and lets people compare changes, create independent branches, and combine work. Each developer has a full local history. GitHub and similar services host repositories and collaboration, but they are not Git itself.

Know first

[Terminal](/en/terminal)

**Files changed**These edits are not committed yet

Create a commitcommit*→*

✓**Homepage update committed**The snapshot is now in local history

Upload commitspush*→*

**GitHub**The remote repository now has the commit

Git tracks commits; GitHub hosts the remote repository

Commit a coherent set of changes to local history, then push those commits when you want to share or back them up on GitHub. Uncommitted edits are not included in a push.

### When to use it

- Save meaningful code changes

  init initializes the project→add selects changes→commit records a version
- Compare the current work with an earlier state

  Each stable small step can be a commit.
- Develop separate ideas on branches

  If a change causes trouble, you can return to an earlier commit.
- Collaborate through a shared remote repository

  💻 Local repositorygit push →☁️ GitHub

### When NOT to use it

- Commit passwords, tokens, or environment secrets

  Without commits for a long time, it is hard to restore a stable version.
- Treat Git as a backup for generated files and large binaries

  ● 111  
  ● Made a few changes  
  ● asdfThe message is unclear, making the version hard to identify later.
- Combine unrelated changes in one unclear commit

  🗂my-first-page🗑 Delete

  Deleting the project directory also loses local history.
- Run unfamiliar destructive commands without checking the target

  .envgit push →☁️

  The secret enters remote commit history.

Anatomy

💻 Working tree *Files you are editing*
git add →
📥 Staging area*Changes selected for the next commit*
git commit →
🗄 Local repository *Your commit history*
git push →
☁️ Remote repository *GitHub*

1Working DirFiles changed in your working tree that are not yet committed

2Staginggit add stages selected changes for the next commit; it does not move the file itself.

3Repositorygit commit records the staged changes as a new commit in local history.

4Remotegit push publishes local commits to a remote repository so collaborators can fetch them.

Typical use cases

Feature development

Commits · main

ML

Fix mobile navigation alignment

10 minutes ago

c7d8e9f

ML

Build homepage layout

2 hours ago

a1b2c3d

ML

Initialize project

3 days ago

0f1e2d3

Bug fix

zsh — my-first-page

**$** **git log --oneline**
c7d8e9f Fix mobile navigation alignment
a1b2c3d Build homepage layout
0f1e2d3 Initialize project
Each line shows a commit ID followed by its message

Team collaboration

zsh — my-first-page

**$** **git revert c7d8e9f**
[main f4e5d6c] Revert "Fix mobile navigation alignment"
Creates a new commit that reverses the selected commit without deleting history

Release history

my-first-page
<> Code ▾

📄 index.htmlBuild homepage layout2 hours ago

📄 README.mdInitialize project3 days ago

📄 .gitignoreInitialize project3 days ago

Further reading

[Pro Gitgit-scm ↗](https://git-scm.com/book/en/v2)[Git Referencegit-scm ↗](https://git-scm.com/docs)
