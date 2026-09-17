# Eurobotics LLM comparison methodology

## Version 1.1 — 17 September 2026

The main Eurobotics chart combines two independent sources:

- **Capability / Y-axis:** Artificial Analysis Intelligence Index v4.3.
- **Economic / X-axis:** Artificial Analysis measured benchmark workload, repriced using **standard non-promotional OpenRouter tariffs**.

This is designed for DevOps, coding-adjacent agent work and AI engineering decisions.

## Why methodology v1.1 exists

A simple API price-per-token chart is not sufficient for reasoning models. Low, Medium, High, XHigh and Max can have the same tariff per token but consume very different numbers of reasoning/output tokens.

Therefore reasoning effort must move the model on the **cost axis**, not only on the intelligence axis.

At the same time, Artificial Analysis may benchmark a model using a different provider tariff from the price available through OpenRouter. We therefore preserve Artificial Analysis' measured task workload and normalize its cost to an OpenRouter standard-price basis.

## X-axis: Eurobotics normalized cost per task

For every model/effort point for which Artificial Analysis publishes a measured `Cost per Intelligence Index task`:

1. take the Artificial Analysis measured cost per task;
2. calculate the Artificial Analysis reference blended tariff;
3. calculate the OpenRouter standard blended tariff;
4. multiply the measured cost by the ratio of the two tariffs.

Formula:

`Eurobotics normalized task cost = AA measured cost/task × (OpenRouter blended tariff / AA blended tariff)`

The blended tariff follows Artificial Analysis' documented **7:2:1** convention:

`blended tariff = 70% cache-read + 20% uncached input + 10% output`

This normalization is a transparent approximation. Artificial Analysis does not expose the complete per-task input/cache/output token matrix as a simple downloadable table for every model, so the 7:2:1 tariff ratio is used as the auditable repricing factor.

## Price selection policy

The baseline chart uses **standard, non-promotional OpenRouter prices**.

- Temporary percentage discounts are excluded.
- For proprietary OpenAI models, the underlying standard OpenAI provider list price shown on OpenRouter is used.
- For open-weight models, a standard first-party/reference provider price is used where OpenRouter exposes it clearly.
- Discounted spot/provider promotions are not used as the baseline.

This avoids distortions such as a temporary Sol promotion making Sol look structurally cheaper than Terra.

## Reasoning effort

Artificial Analysis measures a different cost per task at different reasoning efforts because higher effort consumes more tokens.

That behavior is retained in the Eurobotics x-axis. For example, GPT-5.6 Terra moves from Low to Max both upward in intelligence and rightward in normalized task cost.

## Qwen3 Coder 30B

Artificial Analysis currently reports Intelligence Index = 10 but `Cost per Intelligence Index task = N/A`.

Therefore Qwen3 Coder 30B is shown only as a horizontal intelligence reference and is not assigned an invented x-coordinate.

## Sources

- Artificial Analysis: https://artificialanalysis.ai/
- OpenRouter: https://openrouter.ai/

The CSV in `data/` contains all source URLs, price assumptions, tariff ratios and normalized values.
