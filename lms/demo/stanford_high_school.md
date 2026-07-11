# Stanford High School sample dataset

This deterministic demo seed fills the existing Frappe Learning model with an English-language,
fictional high-school dataset for the 2026-27 academic year.

## Contents

- 20 `LMS Course` records.
- 20 `LMS Batch` class sections.
- Exactly three `Course Instructor` assignments for every course and class.
- 29 fictional teachers with `Course Creator` access.
- 120 fictional students with `LMS Student` access.
- Between 20 and 25 `LMS Batch Enrollment` records per class.
- Automatically generated `LMS Enrollment` records through the standard batch-enrollment hooks.

Names are realistic but entirely synthetic. Every email uses the reserved `.example` domain, and
welcome and enrollment-confirmation emails are disabled.

## Preview

```bash
bench --site <site-name> execute lms.demo.stanford_high_school.preview
```

The preview reports class sizes, total enrollment seats, and the minimum and maximum number of
classes assigned to each student. It does not write to the database.

## Seed

```bash
bench --site <site-name> execute lms.demo.stanford_high_school.seed
```

The seed is idempotent: running it again updates the synthetic users, courses, and classes and only
creates missing enrollments. Before committing, it verifies every instructor and enrollment count;
it rolls back if validation fails.

The same database validation can be run independently:

```bash
bench --site <site-name> execute lms.demo.stanford_high_school.validate_seed
```
