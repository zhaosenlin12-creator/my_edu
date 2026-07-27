---
type: web_source
source_url: "https://vibe-hub.org/en/clone"
title: "Clone"
language: en
category: "clone"
fetched_at: 2026-07-27T10:05:37+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←PushPull Request→

# Clone

You might say

Here's a project URL. How do I download the whole codebase to my computer so I can edit it?

**Create a local copy of a remote repository and its history**·Clone downloads a repository, creates a working directory, and configures the original location as a remote. It is normally the first step when joining an existing project. Check the destination path and repository source before running it.

Know first

[Terminal](/en/terminal)[Git](/en/git)

**Remote repository**Files and commit history

Create a local copyclone*→*

**New local repository**Ready to work on your computer

git clone <repository-url>

Clone creates a new local repository from a remote repository, including its files, branches, and commit history. After cloning once, use pull to bring later remote commits into that local repository.

### When to use it

- Start work on an existing repository

  <> Code ▾https://github.com/oil-oil/my-first-page.git📋Use the green Code button to copy the HTTPS address
- Download a full project history

  **$** **git log --oneline**e7b2d48 Fix button misalignment on mobilea3f9c21 Finish the home-page navigation0f1e2d3 Initialize project
- Create a fresh local working copy

  First clone of the full repository→Then pull incremental updates
- Set up the default remote automatically

  ⑂ Fork→Create a repository copy under your account

  Fork copies on the hosting platform; clone downloads locally

### When NOT to use it

- Clone into a directory that already contains important files

  Download ZIP→git log cannot run

  A ZIP includes working files, not the .git directory or commit history
- Download code from an untrusted source and run it immediately

  **$** **git push**remote: Permission to oil-oil/my-first-page.git denied.
- Clone again every time the remote changes

  📁 my-first-page  
  📁 my-first-page-2  
  📁 my-first-page-latestAfter three clones, it is hard to tell which folder is current
- Assume private dependencies and environment settings are included

  **$** **npm run dev**Error: Cannot find module 'react'

Anatomy

https://github.com/maya-lee/my-first-page.git

1HTTPSAn HTTPS URL works without setting up an SSH key first.

2HostThe Git hosting service, such as GitHub or Gitee

3OwnerThe repository owner; after a fork, this segment becomes your account name

4RepositoryThe repository name, which also becomes the local folder name by default

Variants

git clone

git clone https://github.com/maya-lee/my-first-page.git

Download working files, repository metadata, and reachable commit history

clone + 名字

git clone <address> my-app

Want to change the name of the local folder

Download ZIP

Code ▾ → Download ZIP

When you only need working files and no Git history

Fork

Upper right of the webpage ⑂ Fork

When you need to create a remote copy under your own account

Typical use cases

Join a project

my-first-page
<> Code ▾

HTTPSSSHGitHub CLI

https://github.com/maya-lee/my-first-page.git
📋 Copy URL

Set up a new computer

zsh — ~/projects

**$** **git clone https://github.com/maya-lee/my-first-page.git**
Cloning into 'my-first-page'...
remote: Enumerating objects: 36, done.
remote: Counting objects: 100% (36/36), done.
Receiving objects: 100% (36/36), 12.4 KiB | 2.1 MiB/s, done.
Created a local repository at ~/projects/my-first-page

Review an open-source repository

zsh — my-first-page

**$** **git log --oneline**
e7b2d48 Fix button alignment on mobile
a3f9c21 Finish the home-page navigation
b4c5d67 Home page basic version
0f1e2d3 Initialize project
After cloning, use git log to view the commit history

Create a clean working copy

maya-lee / my-first-page
⑂ Fork **12**

⑂

xiaoli / my-first-page

forked from maya-lee/my-first-page

A fork is a separate repository under your account. Clone the fork locally before working on it and pushing commits to it.

Further reading

[Git - git-clone Documentationgit-scm ↗](https://git-scm.com/docs/git-clone)
