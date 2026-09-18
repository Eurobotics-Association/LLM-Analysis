# Eurobotics LLM comparison methodology

## Version 1.4 — 18 September 2026

The main Eurobotics chart combines two independent sources:

- **Capability / Y-axis:** Artificial Analysis Intelligence Index v4.3.
- **Market pricing / X-axis:** current **non-promotional** OpenRouter API pricing.
- **Workload / effort effect:** Artificial Analysis measured total cost to run the Intelligence Index at each reasoning effort.

## Changes from v1.3

1. **Sol repriced to its true list price (audit fix).** v1.3 used OpenRouter's API headline $2/$10 for Sol, but the OpenRouter page carries `"discount": 0.5` and the provider listing shows the real list price is **$4/$20** — which matches Artificial Analysis' reference tariff exactly. The Sol OpenRouter/AA ratio is therefore 1.0 and the Sol curve now sits to the right of Terra, consistent with its higher Intelligence Index (47 vs 42). Full audit in [AGENTS.md](../AGENTS.md) section 7.
2. **On-chart Sol annotation.** "(*) About SOL: Price is un-discounted on Sept. 18 2026 - note that there was some temporary discount not taken into account for this diagram."
3. **Claude Sonnet 5 added** (Index 38.4, AA measured evaluation cost $6,998.25 at max effort; OpenRouter and AA tariffs identical).
4. **Mistral Medium 3.5 added** (Index 14.9, cost $1,159.93; tariffs identical between sources).
5. **Mistral Small 3.2 added** (Index 7.0; AA measured cost $162.68 repriced ×2.01 because the current OpenRouter tariff `mistralai/mistral-small-2603` $0.15/$0.60 is above AA's $0.10/$0.30 reference).
6. **Llama 3.3 70B (Index 7.7) and Phi-4 (Index 5.9) added as intelligence-reference-only lines** — AA does not publish a comparable total evaluation cost for them (same treatment as Qwen3 Coder 30B).
7. **Timestamped artifact names.** Chart files now end with `eurobotics_YYMMDD_HHSS` per [AGENTS.md](../AGENTS.md) section 1, and the chart prints its generation time.
8. **Clickable links in PDF/SVG.** The PDF carries real hyperlink annotations to this repository and artificialanalysis.ai.
9. **Disclaimer added on-chart and in the README.**

## Repricing formula

`Estimated OpenRouter total evaluation cost = AA total evaluation cost × (OpenRouter blended tariff / AA reference blended tariff)`

The blended tariff uses the 7:2:1 convention: `70% cache-read + 20% uncached input + 10% output`.

For most of the current set (Luna, Terra, Sol at list, GLM-5.3, Gemini 3.1 Pro, Claude Sonnet 5, Claude Opus 5, Claude Fable 5.1, Mistral Medium 3.5) the OpenRouter list tariff equals AA's reference tariff, so the ratio is 1.0 and AA's measured cost is used directly. Exceptions: GLM-5.3 Flash (ratio 0.62), DeepSeek V4.1 Flash (0.50), Mistral Small 3.2 (2.01).

## Important limitation

This is a **repricing estimate**, not an exact OpenRouter invoice. The complete per-model/per-effort token matrix split across cache read, cache write, uncached input, reasoning and answer tokens is not exposed as one simple downloadable table, so Eurobotics uses the 7:2:1 blended-tariff ratio as the reproducible repricing factor. Additionally, OpenRouter charges a cache-write tariff that this blend omits; see [AGENTS.md](../AGENTS.md) section 7.4 for the planned refinement.

## OpenRouter price snapshot (18 September 2026, non-promotional)

| Model | Input / 1M | Output / 1M | Cache read / 1M |
|---|---:|---:|---:|
| GLM-5.3 Flash | $0.09 | $0.30 | $0.018 |
| DeepSeek V4.1 Flash | $0.15 | $0.60 | $0.003 |
| GPT-5.6 Luna | $0.20 | $1.20 | $0.02 |
| GPT-5.6 Terra | $2.00 | $12.00 | $0.20 |
| GPT-5.6 Sol (list) | $4.00 | $20.00 | $0.40 |
| GLM-5.3 | $1.40 | $4.40 | $0.26 |
| Gemini 3.1 Pro | $2.00 | $12.00 | $0.20 |
| Claude Sonnet 5 | $2.00 | $10.00 | $0.20 |
| Claude Opus 5 | $5.00 | $25.00 | $0.50 |
| Claude Fable 5.1 | $10.00 | $50.00 | $0.25 |
| Mistral Medium 3.5 | $1.50 | $7.50 | $0.15 |
| Mistral Small 3.2 (mistral-small-2603) | $0.15 | $0.60 | $0.015 |

## How to detect a promotion (audit rule)

The OpenRouter models API headline price is not proof of list price. Check the model page's pricing JSON for a `"discount"` field: a value like `0.5` means the headline is a temporary promotion and the true list price appears in the provider-level listing (and usually matches Artificial Analysis' reference tariff). Apply this check to every model before plotting.

## Sources

- Artificial Analysis: https://artificialanalysis.ai/
- OpenRouter: https://openrouter.ai/ (list prices, promotions excluded)

The CSV under `data/` records the exact pricing URLs and all transformation fields used by the Matplotlib generator.

