# AGENTS.md — Conventions for automated contributors

This file defines binding conventions for any AI agent or engineer producing a new version of the Eurobotics LLM-Analysis chart and datasets. Read it before generating any artifact.

## 1. Output filename convention

Every generated artifact — charts (PNG, PDF, SVG), data files (CSV, XLSX), and any other exported file (JPG, etc.) — MUST end with the suffix:

`eurobotics_YYMMDD_HHSS`

where YYMMDD is the generation date and HHSS is the generation time (hours + minutes + seconds compressed as HHMMSS truncated to HHSS; keep HH, MM, SS digits so files sort uniquely).

Examples:
- `llm_cost_performance_latest_eurobotics_260918_1445.png`
- `eurobotics_v13_aa_v43_openrouter_nopromo_2026-09-18_eurobotics_260918_1445.csv`

The previous free-form naming (`eurobotics_v12_..._2026-09-18.csv`) is superseded. Keep semantic prefixes if useful, but the `eurobotics_YYMMDD_HHSS` suffix is mandatory and always last before the extension.

## 2. Chart content requirements

The main diagram must contain, in addition to the existing methodology footer:

1. **A clickable link to this repository** (in the PDF/SVG output it must be a real hyperlink, not just text):
   https://github.com/Eurobotics-Association/LLM-Analysis
2. **A clickable link to the benchmark source used for the plotted scores**:
   https://deepswe.datacurve.ai/
   Use `matplotlib` URL support (`ax.text(..., url=...)`) so PDF/SVG viewers open them on click.
3. **The generation date and time** printed on the chart (e.g. "Generated: 2026-09-18 14:45:32 CET") so anyone can tell when the snapshot was produced. Use the actual UTC or Europe/Paris timestamp of the render, not a hardcoded date.

Footer text must stay wrapped to the chart width (see `src/generate_latest_chart.py` `textwrap` block).

## 3. Model set

Add to the plotted model list from v1.3 onward:

- **Claude Sonnet 5.5** — verify the exact current version name and comparable DeepSWE score before plotting, and its non-promotional OpenRouter tariff. Plot as a single point at max effort unless comparable observed effort levels are published.

Consider the existing model set and newer releases, including GLM, DeepSeek, GPT, Gemini, Claude, Mistral, Kimi, Qwen, Llama and Phi. The owner requested removal of GPT-5.6 from the current chart. Plot a model only when the requirements in section 4 can be met; retain earlier snapshots as historical.

## 4. Methodology invariants (do not regress)

- Y-axis: a clearly identified DeepSWE release's comparable pass@1 coding-agent score. Scores from different releases, benchmark versions, configurations, or scopes must not be mixed. Disclose the Epoch AI v1.1 grading review and distinguish its findings from random uncertainty. The proposed change remains under review; publishing stays suspended until the evidence and renderer pass the requirements below.
- X-axis: a transparent estimate of the cost of the comparable measured benchmark workload using only verified, available, **non-promotional OpenRouter provider tariffs**. Benchmark-provider tariffs are not OpenRouter prices and must never be presented as such.
- Select the cheapest eligible OpenRouter provider for the measured token mix, considering uncached input, cache read, output, cache write and any tiered charges that apply. Exclude promotional prices; do not assume a free or special-purpose route is a promotion, but verify its eligibility, availability and compatibility with the benchmark workload, and disclose its constraints. Record provider, model variant, all relevant rates, discount status, availability, source and audit timestamp. Check all eligible routes, not only a model headline. If routes trade off different token-category rates, there may be no universally cheapest route: calculate against the actual workload rather than selecting by a single token rate.
- Reprice actual, comparable benchmark usage by token category and OpenRouter tariff; do not infer an exact workload cost from a 7:2:1 blend, use AA's total unchanged merely because blend ratios match, or invent missing token counts, cache hit rates or cache-write prices. Clearly identify estimates and uncertainty. Do not double-count reasoning tokens when included in output tokens.
- If a model's eligible OpenRouter prices or the benchmark usage required for a defensible cost are not verified, omit the model entirely, including intelligence-only reference lines. Document exclusions and reasons. Do not use another provider's pricing as an OpenRouter substitute.
- Never mix historical Coding Agent Index values with the current Intelligence Index.
- Never use promotional prices in the baseline.
- Plot only verified GPT effort points and do not invent differences where source values are rounded equal; the line must connect only comparable observed effort points.
- Update `docs/methodology.md` and the README in the same change, and commit/push so GitHub actually contains the files (verify by reading back via the GitHub API).

## 5. Version history

- **v1.7 — 2026-10-24:** GPT-6.1 Sol effort curve; Sonnet 5.5, Gemini 4 Argon, Mistral Large 4, and Mistral Small 4; undiscounted OpenRouter price audit; timestamped canonical artifacts.
- **v1.6 — 2026-10-02:** GPT-6 Sol and Luna effort curves, 2 October non-promotional price audit, GLM-5.3 Flash and Mistral Small 3.2 corrections; AA v4.3.2 values for new models.
- **v1.5 — 2026-09-25:** GPT-6 Astra effort curve.
- **v1.4 — 2026-09-18:** Sol list-price correction and expanded model set.
- **v1.3 — 2026-09-18:** non-promotional pricing baseline; Claude Opus 5, Claude Fable 5.1, Gemini 3.1 Pro added; wrapped footer; AGENTS.md conventions introduced.
- **v1.2 — 2026-09-18:** AA v4.3 × OpenRouter repricing with 7:2:1 blend (contained promotional prices; superseded).
- **v1.1 and earlier:** historical, retained in `charts/historical/`.

## 6. Additional requirements for the next version (added 2026-09-18)

### 6.1 Disclaimer on the chart

A short disclaimer in small type must appear at the bottom of the diagram, wrapped to chart width like the other footer lines. Suggested wording (adjust freely but keep all three ideas: informational-only, no budgeting, user verifies):

> Disclaimer: For informational use only - do not use for budgeting. Pricing and benchmark data change frequently; verify current prices and model capability yourself. Eurobotics.org provides this information with no warranty. You are responsible for checking your own pricing and model intelligence requirements.

### 6.2 GitHub Actions rendering

The `render-latest-chart.yml` workflow regenerates timestamped chart artifacts on pushes to `src/` or `data/`, and updates README links to that exact timestamped snapshot. Do not publish a bare `latest` artifact filename. The workflow does not refresh source data from DeepSWE or OpenRouter; price and benchmark refreshes remain an explicit audited step.

### 6.3 Expanded model set (exhaustive small/medium models)

Add these models as single points (max effort, or their only published point), verifying comparable DeepSWE scores, benchmark usage and non-promotional OpenRouter tariffs before plotting:

- **Mistral Small 3**
- **Mistral Medium 3.5**
- **Llama 3.3**
- **Phi-4**

These are candidates alongside section 3. If comparable benchmark usage and eligible OpenRouter prices are unavailable, omit the model from the chart and document the reason, as required in section 4.

### 6.4 Public feedback channel

The repository Issues tab is enabled for the general public. When a chart or methodology change ships, mention in the release or commit message that issues are open for corrections and improvement requests.

## 7. Sol pricing correction (2026-09-18, post-v1.3 audit)

### 7.1 What the audit found

The v1.3 chart intended to use non-promotional OpenRouter prices, but **GPT-5.6 Sol was still plotted at a promotional price**:

- The OpenRouter models API headline for `openai/gpt-5.6-sol` returns **$2.00/M input, $10.00/M output**, which v1.3 treated as the list price.
- OpenRouter's own Sol model page contains an explicit `"discount": 0.5` on that headline price, and its provider-level listing shows the **true list price is $4.00/M input, $20.00/M output**.
- Artificial Analysis independently lists OpenAI's Sol tariff as **$4 / $20** (cache hit $0.40), confirming the OpenRouter $2/$10 figure is the temporary 50% promotion, not a structural list price.
- For contrast, GPT-5.6 Terra's page shows `discount: 0` at $2/$12; Terra was correctly at list price. This is why the published chart made Sol appear artificially cheap and overlapping Terra's cost range.

### 7.2 Historical fix (superseded by section 4)

The earlier audit identified a promotional headline. Current tariffs and providers must be audited afresh using section 4; the old 7:2:1 extrapolation is historical, not a current cost calculation.

### 7.3 Historical annotation

The historical diagram carried this note; do not apply it to a current chart without a current audit:

> (*) About SOL: Price is un-discounted on Sept. 18 2026 - note that there was some temporary discount not taken into account for this diagram.

### 7.4 Issues govern pending methodology work

All proposed methodology, model-set, and chart improvements must be logged as public repository Issues before implementation. The cache-write blend review is tracked in the repository Issues; AGENTS.md records the current binding method only.

### 7.5 Historical GLM-5.3 Flash verification

The 18 September audit recorded a then-current rate. Those figures do not establish current provider pricing or promotional status; re-audit all eligible OpenRouter providers under section 4.


## 8. Tooling preference

Use installed local plugins or MCP tools for the operation whenever a capable one is available. In particular, use the GitHub plugin for repository reads, writes, commits, workflow inspection, and readback verification; use source or browsing tools for live benchmark and pricing checks. Use terminal commands only for work that the available plugin or MCP tools cannot perform, such as local chart rendering or tests. Do not use a terminal command as a substitute for an available plugin or MCP operation.
