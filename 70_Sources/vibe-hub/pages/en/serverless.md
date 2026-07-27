---
type: web_source
source_url: "https://vibe-hub.org/en/serverless"
title: "Serverless"
language: en
category: "serverless"
fetched_at: 2026-07-27T10:05:42+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Feature FlagServer Logs→

# Serverless

You might say

I only have a small feature. Is there a way to run code on demand without buying or managing a server?

**Run backend code on demand without managing a long-running server**·A serverless function is deployed to a managed platform and starts when an HTTP request, schedule, or event triggers it. It reduces server operations for small independent tasks, but runtime limits, cold starts, regions, and stateless execution still shape the design.

Know first

[Backend](/en/backend)[Env Var](/en/env-var)[Deployment](/en/deployment)

Request**POST /api/contact**

*→*

**⚡ Function**Platform starts on demand

*→*

Response**200 OK**

The instance is 0 when there are no requests · Billed by the number of runs

### When to use it

- Small API endpoint

  Good for short, event-driven tasks

  HTTP**Submit form**Webhook**Payment webhook**Cron**Daily summary**
- Webhook handler

  Deploy frontend and functions together

  git push→Build page + API→Get a URL

  The platform can host the runtime, but you still manage configuration, monitoring, and cost.
- Scheduled task

  Keep state in an external service

  Request→Short-lived function→Database / storage
- Event-driven processing with irregular traffic

  Put secrets in platform settings

  Environment variables**AI\_API\_KEY = ••••••••**Git repository**No secrets included**

### When NOT to use it

- Keep important state only in function memory

  Task exceeds the function time limit

  Video transcoding**Estimated 10 minutes**
  *→*
  Function limit**Times out after 10 seconds**
- Run a long job beyond the platform limit

  The next request may use a different instance

  Instance A memory**count = 8**
  *→*
  Instance B memory**count = 0**

  Data that must persist should go into a database or cache.
- Assume there is no infrastructure or cost to manage

  Check platform limits before launch

  Timeout**10s**Region**sin1**Concurrency**100**Calls this month**82%**
- Split a simple workflow into too many tiny functions

  Business logic is wrapped in platform APIs

  vercel.only.doBusinessRule()cloudflare.only.saveOrder()

  Too many platform-specific APIs raise the cost of migrating or refactoring core rules.

Anatomy

API gateway→Function instance→External status

1GatewayThe platform handles URLs, HTTPS, scaling, and request routing.

2FunctionYour code runs when a request or event arrives.

3External StatePersistent state lives in databases or storage, not function memory.

Typical use cases

Contact form API

Next.js API Route**Deploys with the frontend project**

git push→Platform build→/api/contact available

Depends on the repository branch and deployment settings

Payment webhook

Contact form**Request one email at a time**

Email**oil@example.com**Leave a message**Want to know about the team plan**Send

Function result**Email sent**

Scheduled email

Payment callback**Update orders after receiving platform events**

payment.succeeded→Verify signature→Order changed to paid

should be designed to be idempotent to avoid repeated accounting for the same callback

Image processing trigger

Scheduled tasks**Automatically perform a summary every day**

Schedule**Every day at 09:00**Action**Generate yesterday's data**Recent run**✓ 12.4s**
