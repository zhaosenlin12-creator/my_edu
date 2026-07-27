---
type: web_source
source_url: "https://vibe-hub.org/en/stash"
title: "Stash"
language: en
category: "stash"
fetched_at: 2026-07-27T10:05:38+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Worktree.gitignore→

# Stash

You might say

I'm in the middle of changes but need to switch to something else. Can I put this work aside for now?

**Temporarily set aside uncommitted changes**·Stash stores selected working changes and restores a cleaner directory so another task can proceed. It is useful for short interruptions, not as a long-term archive. Name important stashes and inspect conflicts when applying them later.

Know first

[Git](/en/git)[Branch](/en/branch)

**The form has not been changed yet**Cannot be saved as a version yet

Temporarily collapsestash*→*

**Unfinished changes**Replace if needed

*✓***The workspace is clean**You can switch tasks first

git stash push -m "The form is halfway done"

Stash is only suitable for temporarily putting away unfinished changes to facilitate switching branches or handling urgent matters. It is not an official version, nor is it a remote backup; you still need to Commit when completed.

### When to use it

- Pause unfinished work briefly

  **$** **git stash push -m "home-page changes are unfinished"**Saved working directory and index state On main: home-page changes are unfinished
- Switch branches with a dirty working tree

  **$** **git stash apply stash@{0}**Changes restored to the working treeKeep the stash first; drop it after confirming the restore is correct
- Test the current branch without local edits

  **$** **git stash list**stash@{0}: On main: home-page changes are unfinishedstash@{1}: WIP on main: a1b2c3d home-page baselineEach save creates a record; the newest record is numbered 0
- Move a small uncommitted change to another context

  stash@{0}Home-page changes are unfinished

  stash@{1}WIP on main: a1b2c3d

  Use descriptive names to identify saved changes

### When NOT to use it

- Use stash as permanent storage

  stash@{0} … stash@{7}There are 8 records; the earliest was created last monthLeaving history unorganized makes each record's purpose harder to identify
- Build a large anonymous pile of stashes

  Current branch: hotfix/login**$** **git stash pop**Home-page changes were applied to hotfix/loginConfirm the current branch before running pop
- Assume ignored and untracked files are always included

  stash@{2}WIP on main: 3 weeks ago

  Without a description, the record's contents are hard to confirm quickly
- Apply a stash and ignore resulting conflicts

  The earlier change was reimplemented after the fixAn existing stash was not restored, causing duplicate work

Anatomy

**🛠 Working tree** unfinished changes to index.html
stash push →

**stash@{0}** Unfinished home-page changes ← Latest
**stash@{1}** WIP on main: a1b2c3d
**stash@{2}** WIP on main: 0f1e2d3

1Working DirTemporarily stores uncommitted changes so you can switch context without committing them

2stash@{0}The most recent stash. git stash pop uses this entry by default unless you name another one.

3stash@{1}Each git stash push creates a new entry at the top of the stack.

4stash@{2}Higher numbers refer to older entries; restore or drop them once they are no longer needed.

Variants

git stash push

git stash push -m "Home page changes have not been completed"

When you need to set aside local changes before switching tasks; a stash is not pushed to the remote

List

git stash list

View existing stash records

Apply

git stash apply stash@{0}

Restore first but keep the backup, then drop after confirming

Apply

git stash apply

When you want to restore the most recent stash while retaining it

Typical use cases

Quick branch switch

zsh — my-first-page

**$** **git status**
modified: index.html (modification not yet completed)
⚡ Login to the official environment failed, you need to switch to hotfix/login
**$** **git stash push -m "Home page changes have not been completed"**
Saved working directory and index state On main: Home page changes have not been completed
**$** **git checkout hotfix/login**
Switched to branch 'hotfix/login'

Temporary clean state

zsh — my-first-page

**$** **git stash list**
stash@{0}: On main: Home page changes have not been completed
stash@{1}: WIP on main: a1b2c3d Home page basic version
The smaller the number, the newer it is. Pop defaults to stash@{0}

Interrupted task

zsh — my-first-page

**$** **git checkout main**
Switched to branch 'main'
**$** **git stash apply stash@{0}**
On branch main
Changes not staged for commit:
modified: index.html
Changes restored to the working tree
The changes have been restored, please confirm that they are correct before executing drop

Move a small patch

🛠 Home page changes not yet completed
stash push →
📦 stash@{0}
→ Handle other tasks →
🛠 stash apply restore

Further reading

[Git - git-stash Documentationgit-scm ↗](https://git-scm.com/docs/git-stash)[Pro Git - Stashing and Cleaninggit-scm ↗](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)
