---
type: web_source
source_url: "https://vibe-hub.org/en/table"
title: "Table"
language: en
category: "table"
fetched_at: 2026-07-27T10:04:49+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←ChartList→

# Table

You might say

This order data is a mess. Lay it out in a table with one order per row.

**Compare many records across the same columns**·Tables suit orders, members, inventory, and other records that share the same fields. Sorting, filtering, and pagination each need deliberate behavior. When there are many columns, plan for smaller screens, horizontal scrolling, and clear header relationships.

ProjectStatusLast updated ↓

Website refreshIn progressJust now

Annual report designCompletedYesterday

Payment flow rebuildOverdue3 days ago

### When to use it

- Compare records field by field

  TasksStatus

  Sign-in pageIn progress

  Payment flowCompleted
- Sort and filter structured data

  NamePrice ↑Stock

  Keyboard¥ 99210

  Mouse¥ 19986
- Select several rows for a bulk action

  ProjectsStatusActions

  Website redesignIn progressEdit Delete

  Annual report designCompletedEdit Delete
- Review dense operational information

  *🔍 Search usernames*Create user

  Alex ChenAdmin

  Maya LeeMembers

### When NOT to use it

- Use a table for content that has no shared columns

  FieldValue

  Versionv2.4.0

  With one row of data, the header outweighs the content
- Put every possible field on screen at once

  New product launch

  Images and paragraphs crammed into cells become distorted
- Show too many columns unchanged on a narrow phone

  ProjectsStatusOwnerTimeActionsToo many columns force constant horizontal scrolling on mobile
- Use a tree when the task is really comparing several fields

  NameSize

  src/—

  components/—

  Indentation alone makes parent-child relationships unclear

Anatomy

ProjectStatusOwner

Website refreshIn progressAlex Chen

1TableThe entire table: a header + several data rows

2HeaderExplains each column; sort controls usually go here too

3RowOne row per record

4CellThe smallest unit where a row and column meet; keep its content concise

Variants

Basic

NameInventory

Keyboard210

Mouse86

Use this for a modest amount of data with no special requirements

Striped

NameInventory

Keyboard210

Mouse86

When there are many rows, use stripes to help differentiate between adjacent rows

Compact

NameInventory

Keyboard210

Mouse86

Display42

For dense admin tables that fit more rows on screen

Sortable

NamePrice ↑

Keyboard¥99

Mouse¥199

When people need to sort by a column to find an item quickly

Typical use cases

Order management

Export
＋New user

UserRoleStatus

Alex ChenAdministratorActive

Maya LeeMemberDisabled

Member list

AllPending paymentPending shipmentCompleted

Order numberProductAmountStatus

2026071801Wireless headphones¥ 299.00Pending payment

2026071796Mechanical keyboard¥ 199.00To be shipped

Inventory

**July Sales Report**
Export to Excel

WeeklySales ↓Number of ordersChange

Week 29¥ 286,4003,146↑ 12.5%

Week 28¥ 254,6002,903↓ 3.2%

Analytics report

**Activity log**

All activity

All activity*✓*
Created*✓*
Updated*✓*
Deleted*✓*

TimeTeam memberActivity

14:32:05Alex ChenPublished "Website Refresh v2"

14:28:41Maya LeeDeleted "Old Homepage.sketch"

13:56:12KKUpdated member permissions

Further reading

[<table>: The Table elementMDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)[Table PatternWAI-ARIA APG ↗](https://www.w3.org/WAI/ARIA/apg/patterns/table/)
