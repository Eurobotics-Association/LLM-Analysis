# LLM-Analysis

![Latest Eurobotics LLM cost / intelligence chart](charts/latest/llm_cost_performance_latest.svg)

**Latest chart:** [SVG](charts/latest/llm_cost_performance_latest.svg) · [source data](data/eurobotics_v11_aa_v43_openrouter_normalized_2026-09-17.csv) · [Matplotlib code](src/generate_latest_chart.py)

LLM-Analysis is a public Eurobotics project for comparing language models used in **DevOps, coding-adjacent agent work, autonomous engineering workflows and AI-assisted software operations**.

## Eurobotics methodology v1.1

The main chart uses:

- **Y-axis — capability:** Artificial Analysis **Intelligence Index v4.3**
- **X-axis — economic cost:** Artificial Analysis measured benchmark **cost per task**, normalized to **standard non-promotional OpenRouter pricing**
- **Rendering:** Python + Matplotlib

The key correction in v1.1 is that reasoning effort now changes the x-position. Low / Medium / High / XHigh / Max may have the same token tariff, but higher effort consumes more tokens. The chart therefore preserves Artificial Analysis' measured task-cost increase instead of putting all efforts on one vertical price line.

### Repricing rule

> **Eurobotics normalized task cost = AA measured cost/task × (OpenRouter blended tariff / AA blended tariff)**

Both tariff blends use Artificial Analysis' documented **7:2:1** convention:

> **70% cache-read + 20% uncached input + 10% output**

This keeps the workload/effort measurement from Artificial Analysis while using OpenRouter as the market-pricing source.

See [docs/methodology.md](docs/methodology.md) for assumptions and limitations.

## Price policy

The baseline uses **standard, non-promotional OpenRouter tariffs**.

Temporary discounts are excluded. In particular, the current 50% Sol promotion is not used as the structural baseline; its underlying OpenAI standard price is used instead. This prevents temporary sales from reversing the normal Terra/Sol cost relationship.

## Current model set

- GPT-5.6 Luna — Low / Medium / High / XHigh / Max
- GPT-5.6 Terra — Low / Medium / High / XHigh / Max
- GPT-5.6 Sol — Low / Medium / High / XHigh / Max
- GLM-5.3 Flash
- DeepSeek **V4.1 Flash** — latest Flash generation
- GLM-5.3 Max
- Qwen3 Coder 30B A3B — intelligence reference only because AA cost/task is currently N/A

## Sources

- Artificial Analysis: https://artificialanalysis.ai/
- OpenRouter: https://openrouter.ai/

Snapshot: **17 September 2026**.

The CSV records the exact model URLs, AA tariff assumptions, OpenRouter standard tariffs, normalization ratios and final x-values.

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/generate_latest_chart.py
```

The GitHub Actions workflow regenerates PNG, PDF and SVG under `charts/latest/` whenever source or data changes.

## Repository structure

- [`charts/latest/`](charts/latest/) — current ready-to-use chart
- [`data/`](data/) — auditable source data
- [`src/`](src/) — Matplotlib generation code
- [`docs/`](docs/) — methodology and supporting notes
- [`charts/historical/`](charts/historical/) — historical charts retained for reference

## Verification principles

Every update should:

1. keep the benchmark name/version visible;
2. record the price-snapshot date;
3. keep Artificial Analysis and OpenRouter source roles explicit;
4. exclude temporary promotions from the baseline unless a promotion-specific chart is explicitly requested;
5. preserve reasoning-effort workload effects;
6. never invent missing benchmark values;
7. keep all transformation formulas reproducible.

## License

- **Code:** MIT License
- **Charts, documentation and curated data:** CC BY 4.0 (see `LICENSE-CONTENT.md`)
