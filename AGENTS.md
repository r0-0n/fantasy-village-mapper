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

## Efficient editing
- Read `src/INDEX.md` first; find the relevant function, then read only that source file and nearby lines.
- Edit `src/*.js` / `src/style.css`. `dist/app.js` and `dist/style.css` are generated; do not edit them directly.
- Files in `src/manifest.json` are concatenated in order into one classic script. Preserve order and shared globals; do not convert individual files into ES modules without auditing the legacy wrapper chain.
- Run `python3 work/build.py` from the repository root after source edits. It also regenerates the function index. In an exported ZIP use `python3 tools/build.py`.
- Run `python3 work/test.py` for the current regression suite; NODE can specify a Node.js executable. Package with `python3 work/package.py`.
- Ignore `archive/`, old version ZIPs, and generated deliverables during routine searches. The archive contains superseded development scripts, not current sources.
- Avoid reading the full generated JavaScript or full changelog. Use a focused search or the first current changelog entry.
