# LiveBench 2.0 × OpenRouter: feasibility audit

**Draft for review, 30 October 2026. No replacement cost chart is published.** This investigates [issue #10](https://github.com/Eurobotics-Association/LLM-Analysis/issues/10) and the pricing correction in [issue #9](https://github.com/Eurobotics-Association/LLM-Analysis/issues/9).

## Sources inspected

- [LiveBench 2.0 leaderboard](https://livebench.ai/#/) and [methodology](https://livebench.ai/#/methodology), viewed 30 October 2026, release dated 25 October. The site identifies Abacus.AI as sponsor and says results are used for its commercial agent; it should not be described as independent or assumed open-source merely because its methodology is public.
- [LiveBench v1 source repository](https://github.com/LiveBench/LiveBench) and [original paper](https://arxiv.org/abs/2406.19314): these describe the earlier benchmark and do not establish that the 2.0 harness, tasks, or telemetry are publicly available or use identical methods.
- [OpenRouter GLM endpoint API](https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints), [DeepSeek endpoint API](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash-1017/endpoints), and [GPT-6.1 Sol endpoint API](https://openrouter.ai/api/v1/models/openai/gpt-6.1-sol/endpoints). Endpoint listings and availability change; a fresh full audit is required before choosing any route.

The LiveBench 2.0 methodology describes public files containing per-model/per-suite scores, cost and task counts, subcategory scores, release notes and category weights. It does not state that those files include uncached input, cache-read, cache-write or output token counts per model and request. On inspection the documented directly constructed cost/table URLs returned 404; the GitHub connector also returned 404 for the referenced `LiveBench/new-livebench` repository. These access failures do not prove the records do not exist elsewhere. The rendered leaderboard and methodology were accessible. No sufficiently detailed usage data was verified for any model, including those below.

## What the current leaderboard shows

These are LiveBench scores, not OpenRouter prices. They were read from the 25 October 2026 leaderboard on 30 October 2026.

| Display name | Overall score | Agentic | Coding | Observed configuration |
|---|---:|---:|---:|---|
| GPT-6.1 Sol | 84.1 | 68.7 | 96.0 | Highest supported effort per LiveBench's general rule; exact row-specific configuration still to verify |
| GPT-6.1 Terra | 77.8 | 48.6 | 94.3 | Same qualification |
| DeepSeek V4.1 Flash 1017 | 74.0 | 40.9 | 96.0 | Same qualification |
| GLM-5.3 Flash | 62.1 | 19.0 | 80.6 | Same qualification |

LiveBench reports seven suites: agentic (18 tasks), coding (29), browser use (25), research (22), design (25), reasoning (202 questions), and data analysis (150 questions). The published overall is a weighted mean of available suite scores: agentic weight 2, coding and design 1.5 each, the remaining suites 1 each. Missing suites are omitted from the mean, while a measured zero counts. A fault that recurs on a rerun is scored zero; one run per suite is reported. These choices, task mixture, model/tool scaffold, version, provider and effort can materially affect comparison. A single run does not establish uncertainty or a universal intelligence score.

LiveBench's displayed cost-per-successful-task divides its cost per task by its score as a fraction. Since tasks can earn partial credit and overall scores have different suite weights from its cost denominator, this is a **score-normalized cost metric**, not necessarily observed dollars per independently verified successful task or expected cost of retries. The costs use LiveBench's provider rates, and exclude some fixed starting state and harness helper calls. We cannot use these numbers as OpenRouter spend or recover the underlying token mix from them.

## Proposed methodology for a future diagram

1. Choose one frozen LiveBench release and one clearly named scope. Use the same complete suites, model configurations, scoring weights and task set for every plotted point; exclude incomplete rows. Scores from LiveBench 1 and 2, different releases or different harnesses are not interchangeable. Display the suite weights, version and relevant limitations.
2. Obtain auditable usage from the **same runs** that produced those scores, including every billable model call, failures and reruns according to a stated policy. The usage must distinguish uncached input, cache reads, cache writes (including duration where applicable), output including reasoning, and any other billable components. For tiered/context-dependent prices retain per-request context and timing. Establish whether cache counts are subsets of input before summing. A published cost, output-only count or guessed fixed ratio cannot substitute for these records.
3. Audit all eligible OpenRouter endpoints at a timestamp. Record provider, exact model revision, quantization, availability, route restrictions, input/output/cache/write prices, tier conditions and promotional status. Compare the full workload cost for each compatible non-promotional route; category-by-category cheapest rates cannot be spliced across different routes. Do not silently equate a lower-precision endpoint with the benchmarked endpoint.
4. Compute the sum of actual billable quantities times the applicable OpenRouter rates for each request, divided by one million where rates are quoted per million tokens. Include all relevant costs, count reasoning only once when included in output, and make the cache-write accounting consistent with provider tariff definitions. Label it an **estimated repricing of observed usage**, not an invoice or proof that the alternative route achieves the same quality or usage.
5. Prefer cost per benchmark attempt (total repriced cost / number of attempted tasks) against LiveBench score. If a separately defined binary success rate and comparable retry policy are verifiable, an additional cost-per-success estimate may be shown, explicitly labeled. Do not claim LiveBench's partial-credit normalized metric is observed success cost.
6. Omit any point without the required matching score, usage, eligible tariff and provider compatibility evidence. Keep a dated exclusion log and references. Keep the existing renderer and workflow publication guard in place until this evidence and an updated renderer exist.

## Decision gate and next checks

No compliant point or replacement diagram is established by this audit. First obtain the 2.0 per-request records, provider/quantization identities, effort settings, scoring and task coverage for the four models above. Check whether cache write and context tiers are recorded and whether the results correspond to the same task set. Then perform a complete contemporaneous OpenRouter provider audit. If records are unavailable, an independently scoped LiveBench evaluation run through OpenRouter could produce usage and scores together, subject to task/harness availability and a separately approved spending budget; it would be a new evaluation, not a reconstruction of the published leaderboard.

Corrections and improvement requests are welcome through [repository issues](https://github.com/Eurobotics-Association/LLM-Analysis/issues).
