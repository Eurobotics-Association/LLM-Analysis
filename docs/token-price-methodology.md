# Proposed AA Intelligence Index × OpenRouter output-token tariff

**Review-only prototype — 30 October 2026.** This proposes a different question from the withdrawn v1.8 chart: what output-token tariff is quoted for a model with a given AA score? It **does not measure or estimate the cost of a task**, a benchmark run, an invoice, or Codex subscription usage.

[Preview SVG](../charts/preview/aa_v5_output_price_preview_eurobotics_261030_2243.svg) · [Selected-route CSV](../data/aa_v5_openrouter_output_rates_eurobotics_261030_2243.csv) · [Full endpoint snapshot](../data/openrouter_endpoints_eurobotics_261030_2242.json) · [Issue #13](https://github.com/Eurobotics-Association/LLM-Analysis/issues/13)

## Measures and selection

- **Y:** AA Intelligence Index v5 observations from the repository's [30 October v1.8 source snapshot](../data/eurobotics_v18_aa_v5_openrouter_nopromo_eurobotics_261030_1759.csv). Only its score, effort and source-link fields are reused; the withdrawn benchmark-cost and blended-price calculations are not. Scores are rounded in that source. AA's [methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) describes the index and its limitations; it is not an objective measure of all intelligence or coding work.
- **X:** lowest quoted non-promotional output price per million tokens among available OpenRouter endpoint rows that expose `reasoning_effort` support, have status 0, explicitly report `discount: 0`, and a positive output price. Ties use the lexicographically first endpoint tag. Prices are in USD per million and use the base context tier, not a blended tariff.
- The endpoint selection is **lowest output rate only**, not the lowest total cost. Input, cache read/write, tooling and context tiers matter. The CSV records those fields from the same endpoint, along with all reported overrides. Blank means unknown, not free. The snapshot is from 22:42 UTC on 30 October; rates and availability can change.
- Flex endpoints are included when they meet the filter; they are labeled and may have availability or latency constraints. Model/provider quantization is also disclosed. The AA score may have been measured on a different provider or quantization; associating its score with the selected route is an indicative model-level comparison, not a verified quality claim for that route.
- All effort points of a model use the same selected output rate and are connected vertically. Labels L, M, H, XH and Max refer to low, medium, high, extra-high and max. Rounded equal scores overlap; no position is invented. Single published points do not imply an effort curve.
- Gemini 4 Argon was omitted because all reported endpoint quotes had a discount in the snapshot; a verified actual non-promotional listing would be needed. Gemini 4 Carbon has no verified endpoint link in the source snapshot and is omitted. This is not evidence that no eligible route exists at another time.
- The complete endpoint JSON and AA CSV permit review and rerendering of this snapshot, not an automated refresh. The legacy renderer and workflow remain guarded.

## Important interpretation

For the same provider/model/tier, effort levels typically share a tariff; total cost differs with token usage. A model with a lower output tariff may use more output or cached input, incur higher cache-write rates, use different tools, or fail more often. Neither axis establishes the cheapest model for a task. Price-per-token and benchmark score are correlated with neither successful outcomes nor subscription quota in a guaranteed way. OpenRouter credit purchase fees are separate from quoted inference rates.

## Reproduce the preview

With Python 3 and this repository checked out:

```sh
python3 src/generate_token_price_preview.py \
  data/eurobotics_v18_aa_v5_openrouter_nopromo_eurobotics_261030_1759.csv \
  data/openrouter_endpoints_eurobotics_261030_2242.json \
  /tmp/token-preview
```

The script uses only the standard library and generates a timestamped SVG and CSV. Its endpoint selection is a transparent mechanical filter over a dated source; it does not validate availability for a user's account or independently prove benchmark equivalence. Review rate units, route access, promotions, pricing overrides and score provenance again before any public release. The preview is for owner review and is not an instruction to publish.

[Issues are open for corrections and improvement requests.](https://github.com/Eurobotics-Association/LLM-Analysis/issues)
