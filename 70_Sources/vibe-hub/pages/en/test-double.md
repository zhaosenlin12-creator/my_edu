---
type: web_source
source_url: "https://vibe-hub.org/en/test-double"
title: "Test Double"
language: en
category: "test-double"
fetched_at: 2026-07-27T10:05:33+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Test CoverageTest Data and Fixture→

# Test Double

You might say

When testing an order failure message, use a controllable payment test double that returns “payment rejected” instead of depending on the real payment service every time.

**A test double is a controllable object that replaces a real dependency during testing.**·When an order module requests payment, a double can reliably return success, rejection, or timeout so tests verify how the page handles each. Mock, stub, fake, and spy can be different kinds of test double; not every double is simply a Mock, and it cannot prove a real service is connected.

Know first

[Unit Test](/en/unit-test)[API](/en/api)

*Test Double**Mock**Stub**Fake**Spy*

Further reading

[ISTQB GlossaryISTQB ↗](https://glossary.istqb.org/)[Jest Mock FunctionsJest ↗](https://jestjs.io/docs/mock-functions)
