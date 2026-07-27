---
type: web_source
source_url: "https://vibe-hub.org/en/route"
title: "Route & Endpoint"
language: en
category: "route"
fetched_at: 2026-07-27T10:05:41+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Backend FrameworkBackend→

# Route & Endpoint

You might say

When people visit different URLs, how do I send each one to the right code?

**Match a request path and method to the code that handles it**·A backend route, or endpoint, defines where a request goes and which methods it accepts. For example, GET /products may read products while POST /products creates one. Validate input, check access, return meaningful status codes, and keep unrelated operations separate.

Know first

[Backend](/en/backend)[HTTP](/en/http)[API](/en/api)

**GET**`/api/posts`→ List processing

**POST**`/api/posts`→ Create processing

**GET**`/api/posts/:id`→ Details processing

Method and path together determine which code to enter

### When to use it

- Read a collection or record

  The method describes the action; the path identifies the resource.

  Read user**GET /users**Create user**POST /users**
- Create, update, or delete data

  Put the three parameter types in different places

  Path**/users/42**Query**?tab=orders**Request body**{ "name": "Jordan" }**
- Receive a form or webhook

  Every endpoint should define four things

  Input**email**Success**201**Failed**400 / 409**Permission**Sign-in required**
- Expose one clear backend capability

  Test the endpoint by itself first

  curl -X POST /api/orders**201 Created**{ "orderId": "o\_42" }

### When NOT to use it

- Use one endpoint for many unrelated operations

  One endpoint handles everything

  POST /api/doEverything{ "action": "maybe-save-or-delete" }

  The endpoint name does not clearly express whether it reads, updates, or deletes.
- Change data through a read-only method

  Method and action conflict

  Delete**GET /delete/42**Read**POST /getUser**
- Return private records without authorization

  Design only the success path

  200 success→500 failure→No recovery guidance

  Missing parameters and service failures also need clear responses.
- Hide every failure behind the same generic response

  Sensitive information appears in the URL

  GET /report?**api\_key=sk-live-••••***Browser history · access logs · shared screenshots*

Anatomy

GET/api/posts?page=2

1MethodGET reads, POST creates, PATCH updates, and DELETE removes.

2PathThe resource address, usually a consistent noun.

3QueryUsed for filtering, search, sort, and pagination—not secrets.

Typical use cases

List products

Post list**GET /api/posts**

Request parameters**?page=2&tag=design**
*→*
Responses**200 · 20 articles**

Create account

Submit login**POST /api/login**

Email**oil@example.com**Password**••••••••**Login

The request body carries account information, and the session is established after success

Update profile

User details**GET /api/users/:id**

Path parameter**id = u\_23**Name**Alex Chen**Role**editor**

Receive webhook

Delete tasks**DELETE /api/tasks/:id**

Task**Organize homepage copy**After deletion**Process according to product strategy**

Confirm deletion

Confirm first, then request DELETE /api/tasks/t\_42

Further reading

[HTTP request methodsMDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)[An overview of HTTPMDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
