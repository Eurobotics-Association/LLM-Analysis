# Eurobotics LLM comparison methodology

## Version 1.6 — 2 October 2026

The chart maps Artificial Analysis (AA) **Intelligence Index v4.3 series** against the estimated OpenRouter cost to run AA's complete evaluation workload. The latest AA pages use **v4.3.2**. Existing v1.5 Intelligence Index observations are retained; GPT-6 Sol, GPT-6 Luna, and Astra Max use the currently published v4.3.2 observations. Historical Coding Agent Index values are never used.

### Changes from v1.5

- Added GPT-6 Sol and GPT-6 Luna as complete Low, Medium, High, XHigh, and Max effort curves. AA's published index and total evaluation costs are rounded to whole units for these new rows; both axes move by effort. [AA Sol release](https://artificialanalysis.ai/models/releases/gpt-6-sol), [AA Luna release](https://artificialanalysis.ai/models/releases/gpt-6-luna), [AA effort comparisons](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-high-vs-gpt-6-sol-xhigh).
- Added GPT-6 Astra Max (Index 52.7, AA cost $5,324) from [AA's comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-low-vs-gpt-6-astra).
- Audited each model's standard, non-promotional OpenRouter tariff on 2 October 2026. GLM-5.3 Flash's old $0.09/$0.30 rate now appears as a promotion; the first-party Z.ai tariff is $0.15/$0.50 with $0.03 cache read. GLM-5.3 uses Mistral's listed $0.14 cache-read rate at $1.40/$4.40. [GLM Flash providers](https://openrouter.ai/z-ai/glm-5.3-flash), [GLM providers](https://openrouter.ai/z-ai/glm-5.3), [Mistral pricing](https://docs.mistral.ai/inference/pricing).
- Corrected the Mistral Small 3.2 model URL. The previous `mistral-small-2603` page identifies **Mistral Small 4**. AA now marks Small 3.2's Intelligence Index as **estimated** and does not publish a current comparable total evaluation cost. Small 3.2 is therefore an intelligence reference line only. [AA Small 3.2](https://artificialanalysis.ai/models/mistral-small-3-2), [OpenRouter Small 3.2](https://openrouter.ai/mistralai/mistral-small-3.2-24b-instruct).

### Repricing

`Estimated OpenRouter total evaluation cost = AA measured total cost × (OpenRouter blended tariff / AA reference blended tariff)`

Each blend is `0.7 × cache-read + 0.2 × uncached-input + 0.1 × output`, using USD per million tokens. The CSV contains the source tariffs, both blends, ratio, and estimated total for every costed point. If AA provides no comparable current total evaluation cost, no x-coordinate is invented.

The renderer recomputes both blends, the ratio, and every plotted x-coordinate from the AA total and tariff columns. It stops if a rounded derived CSV value differs from the recomputation, or if a reference-only model has an x-coordinate. Thus the chart cannot silently plot a stale or manually altered derived cost.

AA's total includes cache-write charges, while the 7:2:1 blend does not. The result is an estimate of the same evaluation workload at selected OpenRouter provider tariffs, not a quote or invoice. Provider routing, discounts, long-context pricing, and benchmark revisions can change actual spend.

### GPT-6 effort data

| Model | Effort | AA Index | AA total cost / estimated OpenRouter cost |
|---|---|---:|---:|
| GPT-6 Luna | Low / Medium / High / XHigh / Max | 22 / 30 / 33 / 35 / 38 | $11 / $31 / $48 / $67 / $122 |
| GPT-6 Sol | Low / Medium / High / XHigh / Max | 34 / 40 / 42 / 44 / 48 | $269 / $416 / $605 / $855 / $1,536 |
| GPT-6 Astra | Max | 52.7 | $5,324 |

The new Sol and Luna OpenRouter blends match AA's reference blends, so the ratio is 1.0. Their [standard provider tariffs](https://openrouter.ai/openai/gpt-6-sol) and [Luna tariffs](https://openrouter.ai/openai/gpt-6-luna) show no promotion on the selected OpenAI endpoint.

**Provider selection:** Each row uses the named provider in the price snapshot below and the CSV's `Price_Basis` field, usually the model vendor or another named standard provider. This is a consistent non-promotional comparison, **not** an OpenRouter lowest-price search. A different non-promotional provider may offer a lower tariff. The model-page URL contains several provider quotes and may change after the snapshot date; the table records the selected tariff as checked on 2 October.

### OpenRouter price snapshot — 2 October 2026

USD per 1M tokens. Each link points to the audited model listing. The baseline selects a standard provider, excluding temporary discounts, Flex, Fast, and free endpoints.

| Model | Selected standard provider | Input | Output | Cache read | Status |
|---|---|---:|---:|---:|---|
| [GPT-5.6 Luna](https://openrouter.ai/openai/gpt-5.6-luna) | OpenAI | $0.20 | $1.20 | $0.02 | Unchanged |
| [GPT-5.6 Terra](https://openrouter.ai/openai/gpt-5.6-terra) | OpenAI | $2.00 | $12.00 | $0.20 | Unchanged |
| [GPT-5.6 Sol](https://openrouter.ai/openai/gpt-5.6-sol) | OpenAI list / Azure | $4.00 | $20.00 | $0.40 | OpenAI's $2/$10 is 50% off; excluded |
| [GPT-6 Luna](https://openrouter.ai/openai/gpt-6-luna) | OpenAI | $0.10 | $0.50 | $0.01 | Added |
| [GPT-6 Sol](https://openrouter.ai/openai/gpt-6-sol) | OpenAI | $2.00 | $10.00 | $0.20 | Added |
| [GPT-6 Astra](https://openrouter.ai/openai/gpt-6-astra) | OpenAI | $10.00 | $50.00 | $1.00 | Unchanged |
| [GLM-5.3 Flash](https://openrouter.ai/z-ai/glm-5.3-flash) | Z.ai | $0.15 | $0.50 | $0.03 | Repriced; old $0.09/$0.30 appears as a promo |
| [GLM-5.3](https://openrouter.ai/z-ai/glm-5.3) | Mistral | $1.40 | $4.40 | $0.14 | Cache read updated |
| [DeepSeek V4.1 Flash](https://openrouter.ai/deepseek/deepseek-v4.1-flash) | DeepSeek | $0.15 | $0.60 | $0.003 | Unchanged |
| [Gemini 3.1 Pro Preview](https://openrouter.ai/google/gemini-3.1-pro-preview) | Google | $2.00 | $12.00 | $0.20 | Unchanged |
| [Claude Sonnet 5](https://openrouter.ai/anthropic/claude-sonnet-5) | Anthropic | $2.00 | $10.00 | $0.20 | Unchanged |
| [Claude Opus 5](https://openrouter.ai/anthropic/claude-opus-5) | Anthropic | $5.00 | $25.00 | $0.50 | Unchanged |
| [Claude Fable 5.1](https://openrouter.ai/anthropic/claude-fable-5.1) | Anthropic | $10.00 | $50.00 | $0.25 | Unchanged |
| [Mistral Medium 3.5](https://openrouter.ai/mistralai/mistral-medium-3-5) | Mistral | $1.50 | $7.50 | $0.15 | Unchanged; cache from [Mistral pricing](https://docs.mistral.ai/inference/pricing) |
| [Mistral Small 3.2](https://openrouter.ai/mistralai/mistral-small-3.2-24b-instruct) | Mistral | $0.10 | $0.30 | $0.01 | Intelligence reference only |
| [Qwen3 Coder 30B](https://openrouter.ai/qwen/qwen3-coder-30b-a3b-instruct) | Standard listing | $0.07 | $0.27 | — | Intelligence reference only |
| [Llama 3.3 70B](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) | Standard listing | $0.10 | $0.32 | — | Intelligence reference only |
| [Phi-4](https://openrouter.ai/microsoft/phi-4) | Standard listing | $0.07 | $0.14 | — | Intelligence reference only |

The reference-only models have no comparable current AA total evaluation cost, so pricing is documented without claiming a computed x-position. Mistral Small 3.2 uses the Mistral standard provider's complete cache tariff; the OpenRouter headline $0.075/$0.20 route does not state a cache-read rate.

### Why open-weight API models can cost more

Open weights do not set the price of a hosted API. The selected provider still pays for inference hardware and sets its own tariff; this chart does not model self-hosting. On 2 October, Luna's selected OpenAI 7:2:1 tariff was **$0.077/M**, versus **$0.0921/M** for DeepSeek V4.1 Flash on DeepSeek and **$0.101/M** for GLM-5.3 Flash on Z.ai. The cache-read component is cheaper for DeepSeek, while GLM and Luna share the same output price. See the linked provider quotes above.

AA also measured different token use on the same evaluation suite. [AA's Luna Max / DeepSeek comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-deepseek-v4-1-flash) reports 144M versus 253M output tokens and total costs of $122 versus $477 at AA's reference tariffs. Repricing DeepSeek's $477 by the selected OpenRouter/AA blend ratio of 0.5 gives about **$238**. [AA's Luna Max / GLM comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-glm-5-3-flash) reports 144M versus 181M output tokens and $122 versus $280; repricing GLM to Z.ai's selected tariff gives about **$288**. Output counts illustrate workload efficiency but are only one part of the bill: input, cache read, cache write, and token mix also matter.

Those points also have different capability scores: Luna Max is about 38 on AA's Index, DeepSeek Flash about 40, and GLM Flash about 42. The plotted costs describe this benchmark workload at specified providers. They do not establish a general ranking for every real workload.

### Publication

The generator writes timestamped PNG, PDF, and SVG files plus a stable `latest` alias. The README embeds the alias, and GitHub Actions commits the rendered artifacts after a source or data update. The PDF and SVG footer links to the [repository](https://github.com/Eurobotics-Association/LLM-Analysis) and [Artificial Analysis](https://artificialanalysis.ai/), includes the generation timestamp, and carries the informational disclaimer.

Issues are [open for corrections and improvement requests](https://github.com/Eurobotics-Association/LLM-Analysis/issues).
