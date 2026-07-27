---
type: web_source
source_url: "https://vibe-hub.org/en/terminal"
title: "Terminal"
language: en
category: "terminal"
fetched_at: 2026-07-27T10:05:28+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Lintnpm→

# Terminal

You might say

AI gave me a command to run, but I don't know what it will do. Is it safe to run?

**Run text commands in a specific folder on your computer or server**·A terminal gives you a prompt where commands can start tools, install packages, inspect files, and run a project. The current directory changes what a command affects. Read the command and confirm the path before running anything that changes or deletes files.

zsh — my-first-page

**$** **npm run dev**
> my-first-page@0.1.0 dev
✓ Ready in 1.2s
→ Local: **http://localhost:3000**
Open this address in your browser and you will be able to see your page

### When to use it

- Start a development server

  **$** **npm run dev**✓ Ready in 1.2s→ http://localhost:3000
- Install project dependencies

  **$** **ls** List the contents of the current directoryindex.html my-first-page**$** **cd my-first-page** Enter the project directory
- Run build and test commands

  ▲ Build failedError: Cannot find module 'react'at build (build.js:12)
- Inspect files, processes, and logs

  **$** **npm install**added 42 packages in 6s**$** **npm run build**✓ built in 3.2s

### When NOT to use it

- Paste a command you do not understand with elevated permission

  Error: …Error: …(multiple error messages)

  ✕
- Run project commands from an unrelated directory

  **~/Desktop $** **npm run dev**npm error: no package.json
- Share terminal output that contains secrets

  Pasting several commands at once…**npm install**Error: network timeoutIt becomes hard to tell which command caused later results.
- Use a destructive command with an unverified path or wildcard

  **$** **sudo rm -rf** …Run with elevated privileges

Anatomy

$ npm run dev
✓ Ready in 1.2s → http://localhost:3000

1PromptStarting with $ or %; the preceding path represents the current working directory

2CommandThe first word specifies an external program or shell built-in function, such as npm, cd, ls, git

3ArgumentsSupplementary information after the command, such as run dev specifies the script to be executed

4OutputResults, warnings, and errors returned by commands; first look for clues that lead to action

Variants

cd & ls

cd my-first-page  ls

Go into the project directory and list the files in it

npm run

npm run dev

Execute startup or build scripts declared in package.json

Ctrl+C

Ctrl + C

Stop a command or development service running in the foreground

clear

clear

Clear the display when there is too much content on the screen

Typical use cases

Run a project

zsh — my-first-page

**$** **npm run dev**
> my-first-page@0.1.0 dev
> vite
✓ Ready in 1.2s
→ Local: **http://localhost:3000**
The development service runs in this process; the local address will stop responding after aborting the process

Install packages

zsh — my-first-page

Failed to compile
Error: Cannot find module 'react'
 at build (vite.config.js:12)
 at processTicksAndRejections (node:internal)
↑ The error message and call stack must be judged together with the execution command

Build and test

zsh

**~/Desktop $** **ls**
Documents  Downloads  my-first-page
**~/Desktop $** **cd my-first-page**
**~/Desktop/my-first-page $** **ls**
index.html  package.json  README.md

Read logs

zsh — my-first-page

✓ Ready — http://localhost:3000
**^C**
**~/Desktop/my-first-page $** The service has stopped and the terminal returns the prompt
Ctrl + C: Abort the command running in the foreground

Further reading

[Command line crash courseMDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Environment_setup/Command_line)
