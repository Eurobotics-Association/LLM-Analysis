# LLM-Analysis

![Latest Eurobotics LLM cost / intelligence chart](charts/latest/llm_cost_performance_latest.svg)

**Latest chart:** [SVG](charts/latest/llm_cost_performance_latest_eurobotics_260918_1838.svg) · [PNG](charts/latest/llm_cost_performance_latest_eurobotics_260918_1838.png) · [PDF (clickable links)](charts/latest/llm_cost_performance_latest_eurobotics_260918_1838.pdf) · [source data](data/eurobotics_v14_aa_v43_openrouter_nopromo_eurobotics_260918_1512.csv) · [Matplotlib code](src/generate_latest_chart.py)

LLM-Analysis is a public Eurobotics project for comparing language models used in **DevOps, coding-adjacent agent work, autonomous engineering workflows and AI-assisted software operations**.

## Eurobotics methodology v1.4 (current)

- **Y-axis — capability:** Artificial Analysis **Intelligence Index v4.3**
- **X-axis — estimated total API cost:** AA measured evaluation workload repriced to **current non-promotional OpenRouter pricing**
- **Rendering:** Python + Matplotlib
- **Chart artifacts** follow the `eurobotics_YYMMDD_HHSS` naming convention and the PDF embeds clickable links to this repository and artificialanalysis.ai. See [AGENTS.md](AGENTS.md).

The repricing formula:

> Estimated OpenRouter total evaluation cost = AA total evaluation cost × (OpenRouter blended tariff / AA reference blended tariff)

with the blended tariff defined as 70% cache-read + 20% uncached input + 10% output. See [docs/methodology.md](docs/methodology.md).

## Pricing policy

The baseline uses **normal (non-promotional) OpenRouter list pricing**. The Sol price was audited after v1.3 and corrected: OpenRouter's API headline ($2/$10) carries a `"discount": 0.5` field; the true list price is **$4/M input, $20/M output**, matching Artificial Analysis' reference tariff. The chart now uses the un-discounted price and carries an on-chart annotation about it. See [AGENTS.md](AGENTS.md) section 7 for the full audit.

## Model set (v1.4)

- GPT-5.6 Luna — Low / Medium / High / XHigh / Max (curve)
- GPT-5.6 Terra — Low / Medium / High / XHigh / Max (curve)
- GPT-5.6 Sol — Low / Medium / High / XHigh / Max (curve, un-discounted list price)
- Claude Sonnet 5 (max) — single point (Index 38.4, est. $6,998)
- Claude Opus 5 (Max) — single point (Index 50.7, est. $7,275)
- Claude Fable 5.1 (Max) — single point (Index 53.4, est. $13,129)
- Gemini 3.1 Pro Preview — single point (Index 30.4, est. $1,310)
- GLM-5.3 (Max) — single point (Index 44.9, est. $2,503)
- GLM-5.3 Flash — single point (Index 41.9, est. $173)
- DeepSeek V4.1 Flash (Max) — single point (Index 39.5, est. $238)
- Mistral Medium 3.5 (Max) — single point (Index 14.9, est. $1,160)
- Mistral Small 3.2 (Max) — single point (Index 7.0, est. $327 at current OpenRouter tariff)

Intelligence reference only (AA publishes no comparable total evaluation cost): **Qwen3 Coder 30B** (Index 9.6), **Llama 3.3 70B** (Index 7.7), **Phi-4** (Index 5.9).

## Why effort levels move both directions

Reasoning effort changes both the AA Index (vertical) and the measured token workload (horizontal). Higher effort consumes more tokens even at an unchanged per-token tariff, so GPT curves run up and to the right.

## Sources

- Artificial Analysis: https://artificialanalysis.ai/
- OpenRouter: https://openrouter.ai/
- Repository: https://github.com/Eurobotics-Association/LLM-Analysis (issues open for corrections and suggestions)

## Disclaimer

This is for informational use only. Do not use for budgeting. Check pricing by yourself. Eurobotics.org provides this information with no warranty and you are responsible for checking your own pricing and model intelligence requirements.

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/generate_latest_chart.py
```

## Repository structure

- [`charts/latest/`](charts/latest/) — latest ready-to-use chart (timestamped filenames)
- [`data/`](data/) — auditable source and derived data
- [`src/`](src/) — Matplotlib generator
- [`docs/`](docs/) — methodology
- [`charts/historical/`](charts/historical/) — historical charts retained for reference

## License

- **Code:** MIT License
- **Charts, documentation and curated data:** CC BY 4.0 (see `LICENSE-CONTENT.md`)

