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

Footer text must stay wrapped to the chart width (see `src/generate_latest_chart.py` `textwrap` block).

## 3. Model set

Add to the plotted model list from v1.3 onward:

- **Claude Sonnet 5** — verify the exact current version name and AA Intelligence Index on artificialanalysis.ai before plotting, and its non-promotional OpenRouter tariff. Plot as a single point at max effort unless AA publishes multiple effort levels.

Keep all existing models from methodology v1.3: GPT-5.6 Luna/Terra/Sol (full effort curves), GLM-5.3 Flash, GLM-5.3 Max, DeepSeek V4.1 Flash, Gemini 3.1 Pro, Claude Opus 5, Claude Fable 5.1, and Qwen3 Coder 30B as intelligence-reference only.

## 4. Methodology invariants (do not regress)

- Y-axis: Artificial Analysis Intelligence Index v4.3 (or its documented successor version).
- X-axis: AA measured total evaluation cost repriced to **non-promotional** OpenRouter tariffs via the 7:2:1 blended-tariff ratio.
- Never mix historical Coding Agent Index values with the current Intelligence Index.
- Never use promotional prices in the baseline.
- GPT effort levels must move both vertically and horizontally.
- Update `docs/methodology.md` and the README in the same change, and commit/push so GitHub actually contains the files (verify by reading back via the GitHub API).

## 5. Version history

- **v1.3 — 2026-09-18:** non-promotional pricing baseline; Claude Opus 5, Claude Fable 5.1, Gemini 3.1 Pro added; wrapped footer; AGENTS.md conventions introduced.
- **v1.2 — 2026-09-18:** AA v4.3 × OpenRouter repricing with 7:2:1 blend (contained promotional prices; superseded).
- **v1.1 and earlier:** historical, retained in `charts/historical/`.

## 6. Additional requirements for the next version (added 2026-09-18)

### 6.1 Disclaimer on the chart

A short disclaimer in small type must appear at the bottom of the diagram, wrapped to chart width like the other footer lines. Suggested wording (adjust freely but keep all three ideas: informational-only, no budgeting, user verifies):

> Disclaimer: For informational use only - do not use for budgeting. Pricing and benchmark data change frequently; verify current prices and model capability yourself. Eurobotics.org provides this information with no warranty. You are responsible for checking your own pricing and model intelligence requirements.

### 6.2 GitHub Actions workflow issue (known defect)

The `render-latest-chart.yml` workflow regenerates and commits `charts/latest/llm_cost_performance_latest.*` on every push that touches `src/` or `data/`. Problems for the next agent:

1. **It bypasses the naming convention.** The workflow writes files without the `eurobotics_YYMMDD_HHSS` suffix (see section 1). Either update the script to use timestamped names, or render to timestamped filenames and keep a stable `latest` copy/alias so the README image link keeps working.
2. **README coupling.** The README embeds a fixed chart path; if filenames become timestamped, the workflow (or the script) must update the README image/link line in the same commit, or the README must point at the stable alias.

Additionally, the workflow only re-renders on push; it does not refresh source data from artificialanalysis.ai or openrouter.ai. Data refresh is still manual.

### 6.3 Expanded model set (exhaustive small/medium models)

Add these models as single points (max effort, or their only published point), verifying current AA Intelligence Index v4.3 values and non-promotional OpenRouter tariffs before plotting:

- **Mistral Small 3**
- **Mistral Medium 3.5**
- **Llama 3.3**
- **Phi-4**

These join the existing set in section 3 (Claude Sonnet 5 included). If AA does not publish a comparable total evaluation cost for one of them, plot it as an intelligence reference line only (same treatment as Qwen3 Coder 30B) and note why in the CSV and methodology doc.

### 6.4 Public feedback channel

The repository Issues tab is enabled for the general public. When a chart or methodology change ships, mention in the release or commit message that issues are open for corrections and improvement requests.

## 7. Sol pricing correction (2026-09-18, post-v1.3 audit)

### 7.1 What the audit found

The v1.3 chart intended to use non-promotional OpenRouter prices, but **GPT-5.6 Sol was still plotted at a promotional price**:

- The OpenRouter models API headline for `openai/gpt-5.6-sol` returns **$2.00/M input, $10.00/M output**, which v1.3 treated as the list price.
- OpenRouter's own Sol model page contains an explicit `"discount": 0.5` on that headline price, and its provider-level listing shows the **true list price is $4.00/M input, $20.00/M output**.
- Artificial Analysis independently lists OpenAI's Sol tariff as **$4 / $20** (cache hit $0.40), confirming the OpenRouter $2/$10 figure is the temporary 50% promotion, not a structural list price.
- For contrast, GPT-5.6 Terra's page shows `discount: 0` at $2/$12; Terra was correctly at list price. This is why the published chart made Sol appear artificially cheap and overlapping Terra's cost range.

### 7.2 The fix (mandatory from now on)

- **Sol must always be priced at its un-discounted OpenRouter tariff: $4.00/M input, $20.00/M output, $0.40/M cache read** (unless a future audit shows OpenRouter has made that the actual list price with no discount field).
- With the list tariff, the Sol OpenRouter/AA blended ratio is **1.0** (blended $3.08 = AA blended $3.08), so Sol's estimated costs equal the AA measured totals: roughly **$637 / $997 / $1,487 / $2,082 / $3,465** for Low to Max. The Sol curve sits to the **right of Terra**, consistent with its higher Intelligence Index (47 vs 42).
- Any model whose OpenRouter page shows a `discount` field on its headline price must be repriced to the pre-discount listing (or the provider list price) for the baseline. The headline API price alone is not proof of list price.

### 7.3 On-chart annotation

The diagram must carry a small note near the Sol curve:

> (*) About SOL: Price is un-discounted on Sept. 18 2026 - note that there was some temporary discount not taken into account for this diagram.

### 7.4 Related methodology note (do at next revision)

OpenRouter charges a **cache-write tariff** (e.g. $2.50/M on OpenAI models) that the 7:2:1 blended-tariff formula (cache-read/input/output) does not include, while AA measured costs do include cache-write cost. This slightly understates cache-heavy reasoning models. Consider a 7:2:1:1 blend (adding 10% cache-write) or an explicit correction in a future methodology version.

### 7.5 GLM-5.3 Flash verification (no change needed)

The audit also verified GLM-5.3 Flash at **$0.09/$0.30 ($0.018 cache read), discount field 0** on OpenRouter's current page - a genuine list price, not a promo. The older $0.075/$0.25 promo (discount 0.5) still appears in page data but is not the headline. The chart's GLM Flash point is valid as-is.

