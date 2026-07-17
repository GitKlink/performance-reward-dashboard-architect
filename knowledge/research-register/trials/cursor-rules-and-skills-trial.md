---
artifact_id: EX-CORE-001
status: DRAFT
phase: 0
priority: high
depends_on:
  - STD-CORE-001: ../../../docs/standards/naming-standard.md
  - STD-CORE-002: ../../../docs/standards/research-standard.md
  - STD-CORE-003: ../../../docs/standards/citation-standard.md
  - KNOW-CORE-001: ../README.md
  - KNOW-CORE-002: ../sources.yaml
blocks:
  - Phase 0 evidence-standard review
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Trial: Cursor rules and skills evidence

## Purpose

Test the naming, research, citation, source-register, freshness, and uncertainty standards against a current-product question.

This is a standards trial, not the final Cursor architecture specification.

## Research question

What can the repository currently state with authoritative support about Cursor project rules and Agent Skills, and which implementation details remain unverified?

## Decisions supported

- Whether `.cursor/rules` and `.cursor/skills` are appropriate scaffold locations.
- Whether rules and skills should be treated as different context mechanisms.
- Which placeholder components can safely remain in the public repository before activation.
- Which product details require revalidation during Phase 1 and Phase 11.

## Scope

Included:

- project-rule location and format;
- rule application model;
- `SKILL.md` support;
- dynamic skill loading and slash invocation;
- high-level subagent capability introduced in Cursor 2.4.

Excluded:

- exact active skill frontmatter beyond directly supported fields;
- exact custom-subagent file schema;
- subagent tool availability in every Cursor version and plan;
- hooks and custom commands beyond high-level existence;
- final routing and orchestration design.

## Source plan

| Need | Preferred source | Result |
|---|---|---|
| Rule path and metadata | Official Cursor documentation | Found |
| Skill file and invocation | Official Cursor release material | Found |
| Rules versus skills context behaviour | Official Cursor product guidance | Found |
| Exact subagent file schema | Official current documentation | Not sufficiently captured in this trial |
| Community-reported limitations | Practitioner evidence | Deliberately excluded until the official baseline is established |

## Findings

### Project rules

Cursor documents project rules as version-controlled files stored under `.cursor/rules`. The files use MDC, combining metadata and instruction content.[^cursor-rules]

The documentation describes four application modes: always included, auto attached by path pattern, agent requested based on description, and manually invoked.[^cursor-rules]

Cursor recommends focused, actionable, scoped, and composable rules rather than one large undifferentiated instruction file.[^cursor-rules]

### Agent Skills

Cursor's 2.4 release introduced Agent Skills defined in `SKILL.md` files. The release states that skills may include instructions, scripts, and custom commands and may be invoked through the slash-command menu.[^cursor-2-4]

Cursor's product guidance distinguishes skills from always-on rules: skills package specialised knowledge and workflows that are loaded dynamically when relevant, which is intended to keep the working context focused.[^cursor-best-practices]

### Subagents

Cursor's 2.4 release describes subagents as independent agents with separate context that can run specialised work and be configured with prompts, tool access, and models.[^cursor-2-4]

**Unresolved:** This trial does not have sufficient current official evidence to approve the repository's exact custom-subagent file schema or guarantee delegation behaviour across Cursor versions and plans.

The scaffold may reserve `.cursor/agents/*.md` locations, but those files must remain non-operational until Phase 1 and Phase 11 verify the current official schema and runtime behaviour.

## Claims matrix

| Claim ID | Claim | Source IDs | Confidence | Repository treatment |
|---|---|---|---|---|
| CUR-001 | Project rules are stored under `.cursor/rules` | `cursor-rules` | Established | Publish |
| CUR-002 | Rule files use MDC metadata and content | `cursor-rules` | Established | Publish |
| CUR-003 | Skills are defined in `SKILL.md` files | `cursor-2-4-subagents-skills` | Established for Cursor 2.4+ | Publish with version awareness |
| CUR-004 | Skills load dynamically when relevant | `cursor-agent-best-practices` | Established as product guidance | Publish |
| CUR-005 | Skills can be invoked through slash commands | `cursor-2-4-subagents-skills` | Established for documented release | Publish with version awareness |
| CUR-006 | Custom subagents use the exact scaffold schema | None sufficient in this trial | Unresolved | Do not activate or publish as fact |
| CUR-007 | Focused rules reduce context load versus a monolithic rule | `cursor-rules`, `cursor-agent-best-practices` | Supported synthesis | Label as project rationale |

## Project decisions validated by the evidence

1. Keep persistent rules small and bounded.
2. Put procedural methods and domain knowledge in modular skills rather than duplicating them in rules.
3. Keep placeholder rules configured so they cannot apply.
4. Keep placeholder skills non-invokable until frontmatter and behaviour are verified.
5. Keep subagents non-operational until the exact current schema and delegation behaviour are tested.
6. Reverify current Cursor documentation within 30 days of activating product-sensitive components.

These are repository decisions informed by the evidence; they are not claims that Cursor mandates this exact architecture.

## What the trial revealed about the standards

### Naming standard

- Reserved Cursor paths and filenames need explicit exceptions to the general lowercase-kebab convention.
- Active skill names must remain aligned with their folder names.
- Exact product metadata should not be standardised before official verification.

### Research standard

- Current-product research needs both a stable official documentation page and versioned release material.
- A missing official detail must remain unresolved even when community sources appear confident.
- Product guidance can support architectural rationale without becoming an absolute technical guarantee.

### Citation standard

- Descriptive footnotes make claim support easy to audit.
- Version-sensitive claims require the release identifier in the source entry.
- A central source record and local citation can coexist without copying large evidence extracts.

## Open questions for Phase 1

- What is the current official schema for custom subagents?
- Which skill frontmatter fields are formally supported now?
- How are nested skill directories discovered?
- What are the current limits on subagent nesting, parallelism, tools, and plan availability?
- Should explicit workflows use Agent Skills, `.cursor/commands`, or both?

## Acceptance result

**Trial result: PASS WITH OPEN PRODUCT QUESTIONS**

The standards successfully prevented unsupported subagent claims from being promoted to architecture decisions. The rule and skill claims are sufficiently supported for scaffold planning, but all active Cursor components remain blocked pending Phase 1 verification.

## Sources

[^cursor-rules]: Cursor, “Rules,” updated date not stated, retrieved 2026-07-17, https://docs.cursor.com/context/rules. Central source ID: `cursor-rules`.

[^cursor-2-4]: Cursor, “Subagents, Skills, and Image Generation,” release 2.4, 2026, retrieved 2026-07-17, https://cursor.com/changelog/2-4. Central source ID: `cursor-2-4-subagents-skills`.

[^cursor-best-practices]: Cursor, “Best practices for coding with agents,” 2026, retrieved 2026-07-17, https://cursor.com/blog/agent-best-practices. Central source ID: `cursor-agent-best-practices`.
