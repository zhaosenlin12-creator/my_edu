---
type: web_source
source_url: "https://vibe-hub.org/en/tree"
title: "Tree"
language: en
category: "tree"
fetched_at: 2026-07-27T10:04:54+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←TimelineCarousel→

# Tree

You might say

Make it work like folders: click the little arrow to expand the next level.

**Expand and browse data with parent-child levels**·A tree reveals folders, departments, categories, and other hierarchies by expanding and collapsing levels. It may support browsing, selection, or dragging. For permissions and selection, explain clearly how parent and child nodes affect each other.

▸Design Department

▸UI group

Alex Chen

maya-lee

▸User Research Group

Amai

▸R&D Department

Front-end group

Backend Group

### When to use it

- Folder browser

  ▾📁 Design assets

  📄 Home.sketch

  📄 Icons.sketch

  ▸📁 Asset library
- Organization chart

  ▾Level 1 category

  ▾Level 2 category

  ▾Level 3 category

  Leaf node
- Nested category list

  ▾🏢 Acme Tech

  ▾Design

  Alex Chen

  ▸Engineering
- Any data with meaningful parent-child levels

  ▾Page permissions

  View

  Edit

### When NOT to use it

- Turn a simple flat list into a tree

  Province / City / DistrictGuangdong ProvinceShenzhenNanshan District
- Open a very large tree without search or lazy loading

  Project A

  Project B

  Project C

  There’s no parent-child hierarchy, so a list is enough
- Hide the current selection when branches collapse

  ▾ Level 1▾ Level 2Level 3…Deep indentation narrows the content and truncates names
- Leave parent-child selection behavior unexplained

  ▾Expand all

  ▾Node

  Child node

  ▾Node

  Child node

  With everything expanded by default, relationships are hard to scan

Anatomy

▾Design Department▸UI Group

1TreeThe container for the whole tree

2SwitcherShown only for parent nodes; click to expand or collapse

3NodeThe node name; it can be highlighted

4ChildrenIndent one level to show the parent-child relationship

Variants

Checkable

▾Page permissions

View

Edit

To select items by hierarchy, such as when assigning permissions

ShowLine

▾Design Department

▸UI Group

▸User Research Group

When parent-child relationships need to be easier to scan

Directory

▾📁 Design resources

📄 Home.sketch

📄 icon.sketch

Use folder icons to make a file hierarchy easier to scan

Typical use cases

File browser

📁 vibe-ui-guide＋

▾📁 app

📄 globals.css

📄 page.tsx

▸📁 site

▸📁 public

Department tree

Select approver

▾🏢 XX Technology

▾Design Department

![](/assets/avatar-fox.png)Alex Chen

▸R&D Department

CancelOK

Category manager

**Role permissions · Operation**3 / 6 items selected

▾Content management

Publish article

Delete other people’s articles

▸Data dashboard

Save configuration

Permission editor

**Product Category**+ Add new category

▾Digital home appliances128 itemsEdit

Headphone Speaker46 items

Smart Wear32 items

▸Home Life96 items

Further reading

[Tree View PatternWAI-ARIA APG ↗](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)
