# Requirements and acceptance

[Deutsch](../de/REQUIREMENTS.md)

MUST obligations apply when their capability is delivered. SHOULD obligations
require a documented reason if deferred. All implementation acceptance checks
below are **pending**. M0 documentation checks do not satisfy numerical acceptance.

| ID | Level | Requirement | Acceptance |
| --- | --- | --- | --- |
| ST-001 | MUST | Use approved Math dependencies; avoid duplicate generic numerical kernels | AC-001: pinned dependency, capability evidence and integration smoke pass per language |
| ST-002 | MUST | Keep statistical computation independent of UI, files and networking | AC-002: dependency review and in-memory invocation without application infrastructure |
| ST-003 | MUST | Give each public procedure a versioned mathematical contract | AC-003: inputs, domain, formulas, assumptions, errors, method and tolerances reviewed |
| ST-004 | MUST | Expose missing-value policy and observation accounting | AC-004: reject/omit cases verify input, used and excluded counts without silent removal |
| ST-005 | MUST | Distinguish invalid input, undefined statistics and numerical failure | AC-005: boundary cases assert machine-readable status and absent estimates |
| ST-006 | MUST | Return typed, structured analysis results | AC-006: tables/diagnostics consume raw values; rounding does not alter calculations |
| ST-007 | MUST | Preserve complete analysis options and provenance | AC-007: rerun of a recorded recipe matches within its declared reproducibility tier |
| ST-008 | MUST | Validate every procedure against independent evidence | AC-008: manual, boundary and independent reference cases pass documented tolerances |
| ST-009 | MUST | Keep C++ and C# implementations separate and conformant | AC-009: each delivered language executes the shared cases; matrix reports differences |
| ST-010 | MUST | State inferential assumptions and diagnostic limitations | AC-010: approved inference/model cases include assumptions, df where defined and warnings |
| ST-011 | MUST | Specify tails, confidence levels, alternatives and multiplicity | AC-011: extreme-tail and alternative-specific cases plus adjusted/unadjusted labels |
| ST-012 | MUST | Define weights, factor coding and grouping before support | AC-012: unsupported weights rejected; supported semantics checked against approved cases |
| ST-013 | SHOULD | Support repeatable simulation and resampling | AC-013: generator ID, seed/state, stream policy and method version reproduce recorded cases |
| ST-014 | SHOULD | Supply reusable table/plot/report adapters | AC-014: export contains metadata and diagnostics; engine has no renderer dependency |
| ST-015 | MUST | Document each shipped procedure in both languages | AC-015: C++ and C# examples, limitations and EN/DE handbook pages match delivered behavior |
| ST-016 | SHOULD | Measure time/memory before performance optimization | AC-016: benchmark workload, platform, baseline and accuracy impact recorded |
| ST-017 | MUST | Protect data integrity through explicit preparation steps | AC-017: source snapshot unchanged, transform recipe deterministic, exclusions auditable |
| ST-018 | MUST | Maintain compatible contracts and declared package dependencies | AC-018: release matrix links contract, package, Math version and compatibility changes |

## First pilot acceptance scope

M1 targets ST-001 through ST-009, ST-015 and ST-018 for an in-memory descriptive
summary API. ST-007 records procedure/options/dependency identity for direct
calls; a full application recipe runner arrives at M3. ST-010/ST-011 enter with
inference; ST-012 is satisfied initially by explicit rejection of unsupported
weights. ST-017 enters with data/workflow adapters.

For counts, mean, variance, standard deviation, covariance and correlation, the
[pilot contract](../../spec/DESCRIPTIVE-STATISTICS.md) and
[reference cases](../../conformance/descriptive-cases.json) define exact checks.
Other procedures remain catalog entries until their contracts are approved.

## Traceability

Every implementation PR lists requirement IDs, procedure IDs, affected contract
version, Math evidence, test cases and handbook updates. Acceptance is recorded
per procedure and language, not inferred from one successful example or a green
documentation check.
