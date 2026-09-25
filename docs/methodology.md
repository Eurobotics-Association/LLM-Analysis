# Eurobotics LLM comparison methodology

## Version 1.5 — 25 September 2026

The main Eurobotics chart combines two independent sources:

- **Capability / Y-axis:** Artificial Analysis Intelligence Index v4.3.
- **Market pricing / X-axis:** current **non-promotional** OpenRouter API pricing.
- **Workload / effort effect:** Artificial Analysis measured total cost to run the Intelligence Index at each reasoning effort.

## Changes from v1.4

1. **GPT-6 Astra added as a full effort curve** (Low / Medium / High / XHigh — AA publishes no max variant for Astra). OpenRouter lists `openai/gpt-6-astra` at **$10/M input, $50/M output, $1/M cache read with `discount: 0`** — identical to AA's reference tariff, so the repricing ratio is 1.0 and the estimated costs equal AA's measured totals: **$1,536.78 / $2,434.12 / $2,925.01 / $3,802.98** for Low→XHigh. Index values: 45.78 / 49.57 / 50.92 / 52.39. Astra therefore plots above and to the right of GPT-5.6 Sol, consistent with being the successor flagship.

## Carried over from v1.4 (unchanged)

- Sol priced at its un-discounted list tariff $4/$20 (see AGENTS.md section 7).
- Claude Sonnet 5, Mistral Medium 3.5, Mistral Small 3.2 as single points; Llama 3.3 70B, Phi-4 and Qwen3 Coder 30B as intelligence-reference-only lines.
- Timestamped artifact names (`eurobotics_YYMMDD_HHSS`) and a stable `latest` alias refreshed on every render.
- Clickable repo and AA links in the PDF; generation timestamp printed on the chart; disclaimer footer.

## Repricing formula

`Estimated OpenRouter total evaluation cost = AA total evaluation cost × (OpenRouter blended tariff / AA reference blended tariff)`

The blended tariff uses the 7:2:1 convention: `70% cache-read + 20% uncached input + 10% output`.

For most of the current set (Luna, Terra, Sol at list, GLM-5.3, Gemini 3.1 Pro, GPT-6 Astra, Claude Sonnet 5, Claude Opus 5, Claude Fable 5.1, Mistral Medium 3.5) the OpenRouter list tariff equals AA's reference tariff, so the ratio is 1.0 and AA's measured cost is used directly. Exceptions: GLM-5.3 Flash (ratio 0.62), DeepSeek V4.1 Flash (0.50), Mistral Small 3.2 (2.01).

## Important limitation

This is a **repricing estimate**, not an exact OpenRouter invoice. The complete per-model/per-effort token matrix split across cache read, cache write, uncached input, reasoning and answer tokens is not exposed as one simple downloadable table, so Eurobotics uses the 7:2:1 blended-tariff ratio as the reproducible repricing factor. Additionally, OpenRouter charges a cache-write tariff that this blend omits; see AGENTS.md section 7.4 for the planned refinement.

## OpenRouter price snapshot (25 September 2026, non-promotional)

| Model | Input / 1M | Output / 1M | Cache read / 1M | Discount field |
|---|---:|---:|---:|---|
| GLM-5.3 Flash | $0.09 | $0.30 | $0.018 | 0 |
| DeepSeek V4.1 Flash | $0.15 | $0.60 | $0.003 | — |
| GPT-5.6 Luna | $0.20 | $1.20 | $0.02 | — |
| GPT-5.6 Terra | $2.00 | $12.00 | $0.20 | 0 |
| GPT-5.6 Sol (list) | $4.00 | $20.00 | $0.40 | 0.5 on $2/$10 headline |
| GPT-6 Astra | $10.00 | $50.00 | $1.00 | 0 |
| GLM-5.3 | $1.40 | $4.40 | $0.26 | — |
| Gemini 3.1 Pro | $2.00 | $12.00 | $0.20 | — |
| Claude Sonnet 5 | $2.00 | $10.00 | $0.20 | — |
| Claude Opus 5 | $5.00 | $25.00 | $0.50 | — |
| Claude Fable 5.1 | $10.00 | $50.00 | $0.25 | — |
| Mistral Medium 3.5 | $1.50 | $7.50 | $0.15 | — |
| Mistral Small 3.2 (mistral-small-2603) | $0.15 | $0.60 | $0.015 | — |

## How to detect a promotion (audit rule)

The OpenRouter models API headline price is not proof of list price. Check the model page's pricing JSON for a `"discount"` field: a value like `0.5` means the headline is a temporary promotion and the true list price appears in the provider-level listing (and usually matches Artificial Analysis' reference tariff). Apply this check to every model before plotting.

## Sources

- Artificial Analysis: https://artificialanalysis.ai/
- OpenRouter: https://openrouter.ai/ (list prices, promotions excluded)

The CSV under `data/` records the exact pricing URLs and all transformation fields used by the Matplotlib generator.

