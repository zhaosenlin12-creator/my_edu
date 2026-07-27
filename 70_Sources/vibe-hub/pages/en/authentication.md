---
type: web_source
source_url: "https://vibe-hub.org/en/authentication"
title: "Authentication"
language: en
category: "authentication"
fetched_at: 2026-07-27T10:05:41+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←AuthorizationAuthorization→

# Authentication

You might say

How do I verify that someone is who they say they are? I need to add sign-in.

**Verify who is making the request**·Authentication proves an identity through a password, passkey, one-time code, or trusted provider and then maintains a session. Store credentials safely, limit repeated attempts, and protect recovery paths. After identity is known, authorization still decides what that person may do.

Know first

[Route & Endpoint](/en/route)[Database](/en/database)[Env Var](/en/env-var)

Email**you@example.com**
Password**••••••••**
Login

Prove identity*→*Server verification*→*Login status

### When to use it

- Sign a user in

  A mature solution provides common authentication capabilities.

  Password / verification code→Identity service→Secure session
- Maintain a secure session

  Common protections for login cookies

  HttpOnly**Scripts cannot read it**Secure**HTTPS only**SameSite**Limit cross-site sending**
- Verify a sensitive action again

  Failure messages do not reveal account status

  Not recommended**That email does not exist**
  *→*
  Recommended**Incorrect account or password**
- Recover account access through a controlled process

  Signing out must actually invalidate credentials.

  Session valid→Server revokes it→Request again: 401

### When NOT to use it

- Store plain-text passwords

  Passwords cannot be stored in plain text.

  email: oil@example.compassword: **123456**

  If the database leaks, plaintext passwords are exposed immediately.
- Treat a user ID sent by the browser as proof of identity

  JWT contents can usually be decoded and viewed.

  header.payload.signaturepayload: { "email": "oil@example.com" }

  Do not put sensitive information such as passwords or tokens in it.
- Use long-lived tokens with no revocation plan

  Changing a local variable does not prove identity.

  Console change**isLoggedIn = true**
  *→*
  Server check**No valid session · 401**
- Reveal whether a private account exists through detailed errors

  Login endpoint without rate limiting

  1 minute**10,000 attempts**Result**Password guessing can continue**

Anatomy

Identity credentials*→*Server verification*→*Login status

1CredentialPassword, one-time verification code or identity result returned by third-party platform

2VerificationThe server checks the credentials, speed limit and handles the failure. It does not believe that the front end announces that the login is successful.

3SessionUse secure cookies or protected tokens to allow subsequent requests to prove it is the same user

Variants

Cookie Session

`Set-Cookie: session=…`

Common for web apps; browsers send the cookie automatically.

Bearer Token

`Authorization: Bearer …`

Common for mobile apps and standalone APIs.

OAuth Login

Continue with GitHub

Delegate identity proof to a trusted provider.

Typical use cases

Sign in

Email password**Establish login status after successful verification**

Email**oil@example.com**Password**••••••••**Login

Session**✓ Established**

Passkey

One-time verification code**The verification code is only valid for a short period of time**

6-digit verification code**482 913**

Remaining time**04:32**Number of attempts**1 / 5**

Verification

One-time code

Third-party login**Leave identity verification to a mature platform**

Continue using GitHubContinue using Google

The platform returns the identity result, and this site then creates its own session

Account recovery

Exit and expiration**Re-authentication is required after the session expires**

Click to exit→Server-side revoke Session→Protected request → 401

Further reading

[HTTP authenticationMDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)[Sign-in form best practicesweb.dev ↗](https://web.dev/articles/sign-in-form-best-practices)[Authentication Cheat SheetOWASP ↗](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)[Password Storage Cheat SheetOWASP ↗](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
