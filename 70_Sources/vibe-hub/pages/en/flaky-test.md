---
type: web_source
source_url: "https://vibe-hub.org/en/flaky-test"
title: "Flaky Test"
language: en
category: "flaky-test"
fetched_at: 2026-07-27T10:05:34+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Test Data and FixtureAcceptance Criteria→

# Flaky Test

You might say

Run the same commit five times: it sometimes passes and sometimes times out. Check waiting conditions and shared accounts first; do not hide red with endless retries.

**A flaky test sometimes passes and sometimes fails when the code has not changed.**·The same CI commit can time out occasionally, or parallel tests can race for one account and alternate red and green. Unlike a defect that fails every time, flakiness makes the result untrustworthy. Retries can collect clues or temporarily reduce impact, but do not replace finding timing, shared-state, or environment causes.

Know first

[Test Case](/en/test-case)

*Flaky Test*

Further reading

[ISTQB GlossaryISTQB ↗](https://glossary.istqb.org/)[Playwright testing and fixturesPlaywright ↗](https://playwright.dev/docs/intro)
