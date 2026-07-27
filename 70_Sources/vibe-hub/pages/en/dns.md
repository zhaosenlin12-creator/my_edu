---
type: web_source
source_url: "https://vibe-hub.org/en/dns"
title: "DNS"
language: en
category: "dns"
fetched_at: 2026-07-27T10:05:20+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←DomainURL→

# DNS

You might say

I bought a domain, so why do I still need to set up DNS? Help me point it to my server.

**Connect a domain name to the service that should answer**·DNS translates a domain into records that direct browsers and other clients to a host, email service, or verification target. Changes may take time to spread because records are cached. Keep the required record type, name, value, and previous configuration clear before editing.

Know first

[Domain](/en/domain)

🌐BrowserSearch  
vibeui.dev

→

📒DNS ResolverReturn record  
76.223.54.1

→

🖥️Target serviceConnect to the returned  
IP address

### When to use it

- Point a domain to a website

  A@76.223.54.1

  An A record points a name to an IPv4 address.
- Configure a subdomain

  CNAMEwwwvibeui.dev

  A CNAME points one name to another domain.
- Connect email service

  TTL 600Max cache: 10 min
- Verify domain ownership

  $ dig vibeui.dev;; ANSWER: 76.223.54.1

### When NOT to use it

- Delete existing records without checking their purpose

  Awww → 76.223.54.1

  CNAMEwww → vibeui.dev

  A CNAME for the same name generally cannot coexist with an A record.
- Expect every resolver to update immediately

  Changed to AChanged backMultiple changes

  Repeated changes before the cache expires make it hard to trace issues to one configuration.
- Mix up the record name and destination

  TTL 86400Max cache: 1 day

  Old records may remain cached for a long time, so changes also take longer to converge.
- Publish private server credentials as DNS values

  A76.223.54.12

  An incorrect address can send requests to the wrong service or make the site unreachable.

Anatomy

🌐Browser→📒DNS Server→A record  
vibeui.dev → IP→76.223.54.1

1ResolverThe browser usually hands off the query to a recursive resolver; it checks the cache and, if necessary, queries the authoritative DNS

2Authoritative DNSServer that keeps official records for domain names; recursive resolvers get cacheable answers from here

3RecordThe line you registered in the console: A records the IP, CNAME records another domain name

4IP AddressThe found house number is used by the browser to knock on the server's door.

Variants

A Record

A @ → 76.223.54.1

Domain names point to IPv4 addresses, most commonly used

CNAME

CNAME www → vibeui.dev

The domain name points to another domain name, commonly used in hosting

AAAA

AAAA @ → 2606:…:1

Domain name points to IPv6 address

TXT

TXT @ → "verify=8f2k…"

Used when verifying domain name ownership and configuring email addresses

Typical use cases

Website launch

**DNS resolution · vibeui.dev**
＋Add record

TypeHost RecordRecord ValueTTL

A@76.223.54.1600

CNAMEwwwvibeui.dev600

CNAMEblogvibeui.dev600

Subdomain setup

$ dig vibeui.dev

;; QUESTION SECTION:

;vibeui.dev.   IN  A

;; ANSWER SECTION:

vibeui.dev.  600  IN  A  76.223.54.1

;; Query time: 23 msec

Email records

Modify parsing record

TypeA

Record value

TTL
Seconds; smaller TTL facilitates switching, but does not clear existing cache

Save, it will take effect in about 10 minutes

Ownership verification

Migrate to a new server

Old: A @ → 76.223.54.1Deactivated

↓ Modify record value

New: A @ → 76.223.105.8Effective

Before the end of the old record caching, some users may still access the old server; confirm that the traffic has been migrated before closing the old service.

Further reading

[DNSMDN ↗](https://developer.mozilla.org/en-US/docs/Glossary/DNS)
