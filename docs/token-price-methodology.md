# AA Intelligence Index × OpenRouter output-token tariff

**Snapshot — 22 November 2026, Europe/Paris** (the file timestamps are UTC on 21 November). This diagram asks what output-token tariff is quoted for a model with a given AA score. It **does not measure or estimate the cost of a task**, a benchmark run, an invoice, or Codex subscription usage.

[Diagram](../charts/preview/aa_v5_output_price_eurobotics_261121_2322.svg) · [Selected-route CSV](../data/aa_v5_openrouter_output_rates_eurobotics_261121_2322.csv) · [AA score observations](../data/aa_v501_scores_eurobotics_261121_2322.csv) · [Full OpenRouter endpoint snapshot](../data/openrouter_endpoints_eurobotics_261121_2322.json) · [Refresh issue #18](https://github.com/Eurobotics-Association/LLM-Analysis/issues/18)

## Measures and selection

- **Y:** AA Intelligence Index **v5.0.1** observations recorded in the linked score CSV; each row links to its AA model page. Scores are rounded. AA's [methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) explains the index and its limitations; it is not an objective measure of all intelligence or coding work. Rechecking the existing models against the same current index avoids mixing old and new revisions.
- **X:** lowest quoted non-promotional output price per million tokens among available OpenRouter endpoint rows that expose `reasoning_effort` support, have status 0, explicitly report `discount: 0`, and a positive output price. Ties use the lexicographically first endpoint tag. Prices are USD per million and use the base context tier, not a blended tariff. The JSON retains every returned endpoint, including those excluded.
- The endpoint selection is **lowest output rate only**, not the lowest total cost. Input, cache read/write, tools and context tiers matter. The selected-route CSV records those fields where published, overrides, endpoint, revision, provider and quantization. Blank means unknown, not free. Availability and the `discount` field are snapshot evidence, not a guarantee that a particular account can access a route or that every possible promotion was independently disclosed.
- Flex endpoints are included when they meet the filter; they are labeled and may have latency and availability restrictions. Quantization is disclosed. AA may have measured a model on a different provider, quantization or revision. The association is an indicative model-level comparison, not proof of identical quality on the selected route. Parameter support does not establish that every named effort setting behaves identically across providers.
- All observed reasoning-effort points for the new models are shown at the same selected output rate. L, M, H, XH and Max mean low, medium, high, extra-high and max. Rounded equal scores overlap. Concentric markers show when different models share a position; refer to the legend and CSV. A single point does not imply an effort curve.
- AA identifies the plotted Claude Sonnet 5.5, Opus 5.5, Fable 5.1 and Fable 5.2 results as **default fallback**. The single-route output rate shown does not price fallback-model use; these scores do not establish standalone performance for the selected route. Check the AA model pages for the evaluated setup.
- **Excluded:** Gemini 4 Carbon and Gemini 4 Argon had no available endpoint meeting the filter: their returned routes carried a nonzero discount in this snapshot. This is not proof that no qualifying route exists at another time. Retain earlier charts as historical snapshots; no unverified tariff or score is invented.
- This is a manually audited snapshot, not an automatic refresh. The legacy task-cost renderer and workflow remain guarded. The 30 October token-price diagram remains available as a [historical snapshot](../charts/preview/aa_v5_output_price_preview_eurobotics_261030_2251.svg).

## Important interpretation

For the same provider/model/tier, effort levels typically share a tariff; total cost differs with token usage. A model with a lower output tariff may use more output or cached input, incur higher cache-write rates, use different tools, or fail more often. Neither axis establishes the cheapest model for a task. Neither benchmark score nor per-token price predicts successful outcomes or subscription quota in a guaranteed way. OpenRouter credit purchase fees are separate from quoted inference rates.

## Reproduce the diagram

With Python 3 and this repository checked out:

```sh
python3 src/generate_token_price_preview.py \
  data/aa_v501_scores_eurobotics_261121_2322.csv \
  data/openrouter_endpoints_eurobotics_261121_2322.json \
  /tmp/token-preview
```

The standard-library script generates a timestamped SVG and CSV from the captured sources; it does not refresh scores or prices. It does not validate access for a user's account or prove benchmark equivalence. Review source pages, rate units, route access, promotions, pricing overrides and score provenance again before a new release. All timestamps in filenames and endpoint data are UTC.

[Issues are open for corrections and improvement requests.](https://github.com/Eurobotics-Association/LLM-Analysis/issues)
