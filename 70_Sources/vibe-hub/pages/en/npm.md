---
type: web_source
source_url: "https://vibe-hub.org/en/npm"
title: "npm"
language: en
category: "npm"
fetched_at: 2026-07-27T10:05:28+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←TerminalBuild→

# npm

You might say

AI told me to install dependencies, and one command downloaded a ton of stuff. What's going on?

**Install JavaScript packages and run project scripts**·npm is a package manager and command runner for JavaScript projects. package.json records dependencies and named scripts, while the lockfile keeps installed versions reproducible. Install packages intentionally and review scripts before running code from an unfamiliar project.

Know first

[Terminal](/en/terminal)

package.json · Manifest
**"react"**: "^19.0.0"
**"vite"**: "^6.0.0"
**"scripts"**: dev / build

npm  
install  
→

node\_modules · Dependency directory
📦 react
📦 vite
📦…42 packages in total

### When to use it

- Install declared dependencies

  package.json  
  **"dependencies"**: react, vite  
  **"scripts"**: dev, buildManifest: which packages are installed and which commands can run
- Add a library to a project

  **$** **npm install**⸨░░░░░░⸩ idealTreeadded 42 packages in 6s
- Run scripts such as dev, test, and build

  **$** **npm run dev**> vite✓ Ready in 1.2s
- Keep dependency versions reproducible with a lockfile

  ☁️ Clone project→ install →📦 Rebuild from the repository

### When NOT to use it

- Commit the node\_modules directory

  📁 node\_modules / react✎ Edit manually

  When dependencies are reinstalled, local changes like these are usually replaced.
- Delete the lockfile whenever versions conflict

  node\_modules 380MBgit push →

  A large number of reinstallable dependencies entered the repository; .gitignore should exclude them.
- Install a package before checking whether the platform already provides the feature

  📄 package.json🗑

  Dependency and script declarations are missing, so other environments cannot rebuild from the project configuration.
- Run an unfamiliar package script without reading it

  dependencies:  
  react, vue, jquery, lodash, moment, axios, fetch-huh…Adding dependencies before finding the cause broadens the conflict and maintenance surface.

Anatomy

{
  **"name"**: "my-first-page",
  **"dependencies"**: { "react": "^19.0.0" },
  **"scripts"**: { "dev": "vite", "build": "vite build" }
}

1nameThe name and version of the project, used when publishing and sharing

2dependenciesWhich packages and versions are installed; install and move the goods accordingly.

3scriptsnpm run dev runs the command written here

Variants

install

npm install

Install new packages, or rebuild node\_modules

run

npm run dev

Execute shortcut commands in scripts

uninstall

npm uninstall lodash

The bag is no longer needed, so cross it off the list.

lockfile

package-lock.json

Team unified version, don’t change it manually

Typical use cases

Project setup

package.json

{  
  "name": "my-first-page",  
  "dependencies": { "react": "^19.0.0" },  
  "scripts": { "dev": "vite", "build": "vite build" }  
}

Add dependency

zsh — my-first-page

**$** **npm install**
⸨████████░░⸩ reify: react
added 42 packages in 6s
Dependencies will be installed to node\_modules according to package.json and lock files

Development server

my-first-page

📁 node\_modules380 MB · ⚠ Automatically generated, do not move

📄 package.jsonEvents

📄 .gitignoreIt says node\_modules and .env

Production build

zsh — my-first-page

**$** **npm run dev**
> my-first-page@0.1.0 dev
✓ Ready in 1.2s → http://localhost:3000
Shortcut commands in scripts, one for each string

Further reading

[Package management basicsMDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_tools/Package_management)
