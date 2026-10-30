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
2. **A clickable link to the Artificial Analysis Intelligence Index page**:
   https://artificialanalysis.ai/
   Use `matplotlib` URL support (`ax.text(..., url=...)`) so PDF/SVG viewers open them on click.
3. **The generation date and time** printed on the chart (e.g. "Generated: 2026-09-18 14:45:32 CET") so anyone can tell when the snapshot was produced. Use the actual UTC or Europe/Paris timestamp of the render, not a hardcoded date.

Footer text must stay wrapped to the chart width.

## 3. Model set

Add to the plotted model list from v1.3 onward:

- **Claude Sonnet 5.5** — verify the exact current version name and AA Intelligence Index on artificialanalysis.ai before plotting, and its non-promotional OpenRouter tariff. Plot as a single point at max effort unless AA publishes multiple effort levels.

Consider the existing model set and newer releases, including GLM, DeepSeek, GPT, Gemini, Claude, Mistral, Kimi, Qwen, Llama and Phi. The owner requested removal of GPT-5.6 from the current chart. Plot a model only when the requirements in section 4 can be met; retain earlier snapshots as historical.

## 4. Proposed token-price methodology

- Y-axis: one documented version of the Artificial Analysis Intelligence Index, with source and model/effort recorded. Do not mix benchmark versions or historical Coding Agent Index values.
- X-axis: USD per million **output** tokens, on a clearly labeled logarithmic scale. This is a tariff, not a cost per task, dollar value per unit of intelligence, or a bill. Display a prominent warning that different models and efforts use different token quantities.
- For each exact model, select the lowest available non-promotional OpenRouter output tariff among eligible routes supporting reasoning effort. Record the selected provider/endpoint, quantization, service tier and constraints; Flex is not a promotion but may have restrictions. Discounted, unavailable, unsupported and unverified routes do not qualify. This rule minimizes the output rate only and does not establish the cheapest total cost for any workload.
- Record the same route's input, cached-input and cache-write rates, including unknowns and context/time-tier overrides; do not combine the lowest rates from different providers. Prompt, cache, output and tool costs are not captured by the output axis alone.
- AA scores may have been measured using a different endpoint, quantization or harness. Disclose that the price is an associated route quote, not proof that endpoint attains the AA score. Model versions and effort support must be verified. Omit a point if a comparable AA score or eligible OpenRouter output price is not verified.
- Effort points for a single model share the same tariff when the route and tier are unchanged; label each point and connect only observed comparable values. Never move them horizontally by an invented task-cost estimate.
- Use timestamped artifacts, actual render time, clickable source and repository links, and an informational disclaimer. Update README and methodology together. Until approved, keep the legacy renderer and automated publication guard disabled.
- Use Issues for corrections and improvement requests; audit time-sensitive prices, availability and benchmark data before publication.

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

The `render-latest-chart.yml` workflow is suspended while the methodology is under review. A future approved workflow must regenerate timestamped chart artifacts and update README links to the exact snapshot. Do not publish a bare `latest` artifact filename. The workflow does not refresh source data from Artificial Analysis or OpenRouter; price and benchmark refreshes remain an explicit audited step.

### 6.3 Expanded model set (exhaustive small/medium models)

Add these models as single points (max effort, or their only published point), verifying current AA Intelligence Index values and non-promotional OpenRouter tariffs before plotting:

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
