# Eurobotics LLM Cost / Intelligence Map

**Current chart withdrawn pending a pricing and methodology audit.** The 30 October v1.8 chart used named OpenRouter providers rather than selecting the lowest eligible non-promotional route for each measured workload. It also estimated benchmark cost using a 7:2:1 blended-price ratio rather than repricing the workload's actual token categories. Its cost positions must not be treated as the best available OpenRouter prices or as invoices.

The [previous v1.8 snapshot](charts/latest/llm_cost_performance_latest_eurobotics_261030_1801.svg), [previous data](data/eurobotics_v18_aa_v5_openrouter_nopromo_eurobotics_261030_1759.csv) and historical methodology remain available for transparency. They are superseded for pricing purposes. No replacement task-cost diagram is published until each plotted model has verified benchmark usage and qualifying OpenRouter prices.

## Review-only alternative

A [draft output-token price diagram](charts/preview/aa_v5_output_price_preview_eurobotics_261030_2251.svg) and [tariff table](data/aa_v5_openrouter_output_rates_eurobotics_261030_2251.csv) propose a simpler AA v5 score versus OpenRouter output-token price view. It is a dated prototype, **not a task-cost estimate**. Compare input, cache, tier, and provider details before interpreting it. Its AA score was not necessarily measured on the priced route. See the [proposal methodology](docs/token-price-methodology.md) and [issue #13](https://github.com/Eurobotics-Association/LLM-Analysis/issues/13). This preview is not approved for publication.

## Prior task-cost policy

For any future task-cost chart, the cost axis must use the lowest available eligible non-promotional **OpenRouter provider** cost for the measured workload. Record the provider, model and endpoint, pricing components, discount status, availability, audit time, and source. Where providers trade off prices across token types, compare them against the actual workload; the lowest rate for one token type alone does not establish the cheapest provider. Include all applicable input, cache-read, cache-write, output and tiered costs; do not count reasoning tokens twice if they are included in output.

Omit a model entirely if its necessary OpenRouter prices or comparable benchmark token usage cannot be verified. Benchmark scores and token measurements can come from an external evaluation, but benchmark-provider tariffs are not OpenRouter prices. See [methodology](docs/methodology.md) and [issue #9](https://github.com/Eurobotics-Association/LLM-Analysis/issues/9).

## Pending evidence

Artificial Analysis documents detailed evaluation token counts as Pro-only; public benchmark totals and a fixed blended ratio alone do not establish a defensible per-category OpenRouter cost. Its documented token counts may still require provider-specific cache and write details. We are checking which information is available before rebuilding the dataset. [AA API reference](https://artificialanalysis.ai/data-api/docs/reference)

The existing renderer reproduces the **withdrawn** v1.8 methodology and must not be used to publish a replacement until updated. Automated rendering and publication are suspended pending the audit, so a source change cannot silently republish the old method. The new chart will require timestamped artifacts, visible generation time, clickable source links and the informational disclaimer in [AGENTS.md](AGENTS.md).

[Open an issue](https://github.com/Eurobotics-Association/LLM-Analysis/issues) for corrections and improvement requests.

## Why we changed the methodology

The earlier chart tried to estimate the cost of running the same Artificial Analysis evaluation at OpenRouter prices. It multiplied Artificial Analysis's reported total by a fixed blended-price ratio, but the publicly available data did not provide the actual input, output, cache-read and cache-write quantities needed to reprice each workload reliably. It also used selected providers rather than checking the lowest eligible OpenRouter rates. Those approximations could put models in misleading positions, so the old task-cost chart was withdrawn.

The new diagram compares the Artificial Analysis Intelligence Index with a verified OpenRouter **output-token tariff**. We show each observed effort level at the same tariff when it uses the same route, and the companion table records input, cache and provider details. This makes the pricing source and unit explicit, but it does **not** tell you the cost of completing a task: token usage, caching, provider behavior and success rates differ. The Artificial Analysis score may also have been measured on a different provider or quantization than the quoted OpenRouter route. See the [methodology](docs/token-price-methodology.md) for the selection rules and limitations.
