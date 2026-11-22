# Matched Vals trajectory feasibility test

**31 October 2026, review only.** Follow-up to [#16](https://github.com/Eurobotics-Association/LLM-Analysis/issues/16) and draft PR #17. No paid evaluations, external messages, benchmark plots or main-branch changes.

## Decision

**Go for Vals as the leading current capability source; no-go for an OpenRouter-priced task comparison from the inspected public UI alone.** The viewer exposes model calls on the same task, but its cache percentages are rounded, and exact cache writes, route identity and complete billing semantics were not located. These gaps apply to both proprietary and open-weight models. A reliable bulk data interface and reproducible license/refresh process also remain unverified. This is a bounded UI audit, not proof that complete records do not exist elsewhere.

[Princeton HAL](https://github.com/princeton-pli/hal-harness) is **no-go as the main refresh source**: its own repository says updates have paused and the GitHub API marks it archived. HAL remains a useful historical source for agent evaluation methodology and trajectories. Its [website](https://hal.cs.princeton.edu/) says traces include model calls and are distributed encrypted to discourage automated scraping; do not treat historical HAL prices as OpenRouter prices. We did not decrypt or independently validate a full HAL run because the explicitly paused update policy already fails the key freshness requirement.

## Reproducible two-model UI inspection

On 31 October, open [Vals Terminal-Bench 4.0 trajectories](https://www.vals.ai/benchmarks/terminal-bench-4/trajectories), select task **ATRX-VEP-CRISPR**, and choose each model. The model menu showed 100% criteria passed for this task for both models; this is the viewer's task-level display, not independently verified per-run outcome. The initially selected trajectory showed:

| Model chosen | Steps | Input tokens | Output tokens | Vals cost for displayed trajectory |
|---|---:|---:|---:|---:|
| GPT-6.1 Sol | 17 | 583,056 | 34,654 | $0.6034 |
| DeepSeek V4.1 Flash 1017 | 106 | 10,114,646 | 138,686 | $0.2552 |

Values are from the interactive viewer and **are not OpenRouter prices**. One task and one selected run do not establish average task costs, comparative capability, or the cause of differences. The 17/106 include initial prompt steps; no claim that all are uniquely billable calls. Effort, actual upstream provider and per-run pass status were not independently established in this UI inspection. Examples: one GPT step showed 3,150 input with 54% cached; one DeepSeek step showed 2,590 input with 79% cached. Those percentages do not establish exact billed cache counts. The task name identifies the same displayed task; exact sandbox revision, fallback handling and all retry events still need verifying.

## Concrete tariff issue

The [OpenRouter GPT-6.1 Sol endpoint listing](https://openrouter.ai/api/v1/models/openai/gpt-6.1-sol/endpoints) viewed October 31 lists OpenAI standard at $2 input / $10 output / $0.10 cache read / $2.50 cache write per million tokens, with higher rates starting at 272,000 prompt tokens per request. A flex route is displayed at half those base rates with discount zero, but the field alone does not establish its availability, timing, feature support or compatibility with this workload. Other endpoints exist; no route was selected or established as globally cheapest. An actual 583,056-token task total does not establish that any one call crossed the tier. Rounded read rates and unverified writes prevent reproducing even this task exactly. Rates may change and require a fresh audit before any publication. Provider cache behavior and counts cannot automatically be transferred to an alternative route.

## The next evidence gate

1. Find an authorized machine-readable Vals export containing exact per-call token counts (uncached, read and write, write TTL, output/reasoning inclusion), request context, model and provider identity, effort actually sent, task/attempt IDs, outcome, errors, retries and helper calls. The interactive UI's rounded cache percentages cannot supply these precisely. Establish license, stable access and refresh cadence.
2. Reconcile one successful and one failed attempt for both GPT-6.1 Sol and DeepSeek to the benchmark outcome and all calls; compare exact task and harness version and provider/quantization. Then cover all attempted tasks before calculating a point.
3. Capture all eligible available non-promotional OpenRouter routes and rates, including tier and extra charges; calculate each route's full workload only when route compatibility and billing-category semantics are established. If changing route, label the result a conditional repricing, not an observed invoice or proof that scores and cache hits remain unchanged.
4. If these records are unavailable, request them from Vals or a data provider with explicit authorization to contact them. Alternatively propose a separate diagram using the evaluator's own prices, clearly identified and pending agreement to amend the OpenRouter-only rule. Neither a fixed token blend nor extrapolation from the two displayed runs supplies missing evidence.

The [source-selection study](refreshable-task-source-selection.md) describes other academic and general-work candidates. Public issues are open for corrections and improvements.
