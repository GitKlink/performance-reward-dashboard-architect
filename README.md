# Performance & Reward Dashboard Architect

A modular, skills-based Cursor AI agent for designing Power BI dashboards and static executive reporting for Performance & Reward.

The agent is intended for executives, people managers, Business Partners, Reward Partners, and specialist analytics teams. It combines Performance & Reward domain knowledge, consulting-style communication, visual storytelling, dashboard UX, data visualisation, and Power BI implementation guidance.

## Repository state

The repository is in **Phase 0 governance review**.

The complete Cursor-native scaffold, core governance standards, representative evidence trials, artifact register, research register, validation scripts, unit tests, and GitHub Actions workflow are present on branch:

```text
scaffold/repository-foundation
```

Current automated validation covers:

- artifact IDs, paths, dependencies, statuses, and frontmatter;
- central source records and source references;
- repository-local Markdown links;
- 18 unit-test scenarios.

The Phase 0 standards remain drafts until the independent review in GitHub issue #2 is completed and material findings are resolved.

Start with:

1. [`BUILD-ORDER.md`](BUILD-ORDER.md)
2. [`DEPENDENCIES.md`](DEPENDENCIES.md)
3. [`STATUS.md`](STATUS.md)
4. [`ARTIFACT-REGISTER.yaml`](ARTIFACT-REGISTER.yaml)
5. [`docs/architecture/agent-architecture.md`](docs/architecture/agent-architecture.md)
6. [`knowledge/research-register/README.md`](knowledge/research-register/README.md)

## Final agent surface

The installable Cursor agent will primarily live under:

```text
.cursor/
├── rules/
├── agents/
└── skills/
```

Supporting knowledge, schemas, templates, examples, evaluations, and validation scripts remain versioned in this maintained source repository.

## Status warning

Files marked `PLACEHOLDER`, `RESEARCH IN PROGRESS`, or `DRAFT` are not authoritative and must not be treated as completed agent knowledge or active Cursor capabilities.

## Current gates

Before substantive Phase 1 work begins:

- complete the independent Phase 0 review;
- resolve critical and major findings;
- register newly activated validation infrastructure;
- migrate remaining legacy dependency metadata;
- move eligible controls to `IN REVIEW`;
- merge pull request #1.

## License

MIT
