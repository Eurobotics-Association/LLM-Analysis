from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "eurobotics_llm_index_v43_openrouter_2026-09-17.csv"
OUT = ROOT / "charts" / "latest" / "llm_cost_performance_latest"

df = pd.read_csv(DATA)

COLORS = {
    "GPT-5.6 Luna": "#1f77b4",
    "GPT-5.6 Terra": "#ff7f0e",
    "GPT-5.6 Sol": "#d62728",
    "GLM-5.3 Flash": "#17becf",
    "DeepSeek V4.1 Flash": "#2ca02c",
    "GLM-5.3 Max": "#bcbd22",
    "Qwen3 Coder 30B A3B": "#e377c2",
}

MARKERS = {
    "GPT-5.6 Luna": "o",
    "GPT-5.6 Terra": "s",
    "GPT-5.6 Sol": "D",
    "GLM-5.3 Flash": "P",
    "DeepSeek V4.1 Flash": "X",
    "GLM-5.3 Max": "^",
    "Qwen3 Coder 30B A3B": "v",
}

fig, ax = plt.subplots(figsize=(16, 10))

# GPT-5.6 reasoning-effort trajectories. OpenRouter charges the same
# per-token tariff at each effort level, so each family is vertical.
for model in ["GPT-5.6 Luna", "GPT-5.6 Terra", "GPT-5.6 Sol"]:
    d = df[df.Model == model]
    x = d["Eurobotics_Blended_USD_per_1M"].iloc[0]
    ax.plot(
        [x] * len(d),
        d["AA_Intelligence_Index_v4_3"],
        color=COLORS[model],
        marker=MARKERS[model],
        linewidth=2.4,
        markersize=8,
        label=model,
    )

    # Place Sol labels to the left and Terra/Luna labels to the right
    # to keep the expensive-model cluster readable.
    dx = -48 if model == "GPT-5.6 Sol" else 8
    for _, r in d.iterrows():
        ax.annotate(
            f'{r["Level"]} {int(r["AA_Intelligence_Index_v4_3"])}',
            (x, r["AA_Intelligence_Index_v4_3"]),
            xytext=(dx, 3),
            textcoords="offset points",
            fontsize=8.4,
            color=COLORS[model],
        )

# Current single-point references.
for model in ["GLM-5.3 Flash", "DeepSeek V4.1 Flash", "GLM-5.3 Max", "Qwen3 Coder 30B A3B"]:
    r = df[df.Model == model].iloc[0]
    x = float(r["Eurobotics_Blended_USD_per_1M"])
    y = float(r["AA_Intelligence_Index_v4_3"])
    c = COLORS[model]

    ax.axhline(y, color=c, alpha=0.22, linewidth=1.25)
    ax.vlines(x, ymin=7, ymax=y, color=c, linestyle=":", linewidth=1.5, alpha=0.95)
    ax.scatter(
        [x], [y], s=120, color=c, edgecolor="black", linewidth=0.6,
        marker=MARKERS[model], zorder=5, label=model,
    )

    promo = " promo" if bool(r["Current_OpenRouter_Promo"]) else ""
    ax.annotate(
        f'{model}\nIndex {int(y)} | blend ${x:.3g}/M{promo}',
        (x, y), xytext=(8, 7), textcoords="offset points",
        fontsize=8.2, color=c,
        bbox=dict(boxstyle="round,pad=0.22", facecolor="white", edgecolor=c, alpha=0.9),
    )

ax.set_xscale("log")
ax.set_xlim(0.08, 7.5)
ax.set_ylim(7, 50)
xticks = [0.1, 0.12, 0.15, 0.2, 0.3, 0.45, 0.6, 1.0, 1.4, 2.0, 3.0, 4.0, 4.5, 6.0]
ax.xaxis.set_major_locator(FixedLocator(xticks))
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"${x:.2f}" if x < 1 else f"${x:.1f}"))
ax.grid(True, which="major", alpha=0.32)
ax.grid(True, which="minor", alpha=0.07)

ax.set_xlabel(
    "Eurobotics blended OpenRouter API tariff (USD per 1M tokens, log scale)\n"
    "75% input + 25% output; current headline OpenRouter prices as of 17 Sep 2026",
    fontsize=11,
)
ax.set_ylabel("Artificial Analysis Intelligence Index v4.3", fontsize=11)
ax.set_title(
    "Eurobotics LLM Cost / Intelligence Map - DevOps & AI-Agent Selection\n"
    "AA Intelligence Index v4.3 x current OpenRouter API pricing",
    fontsize=16,
    pad=14,
)

handles, labels = ax.get_legend_handles_labels()
seen, out_h, out_l = set(), [], []
for h, label in zip(handles, labels):
    if label not in seen:
        out_h.append(h)
        out_l.append(label)
        seen.add(label)
ax.legend(out_h, out_l, loc="lower right", fontsize=8.5, title="Model / family")

ax.text(
    0.012, 0.97,
    "More attractive <-\nhigher index / lower API tariff",
    transform=ax.transAxes,
    va="top",
    ha="left",
    fontsize=10,
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.35", facecolor="white", alpha=0.88),
)

fig.text(
    0.08, 0.075,
    "Eurobotics methodology v1.0 - Performance: Artificial Analysis Intelligence Index v4.3. "
    "Price: current OpenRouter input/output tariff. Blended x = 75% input + 25% output. "
    "GPT effort levels share the same x because OpenRouter's per-token tariff is unchanged by reasoning effort; "
    "higher effort may still consume more tokens in a real task. Promotional OpenRouter tariffs are snapshot values and may change.",
    fontsize=8.5,
    va="bottom",
)
fig.text(
    0.08, 0.035,
    "Sources: https://artificialanalysis.ai/  |  https://openrouter.ai/  |  Chart generated with Matplotlib  |  Snapshot: 17 Sep 2026",
    fontsize=8.2,
    va="bottom",
)

plt.tight_layout(rect=[0.03, 0.12, 0.98, 0.96])
fig.savefig(str(OUT) + ".png", dpi=220, bbox_inches="tight")
fig.savefig(str(OUT) + ".pdf", bbox_inches="tight")
fig.savefig(str(OUT) + ".svg", bbox_inches="tight")
plt.close(fig)

print(str(OUT) + ".png")
print(str(OUT) + ".pdf")
print(str(OUT) + ".svg")
