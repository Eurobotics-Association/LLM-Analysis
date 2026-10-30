# Eurobotics LLM Cost / Intelligence Map

**Current chart withdrawn pending a pricing and methodology audit.** The 30 October v1.8 chart used named OpenRouter providers rather than selecting the lowest eligible non-promotional route for each measured workload. It also estimated benchmark cost using a 7:2:1 blended-price ratio rather than repricing the workload's actual token categories. Its cost positions must not be treated as the best available OpenRouter prices or as invoices.

The [previous v1.8 snapshot](charts/latest/llm_cost_performance_latest_eurobotics_261030_1801.svg), [previous data](data/eurobotics_v18_aa_v5_openrouter_nopromo_eurobotics_261030_1759.csv) and historical methodology remain available for transparency. They are superseded for pricing purposes. No replacement task-cost diagram is published until each plotted model has verified benchmark usage and qualifying OpenRouter prices.

## Review-only alternative

A [draft output-token price diagram](charts/preview/aa_v5_output_price_preview_eurobotics_261030_2243.svg) and [tariff table](data/aa_v5_openrouter_output_rates_eurobotics_261030_2243.csv) propose a simpler AA v5 score versus OpenRouter output-token price view. It is a dated prototype, **not a task-cost estimate**. Compare input, cache, tier, and provider details before interpreting it. Its AA score was not necessarily measured on the priced route. See the [proposal methodology](docs/token-price-methodology.md) and [issue #13](https://github.com/Eurobotics-Association/LLM-Analysis/issues/13). This preview is not approved for publication.

## Prior task-cost policy

For any future task-cost chart, the cost axis must use the lowest available eligible non-promotional **OpenRouter provider** cost for the measured workload. Record the provider, model and endpoint, pricing components, discount status, availability, audit time, and source. Where providers trade off prices across token types, compare them against the actual workload; the lowest rate for one token type alone does not establish the cheapest provider. Include all applicable input, cache-read, cache-write, output and tiered costs; do not count reasoning tokens twice if they are included in output.

Omit a model entirely if its necessary OpenRouter prices or comparable benchmark token usage cannot be verified. Benchmark scores and token measurements can come from an external evaluation, but benchmark-provider tariffs are not OpenRouter prices. See [methodology](docs/methodology.md) and [issue #9](https://github.com/Eurobotics-Association/LLM-Analysis/issues/9).

## Pending evidence

Artificial Analysis documents detailed evaluation token counts as Pro-only; public benchmark totals and a fixed blended ratio alone do not establish a defensible per-category OpenRouter cost. Its documented token counts may still require provider-specific cache and write details. We are checking which information is available before rebuilding the dataset. [AA API reference](https://artificialanalysis.ai/data-api/docs/reference)

The existing renderer reproduces the **withdrawn** v1.8 methodology and must not be used to publish a replacement until updated. Automated rendering and publication are suspended pending the audit, so a source change cannot silently republish the old method. The new chart will require timestamped artifacts, visible generation time, clickable source links and the informational disclaimer in [AGENTS.md](AGENTS.md).

[Open an issue](https://github.com/Eurobotics-Association/LLM-Analysis/issues) for corrections and improvement requests.
