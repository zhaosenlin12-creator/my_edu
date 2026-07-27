---
type: web_source
source_url: "https://vibe-hub.org/en/url"
title: "URL"
language: en
category: "url"
fetched_at: 2026-07-27T10:05:19+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←DNSHTTP→

# URL

You might say

What's that long string in the address bar? I want every page to have its own permanent address.

**Describe the exact location of a resource on the web**·A URL contains pieces such as protocol, domain, path, query, and fragment. Together they identify a page or resource and may carry filters or an anchor. Keep public URLs readable and stable, and never place passwords or secrets in them.

Know first

[Domain](/en/domain)

https://vibeui.dev/components/button?tab=demo#anatomy

ProtocolDomain namePathParametersAnchor

### When to use it

- Open a specific page

  https://vibe-ui.dev/x/8fk2Copy

  Copied
- Represent a stable resource path

  vibeui.dev/components/buttonA path locates a resource or page within a site.
- Carry non-secret search or filter parameters

  /search?q=button&sort=hotQuery parameters preserve filters or page state in a link.
- Jump to a section with a fragment

  /button#anatomyA fragment identifier can jump to a specific place on the page.

### When NOT to use it

- Put passwords, tokens, or personal secrets in the URL

  ?token=sk-live-8f2k…Links can end up in history, logs, and forwarding records, so they must not contain secrets.
- Change public paths without redirects

  /search?q=my pageSpaces and other characters must be encoded according to URL rules.
- Use an unreadable path when a clear one is possible

  vibeui.devOnly the domain was copied, so the recipient opens the home page.
- Treat query parameters as trusted data

  /pay#amount=999Content after # is not sent to the server.

Anatomy

https://vibeui.dev/components/button?tab=demo#anatomy

1Protocolhttps:// identifies the protocol used to access the resource; see https.

2DomainThe domain identifies the host, and dns resolves it to an IP address.

3PathThe path identifies a resource on that host; /components/button points to one page.

4QueryThe query string starts with ? and sends key=value parameters; & separates multiple parameters.

5HashThe fragment starts with # and points to a location on the page. The browser handles it without sending it to the server.

Variants

Absolute URL

https://vibeui.dev/components/button

Contains protocol and domain name, suitable for external sharing or cross-site reference

Relative Path

/components/button

Jump within the site, no need to change domain name

Anchor Link

#anatomy

Only locate a section of the current page

Typical use cases

Page address

🔒
https://**vibeui.dev**/components/button

Buttons and basic styles

Button

Leave the most important action on the page to the button

Primary buttonSecondary button

Search results

🔍
Button

vibeui.dev/search?q=Button&cat=General

3 related entries found

**Button**

Submit the form, trigger actions, confirm dangerous operations...

**Switch**

Switch with immediate effect...

Shared filter

Share this entry

https://vibeui.dev/components/button#anatomy

Generate poster
Copy link

✓ Copied to clipboard

Section link

Directory of this page

When to use

Scene

Composition structure

Variation

/components/button#anatomy

**Composition structure · Anatomy**

Further reading

[What is a URL?MDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)
