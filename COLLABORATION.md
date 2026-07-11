# Collaboration guide

This repository is a product fork of `frappe/lms`. Joel (`@codejoen`) and Fabian
(`@fabianprogrammer123`) collaborate through short-lived branches and reviewed pull requests.

## Branch model

| Branch | Purpose | Change policy |
| --- | --- | --- |
| `develop` | Clean mirror of `frappe/lms:develop` | Upstream fast-forward updates only |
| `product` | Protected, deployable product integration branch | Pull requests only |
| `feat/*` | New product functionality | Short-lived pull request into `product` |
| `fix/*` | Product bug fixes | Short-lived pull request into `product` |
| `schema/*` | DocType or migration work | Short-lived pull request into `product` |
| `sync/upstream-YYYY-MM-DD` | Integrate new Frappe changes | Pull request into `product` using a merge commit |

Do not use permanent personal branches. One person owns each topic branch, and the other person
reviews it. Work intended for the upstream Frappe project must start from `upstream/develop`, not
from `product`.

## Clone and remotes

Each maintainer works from their own clone:

```bash
gh repo clone codejoen/lms
cd lms
git remote add upstream https://github.com/frappe/lms.git
git fetch --all
```

`origin` is the shared product fork. `upstream` is the open-source Frappe repository.

## Start a change with a worktree

Worktrees are optional local directories. They allow several branches to be checked out at once;
they do not replace branches or pull requests.

```bash
git fetch origin
git worktree add ../lms-course-prerequisites \
  -b feat/course-prerequisites \
  origin/product
cd ../lms-course-prerequisites
```

Only one worktree in the same clone can have a branch checked out. When the pull request is merged:

```bash
git worktree remove ../lms-course-prerequisites
git branch -d feat/course-prerequisites
```

## Commit and pull-request workflow

1. Open a draft pull request early.
2. Keep one logical change in each pull request.
3. Use semantic titles and commits, for example `feat(lms): add course prerequisites`.
4. The author must not approve their own pull request.
5. The other maintainer reviews the code and data-model impact.
6. Resolve every review conversation and obtain a fresh approval after material changes.
7. Merge ordinary product work with **Squash merge**.
8. Merge upstream-sync pull requests with **Create a merge commit** to preserve ancestry.
9. Let GitHub delete the topic branch after merge.

Before final review, the branch owner may rebase their own topic branch:

```bash
git fetch origin
git rebase origin/product
git push --force-with-lease
```

Never rebase or force-push `product` or `develop`. Avoid rebasing a topic branch after another
person has started adding commits to that same branch.

## Data-model decision record

Before changing a DocType, create an Issue that records:

- the user problem and affected workflows;
- existing and proposed DocTypes;
- relationship cardinality and child-table choices;
- field names, types, required/default values, uniqueness, and indexes;
- permissions, ownership, and delete behavior;
- API, frontend, reporting, and fixture impact;
- migration behavior for existing records;
- fresh-install and existing-site upgrade tests;
- backup, rollback, or recovery considerations.

Agree on the model before implementation begins. Avoid editing the same DocType JSON concurrently;
assign one maintainer temporary ownership of each affected model.

## Contents of a data-model pull request

A model change should include every part needed for one deployable result:

- generated DocType JSON;
- Python controller and permission logic;
- relevant client or frontend changes;
- fixtures and hooks, if needed;
- targeted unit tests;
- a one-time patch registered in `lms/patches.txt` when existing data must change;
- documentation of migration and recovery behavior.

Create and modify standard DocTypes with Frappe developer mode so their JSON is tracked. Do not
treat a manual database edit as source code.

Minimum validation for relevant schema changes:

```bash
bench --site lms.test migrate
bench --site lms.test run-tests --doctype "LMS Course"
bench --site lms.test run-tests --app lms
```

Also test a fresh installation and an upgrade of a realistic existing database copy. Take a backup
before applying migrations outside disposable development sites.

## Sync from Frappe

First fast-forward the clean mirror:

```bash
git fetch upstream
git switch develop
git merge --ff-only upstream/develop
git push origin develop
```

Then integrate it through a reviewed product pull request:

```bash
git fetch origin
git switch -c sync/upstream-YYYY-MM-DD origin/product
git merge --no-ff origin/develop
git push -u origin sync/upstream-YYYY-MM-DD
gh pr create --base product --title "chore: sync upstream YYYY-MM-DD"
```

Resolve conflicts on the sync branch, run the full test suite, and merge the pull request using a
merge commit. Never squash an upstream sync.

## Emergency changes

Admin access is not a normal bypass. For an urgent production fix, still open a focused `fix/*`
pull request, run the available checks, and request peer review. If a repository rule must be
temporarily changed, document why in the pull request and restore the rule immediately afterward.
