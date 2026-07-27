---
type: web_source
source_url: "https://vibe-hub.org/en/http"
title: "HTTP"
language: en
category: "http"
fetched_at: 2026-07-27T10:05:20+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←URLHTTPS→

# HTTP

You might say

When I click a button, what actually happens between the browser and the server?

**Send a request and receive a response over the web**·HTTP is the request-response protocol browsers and APIs use. A request includes a method, URL, headers, and sometimes a body; the response includes a status, headers, and content. Methods and status codes should match what actually happened.

Know first

[URL](/en/url)

GET - Get resources  
GET /api/components HTTP/1.1  
Host: api.vibeui.dev

POST - Submit data  
POST /api/login HTTP/1.1  
Content-Type: application/json{ "email": "you@example.com", "pwd": "••••••" }

### When to use it

- Fetch a page or resource

  🔒vibeui.dev/components

  GETPressing Enter in the address bar is a GET.
- Call an API

  you@example.com••••••••

  Sign inPOST
- Submit data to a server

  NetworkFetch/XHR

  GET/api/list200

  POST/api/save200
- Describe success, redirects, client errors, and server errors

  GETPOSTPUTDELETE

### When NOT to use it

- Use a successful status code for a failed operation

  /login?pwd=123456The password entered browser history and server logs.
- Change data with a request intended only for reading

  GET/api/list

  A GET request body has no universal meaning; do not depend on how a server handles it.
- Retry every failed request without limits

  POST/api/order ×3

  Repeated requests can create multiple orders; the server also needs idempotency keys or unique constraints as a safeguard.
- Log sensitive headers or bodies carelessly

  Changing the API format based on assumptions without checking the actual request.

Anatomy

POST /api/login HTTP/1.1  
Host: api.vibeui.dev  
Content-Type: application/json{ "email": "you@example.com", "pwd": "••••••" }

1MethodThe request method describes the action: GET, POST, PUT, PATCH, or DELETE.

2URLThe url identifies the destination; the path and query narrow down the resource.

3HeadersHeaders carry metadata such as the content type, credentials, and request origin.

4BodyThe optional body carries data, commonly with POST, PUT, or PATCH. Content-Type and the API contract define its format.

Variants

GET

GET /api/list?page=1

Obtain resources and pass query parameters in the URL according to the interface convention

POST

POST /api/login

Submit the data and put the content in the request body

PUT & PATCH

PUT /api/items/42

Update existing data, overwrite or partially change

DELETE

DELETE /api/items/7

Please be careful when deleting data.

Typical use cases

Page request

🔒
vibeui.dev/components
⏎

Network · 1 request

components
GET
200
document

API call

Login Vibe

Logging in...

Click moment → POST /api/login

Form submission

Network
Fetch/XHR

list?page=1GET20064 ms

savePOST200120 ms

items/42PUT20098 ms

items/7DELETE20475 ms

File download

$ curl -X POST https://api.vibeui.dev/login \

-H "Content-Type: application/json" \

-d '{"email":"you@example.com","pwd":"123456"}'

{ "token": "eyJhbGciOi…" }

# -X sets the method, -H adds a header, and -d sends the request body.

Further reading

[Overview of HTTPMDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
