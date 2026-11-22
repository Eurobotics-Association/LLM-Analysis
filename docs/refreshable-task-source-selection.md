# Refreshable task-based source: recommendation

Research update 31 October 2026, for [issue #16](https://github.com/Eurobotics-Association/LLM-Analysis/issues/16) and draft PR #17. Earlier research did not inspect the current Vals successor and its trajectories deeply enough.

## Decision

Select [Vals Terminal-Bench 4.0](https://www.vals.ai/benchmarks/terminal-bench-4) as the leading source for the proposed task-based comparison, subject to a full telemetry and OpenRouter pricing audit. It was updated October 29, covers GPT-6.1 Sol/Terra and Astra, Claude, Gemini, GLM and DeepSeek V4.1 Flash 1017, and has an effort comparison for selected models, including Astra, GLM and DeepSeek. It does not demonstrate every effort for every GPT. Its recent update is evidence of recency, not a guaranteed update cadence.

Vals evaluates 66 terminal tasks spanning software, science, ML, operations, hardware, security and media. It describes a common mini-swe-agent harness, three runs per task, binary grading and uncertainty across the three run-level scores. This covers technical agent work, not all general work. Vals is a commercial evaluator, and its published prices must not be labelled OpenRouter prices.

As one source-reported example, GPT-6.1 Sol scored 55.05% at $1.72/test and DeepSeek V4.1 Flash 1017 scored 31.82% at $0.54/test. These are **Vals' results and costs**, not a verified OpenRouter cost comparison. They demonstrate an open-weight model can appear cheaper in another measured task setup; they do not prove bias in AA or universal superiority.

## Direct trajectory inspection

The [Vals trajectory viewer](https://www.vals.ai/benchmarks/terminal-bench-4/trajectories) offers models including GPT-6.1 Sol, GPT-6 Astra, GLM 5.3 and DeepSeek V4.1 Flash 1017. On October 31 its default Claude Fable 5 run for ATRX-VEP-CRISPR showed 54 steps, 6,217,844 input and 261,048 output tokens. One step showed 140,679 input, 95% cached, and 13,908 output. The viewer shows per-step counts and Vals costs, but the cached percentage is rounded. Exact cache read/write quantities, write TTL, actual provider/quantization, per-call tier, fallback/helper billing and an authorized bulk export remain unverified. This is promising evidence, not a complete OpenRouter billing ledger.

If exact joinable records and compatible non-promotional OpenRouter routes are established, compute the cost of every scored attempt and chart success versus cost/attempt using the same task and error policy for both model families. Connect only observed effort settings with matched configuration. If these records are unavailable, keep capability information separate and link to Vals' independently labelled costs; do not publish them as OpenRouter prices. A separately labeled alternative-source cost diagram would require changing the project's pricing requirement.

## Broader search

| Source | Relevance | Freshness and cost limitations |
|---|---|---|
| [Vals Index v2.1](https://www.vals.ai/benchmarks/vals_index_v2_1) | Current multidomain finance, coding, legal and tax scores including GPT, GLM and DeepSeek. | Useful general-work companion. Composite weights and setups differ from Terminal-Bench; costs are not verified OpenRouter prices. |
| [Princeton HAL](https://hal.cs.princeton.edu/) and [paper](https://arxiv.org/abs/2510.11977) | Princeton-led multi-institution work reports 21,730 agent rollouts and releases model-call traces for diverse benchmarks. | Search surfaced primarily 2025 model results; direct page access returned 403 in this audit. Current-model cadence and complete route/billing data not established. |
| [OpenCompass](https://github.com/open-compass/opencompass) and [leaderboard rules](https://opencompass.org.cn/rules/en/) | Broad Chinese evaluation framework across proprietary and open-weight models. | Monthly manufacturer application limits are not a guaranteed monthly publication schedule. Exact matching billing ledger and cost-per-task coverage not verified. |
| [Tsinghua AgentBench](https://github.com/THUDM/AgentBench) | Open academic agent benchmark and harness. | Current leaderboard refresh and OpenRouter billing telemetry not verified. |
| [COSPA official336](https://github.com/shisa-ai/cospa/blob/main/reports/cost-performance-official336.md) | Public common-task effort results and a historical cross-check. | Report metadata observed September 9; new-model update cadence not established. Configured prices are not a complete OpenRouter audit. |
| [LiveBench 2.0](https://livebench.ai/) | Recent broad general-work capability results, including open-weight and proprietary families. | Matching public per-call billing and broad effort coverage remain unverified. |

No unsupported claims are made about the existence or absence of projects at MIT, the Chinese Academy of Sciences, or Tianjin University. Academic affiliation does not by itself demonstrate ongoing coverage or complete telemetry.

## Next work

1. Pin Vals' version, task IDs, exact run dates, models, effort settings and harness; inspect GPT, GLM and DeepSeek successful and failed attempts and identify refusals/fallbacks.
2. Locate an authorized machine-readable trajectory/usage export with exact per-call uncached, cache-read/write and output counts, request context, route identity, retries and helper calls. Reconcile it to the Vals score. Rounded cache percentages alone are insufficient.
3. For qualifying runs, audit every eligible OpenRouter endpoint, non-promotional status, full rates, tier and quantization. Price the complete workload per route. Alternative-provider results are conditional because model behavior, tokenization and cache can change.
4. Publish an experimental table with costs, outcomes, provenance, uncertainty and exclusions only after verification. Keep benchmark versions and dissimilar harnesses apart.
5. Check source changes monthly and after major model releases; record the latest observed update and run dates, flag stale coverage and reassess. This is the project's proposed checking schedule, not Vals' commitment.

No benchmark calls, expenditure, external outreach or chart publication were performed. Issues are open for corrections and improvements.
