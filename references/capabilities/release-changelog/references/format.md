# Changelog format examples

Reuse the target repository's format and workflow. These examples are defaults for a new file, not migration requirements. Keep released history intact.

## Direct pending entries

```markdown
# Changelog

All notable changes to this project are documented here.

## [Unreleased]

### Added

- Invite teammates by email from the dashboard.
```

Where the project uses Keep a Changelog, categories are `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security`; omit empty categories. Use its versioning convention, not an assumed SemVer policy. Versioned headings commonly use `## [X.Y.Z] - YYYY-MM-DD`; use evidenced release identity and dates, never copy example values as real releases.

## Optional fragments

Use fragments only when already established or explicitly requested. Prefer the existing generator and schema (for example, Changesets or Towncrier). A minimal Markdown scheme can use a unique `changelog.d/<id>.md` file:

```markdown
Added
- Invite teammates by email from the dashboard.
```

Check filename collisions and existing content; task or phase IDs are not guaranteed unique. Fragments reduce shared-file conflicts but do not eliminate conflicts or replace integration checks. No planning-file transition automatically writes a fragment.

## Assembly

1. Select entries for the authorized release; account for direct pending entries and fragments without duplication.
2. Group using the established categories and preserve all selected meaning.
3. Insert the evidenced version/date above prior releases and retain unrelated pending work.
4. Verify coverage before deleting only the assembled fragments.
5. Add compare links only when the host, repository, tag names, and comparison syntax are verified. No remote or uncertain visibility: omit rather than fabricate or disclose private URLs.

For public or unknown visibility, write external benefits without internal paths, private tracker links, code names, secrets, or embargoed details. Confirmed private context may allow internal terminology, but not secret disclosure. Scrub fragments at creation, not only assembly.

## Quality checks

- Every claim is supported by the scoped diff, behavior, or release evidence.
- Entries describe outcomes rather than copying commit subjects.
- Pending and released changes are clearly separated.
- Existing released sections retain their content and order.
- Version, dates, links, and fragment schema follow authoritative project evidence.
- Authorized local edits do not require another blanket approval; publication still requires its own authority and actual project gates.
