---
type: web_source
source_url: "https://vibe-hub.org/en/tree-select"
title: "TreeSelect"
language: en
category: "tree-select"
fetched_at: 2026-07-27T10:04:46+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←CascaderDatePicker→

# TreeSelect

You might say

The options are nested, so people need to expand a level before choosing from it.

**Choose one or more items from a hierarchy**·A tree selector fits departments, categories, and permission scopes with parent-child relationships. Explain whether selecting a parent includes its children, what a partial selection means, and which level is actually submitted.

Know first

[Tree](/en/tree)[Checkbox](/en/checkbox)

R&D DepartmentFront-end group

*▾*R&D Department

Front-end group

Backend Group

Server

*▸*Design Department

### When to use it

- Department selection

  Engineering ×2

  ☑ Engineering☑ Frontend☐ Backend☐ Design
- Nested categories

  ☑ Apparel☑ Men’s clothing☑ Shirts☐ Electronics☑ Home

  Three categories selected across unrelated departments
- Permission scope

  ☑ Engineering→ Automatically includes the whole branch

  Engineering ×Frontend ×Backend ×
- Choose across several hierarchy branches

  FrontendEngineering / **Frontend**TeamDesign / **Frontend**Experience

### When NOT to use it

- Force flat data into a tree

  Province / City / DistrictGuangdong ProvinceShenzhenNanshan District
- Hide the meaning of partial selection

  FrontendBackendDesign
- Load a huge tree without search or lazy loading

  ▾Engineering

  ▸Frontend

  You only want to view the org chart, but you’re forced to select something
- Submit a different level from the one the user sees

  ▾ BeijingShanghaiGuangzhou

  Cities have no parent-child relationship; this hierarchy is artificial

Anatomy

R&D*▾*R&D DepartmentFront-end group

1TriggerShows selected nodes as labels

2Tree PanelOverlay showing full tree options

3Parent NodeCan expand and collapse. Selecting a parent usually affects its children.

4CheckboxMarks selected items; “partially selected” means only some child items are selected

5Child NodeIndent one level to reflect affiliation

Variants

Single

*▾*R&D Department

Front-end group

Back-end group

Used when selecting only one node in hierarchical data

Multiple

R&D department

Front-end group

Backend Group

When users need to select several nodes across branches.

Cascade Check

*▾*R&D Department

Front-end group

Backend Group

When selecting a parent should select its entire branch.

Searchable

R&D Department / **Front-End** Group

Design Department / **Front-End** Experience Group

When the tree is large, let users search for the target node first.

Typical use cases

Team directory

**Role: Operations Specialist**

Viewable data range

R&D Department ×Front-End Group ×

Save permissions

*▾*R&D Department

Front-end group

Backend Group

*▸*Design Department

Category assignment

Share "Q3 Planning Document"

Who can see

R&D Department ×Marketing Department ×

Access control

**Content data**Apparel ×Home ×

*▾*Apparel

Men's clothing

Women's clothing

*▸*Home

Folder picker

Add reviewer

![](/assets/avatar-fox.png)Alex ChenSelected
![](/assets/avatar-robot.png)AjiSelected

*▾*R&D Department

Alex Chen

Aji

Wang Dali

Further reading

[Tree View PatternWAI-ARIA APG ↗](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)
