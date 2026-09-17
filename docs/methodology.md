# Methodology and data provenance

## Purpose

The charts in this repository are built for practical AI-assisted software engineering and DevOps model selection. The central requirement is auditability: a reviewer should be able to trace every plotted coordinate to a source and understand the unit represented on each axis.

## Panel A: Coding Agent Index v1.1

Panel A is a historical reconstruction of the Artificial Analysis Coding Agent Index v1.1 cost/performance view from July 2026.

The score series and cost trajectories are based on the accessible Greenbyte digitization/reconstruction of the AA v1.1 chart, with best/max scores cross-checked against OpenAI's GPT-5.6 launch material. The chart uses a logarithmic x-axis because benchmark-run costs span orders of magnitude.

The source trajectory labels P1...P5/Max are mapped to the documented OpenAI reasoning-effort ladder for display. Source-point IDs are retained in the CSV. The Luna P1/None point is retained in data but omitted from the visible curve because it is anomalous and not useful for the intended operational comparison.

## Panel B: Intelligence Index v4.3

Panel B uses the current Artificial Analysis Intelligence Index v4.3 and **total cost to run the full Intelligence Index**.

Snapshot date: **2026-09-17**.

Current plotted values:

| Model | AA Intelligence Index | Total AA Index evaluation cost (USD) | Status |
|---|---:|---:|---|
| GLM-5.3-Flash | 42 | 280.28 | measured/published |
| DeepSeek V4 Flash 0731 Max | 35 | 474.19 | measured/published |
| Z.ai GLM-5.3 Max | 45 | 2,503.48 | measured/published |
| GPT-5.6 Luna Max | 38 | 319.93 | measured/published |
| GPT-5.6 Terra Max | 42 | 2,500.72 | measured/published |
| GPT-5.6 Sol Max | 47 | 3,465 | measured/published |
| Qwen3 Coder 30B A3B | 10 (estimated by AA) | unavailable | horizontal reference only |

### Why Sol is around USD 3,465, not USD 3.08

Both figures are valid but measure different things:

- approximately **USD 3.08 per 1M tokens** = Artificial Analysis blended API token price for GPT-5.6 Sol Max;
- approximately **USD 3,465** = Artificial Analysis total cost to run all evaluations in the current Intelligence Index.

The earlier chart accidentally used the first quantity while the intended comparison was the second. The current chart corrects this.

## Missing values

If a model does not have a published comparable total evaluation cost, the generator must not fabricate one from its list token price. Such a model may be shown as a horizontal score reference, with a clear note that the x-coordinate is unavailable.

## Reproducibility

The Matplotlib source is in `src/generate_latest_chart.py`. Numeric inputs are stored in `data/`. The chart outputs are generated as PNG, PDF and SVG so they can be reviewed visually, embedded in documentation, or inspected as vector graphics.
