# Eurobotics LLM comparison methodology

## Version 1.0 - 17 September 2026

The main Eurobotics chart intentionally combines **two independent sources**:

- **Performance / Y-axis:** Artificial Analysis Intelligence Index v4.3
- **API pricing / X-axis:** current OpenRouter model pricing

This separation is deliberate. Artificial Analysis is used as the independent evaluation source; OpenRouter is used as the practical market-price source for models consumed through an API gateway.

## X-axis definition

OpenRouter publishes input and output prices separately. To put every model on one x-axis, Eurobotics defines a simple reference tariff:

`Eurobotics blended price = 0.75 x input price + 0.25 x output price`

All values are USD per 1 million tokens.

Why 75/25?

1. Input and output prices are available for every model in the comparison.
2. It avoids mixing in cache discounts that are unavailable or structured differently for some providers.
3. It is simple, reproducible, and easy for another professional or AI system to audit.

The blended price is a **reference API tariff**, not a prediction of the cost of a real job.

## Reasoning effort

For GPT-5.6 Luna, Terra and Sol, OpenRouter's per-token price does not change between Low, Medium, High, XHigh and Max reasoning effort. Therefore those points share the same x-coordinate.

A higher reasoning effort may consume more tokens and therefore produce a larger final invoice. That is intentionally *not* represented by this tariff chart.

A future Eurobotics workload benchmark can measure real cost per completed DevOps task.

## Promotions and price snapshots

Where OpenRouter's model page currently displays a promotional headline tariff, the chart uses that price and marks it as promotional.

Therefore every chart is a dated snapshot. Pricing must be refreshed before making a procurement decision.

Current snapshot: **17 September 2026**.

## Current model set

- GPT-5.6 Luna: Low / Medium / High / XHigh / Max
- GPT-5.6 Terra: Low / Medium / High / XHigh / Max
- GPT-5.6 Sol: Low / Medium / High / XHigh / Max
- GLM-5.3 Flash
- DeepSeek V4.1 Flash (latest Flash generation)
- GLM-5.3 Max
- Qwen3 Coder 30B A3B

## Sources

- Artificial Analysis: https://artificialanalysis.ai/
- OpenRouter: https://openrouter.ai/

The CSV committed under `data/` records the exact OpenRouter model URLs used for the price snapshot.
