---
type: web_source
source_url: "https://vibe-hub.org/en/sidebar-layout"
title: "Sidebar"
language: en
category: "sidebar-layout"
fetched_at: 2026-07-27T10:05:17+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Top NavSingle Page→

# Sidebar

You might say

Put the feature menu in a left sidebar and show the content in a big area on the right, like an admin dashboard.

**Keep navigation in a vertical column beside the content**·A sidebar suits products with many sections, grouped tools, or workspaces that users switch between often. Give the content enough room and provide a compact or temporary version on smaller screens. Do not make every nested level visible at once.

Know first

[Menu](/en/menu)

**Navigation**

Top barContent area

### When to use it

- Admin system

  DashboardProjectsMembersSettings
- Workspace product

  →
- Many grouped destinations

  flex: 1 · takes the remaining width
- Navigation that needs labels and icons

  HomeComponentsTemplatesSettings

### When NOT to use it

- Use a wide permanent sidebar on a narrow screen

  AnnouncementAd
- Expand every nested group by default

  width: 960px
- Mix page navigation with unrelated content

  Keeping a full-width sidebar on mobile leaves too little width for the body.
- Leave too little width for the main task

  ▾Expand all

  ▾Node

  Child node

  ▾Node

  Child node

  With everything expanded by default, relationships are hard to scan

Anatomy

**Navigation**Top bar · Breadcrumbs / Search / AvatarContent area · flex: 1

1SidebarHosts hierarchical navigation, which can be set to a fixed width or collapsed state

2HeaderBreadcrumbs, search, location of user avatar

3MainTables, forms and other work content can expand and contract with the sidebar

Variants

Fixed

By default in the background, the navigation is always on the left side

Collapsible

When content needs more horizontal space

Drawer

On mobile, click the hamburger button to slide out

Typical use cases

Admin dashboard

**Shop backstage**
📊 Dashboard
🧾 Order Management
📦 Product Library
👥 Customer
⚙️ Settings

**Order management**
＋ Create new order

#20260721-018 · Lin Xiaoman¥ 239.00Shipping

#20260721-017 · Chen Mo¥ 88.00Pending payment

#20260720-132 · Ah Li¥ 459.00Completed

Team workspace

**Data dashboard**
📈 Overview
🌐 Traffic Source
🔻 Conversion Funnel
🔁 User retention
📑 Report Center

Visit today

12,847

New user

1,203

Conversion rate

3.2%

Email client

**Cloud console**
🖥 Production environment
🧪 Pre-release environment
🚀 Deployment record
🔔 Monitoring Alarm
🔑 Access Key

**server-prod-01**
Running

➜ vibekit deploy --prod

Build completed · 34 files · 2.1s

✓ is online at https://app.example.com

Analytics product

**Work Hub**
📮 Inbox **3**
📅 Calendar
✅ Tasks
☁️ Drive
📝 Notes

**Inbox**

![](/assets/avatar-fox.png)

Lin Xiaoman

I reviewed the plan. Two changes and it’s ready to publish.

10:24

![](/assets/avatar-robot.png)

GitHub

[vibe-ui] PR #48 was approved

09:51

![](/assets/avatar-fox.png)

Chen Mo

I’ll send the materials for Friday’s review shortly.

Yesterday
