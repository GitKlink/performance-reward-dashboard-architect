# Changelog

All notable changes to this project will be documented here.

The project intends to follow Semantic Versioning once the first tagged release is prepared.

## Unreleased

### Added

- Initial public repository
- Complete Cursor-native repository scaffold
- Authoritative phased build-order and dependency-control framework
- Machine-readable artifact register with immutable IDs
- Draft naming, research, and citation standards
- Central research register and reusable source records
- Five Phase 0 standards trials covering current Cursor features, new-hire premium, consulting attribution, graphical perception, and internal architecture decisions
- Phase 0 internal pre-review with finding and resolution tracking
- Independent-review issue and copy-paste review instructions for a fresh reviewer context
- Artifact dependency validator with seven unit-test scenarios
- Internal Markdown link validator with five unit-test scenarios
- Source-register validator with six unit-test scenarios
- GitHub Actions workflow running all tests and repository validators
- Development dependency definition for PyYAML
- Artifact-specific Phase 1 architecture, standards, and planning placeholders
- Safe non-applying placeholders for Cursor rules, skills, and subagents
- Placeholder schemas, templates, examples, evaluations, and remaining validation scripts

### Changed

- Core standards moved to content version `0.2.0` after the internal correction pass
- Research and citation approval gates no longer depend circularly on later Phase 3 and Phase 4 delivery
- Phase 0 now requires a validated research field contract; formal schema implementation remains in Phase 2
- Added `TEST` and `INFRA` artifact types and registered active tests and CI infrastructure
- Source records now separate registered `relevant_artifacts` from future `planned_consumers`
- Active Phase 0 and registered Phase 1 Markdown artifacts use canonical dependency objects
- Dependency and source-register warnings now fail CI
- New-hire premium cohort logic now includes all eligible commenced hires regardless of later employment status, preventing survivorship bias
- Naming standard now documents the initial `scaffold/` branch type and reserves `ARTIFACT-REGISTER.yaml`
- Research planning records IBCS Version 2.0 as the current standard baseline rather than assuming Version 1.2 remains current

### Validation status

The active branch currently passes:

- all 18 unit-test scenarios;
- artifact ID, path, dependency, cycle, frontmatter, and maturity validation;
- source-register validation with warnings treated as errors;
- internal-link validation;
- dependency validation with warnings treated as errors.

### Review status

The internal pre-review initially identified one critical, seven major, and four minor findings. All internal critical and major findings have been resolved.

The Phase 0 package is ready for a genuinely independent review under GitHub issue #2. Standards remain `DRAFT` until that review is completed and its critical and major findings are resolved.

### Known work remaining

- Complete the independent Phase 0 review
- Resolve any independent critical and major findings
- Move eligible standards and controls to `IN REVIEW`, then `APPROVED`
- Merge pull request #1
- Begin substantive Phase 1 architecture work
