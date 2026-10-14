# Fantasy Village Mapper

## Versioning
Follow the user's A.B.C policy, not standard semantic versioning:
- A: change in the app's premise or core concept.
- B: new features.
- C: bug fixes or changes to existing functionality.

For each completed, user-visible change, increment the highest applicable component once. Reset lower components to zero when A or B increases. Group related changes made for one request into one version. Do not increment for documentation-only work or packaging the same source.

Keep VERSION, the visible version in dist/index.html, and CHANGELOG.md synchronized. Record the concrete resulting behavior in Dutch in CHANGELOG.md. Rebuild the standalone HTML deliverables when source changes. Preserve existing user data and backwards-compatible imports.

The initial tracked baseline is 1.0.0. Earlier prototype iterations were not individually versioned; do not invent historical version numbers.

## Persistent user data
Never reset user input during an update. Preserve the existing storage key, use additive/backwards-compatible migrations, and test older saved schemas and full export roundtrips when changing persistence. Keep names, IDs, links, images and geometry. Do not refresh a browser with an open unsaved form. Component exports do not replace the full chronicle backup.

Update the version query on CSS and JavaScript references in dist/index.html on every release, so existing browser tabs load the matching assets. Standalone packaging must replace these versioned references.
