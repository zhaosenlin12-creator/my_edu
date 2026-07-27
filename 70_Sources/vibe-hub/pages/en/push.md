---
type: web_source
source_url: "https://vibe-hub.org/en/push"
title: "Push"
language: en
category: "push"
fetched_at: 2026-07-27T10:05:37+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←PullClone→

# Push

You might say

My local changes are ready. How do I send them to GitHub so everyone else can see them?

**Upload local commits to a remote repository**·Push sends commits and branch references to a remote such as GitHub. It shares committed history, not uncommitted files. The remote may reject the push if new work exists there or if branch rules require review.

Know first

[Git](/en/git)[Commit](/en/commit)

**Local repository**Two commits ahead

Upload commitspush*→*

**Remote repository**Branch updated on GitHub

git push

Push sends local commits to a remote branch. It does not include uncommitted edits. Afterward, confirm that GitHub shows the expected commit on the expected branch.

### When to use it

- Back up committed work to the remote

  💻 Local repositorygit push →☁️ GitHub
- Share a branch with teammates

  **$** **git push**! [rejected] main -> main (non-fast-forward)hint: 'git pull' before pushing again.
- Update a pull request

  .gitignore  
  node\_modules  
  **.env**Untracked files that match the rule are skipped; tracked files need separate handling.
- Publish a reviewed commit history

  Refresh GitHub—the latest commit is there✓ Uploaded

  After pushing, verify the remote branch and latest commit

### When NOT to use it

- Expect uncommitted changes to be uploaded

  💻 Local ●●●●☁️ Empty

  If you commit without pushing, the remote repository does not have those commits
- Force-push a shared branch without coordination

  **$** **git push --force**+ a3f9c21...e7b2d48 main -> main (forced update)Existing commits on the remote branch may be rewritten
- Push secrets and try to delete them later

  .envPublicly visible on GitHub

  Once a secret is pushed to a remote repository, treat it as exposed even if the commit is deleted
- Ignore a rejection without checking remote changes

  node\_modules 380MBgit push →

  A large number of reinstallable dependencies entered the repository; .gitignore should exclude them.

Anatomy

git pushoriginmain

1git pushPublishes commits from a local branch to its remote counterpart

2originThe remote’s short name; Git names the cloned source origin by default.

3BranchThe local branch being pushed, usually main or a feature branch

Variants

git push

git push

Sync local branch commits to remote

push -u

git push -u origin main

Establish a tracking relationship between local and remote branches when pushing for the first time

push --force

git push --force

Rewrites remote history; use it only when you understand who and what it will affect

Typical use cases

Publish feature branch

zsh — my-first-page

**$** **git push**
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Writing objects: 100% (8/8), 1.24 KiB | 1.24 MiB/s, done.
To github.com:maya-lee/my-first-page.git
 a3f9c21..e7b2d48 main -> main

Update pull request

zsh — my-first-page

**$** **git push**
To github.com:maya-lee/my-first-page.git
! [rejected] main -> main (non-fast-forward)
error: failed to push some refs
hint: Updates were rejected because the remote contains
hint: work that you do not have locally.
hint: 'git pull' before pushing again.
Pull and integrate the remote commits, then push again

Share a fix

my-first-page
Just refreshed

📄 index.htmlFix mobile button alignment1 minute ago

📄 style.cssFix mobile button alignment1 minute ago

📄 .gitignoreInitialize project3 days ago

✓ Latest commit found on the remote branch

Sync remote backup

Working directory

📄 index.html  
📄 style.css  
📄 .gitignore  
📄 .env　🔑

Remote repository

📄 index.html  
📄 style.css  
📄 .gitignore  
.env is ignored ✓

Further reading

[Git - git-push Documentationgit-scm ↗](https://git-scm.com/docs/git-push)[Pro Git - Working with Remotesgit-scm ↗](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
