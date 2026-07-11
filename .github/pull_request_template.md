## Summary

Describe the user problem and the solution. Keep the pull request focused on one logical change.

## Change type

- [ ] Feature
- [ ] Bug fix
- [ ] Data model or migration
- [ ] Upstream sync
- [ ] Documentation or maintenance

## Data model and migration

- [ ] No data model change
- [ ] DocType fields and relationships are documented
- [ ] Existing-data migration is included in `lms/patches.txt`, or is not required
- [ ] Permissions, indexes, defaults, and delete behavior were reviewed
- [ ] A fresh installation and an existing-site upgrade were tested

Explain migration and rollback/recovery considerations, or write `Not applicable`:

## Validation

List the commands and manual scenarios used to validate the change:

- [ ] Relevant Frappe tests
- [ ] Frontend tests, when applicable
- [ ] `bench --site <site> migrate`, when applicable
- [ ] Manual smoke test

## Upstream impact

- [ ] This is specific to our product branch
- [ ] This may be suitable for a separate pull request to `frappe/lms`
- [ ] This is an upstream-sync pull request and must use a merge commit

## Reviewer notes

Call out risky files, unresolved decisions, screenshots, and areas that deserve extra attention.
