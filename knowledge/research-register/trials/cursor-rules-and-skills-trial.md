---
artifact_id: EX-CORE-001
status: DRAFT
phase: 0
priority: high
depends_on:
  - artifact_id: STD-CORE-001
    path: ../../../docs/standards/naming-standard.md
  - artifact_id: STD-CORE-002
    path: ../../../docs/standards/research-standard.md
  - artifact_id: STD-CORE-003
    path: ../../../docs/standards/citation-standard.md
  - artifact_id: KNOW-CORE-001
    path: ../README.md
  - artifact_id: KNOW-CORE-002
    path: ../sources.yaml
blocks:
  - Phase 0 current-product evidence review
  - ARCH-CORE-001
  - ARCH-CORE-002
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Trial: Cursor rules and skills evidence

## Purpose

Test the naming, research, citation, source-register, freshness, and uncertainty standards against a current-product question.

This is a standards trial, not the final Cursor architecture specification.

## Research question

What can the repository state with authoritative support about Cursor project rules and Agent Skills, and which implementation details remain unverified?

## Decisions supported

- Whether `.cursor/rules` and `.cursor/skills` are appropriate scaffold locations.
- Whether rules and skills should be treated as different context mechanisms.
- Which placeholder components may safely exist before activation.
- Which details require revalidation during architecture and orchestrator implementation.

## Scope

Included:

- project-rule location and format;
- rule application model;
- `SKILL.md` support;
- dynamic skill loading and slash invocation;
- high-level subagent capability described for Cursor 2.4.

Excluded:

- exact active skill frontmatter beyond directly supported fields;
- exact custom-subagent file schema;
- tool availability across every version and plan;
- final routing and orchestration design.

## Findings

### Project rules

Cursor documents project rules as version-controlled MDC files stored under `.cursor/rules`.[^cursor-rules]

The documentation describes four application modes: always included, attached by path pattern, requested by the agent based on description, and manually invoked.[^cursor-rules]

Cursor recommends focused, actionable, scoped, and composable rules rather than one large undifferentiated instruction file.[^cursor-rules]

### Agent Skills

Cursor's 2.4 release introduced Agent Skills defined in `SKILL.md` files. Skills may include instructions, scripts, and custom commands and may be invoked through the slash-command menu.[^cursor-skills]

Cursor's product guidance distinguishes dynamically loaded skills from persistent rules and presents this separation as a way to keep context focused.[^cursor-practices]

### Subagents

Cursor's 2.4 release describes subagents as independent agents with separate context and configurable prompts, tool access, and models.[^cursor-skills]

**Unresolved:** The evidence captured here is insufficient to approve the repository's exact custom-subagent file schema or guarantee delegation behaviour across current versions and plans.

The scaffold may reserve `.cursor/agents/*.md`, but those files remain non-operational until the current official schema and runtime behaviour are verified.

## Claims matrix

| Claim ID | Claim | Source IDs | Confidence | Treatment |
|---|---|---|---|---|
| CUR-001 | Project rules are stored under `.cursor/rules` | `cursor-rules` | Established | Publish |
| CUR-002 | Rule files use MDC metadata and content | `cursor-rules` | Established | Publish |
| CUR-003 | Skills are defined in `SKILL.md` files | `cursor-2-4-subagents-skills` | Established for documented release | Publish with version awareness |
| CUR-004 | Skills load dynamically when relevant | `cursor-agent-best-practices` | Established as product guidance | Publish |
| CUR-005 | Skills may be invoked through slash commands | `cursor-2-4-subagents-skills` | Established for documented release | Publish with version awareness |
| CUR-006 | The scaffold's exact subagent schema is currently approved | No sufficient source | Unresolved | Do not activate |
| CUR-007 | Focused rules plus skills should reduce persistent context load | `cursor-rules`, `cursor-agent-best-practices` | Supported synthesis | Use as project rationale |

## Project decisions validated

1. Keep persistent rules small and bounded.
2. Put specialised methods and domain knowledge in modular skills.
3. Keep placeholder rules non-applying.
4. Keep placeholder skills non-invokable until metadata is verified.
5. Keep subagents non-operational until schema and delegation behaviour are tested.
6. Reverify product-sensitive claims within 30 days of activation.

These are repository decisions informed by the evidence, not claims that Cursor mandates this exact architecture.

## Open Phase 1 questions

- What is the current official custom-subagent schema?
- Which skill frontmatter fields are currently supported?
- How are nested skills discovered?
- What are the current limits on subagent nesting, parallelism, tools, and plan availability?
- When should explicit workflows use skills, commands, or both?

## Acceptance result

**Trial result: PASS WITH OPEN PRODUCT QUESTIONS**

The standards prevented unsupported subagent claims from becoming architecture facts. The rule and skill evidence is sufficient for scaffold planning, but active Cursor components remain blocked pending Phase 1 verification.

## Sources

[^cursor-rules]: Cursor, “Rules,” updated date not stated, retrieved 2026-07-17, https://docs.cursor.com/context/rules. Central source ID: `cursor-rules`.

[^cursor-skills]: Cursor, “Subagents, Skills, and Image Generation,” release 2.4, 2026, retrieved 2026-07-17, https://cursor.com/changelog/2-4. Central source ID: `cursor-2-4-subagents-skills`.

[^cursor-practices]: Cursor, “Best practices for coding with agents,” 2026, retrieved 2026-07-17, https://cursor.com/blog/agent-best-practices. Central source ID: `cursor-agent-best-practices`.
