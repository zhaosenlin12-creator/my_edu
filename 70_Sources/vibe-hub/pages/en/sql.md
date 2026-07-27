---
type: web_source
source_url: "https://vibe-hub.org/en/sql"
title: "SQL"
language: en
category: "sql"
fetched_at: 2026-07-27T10:05:41+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←DatabaseBrowser Storage→

# SQL

You might say

How do I write a query for users who placed an order in the last seven days?

**Ask a relational database to read or change structured records**·SQL can select, filter, join, insert, update, and delete data in relational databases. Parameterize user values instead of building query strings, and inspect indexes and execution plans when a query becomes slow. A correct query still needs authorization around it.

Know first

[Database](/en/database)

`SELECT name, city`
`FROM users`
`WHERE city = 'Shenzhen'`

Hit these lines

idnamecity

1XiaoliShenzhen

2AjiHangzhou

3Xiao LinShanghai

### When to use it

- Filter and sort records

  Learn to read data first

  Query**SELECT \* FROM users WHERE id = 42**
  *→*
  Result**42 · Jordan**
- Join related tables

  Preview the impact before deleting or changing data

  SELECT ... WHERE id=42→Confirm 1 row→DELETE
- Aggregate totals and counts

  Treat input only as data

  SELECT \* FROM users WHERE email = **$1**$1 = "oil@example.com"

  The parameter is not executed as another piece of SQL.
- Update data inside a transaction

  Give AI the table schema too

  users.id**uuid**users.email**text · unique**Output**Explain how many rows are affected**

### When NOT to use it

- Concatenate untrusted input into a query

  Deletion without WHERE

  Run**DELETE FROM users**
  *→*
  Impact**12,480 rows deleted**
- Select every column when only a few are needed

  Concatenate input directly into SQL

  email = **' OR 1=1 --**SELECT \* FROM users WHERE email = '' OR 1=1
- Run an unbounded update or delete

  Run a write operation in production without confirming the conditions

  Current environment**PRODUCTION**About to run**UPDATE users ...**

  Verify first with test data or in a transaction
- Assume a database permission replaces application authorization

  Display text cannot replace stable fields

  Store only**"Premium member"**
  *→*
  Should be**plan\_id: pro\_2026**

Anatomy

`SELECT name FROM users WHERE city = ?`

idnamecity

1MiaShenzhen

1ActionSELECT, INSERT, UPDATE or DELETE, decide whether to read or modify

2TableRelational data collection to be operated; first confirm the table name and field structure

3ConditionWHERE limits the scope of influence; placeholders such as question marks are safely passed by parameterized queries.

Variants

SELECT

**SELECT**Read matching rows

Read records without changing them.

INSERT

**INSERT**Add a new row

Create a new record.

UPDATE

**UPDATE**Change the row hit by WHERE

Update selected records; check the WHERE clause.

DELETE

**DELETE**Delete the row hit by WHERE

Remove selected records after checking recovery.

Typical use cases

Order query

Query users**SELECT to find records that meet the conditions**

SELECT id, name, planFROM usersWHERE plan = 'pro';

Result: u\_23 · Alex Chen · pro

User lookup

New task**INSERT creates a record**

Execute**INSERT INTO tasks ...**
*→*
Return**id = task\_8842**

Analytics total

Update data**UPDATE only modifies the specified user**

UPDATE usersSET city = 'Shenzhen'WHERE id = 'u\_23';

Affects 1 row · Modification successful

Data update

Delete record**Confirm WHERE before DELETE**

SELECT WHERE id=t\_42→Confirm 1 line→DELETE

Avoid accidentally deleting the entire table

Further reading

[SQL injectionMDN ↗](https://developer.mozilla.org/en-US/docs/Glossary/SQL_injection)
