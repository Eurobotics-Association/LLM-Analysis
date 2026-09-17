from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter

# Eurobotics methodology v1.1 — AA workload repriced to standard OpenRouter tariffs.
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "eurobotics_v11_aa_v43_openrouter_normalized_2026-09-17.csv"
OUT = ROOT / "charts" / "latest" / "llm_cost_performance_latest"

df = pd.read_csv(DATA)

colors = {
    "GPT-5.6 Luna":"#1f77b4",
    "GPT-5.6 Terra":"#ff7f0e",
    "GPT-5.6 Sol":"#d62728",
    "GLM-5.3 Flash":"#17becf",
    "DeepSeek V4.1 Flash":"#2ca02c",
    "GLM-5.3 Max":"#bcbd22",
    "Qwen3 Coder 30B A3B Instruct":"#e377c2",
}
markers = {
    "GPT-5.6 Luna":"o","GPT-5.6 Terra":"s","GPT-5.6 Sol":"D",
    "GLM-5.3 Flash":"P","DeepSeek V4.1 Flash":"X","GLM-5.3 Max":"^"
}

fig, ax = plt.subplots(figsize=(16,10))

for model in ["GPT-5.6 Luna","GPT-5.6 Terra","GPT-5.6 Sol"]:
    d = df[df.Model==model].sort_values("Eurobotics_Normalized_Cost_per_Task_USD")
    ax.plot(d["Eurobotics_Normalized_Cost_per_Task_USD"],
            d["AA_Intelligence_Index_v4_3"],
            marker=markers[model], linewidth=2.6, markersize=8,
            color=colors[model], label=model)
    for _,r in d.iterrows():
        ax.annotate(f'{r["Effort"]}\n{int(r["AA_Intelligence_Index_v4_3"])}',
                    (r["Eurobotics_Normalized_Cost_per_Task_USD"],r["AA_Intelligence_Index_v4_3"]),
                    xytext=(6,5), textcoords="offset points",
                    fontsize=8.1,color=colors[model])

for model in ["GLM-5.3 Flash","DeepSeek V4.1 Flash","GLM-5.3 Max"]:
    r=df[df.Model==model].iloc[0]
    x=float(r["Eurobotics_Normalized_Cost_per_Task_USD"])
    y=float(r["AA_Intelligence_Index_v4_3"])
    c=colors[model]
    ax.axhline(y,color=c,linewidth=1.3,alpha=.22)
    ax.vlines(x,ymin=8,ymax=y,color=c,linestyle=":",linewidth=1.5,alpha=.95)
    ax.scatter([x],[y],s=120,color=c,marker=markers[model],
               edgecolor="black",linewidth=.6,zorder=5,label=model)
    ax.annotate(f'{model}\nIndex {int(y)} | ${x:.3f}/task',
                (x,y),xytext=(8,7),textcoords="offset points",
                fontsize=8.3,color=c,
                bbox=dict(boxstyle="round,pad=0.22",facecolor="white",edgecolor=c,alpha=.9))

qy=10
qc=colors["Qwen3 Coder 30B A3B Instruct"]
ax.axhline(qy,color=qc,linestyle="--",linewidth=1.3,alpha=.55)
ax.text(.012,(qy-8)/(50-8)+.008,
        "Qwen3 Coder 30B A3B — AA Index 10; AA cost/task N/A → no normalized x-position",
        transform=ax.transAxes,fontsize=8.4,color=qc,ha="left",va="bottom",
        bbox=dict(boxstyle="round,pad=.22",facecolor="white",edgecolor=qc,alpha=.9))

ax.set_xscale("log")
ax.set_xlim(.008,3.0); ax.set_ylim(8,50)
ticks=[.01,.02,.03,.05,.1,.15,.2,.3,.5,.75,1,1.5,2,3]
ax.xaxis.set_major_locator(FixedLocator(ticks))
ax.xaxis.set_major_formatter(FuncFormatter(lambda x,pos:f"${x:.2f}" if x<1 else f"${x:.1f}"))
ax.grid(True,which="major",alpha=.33); ax.grid(True,which="minor",alpha=.08)
ax.set_xlabel("Eurobotics normalized cost per Artificial Analysis Intelligence Index task (USD, log scale)\nAA measured workload/effort repriced to standard non-promotional OpenRouter tariffs",fontsize=11)
ax.set_ylabel("Artificial Analysis Intelligence Index v4.3",fontsize=11)
ax.set_title("Eurobotics LLM Cost / Intelligence Map — DevOps & AI-Agent Selection\nAA Intelligence Index v4.3 × OpenRouter-standard normalized task cost",fontsize=16,pad=14)

handles,labels=ax.get_legend_handles_labels()
seen=set();hh=[];ll=[]
for h,l in zip(handles,labels):
    if l not in seen: hh.append(h);ll.append(l);seen.add(l)
ax.legend(hh,ll,loc="lower right",fontsize=8.5,title="Model / family")
ax.text(.012,.97,"More attractive ↖\nhigher intelligence / lower normalized task cost",
        transform=ax.transAxes,va="top",ha="left",fontsize=10,fontweight="bold",
        bbox=dict(boxstyle="round,pad=.35",facecolor="white",alpha=.88))

fig.text(.08,.078,
    "Eurobotics methodology v1.1: Y = Artificial Analysis Intelligence Index v4.3. "
    "X = AA measured cost/task repriced to standard, non-promotional OpenRouter tariffs. "
    "Repricing factor = OpenRouter 7:2:1 blended tariff / AA 7:2:1 blended tariff "
    "(70% cache-read, 20% uncached input, 10% output).",
    fontsize=8.4,va="bottom")
fig.text(.08,.035,
    "Sources: https://artificialanalysis.ai/ | https://openrouter.ai/ | Matplotlib | Snapshot: 17 Sep 2026. "
    "Qwen3 Coder 30B is not x-plotted because AA currently publishes no cost/task for that model.",
    fontsize=8.1,va="bottom")
plt.tight_layout(rect=[.03,.13,.98,.96])
fig.savefig(str(OUT)+".png",dpi=220,bbox_inches="tight")
fig.savefig(str(OUT)+".pdf",bbox_inches="tight")
fig.savefig(str(OUT)+".svg",bbox_inches="tight")
