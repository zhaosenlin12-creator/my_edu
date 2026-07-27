---
type: web_source
source_url: "https://vibe-hub.org/en/menu"
title: "Menu"
language: en
category: "menu"
fetched_at: 2026-07-27T10:05:00+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←SearchBreadcrumb→

# Menu

You might say

There are too many features now. Add a menu so people can find their way around.

**Help people move between the main sections of a product**·A menu groups destinations and makes the current location visible. Keep labels consistent, group related items, and avoid making the hierarchy deeper than the product requires. Actions such as sign out should be distinguished from navigation links.

HomeProductsDocumentationPricing

▦Dashboard
▤item
✉Message3
⚙Settings

### When to use it

- Primary product navigation

  **Home**ProductDocsPricing
- A compact group of destinations

  DashboardProjectsMembersSettings
- Nested sections with a real hierarchy

  ProjectsAll projectsAssigned to meSystemMembersSettings
- Account or workspace navigation

  OverviewDataMembers

  The highlight shows where you are

### When NOT to use it

- Mix unrelated actions and destinations without distinction

  CommentsHistorySave
- Create deep nesting for a simple site

  DashboardProjectsTasksFilesMembersCalendarReportsMessagesSettingsTrash
- Hide the active location

  SaveDeleteExport
- Rename the same destination in different menus

  HomeAbout

Anatomy

▦Dashboard3

▤item
⚙Settings

1ContainerThe whole menu — lays out the items and tracks which one is active

2MenuItemA clickable entry that navigates to its page

3IconOptional — helps users recognize the feature at a glance

4BadgeOptional — flags unread counts or fresh content

Variants

Horizontal

HomeProductsDocuments

When there are only a few navigation items and enough horizontal space for a top bar.

Vertical

▦Dashboard▤Project⚙Settings

When there are many functions that need to stay visibly grouped

Collapsed

▦▤⚙

When the content area is too narrow, collapse it to icon-only navigation.

Typical use cases

App sidebar

YunYunfan Backstage

▦ Dashboard
▤ Project Management
✉ Message Center*3*
⚙ System Settings

**Data Overview**

Visit today

12,483

New user

356

Account menu

**◆ Museon**
Homepage
Product
Documentation
Pricing

Log in
Free trial

**Make team collaboration clearer**

Workspace navigation

Development Guide

Quick Start
Installation and configuration

Core concept

Component model
Status management
Style scheme

**Installation and configuration**

npm install museon-ui

Mobile menu

**Mall homepage**

![](/assets/avatar-fox.png)**Alex Chen**

🏠 Home
🛒 My order
⭐ Favorites
⚙ Settings

Further reading

[Menu and Menubar PatternWAI-ARIA APG ↗](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/)
