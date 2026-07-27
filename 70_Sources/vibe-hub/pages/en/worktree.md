---
type: web_source
source_url: "https://vibe-hub.org/en/worktree"
title: "Worktree"
language: en
category: "worktree"
fetched_at: 2026-07-27T10:05:38+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Pull RequestStash→

# Worktree

You might say

I'm halfway through a feature and an urgent bug just came up. I don't want to clean up my current work first.

**Check out another branch in a second working directory**·A Git worktree lets one repository have several working directories at the same time. It is useful when a long task must stay open while another branch needs attention. Each worktree has its own checked-out files, but they share the repository history.

Know first

[Branch](/en/branch)[Terminal](/en/terminal)

The same Git history

**Project master version**Keep running

**New feature version**Modified in another folder

git worktree add new folder new branch

Worktree allows the same Git project to appear in two folders at the same time, and each folder opens a different branch. It is suitable for people who do not want to interrupt their current work but need to deal with another thing temporarily.

### When to use it

- Handle an urgent fix without closing current work

  **$** **git worktree add -b hotfix/login ../my-first-page-hotfix main**Preparing worktree (new branch 'hotfix/login')HEAD is now at a1b2c3d home-page baseline
- Compare two branches side by side

  📁 my-first-pagemain · home-page changes not committed📁 my-first-page-hotfixhotfix/login · fix sign-in issue
- Run separate builds from the same repository

  Window AAI updates feat/nav navigation

  Window BAI updates feat/pricing page

  Each directory has an independent branch, so changes do not overwrite one another
- Keep a long-running task open while reviewing another branch

  **$** **git worktree remove ../my-first-page-hotfix****$** **git worktree list**/Users/hu/my-first-page a1b2c3d [main]Removed the linked working directory; only the main one remains

### When NOT to use it

- Create worktrees without tracking where they live

  **$** **git checkout hotfix/login**error: Your local changes would be overwritten by checkout.Uncommitted changes block switching branches; handle them first
- Edit the same generated output from several worktrees

  **$** **git worktree list**my-first-page a1b2c3d [main]my-first-page-hotfix a1b2c3d [hotfix/login]my-first-page-test 0f1e2d3 [feat/test]my-first-page-old 9a8b7c6 [feat/old]An uncleaned working directory takes disk space and adds maintenance cost
- Delete the directory manually and leave stale metadata

  **$** **git worktree add ../dup main**fatal: 'main' is already checked out at '…/my-first-page'The same branch can work in only one directory at a time
- Use worktrees when simply switching a clean branch is enough

  📁 my-first-page-hotfixRight-click → Move to Trash

  Git still retains this working directory's registration

Anatomy

🗄 The same local repository (.git) Shared history and branch references

📁 my-first-pagemainMain working directory
📁 my-first-page-hotfixhotfix/loginadd the directory next to it

1RepositoryThe main working directory contains .git; all worktrees share the same set of history and branch references

2Main WorktreeCommonly used working directory, currently checking out the main branch

3Linked WorktreeCheck out another branch through the additional directory created by worktree add

Variants

Add

git worktree add -b hotfix/login ../hotfix main

When you want to open a new branch and working directory from main

List

git worktree list

View the existing working directory and its branches

Remove

git worktree remove ../hotfix

After completing the task and confirming that the directory does not need to be preserved

Typical use cases

Urgent hotfix

zsh — my-first-page

**$** **git worktree add -b hotfix/login ../my-first-page-hotfix main**
Preparing worktree (new branch 'hotfix/login')
HEAD is now at a1b2c3d Initial home page
**$** **ls ..**
my-first-page my-first-page-hotfix
The extra working directory shares the same repository history

Parallel feature

📁 my-first-page

main

Homepage changes have not been completed  
3 files have not been submitted

📁 my-first-page-hotfix

hotfix/login

Formal environment login failed  
Fix here → Commit → Push

Code review

Window A

AI is changing the navigation bar

my-first-page-nav · feat/nav

Running...

Window B

AI is changing the pricing page

my-first-page-pricing · feat/pricing

Running...

Each one occupies one worktree. After the modification, each will open a PR and do not cover each other

Side-by-side comparison

zsh — my-first-page

**$** **git worktree list**
/Users/hu/my-first-page a1b2c3d [main]
/Users/hu/my-first-page-hotfix e5f6a7b [hotfix/login]
**$** **git worktree remove ../my-first-page-hotfix**
**$** **git worktree list**
/Users/hu/my-first-page a1b2c3d [main]
After the repair is completed, the linked working directory has been removed

Further reading

[Git - git-worktree Documentationgit-scm ↗](https://git-scm.com/docs/git-worktree)
