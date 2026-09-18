from pathlib import Path
import textwrap

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "eurobotics_v13_aa_v43_openrouter_nopromo_2026-09-18.csv"
OUT = ROOT / "charts" / "latest" / "llm_cost_performance_latest"

df = pd.read_csv(DATA)

colors = {
    "GPT-5.6 Luna": "#1f77b4",
    "GPT-5.6 Terra": "#ff7f0e",
    "GPT-5.6 Sol": "#d62728",
    "GLM-5.3 Flash": "#17becf",
    "DeepSeek V4.1 Flash": "#2ca02c",
    "GLM-5.3": "#bcbd22",
    "Gemini 3.1 Pro": "#9467bd",
    "Claude Opus 5": "#8c564b",
    "Claude Fable 5.1": "#e377c2",
    "Qwen3 Coder 30B": "#7f7f7f",
}
markers = {
    "GPT-5.6 Luna": "o",
    "GPT-5.6 Terra": "s",
    "GPT-5.6 Sol": "D",
    "GLM-5.3 Flash": "P",
    "DeepSeek V4.1 Flash": "X",
    "GLM-5.3": "^",
    "Gemini 3.1 Pro": "v",
    "Claude Opus 5": "p",
    "Claude Fable 5.1": "h",
}

fig, ax = plt.subplots(figsize=(16, 10))

for model in ["GPT-5.6 Luna", "GPT-5.6 Terra", "GPT-5.6 Sol"]:
    d = df[df.Model == model].sort_values("Est_OR_Total_Cost")
    ax.plot(
        d.Est_OR_Total_Cost, d.AA_Index,
        marker=markers[model], linewidth=2.6, markersize=8,
        color=colors[model], label=model,
    )
    for _, r in d.iterrows():
        ax.annotate(
            "{0}\n{1:g}".format(r.Effort, r.AA_Index),
            (r.Est_OR_Total_Cost, r.AA_Index),
            xytext=(6, 5), textcoords="offset points",
            fontsize=8, color=colors[model],
        )

for model in ["GLM-5.3 Flash", "DeepSeek V4.1 Flash", "GLM-5.3",
              "Gemini 3.1 Pro", "Claude Opus 5", "Claude Fable 5.1"]:
    r = df[df.Model == model].iloc[0]
    x = float(r.Est_OR_Total_Cost)
    y = float(r.AA_Index)
    c = colors[model]
    ax.axhline(y, color=c, alpha=0.18, linewidth=1.2)
    ax.vlines(x, 8, y, color=c, linestyle=":", linewidth=1.5)
    ax.scatter([x], [y], s=130, color=c, marker=markers[model],
               edgecolor="black", linewidth=0.6, zorder=5, label=model)
    ax.annotate(
        "{0} ({1})\nIndex {2:g} | est. ${3:,.0f}".format(model, r.Effort, y, x),
        (x, y), xytext=(8, 7), textcoords="offset points",
        fontsize=8.2, color=c,
        bbox=dict(boxstyle="round,pad=.2", facecolor="white", edgecolor=c, alpha=0.9),
    )

qwen_idx = 9.6
ax.axhline(qwen_idx, color=colors["Qwen3 Coder 30B"], linestyle="--", alpha=0.55)
ax.text(
    0.012, 0.062,
    "Qwen3 Coder 30B A3B - AA Index 9.6; no comparable AA total evaluation cost published",
    transform=ax.transAxes, fontsize=8.3, color=colors["Qwen3 Coder 30B"],
    bbox=dict(boxstyle="round,pad=.2", facecolor="white",
              edgecolor=colors["Qwen3 Coder 30B"], alpha=0.9),
)

ax.set_xscale("log")
ax.set_xlim(20, 16000)
ax.set_ylim(8, 56)
ticks = [25, 50, 75, 100, 150, 200, 300, 500, 750, 1000, 1500, 2000, 3000,
         5000, 7500, 10000, 15000]
ax.xaxis.set_major_locator(FixedLocator(ticks))
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: "${:,.0f}".format(v)))
ax.grid(True, which="major", alpha=0.33)
ax.grid(True, which="minor", alpha=0.08)

ax.set_xlabel(
    "Estimated total OpenRouter API cost to run the AA Intelligence Index (USD, log scale)\n"
    "AA evaluation workload repriced at current non-promotional OpenRouter tariffs"
)
ax.set_ylabel("Artificial Analysis Intelligence Index v4.3")
ax.set_title(
    "Eurobotics LLM Cost / Intelligence Map\n"
    "AA Intelligence Index v4.3 x non-promotional OpenRouter pricing",
    fontsize=16, pad=14,
)

handles, labels = ax.get_legend_handles_labels()
seen = set()
hh, ll = [], []
for h, l in zip(handles, labels):
    if l not in seen:
        hh.append(h)
        ll.append(l)
        seen.add(l)
ax.legend(hh, ll, loc="lower right", fontsize=8.5, title="Model / family")

ax.text(
    0.012, 0.97,
    "More attractive NW arrow: higher intelligence / lower estimated total API cost",
    transform=ax.transAxes, va="top", fontsize=10, fontweight="bold",
    bbox=dict(boxstyle="round,pad=.35", facecolor="white", alpha=0.88),
)

footer_1 = (
    "Eurobotics methodology v1.3: Y = Artificial Analysis Intelligence Index v4.3. "
    "X = AA measured total evaluation cost repriced to current non-promotional OpenRouter "
    "tariffs via the ratio of 7:2:1 blended prices (70% cache-read / 20% input / 10% output). "
    "This is a reproducible estimate, not an exact OpenRouter invoice."
)
footer_2 = (
    "No temporary promotional prices are used in the baseline. GPT effort levels "
    "(Low/Medium/High/XHigh/Max) move both vertically and horizontally because higher effort "
    "consumes more tokens. Claude Fable 5.1 (max) at ~$13.1k reflects AA measured token "
    "volume for its evaluation run; it is the top-right extreme of this snapshot."
)
footer_3 = (
    "Sources: artificialanalysis.ai | openrouter.ai | Matplotlib | Price snapshot: 18 Sep 2026"
)
wrap_at = 168
footer_lines = textwrap.wrap(footer_1, wrap_at) + textwrap.wrap(footer_2, wrap_at) + textwrap.wrap(footer_3, wrap_at)
n = len(footer_lines)
line_height = 0.017
for i, line in enumerate(footer_lines):
    fig.text(0.05, 0.010 + line_height * (n - 1 - i), line, fontsize=8.1, va="bottom")

bottom_margin = 0.030 + line_height * n
plt.tight_layout(rect=[0.03, bottom_margin, 0.98, 0.96])
fig.savefig(str(OUT) + ".png", dpi=220, bbox_inches="tight")
fig.savefig(str(OUT) + ".pdf", bbox_inches="tight")
fig.savefig(str(OUT) + ".svg", bbox_inches="tight")

