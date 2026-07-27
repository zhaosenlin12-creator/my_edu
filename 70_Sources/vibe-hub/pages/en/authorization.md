---
type: web_source
source_url: "https://vibe-hub.org/en/authorization"
title: "Authorization"
language: en
category: "authorization"
fetched_at: 2026-07-27T10:05:42+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←AuthenticationAuthentication→

# Authorization

You might say

After people sign in, I still need different access levels for admins and regular users.

**Decide what an authenticated user is allowed to see or change**·Authorization checks permissions for each resource and action after the user's identity is known. A person may view one project but not another, or edit content without managing billing. Enforce the rule on the backend for every request, not only by hiding controls in the interface.

Know first

[Authentication](/en/authentication)[Database](/en/database)

Current User**Member · Xiaolin**

View items*Allow*

Edit own tasks*Allow*

Delete other people's tasks*Reject*

Manage all accounts*Reject*

### When to use it

- Check record ownership

  Every sensitive action goes through an authorization check.

  Current user→Authorization rule→Allow / deny
- Apply roles and permissions

  Beyond roles, check the relationship to the resource.

  Current user**u\_23**Post author**u\_23**Result**Edit allowed**
- Limit access by workspace or organization

  Deny by default; allow as needed

  Default**DENY**Explicitly allow**viewer → read**
- Protect administrative and billing actions

  Record administrative actions

  16:42 · admin\_u7disabled user\_u23reason: repeated abuse

### When NOT to use it

- Rely on hidden buttons as access control

  Hiding a button does not secure the endpoint.

  Page**No delete button**
  *→*
  Direct request**DELETE /users/42 → 204**
- Check a role but ignore which record is being accessed

  An identity claimed by the frontend can be forged.

  POST /api/admin/delete{ "userId": "u\_23", **"role": "admin"** }
- Grant broad administrator access for convenience

  Signing in does not mean you can view all data.

  Signed in→Access someone else's bill→Should be 403
- Cache permissions without handling changes and revocation

  The same rule is scattered across several places

  users.ts**Check admin**orders.ts**Forgot to check**reports.ts**Different rule**

Anatomy

whocanwhatacts onwhich resource

1SubjectCurrently authenticated users, along with roles and memberships in trusted sources

2ActionThe ability to read, edit, delete, approve, etc. requires judgment on an item-by-item basis

3ResourceTarget record, project or file; also check who owns it and which organization it belongs to

Variants

Role-based

viewer · editor · admin

Simple systems with clear roles.

Ownership

post.userId === me.id

Users may only operate on their own data.

Membership

project\_members

Team and collaboration products.

Typical use cases

Project access

Personal data**Judge editing permissions based on resource ownership**

Current user**u\_23**Profile owner**u\_23**Results**Allow editing**

Team roles

Project members**Membership determines viewing permissions**

Project**VibeHub**User role**viewer**Permissions**Viewable · Cannot be deleted**

Admin settings

Administrator operations**Block accounts and leave audit records**

Target account**user\_42**Reason**Repeated abuse**

Confirm ban

Record admin\_u7 · 16:42 · disable user\_42

Billing permission

Paid function**Subscription status is confirmed by the server**

Current Plan**Free**
*→*
Export HD files**Requires Pro**

Hiding a control is not enough; the server must still check subscription access

Further reading

[Authorization Cheat SheetOWASP ↗](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
