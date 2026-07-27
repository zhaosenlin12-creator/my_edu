---
type: web_source
source_url: "https://vibe-hub.org/en/pull-request"
title: "Pull Request"
language: en
category: "pull-request"
fetched_at: 2026-07-27T10:05:37+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←CloneWorktree→

# Pull Request

You might say

My changes are done. Have someone review them before they go into the main version.

**Ask others to review and merge the work from one branch**·A pull request is a collaboration feature on Git hosting platforms, not a core Git command. It collects the change summary, discussion, automated checks, and review before a branch is merged. Keep its scope focused and explain how the result was verified.

Know first

[Branch](/en/branch)[Push](/en/push)[Diff](/en/diff)

New feature branch**Update homepage navigation**3 files have changed

Send to others for reviewPull Request*→*

*✓* Explain clearly*✓* Pass the check**Can be merged into the main version**

Create a Pull Request on GitHub

Pull Request is a check page, not a terminal command. It centralizes "why it was changed, what was changed, and how to verify it" to the team for confirmation, and then merges it into the main version after confirmation.

### When to use it

- Request code review

  feat/dark-mode was pushed to the remote

  feat/dark-modeCompare & pull request
- Discuss a proposed change

  feat: add dark mode to the home pageWhat changed: dark-mode support for navigation and cards  
  How to verify: toggle the switch in the upper-right corner
- Run checks before merging

  Squash and merge ▾

  Create a merge commitSquash and mergeRebase and merge

  Squash 7 intermediate commits into 1 main-branch commit
- Keep a record of why a branch entered main

  Merged#12 feat: dark mode

  Merged#11 fix: mobile navigation wrapping

  Personal projects can keep documented change records too

### When NOT to use it

- Open one request for several unrelated features

  **$** **git pull-request**git: 'pull-request' is not a git command.A PR is a GitHub web feature, not a command
- Use only the title and provide no context

  Openupdate #14

  The title and description are too vague to understand the scope
- Merge while required checks or questions remain unresolved

  Files changed **37**+2,140 −867

  One PR contains three features, making the review scope too large
- Treat review as permission to skip your own testing

  Commit message:  
  ● wip  
  ● Adjust implementation  
  ● Fix styles  
  ● Finish changesHistory was not organized by project convention, making later tracing harder

Anatomy

● Openfeat: Home page with dark mode #12

Alex Chen wants to merge **feat/dark-mode** into **main**

ConversationCommits 3Checks ✓Files changed 2

✓ No conflict, can be automatically mergedSquash and merge ▾

1Title & #Explain in one sentence what was changed; #12 is the number of this application form

2BranchesFrom which branch to merge into which branch: feat/dark-mode → main

3TabsConversation discussion, Commits save point, Files changed line by line changes

4Merge ButtonClick after passing inspection, testing and approval; the method of merging follows the project agreement.

Variants

Squash

3 commits → Organized into 1 entry into main

When you need to organize a set of intermediate commits into a complete change

Merge Commit

Keep each commit as is + merge nodes

Used when complete process records need to be kept

Rebase

Commits are queued and received at the end of main

The history is a straight line with no merge nodes.

Typical use cases

Feature review

Open a pull request

base: main
←
compare: feat/dark-mode
✓ Able to merge

What has been changed: Navigation bar + card supports dark colors  
How to verify: switch the upper right corner switch to see the effect

Create pull request

Bug-fix review

feat: Home page plus dark mode #12

● Open
Alex Chen wants to merge 3 commits from feat/dark-mode into main

ri

you · 2 hours ago · **Approved**

The instructions are clearly written, and the contrast of the navigation bar in dark colors is fine and can be used.

ConversationCommits 3Checks ✓Files changed 2

Design discussion

**Files changed 2**
+18 −4

📄 index.html

- <button>Click me</button>

+ <button class="btn btn-primary">Start now</button>

</section>

Release change

✓ This branch has no conflicts with the base branch

Squash and merge ▾

3 commits will be compressed into 1 entry into main: feat: Home page with dark mode (#12)

⤴ Merged
Alex Chen merged 3 commits into main

Further reading

[Pro Git - Contributing to a Projectgit-scm ↗](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project)
