# LLM-Analysis

![Latest Eurobotics LLM cost / intelligence chart](charts/latest/llm_cost_performance_latest.png)

**Latest chart:** [PNG](charts/latest/llm_cost_performance_latest.png) · [PDF](charts/latest/llm_cost_performance_latest.pdf) · [SVG](charts/latest/llm_cost_performance_latest.svg) · [source data](data/eurobotics_llm_index_v43_openrouter_2026-09-17.csv) · [Matplotlib code](src/generate_latest_chart.py)

LLM-Analysis is a public Eurobotics project for comparing language models used in **DevOps, coding-adjacent agent work, autonomous engineering workflows, and AI-assisted software operations**.

## Eurobotics methodology

The main chart uses **two independent sources on purpose**:

- **Y-axis - capability:** Artificial Analysis **Intelligence Index v4.3**
- **X-axis - market price:** current **OpenRouter API pricing**
- **Charting:** Python + Matplotlib

The rationale is simple: use an independent benchmark for capability and use the market price that an API user can actually see and buy through OpenRouter.

### One price number per model

OpenRouter publishes separate input and output prices. Eurobotics therefore defines a transparent reference tariff:

> **Eurobotics blended API tariff = 75% input price + 25% output price**

The result is expressed in USD per 1 million tokens. This is a **reference tariff**, not a prediction of the final cost of a real task.

For GPT-5.6, reasoning effort changes benchmark performance but not the API price per token. Therefore Low / Medium / High / XHigh / Max appear vertically at the same x-coordinate. Higher reasoning effort may still consume more tokens in a real workload.

Promotional OpenRouter prices are used when they are the current headline price and are marked as such. Every chart is therefore a dated price snapshot.

See [docs/methodology.md](docs/methodology.md) for the full method and assumptions.

## Models currently included

- GPT-5.6 Luna - Low / Medium / High / XHigh / Max
- GPT-5.6 Terra - Low / Medium / High / XHigh / Max
- GPT-5.6 Sol - Low / Medium / High / XHigh / Max
- GLM-5.3 Flash
- DeepSeek **V4.1 Flash** - latest Flash generation
- GLM-5.3 Max
- Qwen3 Coder 30B A3B

## Current snapshot

**17 September 2026**

Notable current OpenRouter headline prices used by the chart include:

| Model | Input / 1M | Output / 1M | Eurobotics blend |
|---|---:|---:|---:|
| GLM-5.3 Flash | $0.075 | $0.25 | $0.11875 |
| Qwen3 Coder 30B A3B | $0.07 | $0.27 | $0.12 |
| DeepSeek V4.1 Flash | $0.15 | $0.60 | $0.2625 |
| GPT-5.6 Luna | $0.20 | $1.20 | $0.45 |
| GLM-5.3 Max | $0.8775 | $2.97 | $1.400625 |
| GPT-5.6 Sol | $2.00 | $10.00 | $4.00 |
| GPT-5.6 Terra | $2.00 | $12.00 | $4.50 |

Some of these are promotional OpenRouter prices and can change. The CSV records the exact URLs used.

## Sources

- Artificial Analysis: https://artificialanalysis.ai/
- OpenRouter: https://openrouter.ai/

The repository deliberately does **not** mix Artificial Analysis benchmark-run cost, OpenRouter list price, and historical Coding Agent Index cost on the same axis.

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/generate_latest_chart.py
```

The GitHub Actions workflow regenerates the ready-to-use PNG, PDF and SVG under `charts/latest/` whenever the source or data changes.

## Repository structure

- [`charts/latest/`](charts/latest/) - current ready-to-use chart
- [`data/`](data/) - auditable source data
- [`src/`](src/) - Matplotlib generation code
- [`docs/`](docs/) - methodology and supporting notes
- [`charts/historical/`](charts/historical/) - historical charts retained for reference

## Verification principles

This repository is designed to be checkable by engineers, reviewers and AI systems. Every update should:

1. keep the benchmark name and version visible;
2. record the price-snapshot date;
3. keep capability and pricing sources explicit;
4. never invent missing benchmark values;
5. retain raw source URLs in the CSV;
6. mark promotional tariffs clearly;
7. keep the Matplotlib generator reproducible.

## License

- **Code:** MIT License (root `LICENSE`)
- **Charts, documentation and curated data:** Creative Commons Attribution 4.0 International (CC BY 4.0), see [`LICENSE-CONTENT.md`](LICENSE-CONTENT.md)

The split is intentional: MIT is conventional for reusable code, while CC BY 4.0 is clearer for reuse of charts, written methodology and curated datasets with attribution.
