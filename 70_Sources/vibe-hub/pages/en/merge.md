---
type: web_source
source_url: "https://vibe-hub.org/en/merge"
title: "Merge"
language: en
category: "merge"
fetched_at: 2026-07-27T10:05:36+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←BranchPull→

# Merge

You might say

The feature I built separately works. How do I bring it back into the main version?

**Combine the commits from one branch into another**·Merge brings two lines of history together. Git can combine independent changes automatically, but overlapping edits may create conflicts that a person must resolve. Review the result and run tests after resolving, because a clean text merge can still break behavior.

Know first

[Branch](/en/branch)[Commit](/en/commit)

main version

New Features

✓**The main version has been updated**The changes on both sides have been put together

git merge feature/new-nav

Merge brings the completed changes of another branch into the current branch. If both sides have changed the same place, Git will pause and ask you to decide what to keep in the end.

### When to use it

- Bring a reviewed feature into main

  main
- Combine work from two branches

  main
- Keep both lines of history

  <<<<<<< HEADTitle: Xiaoli's home page=======Title: Xiaoli's photography home page>>>>>>> feature
- Integrate a finished fix

  Edit final content→git add→git commit

### When NOT to use it

- Resolve a conflict without understanding both sides

  The feature branch still has an error→ merge →main has the same bug

  Merging unverified changes into main raises release risk
- Merge into the wrong target branch

  ~~Title: Xiaoli's home page~~  
  ~~Title: Xiaoli's photography home page~~Deleting both sides can remove existing functionality
- Assume no text conflict means no product conflict

  <<<<<<< HEAD  
  Title: Xiaoli's home pageLeaving conflict markers can make code unparsable
- Mix unrelated cleanup into conflict resolution

  merge ✓→push ✓→Production error

Anatomy

<<<<<<< HEAD
<h1>Xiaoli's homepage</h1>
=======
<h1>Xiaoli’s photography homepage</h1>
>>>>>>> feature/new-nav

1<<<<<<< HEADStarting here is the conflict area, HEAD refers to the version of the branch you are currently on.

2Current ChangeWhat does this line look like on the current branch? It is usually the content of the main line.

3=======The boundary between the upper and lower versions must be deleted together when resolving the conflict.

4Incoming ChangeWhat does this line look like on the merged branch?

5>>>>>>> branchThe conflict area ends here, marking which branch the content comes from.

Variants

Fast-forward

Updating a3f9c21..e7b2d48

The target branch has no independent new commits

Merge Commit

Merge made by the 'ort' strategy.

There are new commits on both sides and the merge node needs to be retained

merge --abort

git merge --abort

When you need to abandon the current unfinished merge

Typical use cases

Feature integration

zsh — my-first-page

**$** **git switch main**
Switched to branch 'main'
**$** **git merge feature/new-nav**
Merge made by the 'ort' strategy.
 index.html | 24 ++++++++++++++-----
 1 file changed, 16 insertions(+), 8 deletions(-)

Pull request merge

📄 index.html⚠ 1 conflict

<<<<<<< HEAD (main line)

<h1>Xiaoli’s homepage</h1>

=======

<h1>Xiaoli’s photography homepage</h1>

feature/new-nav (branch)

Edit to the final content, remove all conflict tags and resubmit

Release preparation

📄 index.html Merge conflict

Adopt current changesAdopt incoming changesKeep changes from both parties

<h1>Xiaoli’s homepage</h1> (current · HEAD)

<h1>Xiaoli's photography homepage</h1> (incoming · branch)

You can choose to keep current changes, incoming changes, or both changes

Conflict resolution

New navigation bar #2

maya-lee wants to merge feature/new-nav into main

✓
This branch has no conflict with the base branch

Merge pull request

Click this green button on the web page, the effect is equivalent to git merge

Further reading

[Git - git-merge Documentationgit-scm ↗](https://git-scm.com/docs/git-merge)[Pro Git - Basic Branching and Merginggit-scm ↗](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
