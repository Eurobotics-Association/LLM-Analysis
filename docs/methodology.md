# Eurobotics LLM comparison methodology

## Current status — 30 October 2026

**The v1.8 cost chart is withdrawn pending issue #9.** It selected named providers rather than the best eligible non-promotional OpenRouter route, and applied a 7:2:1 blended-price ratio to a benchmark total instead of repricing the actual workload token categories. Do not interpret its x-coordinates as best available OpenRouter costs or as invoices. Sections describing v1.8 and earlier below are historical records, not current publication rules.

The corrected policy is documented in [AGENTS.md](../AGENTS.md): benchmark usage must be repriced with verified eligible OpenRouter provider rates, including applicable input, output, cache and tiered charges. Compare eligible providers on the actual token mix; do not use benchmark-provider rates as OpenRouter rates or invent missing usage data. Models without the required evidence are omitted from the diagram. Record the provider and endpoint, availability, discount status, all relevant rates, benchmark model/effort, data source and audit time.

Artificial Analysis documents detailed evaluation token counts as Pro-only, and its cost methodology combines reported tokens with live measurements of typical cache-hit rates. It is not yet established that the public information includes the required per-category input, cache-read and cache-write quantities. A fixed blended ratio cannot recover them. See [AA API reference](https://artificialanalysis.ai/data-api/docs/reference), [AA benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), and [issue #9](https://github.com/Eurobotics-Association/LLM-Analysis/issues/9).

For illustration, the OpenRouter endpoint API on 30 October returned GLM-5.3 Flash Z.ai rates of $0.15 input / $0.50 output / $0.03 cache read per million tokens, while other undiscounted routes included Relace at $0.018 / $0.1402 / $0.018 and OpenInference FP4 at $0.0189 / $0.0569 / $0.0172. These are price components, not computed benchmark costs. Their relative total depends on the workload, cache-write charges and route compatibility; OpenInference's FP4 quantization is not evidence that it reproduces AA's measured model quality. Recheck live availability and discount fields before selecting any route. [OpenRouter endpoint data](https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints)

For DeepSeek V4.1 Flash 1017 the same endpoint audit returned an undiscounted Morph FP8 route at $0.022 input / $0.192 output / $0.004 cache read per million tokens, far below the previously selected SiliconFlow rates of $0.30 / $1.20 / $0.006. Other routes trade off categories; the DeepSeek provider's rates vary by time. This observation is not a benchmark-cost calculation or proof of identical model behavior across providers. [OpenRouter endpoint data](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash-1017/endpoints)


## Alternative proposal — review only

The [token-price proposal](token-price-methodology.md) pairs an AA Intelligence Index v5 snapshot with eligible OpenRouter output-token prices. It does not calculate cost per task. The previous chart remains withdrawn and automatic publication remains suspended pending review. See [issue #13](https://github.com/Eurobotics-Association/LLM-Analysis/issues/13).

## Version 1.8 — 30 October 2026

The chart uses **AA Intelligence Index v5** and AA's published total cost to run its complete v5 evaluation, excluding repeats. v5 changed the test suite, so v4.3 scores and totals are not comparable and are retained only in historical snapshots. Values in the [source CSV](../data/eurobotics_v18_aa_v5_openrouter_nopromo_eurobotics_261030_1759.csv) are rounded published values; links and audit dates are included per row. Supporting observations are in the [working audit](v5-audit.md).

### Changes and coverage

GPT-5.6 Luna, Terra and Sol are removed from the current chart at the owner's request. GPT-6.1 Terra's five effort levels and Kimi K3.1 Pro are added; DeepSeek V4.1 Flash is replaced by the October 1017 snapshot, and Claude Opus 5 by Opus 5.5. The complete GPT-6.1 Sol and Astra effort series are updated to v5. AA rounds Astra High and XHigh both to 55; the chart does not invent a vertical difference. GPT-6 Luna now includes all five effort levels; Medium has v5 Index 18 and AA total evaluation cost $40, as reported in the [AA comparison](https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-medium-vs-gpt-6-luna-medium).

Gemini 4 Carbon is an intelligence-only reference because its OpenRouter provider price was not verified. Haiku 5.5 is an intelligence-only reference because AA's launch report identified a long-context price-tier limitation whose resolution has not been verified. An AA score is never assigned a fabricated cost. GPT-6 Sol, Gemini 3.1 Pro, Mistral Small 4, Qwen3 Coder 30B, Llama 3.3 and Phi-4 are omitted from the v5 chart because a comparable v5 score was not verified in the accessible source; their v4.3 values remain in previous snapshots. This does not establish that AA has never measured them.

### Price audit and limitations

The CSV records the 30 October AA and OpenRouter prices, per million tokens, and selected standard provider. Terra uses OpenAI $1/$5/$0.05, Kimi Moonshot $2/$10/$0.20, GLM-5.3 Flash Z.ai $0.15/$0.50/$0.03, and DeepSeek 1017 SiliconFlow $0.30/$1.20/$0.006 (input/output/cache read). Mistral Large 4's selected Mistral standard tariff is $0.70/$2.10/$0.07. Other available providers may be cheaper; this is not a lowest-price search. The Argon baseline uses the pre-discount Google AI Studio tariff $4/$20/$0.20 rather than the 50% offer. Kimi's weights status differs between source descriptions and has not been independently confirmed.

The renderer computes the ratio of the two 7:2:1 blended tariffs and multiplies it by AA's measured total, checking the CSV's stored results. This approximation assumes that the ratio is representative of the evaluation's token mix. AA total cost includes cache writes but the blend omits them; applying a 7:2:1:1 blend without measured write volumes and corresponding tariffs would not resolve this reliably. Retain 7:2:1 pending the review in issue #5; do not interpret the estimate as a quote or invoice. Context-tier pricing, routing and fallback choices can also change results.

All chart formats show their generation timestamp; the PDF and SVG include clickable AA and repository links. Timestamped filenames are authoritative and README links point to one snapshot. The chart is informational only and must not be used for budgeting.

## Version 1.7 — 24 October 2026

The chart maps Artificial Analysis (AA) **Intelligence Index v4.3 series** against the estimated OpenRouter cost to run AA's complete evaluation workload. The latest AA pages use **v4.3.2**. Existing v1.5 Intelligence Index observations are retained; GPT-6 Sol, GPT-6 Luna, and Astra Max use the currently published v4.3.2 observations. Historical Coding Agent Index values are never used.

### Changes from v1.6

- Replaced Claude Sonnet 5 with **Claude Sonnet 5.5** (AA Index 56.00), Mistral Medium 3.5 with **Mistral Large 4** (38.38), and Mistral Small 3.2 with **Mistral Small 4** (11.27). All have published AA total evaluation costs and `discount: 0` selected OpenRouter tariffs.
- Added **Gemini 4 Argon** (AA Index 52.56) and GPT-6.1 Sol's Low, Medium, High, XHigh, and Max effort curve (42.08 / 47.78 / 50.24 / 51.04 / 51.83). Gemini's headline price has `discount: 0.5`; this revision uses its $4/$20/$0.20 undiscounted tariff.
- Re-checked every newly added or replaced OpenRouter model on 24 October 2026. A row is excluded unless both a current AA Index/total evaluation cost and a selected undiscounted OpenRouter tariff are published.
- Canonical PNG, PDF, and SVG artifacts now have timestamped filenames; the renderer updates README links to that exact snapshot.

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

### OpenRouter price snapshot — 24 October 2026

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
| [Claude Sonnet 5.5](https://openrouter.ai/anthropic/claude-sonnet-5.5) | Anthropic | $2.00 | $10.00 | $0.10 | `discount: 0` |
| [Claude Opus 5](https://openrouter.ai/anthropic/claude-opus-5) | Anthropic | $5.00 | $25.00 | $0.50 | Unchanged |
| [Claude Fable 5.1](https://openrouter.ai/anthropic/claude-fable-5.1) | Anthropic | $10.00 | $50.00 | $0.25 | Unchanged |
| [Mistral Large 4](https://openrouter.ai/mistralai/mistral-large-4-0) | Mistral | $1.36 | $4.18 | $0.14 | `discount: 0` |
| [Mistral Small 4](https://openrouter.ai/mistralai/mistral-small-2603) | Mistral | $0.15 | $0.60 | $0.015 | `discount: 0` |
| [Gemini 4 Argon](https://openrouter.ai/google/gemini-4-argon) | Google | $4.00 | $20.00 | $0.20 | Undiscounted; displayed $2/$10 has `discount: 0.5` |
| [GPT-6.1 Sol](https://openrouter.ai/openai/gpt-6.1-sol) | OpenAI | $2.00 | $10.00 | $0.10 | `discount: 0` |
| [Qwen3 Coder 30B](https://openrouter.ai/qwen/qwen3-coder-30b-a3b-instruct) | Standard listing | $0.07 | $0.27 | — | Intelligence reference only |
| [Llama 3.3 70B](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) | Standard listing | $0.10 | $0.32 | — | Intelligence reference only |
| [Phi-4](https://openrouter.ai/microsoft/phi-4) | Standard listing | $0.07 | $0.14 | — | Intelligence reference only |

The reference-only models have no comparable current AA total evaluation cost, so pricing is documented without claiming a computed x-position. Mistral Small 3.2 uses the Mistral standard provider's complete cache tariff; the OpenRouter headline $0.075/$0.20 route does not state a cache-read rate.

### Why open-weight API models can cost more

Open weights do not set the price of a hosted API. The selected provider still pays for inference hardware and sets its own tariff; this chart does not model self-hosting. On 2 October, Luna's selected OpenAI 7:2:1 tariff was **$0.077/M**, versus **$0.0921/M** for DeepSeek V4.1 Flash on DeepSeek and **$0.101/M** for GLM-5.3 Flash on Z.ai. The cache-read component is cheaper for DeepSeek, while GLM and Luna share the same output price. See the linked provider quotes above.

AA also measured different token use on the same evaluation suite. [AA's Luna Max / DeepSeek comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-deepseek-v4-1-flash) reports 144M versus 253M output tokens and total costs of $122 versus $477 at AA's reference tariffs. Repricing DeepSeek's $477 by the selected OpenRouter/AA blend ratio of 0.5 gives about **$238**. [AA's Luna Max / GLM comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-glm-5-3-flash) reports 144M versus 181M output tokens and $122 versus $280; repricing GLM to Z.ai's selected tariff gives about **$288**. Output counts illustrate workload efficiency but are only one part of the bill: input, cache read, cache write, and token mix also matter.

Those points also have different capability scores: Luna Max is about 38 on AA's Index, DeepSeek Flash about 40, and GLM Flash about 42. The plotted costs describe this benchmark workload at specified providers. They do not establish a general ranking for every real workload.

### Publication

The generator writes timestamped PNG, PDF, and SVG files. The README links to the same timestamped snapshot, and GitHub Actions commits the rendered artifacts after a source or data update. Every format carries a visible generation timestamp. The PDF and SVG footer links to the [repository](https://github.com/Eurobotics-Association/LLM-Analysis) and [Artificial Analysis](https://artificialanalysis.ai/) and carries the informational disclaimer.

Issues are [open for corrections and improvement requests](https://github.com/Eurobotics-Association/LLM-Analysis/issues).
