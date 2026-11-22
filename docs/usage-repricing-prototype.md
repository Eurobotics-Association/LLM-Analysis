# Prototype: measured benchmark usage × OpenRouter tariffs

**Review experiment, 3 November 2026.** Related to [#16](https://github.com/Eurobotics-Association/LLM-Analysis/issues/16), [#9](https://github.com/Eurobotics-Association/LLM-Analysis/issues/9) and draft [#17](https://github.com/Eurobotics-Association/LLM-Analysis/pull/17). No chart is generated. The current token-price chart remains unchanged.

## Recommendation and decision

The proposed design is valid: take a **single benchmark's comparable overall score and usage from the same measured attempts**, reprice each billable category using an audited eligible OpenRouter provider, and chart score against cost per task. Use the same method for all model families and each observed reasoning setting. AA Intelligence Index could be the y-axis only when the corresponding AA workload's usage is available; another benchmark's token use does not describe the cost of AA's tasks. COSPA is a useful public-data test but its overall score measures coding tasks, not general intelligence.

The actual test below produces **two output-charge components**, not full task costs. It succeeds as an arithmetic and data-join prototype but **fails the publication gate** for a verified cost comparison. Missing cache and route/tier evidence means an exact OpenRouter cost cannot be reconstructed. No unverified x-coordinates are proposed, no rate is claimed to be the cheapest eligible endpoint, and source-provider quality equivalence is not established.

## Test on an actual public dataset

[COSPA official336 report](https://github.com/shisa-ai/cospa/blob/main/reports/cost-performance-official336.md) says each campaign covers the same 336 coding tasks, with one attempt per task. The [points file](https://github.com/shisa-ai/cospa/blob/main/reports/cost-performance/points.json) (Git blob `da888bea6dfdd09faf345309731bb631a54294e1`, read 3 November) joins pass counts and total input/output usage. Its scores are a proportion of tasks passed, **not AA Intelligence Index**. Model names and exact effort must remain as published.

| Model and effort | Score | Input tokens | Output tokens | Run ID |
|---|---:|---:|---:|---|
| GPT-5.6 Luna low | 119/336 = 35.42% | 20,848,421 | 637,499 | `gpt56luna-vanilla-low-official336-c8-20260830` |
| DeepSeek V4 Flash 0731 low | 108/336 = 32.14% | 281,114,680 | 3,287,541 | `ds4-vanilla-low-matrix-c8-20260818` |

Public usage is matched at campaign level, not yet independently reconciled with every scored task, error and retry. COSPA identifies the GPT run as `codex/gpt-5.6-luna`, and DeepSeek as `local/deepseek-v4-flash-0731`. An OpenRouter endpoint is therefore a **counterfactual**: model revision, serving stack, quantization, settings, cache and token use might differ. COSPA's own cost numbers use configured rates and must not be relabelled OpenRouter prices. This historical set lacks current frontier coverage and demonstrably regular updates.

### Calculation actually tested

The [OpenRouter GPT-5.6 Luna model page](https://openrouter.ai/openai/gpt-5.6-luna), captured through browsing 3 November, lists OpenAI standard output at $1.20 per million. The [DeepSeek V4 Flash 0731 provider page](https://openrouter.ai/deepseek/deepseek-v4-flash-0731) showed DeepInfra output at $0.18 per million in a search snapshot. These are illustrative listed output rates only. Discount fields, real-time route availability, matching revision/precision, all eligible routes and applicable tiers were **not** verified end to end.

For a flat output rate, the output component is `output_tokens / 1,000,000 × output_rate / 336`:

| Run | Calculation | Output component / attempted task |
|---|---|---:|
| Luna low | 637,499 × $1.20 / 1,000,000 / 336 | $0.002277 |
| DeepSeek low | 3,287,541 × $0.18 / 1,000,000 / 336 | $0.001761 |

These figures **exclude all input, cache, writes, tools, retries not present in totals and any tier differences**. They are not prices paid, not total cost estimates, not a provider ranking, and not proof that either selected route would reproduce the score. They are not unconditional lower bounds on costs across providers; they are only conditional output components at the displayed hypothetical rates. Because the DeepSeek endpoint page and endpoint API differ or change over time, rates must be freshly audited before use. The user's current chart excludes GPT-5.6; its use here is solely an historical arithmetic test.

## What is required to turn it into a task-cost point

For every model and effort:
1. Freeze identical benchmark revision, task set, agent setup and task outcome/attempt policy. Identify exact model/quantization/provider, effort parameter and time.
2. Obtain billable per-call uncached input, cache read and write, output including reasoning, request context and tier, other charges, failed attempts and retries. Establish whether read/write counts overlap input; output reasoning must not be double-counted. The COSPA points file has input/output totals but not the distinct cache categories or per-request tiers. Missing is unknown, not zero.
3. Snapshot all eligible, available non-promotional OpenRouter endpoints, discount status, provider/variant, rates, context tiers, extra charges and constraints. Compute each provider's cost across the *whole measured mix* and select the lowest compatible route; do not combine categories across providers. Reproducing behavior and cache hits on a different provider is not guaranteed.
4. Sum all call costs and divide by the number of attempted tasks, including failures and retries. Show binary success rate against cost per attempt, with cost per success = all costs / passes where passes > 0 and coverage and uncertainty. A weighted or partial-credit index is a score, not a success probability.
5. Audit an entire common model cohort before publishing a diagram. For maintained coverage, investigate exact export and effort coverage on [Vals Terminal-Bench 4.0](https://www.vals.ai/benchmarks/terminal-bench-4) alongside [SKYEVAL](https://skyeval.com/sla/leaderboard?type=official). Recent observations are not a guarantee of continuing refresh.

## AA path

[AA's API reference](https://artificialanalysis.ai/data-api/docs/reference) says the free model endpoint excludes intelligence-evaluation token counts; Pro includes additional token data. We do not have Pro access and have not verified that Pro contains the request-level cache/write/tier records needed to price the exact workload. [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) says its cost uses provider-reported token counts where available together with live measurements of typical cache hits, rather than necessarily the evaluation run's actual cache behavior. Its reported overall cost or a 7:2:1 tariff ratio cannot recover missing categories. The existing AA Index versus OpenRouter output-token price chart remains useful, but is not task cost.

**Next concrete gate:** obtain a public or voluntarily provided exact billing ledger joined to comparable scored runs, or run a separately scoped small benchmark with a pre-agreed budget and full instrumentation. Until then the above arithmetic is an output-only diagnostic, not a verified cost estimate or chart. Public issues are open for corrections and improvements.
