# Eurobotics LLM comparison methodology

## Version 1.2 — 18 September 2026

The main Eurobotics chart combines two independent sources:

- **Capability / Y-axis:** Artificial Analysis Intelligence Index v4.3.
- **Market pricing / X-axis:** current OpenRouter headline API pricing.
- **Workload / effort effect:** Artificial Analysis measured total cost to run the Intelligence Index at each reasoning effort.

## Why v1.2

A raw token tariff is not enough for reasoning models. Low, Medium, High, XHigh and Max can have the same per-token price while consuming very different token volumes.

So the x-axis is no longer a simple token tariff. It is an **estimated total OpenRouter cost to run the same Artificial Analysis Intelligence Index workload**.

## Repricing formula

Artificial Analysis publishes the total cost to run its Intelligence Index for each evaluated model/effort. Eurobotics reprices that measured workload to current OpenRouter pricing:

\`Estimated OpenRouter total evaluation cost = AA total evaluation cost × (OpenRouter blended tariff / AA reference blended tariff)\`

The blended tariff uses the same 7:2:1 convention:

\`70% cache-read + 20% uncached input + 10% output\`

This preserves the observed increase in workload at higher reasoning strengths while shifting the price basis to OpenRouter.

## Important limitation

This is a **repricing estimate**, not an exact OpenRouter invoice.

Artificial Analysis exposes total evaluation cost and several token-use measures, but the complete per-model/per-effort token matrix split across cache read, cache write, uncached input, reasoning and answer tokens is not exposed as one simple downloadable table. Therefore Eurobotics uses the 7:2:1 blended-tariff ratio as the reproducible repricing factor.

## OpenRouter price policy

Version 1.2 deliberately uses the **current OpenRouter headline price shown on the model/comparator pages**, because OpenRouter is the practical market source for this project.

That means active promotions are included and marked with \`*\`.

Examples at the 18 September 2026 snapshot:

- GLM-5.3 Flash: $0.075/M input, $0.25/M output, $0.015/M cache read.
- GPT-5.6 Terra: $2/M input, $12/M output, $0.20/M cache read.
- GPT-5.6 Sol: current 50% promotion, $2/M input, $10/M output, $0.20/M cache read.
- DeepSeek V4.1 Flash: $0.15/M input, $0.60/M output, $0.015/M cache read.
- GLM-5.3: current headline about $1/M input, $3.41/M output, $0.20/M cache read.

Promotions can temporarily reverse the normal list-price ordering. This is not hidden: the chart is a dated market snapshot.

## Why the GLM-5.3 Flash / Terra gap is so large

The gap is real at the current OpenRouter snapshot. GLM-5.3 Flash is priced at roughly 1/27 of Terra on uncached input and 1/48 on output. The resulting benchmark-cost estimate is therefore much lower even though both are near 42 on the Intelligence Index.

The chart should be interpreted as a **current market cost/performance snapshot**, not as a permanent structural price ranking.

## Qwen3 Coder 30B

Artificial Analysis currently reports Intelligence Index = 10 but does not publish a comparable cost/task or total evaluation cost. It is therefore shown only as an intelligence reference and receives no invented x-coordinate.

## Sources

- Artificial Analysis: https://artificialanalysis.ai/
- OpenRouter: https://openrouter.ai/

The CSV under \`data/\` records the exact pricing URLs and all transformation fields used by the Matplotlib generator.
