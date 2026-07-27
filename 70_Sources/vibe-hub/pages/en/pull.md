---
type: web_source
source_url: "https://vibe-hub.org/en/pull"
title: "Pull"
language: en
category: "pull"
fetched_at: 2026-07-27T10:05:37+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←MergePush→

# Pull

You might say

My teammate says they're done with their changes. How do I get their version onto my computer?

**Download remote changes and integrate them into the current branch**·Git pull usually runs fetch and then merge or rebase. It updates the current branch with work from its configured remote branch. Check local changes and the active branch first so a convenient command does not create an unexpected integration.

Know first

[Git](/en/git)[Commit](/en/commit)[Merge](/en/merge)

**Remote repository**Two commits ahead of your local branch

Fetch and integrate commitspull*→*

**Local repository**Now up to date

git pull

Use pull when the repository already exists on your computer and you need remote commits. Git fetches them and integrates them into your current branch. Commit or stash local changes first if they could conflict.

### When to use it

- Update a local branch from its remote

  **$** **git status --short**(No output; working tree clean)**$** **git pull**Fast-forward
- Receive teammates' commits

  Device A 💻 push→☁️→Device B 💻 pull
- Synchronize before starting new work

  cloneFirst: copy working files and repository history

  pullNext: fetch and integrate remote updates
- Bring remote changes into a clean working state

  **$** **git pull**Auto-merging index.htmlCONFLICT (content): Merge conflict in index.htmlPulling can also cause conflicts that need manual resolution

### When NOT to use it

- Pull without checking which branch is active

  A teammate pushed 12 new commitsLocal is still on the old version

  Staying out of sync with the remote widens branch differences and increases merge conflicts
- Use it with unresolved local changes

  Automatic merge failed;fix conflicts and then commit the result.**(main|MERGING) $** Conflicts are unresolved
- Assume it only downloads files without integrating

  3 files changed after pullChanges not reviewed

  Continuing to edit may overwrite work a collaborator already finished
- Resolve resulting conflicts by blindly choosing one side

  **$** **git pull**Already up to date.Changes not saved in Git history cannot be recovered

Anatomy

☁️ New commits on remote repository *GitHub*
git fetch →
🗄 Local repository*download first, but don’t touch your files*
git merge →
💻 Workspace*New code incorporated*

1RemoteThe remote branch contains commits collaborators have pushed

2FetchDownloads remote commits and updates remote-tracking references without changing working-tree files

3Local RepoFetched commits remain separate until you merge or rebase them.

4MergeIntegrates fetched commits into the current branch; conflicts may occur here

5Working DirAfter integration, the working tree reflects the updated current branch

Variants

git pull

git status && git pull

Check local changes before bringing in remote updates

git fetch

git fetch

Get remote updates, but don't merge them into the current branch yet

up to date

Already up to date.

This message means your current branch already matches the remote

Typical use cases

Start of day sync

zsh — my-first-page

**$** **git pull**
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
Updating a3f9c21..e7b2d48
Fast-forward
 index.html | 12 +++++++-----
 1 file changed, 7 insertions(+), 5 deletions(-)

Before a push

zsh — my-first-page

**$** **git pull**
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
Resolve the conflict in the file, then run git add and git commit

Receive team changes

git clone

First setup: create a local repository from a remote one

📦 Downloads files and commit history

git pull

Ongoing work: bring remote commits into an existing local branch

📄 Fetches and integrates new commits

Update a long-lived branch

🏢💻

Work computer  
**git push**

→

☁️

GitHub  
Remote repository

→

🏠💻

Home computer  
**git pull**

Push committed work from one computer, then pull it into the other repository

Further reading

[Git - git-pull Documentationgit-scm ↗](https://git-scm.com/docs/git-pull)[Pro Git - Working with Remotesgit-scm ↗](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
