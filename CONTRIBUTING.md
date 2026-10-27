# Contributing

Thank you for helping improve this FG-TIDA Working Group charter. This document explains how to propose and make changes.

## Ground rules

- **Do not commit directly to `main`.** `main` is the published branch — every push to it rebuilds and republishes the charter (web page and PDF). All changes go through a Pull Request.
- Keep discussion in **issues and pull requests**, so the review and decision history is preserved.

## How to propose a change

1. **Open an issue** describing what should change and why. (Optional for small fixes; recommended for anything substantive.)
2. **Create a branch** from `main`:

   ```shell
   git checkout -b update-scope
   ```

   Example branch names: `update-scope`, `update-deliverables`, `charter-v0.2`, `review-milestones`.
3. **Edit the charter** in `src/doc/index.rst`. See [HOWTO.md](HOWTO.md) to build and preview locally, and [WG-ONBOARDING.md](WG-ONBOARDING.md) for section-by-section guidance.
4. **Commit** with a clear message and **open a Pull Request** against `main`.
5. The **Working Group reviews** the Pull Request. Resolve comments until it is approved.
6. A **chair (or maintainer) merges** the Pull Request. The site and PDF are then rebuilt and published automatically.

## Review and approval

- Pull Requests should be reviewed by the Working Group before merging.
- Chairs are responsible for merging approved changes and for deciding when to cut a new charter version (update the revision history when scope or deliverables change materially).

## Before you submit

- Replace any `<...>` placeholders you touched — the published charter should contain no unresolved template values.
- Keep the charter concise (approximately 600–1,200 words).
- Keep people's names only in the **Group Information** section.
- Check that the preview builds (GitHub Actions, or locally — see [HOWTO.md](HOWTO.md)).

## Questions

For questions about this charter's content, open an issue in this repository.
For problems with the shared template itself (build, PDF, CI), open an issue in
[`FG-TIDA/wg-charter-template`](https://github.com/FG-TIDA/wg-charter-template).
