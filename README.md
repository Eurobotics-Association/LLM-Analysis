# LLM-Analysis

![Latest Eurobotics LLM cost / intelligence chart](charts/latest/llm_cost_performance_latest.svg)

**Latest chart:** [SVG](charts/latest/llm_cost_performance_latest.svg) · [PNG](charts/latest/llm_cost_performance_latest.png) · [PDF](charts/latest/llm_cost_performance_latest.pdf) · [source data](data/eurobotics_v13_aa_v43_openrouter_nopromo_2026-09-18.csv) · [Matplotlib code](src/generate_latest_chart.py)

LLM-Analysis is a public Eurobotics project for comparing language models used in **DevOps, coding-adjacent agent work, autonomous engineering workflows and AI-assisted software operations**.

## Eurobotics methodology v1.3 (current)

- **Y-axis — capability:** Artificial Analysis **Intelligence Index v4.3**
- **X-axis — estimated total API cost:** AA measured evaluation workload repriced to **current non-promotional OpenRouter pricing**
- **Rendering:** Python + Matplotlib

The repricing formula:

> Estimated OpenRouter total evaluation cost = AA total evaluation cost × (OpenRouter blended tariff / AA reference blended tariff)

with the blended tariff defined as 70% cache-read + 20% uncached input + 10% output. See [docs/methodology.md](docs/methodology.md).

## Pricing policy

The baseline uses **normal (non-promotional) OpenRouter list pricing**. Temporary promotional discounts are excluded because they distort structural comparisons between models. Sol's former 50% promo and GLM-5.3 Flash's 50% promo are therefore no longer in the baseline; GLM Flash is plotted at its normal $0.09/$0.30 tariff.

## Model set

- GPT-5.6 Luna — Low / Medium / High / XHigh / Max (curve)
- GPT-5.6 Terra — Low / Medium / High / XHigh / Max (curve)
- GPT-5.6 Sol — Low / Medium / High / XHigh / Max (curve)
- GLM-5.3 Flash — single point (Index 41.9, est. $173)
- GLM-5.3 (Max) — single point (Index 44.9, est. $2,503)
- DeepSeek V4.1 Flash (Max) — single point (Index 39.5, est. $238)
- Gemini 3.1 Pro Preview — single point (Index 30.4, est. $1,310)
- Claude Opus 5 (Max) — single point (Index 50.7, est. $7,275)
- Claude Fable 5.1 (Max) — single point (Index 53.4, est. $13,129)
- Qwen3 Coder 30B A3B — intelligence reference only (Index 9.6); AA publishes no comparable total evaluation cost for it

Sanity check: GLM-5.3 Flash (est. $173) vs Terra High (est. $768) is a ~4.4× gap; against Terra Max it is ~14×. The user-remembered ~6× practical gap sits between these, consistent with mid-effort Terra usage. The extreme left position of GLM Flash is real at current OpenRouter tariffs.

## Why effort levels move both directions

Reasoning effort changes both the AA Index (vertical) and the measured token workload (horizontal). Higher effort consumes more tokens even at an unchanged per-token tariff, so GPT curves run up and to the right.

## Sources

- Artificial Analysis: https://artificialanalysis.ai/
- OpenRouter: https://openrouter.ai/

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/generate_latest_chart.py
```

## Repository structure

- [`charts/latest/`](charts/latest/) — latest ready-to-use chart
- [`data/`](data/) — auditable source and derived data
- [`src/`](src/) — Matplotlib generator
- [`docs/`](docs/) — methodology
- [`charts/historical/`](charts/historical/) — historical charts retained for reference

## License

- **Code:** MIT License
- **Charts, documentation and curated data:** CC BY 4.0 (see `LICENSE-CONTENT.md`)

