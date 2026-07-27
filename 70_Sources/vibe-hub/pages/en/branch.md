---
type: web_source
source_url: "https://vibe-hub.org/en/branch"
title: "Branch"
language: en
category: "branch"
fetched_at: 2026-07-27T10:05:36+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←CommitMerge→

# Branch

You might say

I need to try a different approach, but I don't want to break the version that works now.

**Develop an independent line of work without changing the main line**·A branch is a movable name pointing to a series of commits. It lets a feature, fix, or experiment proceed separately and later be merged. Create branches from the right starting point and keep their purpose small enough to review.

Know first

[Commit](/en/commit)

Main versionStay stable

Split here

New featureIndividual modification

git switch -c feature/new-nav

The branch is like an independent version line. You can modify and test on the "new features" line, and the main version will still be in its original stable state.

### When to use it

- Build a feature separately

  main
- Fix a bug without disturbing ongoing work

  feature/new-navfeature/dark-mode
- Try an experiment

  **$** **git switch main**Switched to branch 'main'The working directory is updated to main's file version
- Prepare a release or urgent patch

  main

  feature

### When NOT to use it

- Use one long-lived branch for unrelated work

  main
- Create it from an outdated or wrong starting point

  ⑂ test1  
  ⑂ aaa  
  ⑂ New branch 2A vague name makes branches hard to distinguish later
- Keep finished branches forever without a reason

  **$** **git switch main**error: Your local changes would beoverwritten by checkout.Uncommitted changes can block a switch or remain in the working directory afterward
- Assume switching branches saves uncommitted changes safely

  main

Anatomy

main

feature/new-nav

HEAD → You are now in feature/new-nav

1mainDefault branches usually contain verified changes; whether direct commits are allowed depends on team rules

2BaseA new branch is created from a certain commit, and the starting point corresponds to the snapshot at that time

3Feature BranchCan be named according to feature/function name for independent development and testing

4HEADHEAD points to the currently checked-out branch or commit, and git switch will update its point.

Variants

switch -c

git switch -c feature/new-nav

Create and switch to a new branch from the current commit

switch

git switch main

Switch the working directory to the file version of main

branch

git branch

View local branch list

branch -d

git branch -d feature/new-nav

After confirming that the branch has been merged or is no longer needed

Typical use cases

Feature branch

zsh — my-first-page

**$** **git switch -c feature/new-nav**
Switched to a new branch 'feature/new-nav'
Create and switch to a new branch from the current commit

Bug-fix branch

my-first-pagePublic

⑂ main ▾

Switch branch

**✓ main** Default

feature/new-nav

View all branches (2)

Experiment

<nav class="top-nav">  
 <a>Homepage</a>  
</nav>

⑂ **feature/new-nav**⊘ 0　⚠ 0Ln 3, Col 1

Confirm the current branch displayed in the lower left corner before starting modification

Release branch

your branch

⑂ mainDefaultUpdated 2 hours ago

⑂ feature/new-navUpdated 5 minutes agoNew pull request

Further reading

[Git - git-branch Documentationgit-scm ↗](https://git-scm.com/docs/git-branch)[Pro Git - Branches in a Nutshellgit-scm ↗](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
