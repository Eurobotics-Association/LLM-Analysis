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

