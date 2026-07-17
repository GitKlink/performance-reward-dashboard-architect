# Changelog

All notable changes to this project will be documented here.

The project intends to follow Semantic Versioning once the first tagged release is prepared.

## Unreleased

### Added

- Initial public repository
- Complete Cursor-native repository scaffold
- Authoritative phased build-order framework
- Artifact dependency model and machine-readable artifact register
- Draft repository naming standard
- Draft evidence-based research standard
- Draft citation and source-provenance standard
- Central research register and reusable source records
- Five Phase 0 standards trials covering current Cursor features, new-hire premium, consulting attribution, graphical perception, and internal architecture decisions
- Artifact dependency validator and seven initial unit-test scenarios
- Internal Markdown link validator and five unit-test scenarios
- Source-register validator and six unit-test scenarios
- GitHub Actions workflow running all tests and repository validators
- Development dependency definition for PyYAML
- Artifact-specific Phase 1 architecture, standards, and planning placeholders
- Safe non-applying placeholders for Cursor rules, skills, and subagents
- Placeholder schemas, templates, examples, evaluations, and remaining validation scripts
- Phase 0 independent-review issue

### Changed

- Phase 0 status now records successful automated validation
- Build gates define minimum prerequisite status for prototyping, evaluation, approval, and release
- Research planning records IBCS Version 2.0 as the current standard baseline rather than assuming Version 1.2 remains current
- Dependency validation temporarily supports legacy Phase 0 dependency syntax while flagging it for migration

### Validation status

The active branch currently passes:

- all unit tests;
- artifact dependency validation;
- source-register validation;
- internal-link validation.

### Known work remaining

- Register the validation workflow and newly activated validators in the artifact register
- Migrate remaining active dependency metadata to the canonical object format
- Complete independent Phase 0 review before moving standards to `IN REVIEW`
