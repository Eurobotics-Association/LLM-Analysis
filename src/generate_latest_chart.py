from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "eurobotics_v12_aa_v43_openrouter_total_cost_2026-09-18.csv"
OUT = ROOT / "charts" / "latest" / "llm_cost_performance_latest"

df = pd.read_csv(DATA)

colors = {
    "GPT-5.6 Luna":"#1f77b4",
    "GPT-5.6 Terra":"#ff7f0e",
    "GPT-5.6 Sol":"#d62728",
    "GLM-5.3 Flash":"#17becf",
    "DeepSeek V4.1 Flash":"#2ca02c",
    "GLM-5.3 Max":"#bcbd22",
    "Qwen3 Coder 30B":"#e377c2",
}
markers = {
    "GPT-5.6 Luna":"o","GPT-5.6 Terra":"s","GPT-5.6 Sol":"D",
    "GLM-5.3 Flash":"P","DeepSeek V4.1 Flash":"X","GLM-5.3 Max":"^"
}

fig, ax = plt.subplots(figsize=(16,10))

for model in ["GPT-5.6 Luna","GPT-5.6 Terra","GPT-5.6 Sol"]:
    d = df[df.Model==model].sort_values("Est_OR_Total_Cost")
    ax.plot(d.Est_OR_Total_Cost, d.AA_Index,
            marker=markers[model], linewidth=2.6, markersize=8,
            color=colors[model], label=model)
    for _,r in d.iterrows():
        star="*" if "promo" in str(r.Price_Note).lower() else ""
        ax.annotate(f"{r.Effort}{star}\\n{int(r.AA_Index)}",
                    (r.Est_OR_Total_Cost,r.AA_Index),
                    xytext=(6,5), textcoords="offset points",
                    fontsize=8, color=colors[model])

for model in ["GLM-5.3 Flash","DeepSeek V4.1 Flash","GLM-5.3 Max"]:
    r=df[df.Model==model].iloc[0]
    x=float(r.Est_OR_Total_Cost); y=float(r.AA_Index); c=colors[model]
    ax.axhline(y,color=c,alpha=.2,linewidth=1.2)
    ax.vlines(x,8,y,color=c,linestyle=":",linewidth=1.5)
    ax.scatter([x],[y],s=120,color=c,marker=markers[model],
               edgecolor="black",linewidth=.6,zorder=5,label=model)
    star=" *" if "promo" in str(r.Price_Note).lower() else ""
    ax.annotate(f"{model}{star}\\nIndex {int(y)} | est. $" + f"{x:,.0f}",
                (x,y),xytext=(8,7),textcoords="offset points",
                fontsize=8.2,color=c,
                bbox=dict(boxstyle="round,pad=.2",facecolor="white",edgecolor=c,alpha=.9))

ax.axhline(10,color=colors["Qwen3 Coder 30B"],linestyle="--",alpha=.55)
ax.text(.012,.065,
        "Qwen3 Coder 30B A3B — AA Index 10; no comparable AA total evaluation cost",
        transform=ax.transAxes,fontsize=8.3,color=colors["Qwen3 Coder 30B"],
        bbox=dict(boxstyle="round,pad=.2",facecolor="white",
                  edgecolor=colors["Qwen3 Coder 30B"],alpha=.9))

ax.set_xscale("log"); ax.set_xlim(20,4000); ax.set_ylim(8,50)
ticks=[25,50,75,100,150,200,300,500,750,1000,1500,2000,2500,3000,4000]
ax.xaxis.set_major_locator(FixedLocator(ticks))
ax.xaxis.set_major_formatter(FuncFormatter(lambda x,pos:f"$" + f"{x:,.0f}"))
ax.grid(True,which="major",alpha=.33)
ax.grid(True,which="minor",alpha=.08)

ax.set_xlabel(
    "Estimated total OpenRouter API cost to run the AA Intelligence Index (USD, log scale)\\n"
    "AA evaluation workload repriced to current OpenRouter headline tariffs")
ax.set_ylabel("Artificial Analysis Intelligence Index v4.3")
ax.set_title(
    "Eurobotics LLM Cost / Intelligence Map\\n"
    "AA Intelligence Index v4.3 × current OpenRouter pricing",
    fontsize=16,pad=14)

handles,labels=ax.get_legend_handles_labels()
seen=set(); hh=[]; ll=[]
for h,l in zip(handles,labels):
    if l not in seen:
        hh.append(h); ll.append(l); seen.add(l)
ax.legend(hh,ll,loc="lower right",fontsize=8.5,title="Model / family")

ax.text(.012,.97,
        "More attractive ↖\\nhigher intelligence / lower estimated total API cost",
        transform=ax.transAxes,va="top",fontsize=10,fontweight="bold",
        bbox=dict(boxstyle="round,pad=.35",facecolor="white",alpha=.88))

fig.text(.08,.076,
    "Eurobotics methodology v1.2: Y = Artificial Analysis Intelligence Index v4.3. "
    "X = AA total evaluation cost repriced to current OpenRouter prices. "
    "Repricing uses the OpenRouter/AA ratio of a 7:2:1 blended tariff "
    "(70% cache-read, 20% input, 10% output). This is an estimate because the full "
    "per-model token-type matrix is not exposed as one simple downloadable table.",
    fontsize=8.2,va="bottom")
fig.text(.08,.044,
    "* Current OpenRouter promotional/headline price. Current promotions can change the ordering; "
    "Sol and GLM-5.3 Flash are presently discounted.",
    fontsize=8.1,va="bottom")
fig.text(.08,.017,
    "Sources: https://artificialanalysis.ai/  |  https://openrouter.ai/  |  "
    "Matplotlib  |  Price snapshot: 18 Sep 2026",
    fontsize=8.1,va="bottom")

plt.tight_layout(rect=[.03,.13,.98,.96])
fig.savefig(str(OUT)+".png",dpi=220,bbox_inches="tight")
fig.savefig(str(OUT)+".pdf",bbox_inches="tight")
fig.savefig(str(OUT)+".svg",bbox_inches="tight")
