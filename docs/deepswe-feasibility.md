# DeepSWE × OpenRouter: trial-level feasibility audit

**Review draft, 30 October 2026; no replacement diagram is approved by this audit.** Tracked by [issue #12](https://github.com/Eurobotics-Association/LLM-Analysis/issues/12).

## Purpose and scoring

The proposed chart measures coding-agent performance on **DeepSWE v1.1**, not general intelligence. The official [leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json) defines pass@1 as the proportion of scored rollout attempts that pass; provider/verifier/network errors are excluded, while context-window failures and agent timeouts count as failures. The 113-task benchmark uses mini-swe-agent; report uncertainty and task/attempt coverage rather than treating adjacent differences as conclusive. Do not mix scores from other harnesses, benchmark revisions, run policies, or lab-reported evaluations into a single curve without validating comparability.

## Audit of actual trial records

On 30 October 2026 UTC, read the [official trial index](https://deepswe.datacurve.ai/artifacts/v1.1/trials.json) and [leaderboard](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json). The index contains 31,617 records; 31,462 have `source == deep-swe`, `eval_scope == full`, and `included_in_score == true`. This filter documents scored attempts only; other billable failures require separate accounting. It is not a complete definition of total spend.

| Exact model in index | Effort levels and scored trials | Category completeness in index | Result |
|---|---|---|---|
| gpt-6-astra | low, medium, high, xhigh, max: 452 trials each | All 2,260 have separate uncached input, cache reads, cache writes and output; all have null peak context | Strong candidate for tier audit; not yet a validated OpenRouter cost |
| glm-5-3-flash | max: 448 trials | All have input, aggregate cache and output, but none have the separate uncached/read/write fields | Do not assume cache field semantics or write quantity |
| deepseek-v4-flash | max: 452 trials | All have input, aggregate cache and output, but none have the separate uncached/read/write fields | Older model, not V4.1 Flash 1017; incomplete accounting |
| gpt-6-1-sol | none found under this exact model ID | — | No official matched trial found |
| gpt-6-1-terra | none found under this exact model ID | — | No official matched trial found |
| deepseek-v4-1-flash-1017 | none found under this exact model ID | — | No official matched trial found |

The 448 scored GLM Flash records label `provider: anthropic` despite the `glm-5-3-flash` model ID. That is an unexpected metadata value, **not proof Anthropic served the model**. Its meaning and actual inference route need primary-source clarification before provider matching. Some of those records say `has_trajectory: true`; the index alone does not establish whether per-call accounting is contained in accessible trajectories. The Astra records in the same audit carry `metrics_source: verified_openai_handoff` and `has_trajectory: false`; validate coverage and source semantics rather than assuming all raw calls are available.

The Astra [OpenRouter endpoint listing](https://openrouter.ai/api/v1/models/openai/gpt-6-astra/endpoints) inspected in this audit includes context-dependent price overrides at 272,000 prompt tokens. A trial's total input aggregated over many calls cannot determine how many calls crossed a per-request tier, and its recorded peak context is null. Thus complete aggregate token categories alone are not sufficient to apply those tariffs faithfully. Check whether other source records establish per-request tier use and evaluate all available compatible non-promotional routes before repricing. Some endpoints have different service/variant constraints; a `discount: 0` field alone does not establish that a route is eligible.

GLM Flash endpoints have different pricing and quantization. We cannot transfer quality or cache behavior measured on an unidentified endpoint to a different FP4 or FP8 route as a verified result. Endpoint availability, prices, promotion and tier constraints must be checked contemporaneously against the [OpenRouter endpoint API](https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints).

**Snapshot fingerprints:** SHA-256 of the trial index bytes: `310cb428fe8914cff21b8edcb0b17256884efca55666bd6d6646d223c77d2ce6`; leaderboard: `a7c15d66288fd249c020b9931c017b92d1a3b90e480b3ff34974b752bd030019`. These mutable source URLs may later serve different bytes. The 50 MB index was read locally for the analysis and is not committed to the repository.

## Benchmark integrity

[Epoch AI's 7 September review](https://epoch.ai/benchmarks/deepswe/review) found false-negative grading issues in at least 23 of 113 v1.1 tasks and rated the benchmark flawed. Its review was partial and stopped after reaching its threshold; it does not establish the actual error rate of every model or that each of the 23 was always misgraded. [Datacurve's v1.1 revision](https://deepswe.datacurve.ai/blog/deepswe-v1-1) predates that review. A subsequent correction or regrading of the exact scored runs has not been verified. Disclose this limitation prominently in any experimental chart; do not claim the benchmark is unbiased or that the error bars account for systematic grading errors.

## Proposed publication criteria

1. Freeze the task set, benchmark and harness versions, attempts, model/effort and grading policy. Use pass@1 with confidence intervals and clearly disclose excluded infrastructure errors and Epoch's findings.
2. For each point, retain usage by call and billing category and all relevant context tiers, cache behavior, discounts, extra charges, and failed/retried calls. Reconcile the actual model and provider identity, route and quantization. Missing evidence is not zero.
3. Compare all verified eligible, available, non-promotional OpenRouter routes using the same actual workload, price each call under the appropriate tier, and retain timestamped source evidence. This is an estimate of the measured workload under a stated route; it is not proof another route would produce the same tokens, cache hits or score.
4. Plot verified attempts per dollar or average USD per attempted task, clearly specify the denominator and excluded calls, and connect only observed comparable effort levels. Do not interpolate missing points or equate software engineering success with general intelligence.
5. Exclude an entire point if any required source, provider, effort, usage, pricing, tier or compatibility evidence is missing. Document exclusions; do not publish an artificial intelligence-only line. Preserve the existing guard until every point and chart output passes validation.

## Decision

The audit cannot yet produce a compliant comparative chart. The missing target models, GLM provider anomaly, missing GLM/DeepSeek cache categories, Astra tier ambiguity, and unresolved grading review are concrete barriers. Obtain authoritative trial telemetry and route metadata or conduct a separately designed benchmark; then rerun the audit. Do not merge or publish a replacement diagram until these checks pass.
