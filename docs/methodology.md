# Eurobotics LLM comparison methodology

## Version 1.3 — 18 September 2026

The main Eurobotics chart combines two independent sources:

- **Capability / Y-axis:** Artificial Analysis Intelligence Index v4.3.
- **Market pricing / X-axis:** current **non-promotional** OpenRouter API pricing.
- **Workload / effort effect:** Artificial Analysis measured total cost to run the Intelligence Index at each reasoning effort.

## Changes from v1.2

1. **Promotions removed from the baseline.** v1.2 used OpenRouter headline prices that included active promotions (Sol 50% off, GLM-5.3 Flash 50% off). v1.3 uses normal list prices so structural comparisons are not distorted.
2. **Claude Opus 5, Claude Fable 5.1 and Gemini 3.1 Pro added.**
3. **GPT families plotted as full effort curves** (Low / Medium / High / XHigh / Max); other models are single points at max effort (Gemini at its only published point).
4. **Footer text is wrapped to the chart width** so no large blank area is generated.

## Repricing formula

`Estimated OpenRouter total evaluation cost = AA total evaluation cost × (OpenRouter blended tariff / AA reference blended tariff)`

The blended tariff uses the same 7:2:1 convention: `70% cache-read + 20% uncached input + 10% output`.

For GPT-5.6 Luna and Terra the OpenRouter and AA tariffs are identical, so the ratio is 1.0 and the AA measured cost is used directly. For Sol the ratio is 0.5 (OpenRouter $2/$10 vs AA $4/$20 reference). For GLM-5.3 Flash it is 0.62 at normal tariffs. For GLM-5.3, Claude Opus 5, Claude Fable 5.1 and Gemini 3.1 Pro the AA reference tariffs match OpenRouter's list prices, so the ratio is 1.0. DeepSeek V4.1 Flash's AA reference ($0.30 input / $1.20 output) differs from OpenRouter ($0.15 / $0.60) giving a 0.5 ratio.

## Important limitation

This is a **repricing estimate**, not an exact OpenRouter invoice. The complete per-model/per-effort token matrix split across cache read, cache write, uncached input, reasoning and answer tokens is not exposed as one simple downloadable table, so Eurobotics uses the 7:2:1 blended-tariff ratio as the reproducible repricing factor.

## OpenRouter price snapshot (18 September 2026, non-promotional)

| Model | Input / 1M | Output / 1M | Cache read / 1M |
|---|---:|---:|---:|
| GLM-5.3 Flash | $0.09 | $0.30 | $0.018 |
| DeepSeek V4.1 Flash | $0.15 | $0.60 | $0.003 |
| GPT-5.6 Luna | $0.20 | $1.20 | $0.02 |
| GPT-5.6 Terra | $2.00 | $12.00 | $0.20 |
| GPT-5.6 Sol | $2.00 | $10.00 | $0.20 |
| GLM-5.3 | $1.40 | $4.40 | $0.26 |
| Gemini 3.1 Pro | $2.00 | $12.00 | $0.20 |
| Claude Opus 5 | $5.00 | $25.00 | $0.50 |
| Claude Fable 5.1 | $10.00 | $50.00 | $0.25 |

## Qwen3 Coder 30B

Artificial Analysis reports Intelligence Index = 9.6 for Qwen3 Coder 30B A3B but does not publish a comparable total evaluation cost. It is shown only as an intelligence reference line and receives no invented x-coordinate.

## Sources

- Artificial Analysis: https://artificialanalysis.ai/
- OpenRouter: https://openrouter.ai/ (list prices, promotions excluded)

The CSV under `data/` records the exact pricing URLs and all transformation fields used by the Matplotlib generator.

