# Intelligence Index v5 refresh: working audit

This is research for the proposed next release, not the published v1.7 data.
Scores and total evaluation costs below are AA Intelligence Index v5 values;
the total is not the weighted cost per task. Prices are USD per million tokens.
Accessed 30 October 2026. Recheck before publication.

| Model / effort | AA score | AA total cost | AA input / output / cache read | Evidence |
|---|---:|---:|---|---|
| GPT-6.1 Terra Low / Medium / High / XHigh / Max | 29 / 38 / 42 / 45 / 51 | 111 / 190 / 267 / 400 / 972 | 1 / 5 / 0.05 | [Low](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-low-vs-glm-5-3-low), [Medium](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-medium-vs-gpt-6-1-sol-medium), [High](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-high-vs-gpt-6-1-sol-high), [XHigh](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-xhigh-vs-gpt-6-1-sol-xhigh), [Max](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-vs-gpt-6-1-sol) |
| GPT-6.1 Sol Low / Medium / High / XHigh / Max | 35 / 46 / 50 / 52 / 55 | 238 / 389 / 573 / 718 / 1124 | 2 / 10 / 0.10 | [Low and Medium](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-medium), [High](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-high-vs-gpt-6-1-sol-high), [XHigh](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-xhigh-vs-gpt-6-1-sol-xhigh), [Max](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-vs-gpt-6-1-sol) |
| Kimi K3.1 Pro | 46 | 3153 | 2 / 10 / 0.20 | [AA comparison](https://artificialanalysis.ai/models/comparisons/gemini-4-carbon-vs-kimi-k3-1-pro) |
| Gemini 4 Carbon High | 59 | 8240 | 4 / 20 / 0.20 | [AA comparison](https://artificialanalysis.ai/models/comparisons/gemini-4-carbon-vs-kimi-k3-1-pro) |
| DeepSeek V4.1 Flash 1017 Max | 32 | 521 | 0.30 / 1.20 / 0.006 | [AA comparison](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-1017-vs-glm-5-3-flash) |
| GLM-5.3 Flash | 28 | 378 | 0.15 / 0.50 / 0.03 | [AA comparison](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-glm-5-3) |
| GLM-5.3 Max | 32 | 3496 | 1.40 / 4.40 / 0.26 | [AA comparison](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-glm-5-3) |
| Claude Haiku 5.5 Max | 36 | 339 | 0.10 / 0.50 / 0.01 | [AA comparison](https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-vs-claude-opus-5-5) |
| Claude Opus 5.5 Max, default fallback | 58 | 8910 | 4 / 20 / 0.20 | [AA comparison](https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-vs-claude-opus-5-5) |
| Claude Sonnet 5.5 Max, default fallback | 54 | 7981 | 2 / 10 / 0.10 | [AA comparison](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-vs-gpt-6-1-sol) |
| Gemini 4 Argon High | 50 | 6103 | 4 / 20 / 0.20 | [AA comparison](https://artificialanalysis.ai/models/comparisons/gemini-4-argon-vs-gpt-6-1-sol) |
| Mistral Large 4 High | 26 | 1359 | 0.70 / 2.10 / 0.07 | [AA comparison](https://artificialanalysis.ai/models/comparisons/mistral-large-4-vs-glm-5-3) |
| Claude Fable 5.1 Max, default fallback | 49 | 13327 | 10 / 50 / 0.25 | [AA comparison](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-claude-fable-5-1) |

## OpenRouter checks and remaining work

- [GPT-6.1 Terra](https://openrouter.ai/openai/gpt-6.1-terra) lists OpenAI standard at 1 / 5 / 0.05; Fast and Flex are excluded.
- [Kimi K3.1 Pro](https://openrouter.ai/moonshotai/kimi-k3.1-pro) lists Moonshot standard at 2 / 10 / 0.20. AA currently calls the model proprietary while OpenRouter calls it open-weight; do not claim the weights are released without checking the actual publication and license.
- [GLM-5.3 Flash](https://openrouter.ai/z-ai/glm-5.3-flash) lists Z.ai standard at 0.15 / 0.50 / 0.03. Other provider rates are lower and some explicitly discounted; the current methodology selects a named standard provider rather than the cheapest route.
- [Haiku 5.5](https://openrouter.ai/anthropic/claude-haiku-5.5) lists Anthropic standard at 0.10 / 0.50 / 0.01. AA's [launch analysis](https://artificialanalysis.ai/articles/claude-haiku-5-5) warned that long-context tiered pricing was initially omitted from cost calculations; verify whether the current v5 total incorporates it before plotting a cost.
- OpenRouter has a separate [DeepSeek 1017 listing](https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017); audit the provider's current non-promotional tariff and cache-read price.
- Confirm Carbon's OpenRouter listing and undiscounted provider tariff. A failed page lookup is not proof it is unavailable.
- Audit current OpenRouter provider prices and discount details for every other retained point; collect remaining v5 effort data and determine which reference-only models have a v5 score. AA comparison pages can show blank v5 scores and totals, while older cached pages can still display v4.3.2.
- Do not combine the v4.3 points or totals with v5. Do not treat AA's weighted cost per task as total evaluation cost.
- The existing 7:2:1 blend excludes cache writes even though AA's measured total includes them. Issue #5 calls for investigation; a 7:2:1:1 formula cannot be assumed valid without evidence about the workload's token mix and both providers' cache-write tariffs.
