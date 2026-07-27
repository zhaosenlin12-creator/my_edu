---
type: web_source
source_url: "https://vibe-hub.org/en/cdn"
title: "CDN"
language: en
category: "cdn"
fetched_at: 2026-07-27T10:05:21+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←HTTPSPort→

# CDN

You might say

People far away say the images load slowly. Can they download them from somewhere closer?

**Serve static files from locations closer to visitors**·A content delivery network caches images, scripts, styles, and sometimes pages across many edge locations. It can reduce latency and protect the origin from repeated traffic. Plan cache rules and invalidation so visitors do not receive outdated files.

Know first

[Domain](/en/domain)[DNS](/en/dns)

🖥️OriginOriginal file

→

📍 Hong Kong node (copy) 18ms

📍 Frankfurt node (copy) 22ms

📍 Los Angeles node (copy) 26ms

### When to use it

- Deliver images and static assets

  logo.pngCDN

  app.jsCDN

  A CDN can cache and distribute static assets.
- Reduce latency across regions

  Deployment successful; distributed to global edge locations.
- Cache public files with stable versions

  Shenzhen userHong Kong edge · 18ms

  Berlin userFrankfurt · 22ms
- Absorb repeated requests before they reach the origin

  logo.png updatedRefresh cache

  After a purge, edge nodes fetch the new file from origin.

### When NOT to use it

- Cache private or personalized responses as public

  Berlin userDirect to origin · 380ms

  When users are far from the origin, asset-transfer latency increases.
- Change a file without updating or invalidating its cache

  logo.pngCached for 30 days

  Without versioning or a refresh strategy, users may keep seeing old assets.
- Assume a CDN fixes slow application logic

  /api/balanceCached for 1 hour

  Private dynamic data such as account balances needs strict caching rules and authorization isolation.
- Ignore cost and regional requirements

  index.htmlCached for 1 year

  With an overly long cache period and no update strategy, users may keep seeing an old version.

Anatomy

🖥️Origin→📍 Hong Kong node 18ms📍 Frankfurt node 22msCache for 30 days

1OriginThe origin is contacted only when an edge node does not have the requested file.

2Edge NodeAn edge location near the user that caches files and serves them directly

3CacheHow long an edge node keeps a cached file before fetching a fresh copy from the origin

Variants

Static Assets

cdn.vibeui.dev/logo.png

Images, JS, CSS are sent to edge nodes

Full Site

vibeui.dev Edge

HTML also uses nodes, and dynamic parts return to the source

OSS + CDN

uploads.vibeui.dev/u/8f2k.jpg

Images uploaded by users are also sent to CDN

Typical use cases

Image delivery

🚀

Deployed successfully

vibeui.dev updated in 38 seconds

✓ Distributed to 26 edge nodes

Static resources are accelerated by global CDN, and the HTTPS certificate has been automatically renewed

JavaScript assets

**Edge node · Real-time delay**

📍 Hong Kong
Services: Shenzhen, Guangzhou
18ms

📍 Frankfurt
Services: Berlin, Paris
22ms

📍 Los Angeles
Services: San Francisco, Seattle
26ms

For the same batch of files, each user will fetch them from the nearest node

Global website

**CDN cache · Last 7 days**

Cache hit rate

92.4%

Back to origin request

7.6%

Save origin site bandwidth

86 GB

More than 90% of requests are resolved at the node, and the origin site has almost no pressure

Download files

Refresh cache

Let global nodes discard old files and go back to the source to get the latest version

Purge

✓ 26 nodes have been refreshed and will take effect globally in about 30 seconds

Further reading

[CDNMDN ↗](https://developer.mozilla.org/en-US/docs/Glossary/CDN)[Content delivery networks (CDNs)web.dev ↗](https://web.dev/articles/content-delivery-networks)
