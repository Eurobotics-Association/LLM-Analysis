from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter

OUT = Path(__file__).resolve().parents[1]
(OUT / 'charts' / 'latest').mkdir(parents=True, exist_ok=True)
(OUT / 'data').mkdir(parents=True, exist_ok=True)
(OUT / 'src').mkdir(parents=True, exist_ok=True)
(OUT / 'docs').mkdir(parents=True, exist_ok=True)

historical_rows = [
    ('GPT-5.6 Sol','P1',396,57.3), ('GPT-5.6 Sol','P2',499,68.3),
    ('GPT-5.6 Sol','P3',857,73.7), ('GPT-5.6 Sol','P4',1182,76.4),
    ('GPT-5.6 Sol','P5',1492,78.1), ('GPT-5.6 Sol','Max',2018,80.0),
    ('GPT-5.6 Terra','P1',114,38.6), ('GPT-5.6 Terra','P2',146,52.5),
    ('GPT-5.6 Terra','P3',260,63.2), ('GPT-5.6 Terra','P4',456,71.0),
    ('GPT-5.6 Terra','P5',537,72.4), ('GPT-5.6 Terra','Max',776,77.4),
    ('GPT-5.6 Luna','P1',27.1,35.6), ('GPT-5.6 Luna','P2',17.6,40.8),
    ('GPT-5.6 Luna','P3',35.3,57.6), ('GPT-5.6 Luna','P4',69.2,66.9),
    ('GPT-5.6 Luna','P5',90.8,69.8), ('GPT-5.6 Luna','Max',111,74.6),
    ('GPT-5.5','P1',346,44.1), ('GPT-5.5','P2',420,56.6),
    ('GPT-5.5','P3',963,69.7), ('GPT-5.5','P4',970,71.7),
    ('GPT-5.5','XHigh',1763,76.4),
    ('Claude Opus 4.8','P1',1080,67.0), ('Claude Opus 4.8','Max',2534,72.5),
    ('Claude Fable 5','Max',3864,77.2),
    ('Gemini 3.1 Pro Preview','Preview',664,42.7),
]
hist = pd.DataFrame(historical_rows, columns=['Model','SourcePoint','Aug21_estimated_cost_USD','Index_score'])
launch_factor = {'GPT-5.6 Luna':0.2, 'GPT-5.6 Terra':0.8, 'GPT-5.6 Sol':0.8}
hist['Launch_estimated_cost_USD'] = hist.apply(lambda r: r['Aug21_estimated_cost_USD']/launch_factor.get(r['Model'],1.0), axis=1)
map56 = {'P1':'None','P2':'Low','P3':'Medium','P4':'High','P5':'Extra-high','Max':'Max'}
map55 = {'P1':'None','P2':'Low','P3':'Medium','P4':'High','XHigh':'Extra-high'}
def effort_label(row):
    if row['Model'].startswith('GPT-5.6'):
        return map56[row['SourcePoint']]
    if row['Model'] == 'GPT-5.5':
        return map55[row['SourcePoint']]
    return row['SourcePoint']
hist['EffortLabel'] = hist.apply(effort_label, axis=1)
hist.to_csv(OUT/'data'/'historical_coding_agent_index_v11.csv', index=False)
hist_plot = hist[~((hist.Model=='GPT-5.6 Luna') & (hist.SourcePoint=='P1'))].copy()

current_rows = [
    ('GLM-5.3-Flash',42,280.28,'Z.ai','measured'),
    ('DeepSeek V4 Flash 0731 Max',35,474.19,'DeepSeek','measured'),
    ('Z.ai GLM-5.3 Max',45,2503.48,'Z.ai','measured'),
    ('Qwen3 Coder 30B A3B',10,None,'Alibaba','index estimated; total eval cost unavailable'),
    ('GPT-5.6 Luna Max',38,319.93,'OpenAI','measured'),
    ('GPT-5.6 Terra Max',42,2500.72,'OpenAI','measured'),
    ('GPT-5.6 Sol Max',47,3465.00,'OpenAI','measured'),
]
current = pd.DataFrame(current_rows, columns=['Model','Intelligence_Index','Total_Index_Cost_USD','Vendor','Status'])
current.to_csv(OUT/'data'/'current_intelligence_index_v43.csv', index=False)

colors = {
    'GPT-5.6 Luna':'#1f77b4','GPT-5.6 Terra':'#ff7f0e','GPT-5.6 Sol':'#d62728',
    'GPT-5.5':'#9467bd','Claude Opus 4.8':'#8c564b','Claude Fable 5':'#e377c2',
    'Gemini 3.1 Pro Preview':'#7f7f7f','GLM-5.3-Flash':'#17becf',
    'DeepSeek V4 Flash 0731 Max':'#2ca02c','Z.ai GLM-5.3 Max':'#bcbd22',
    'Qwen3 Coder 30B A3B':'#ff1493','GPT-5.6 Luna Max':'#1f77b4',
    'GPT-5.6 Terra Max':'#ff7f0e','GPT-5.6 Sol Max':'#d62728',
}

fig = plt.figure(figsize=(16,13))
ax1 = fig.add_axes([0.07,0.56,0.89,0.34])
line_models=['GPT-5.6 Luna','GPT-5.6 Terra','GPT-5.6 Sol','GPT-5.5','Claude Opus 4.8']
markers=['o','s','D','^','P']
for model,marker in zip(line_models,markers):
    d=hist_plot[hist_plot.Model==model]
    ax1.plot(d['Launch_estimated_cost_USD'],d['Index_score'],marker=marker,linewidth=2.2,markersize=7.5,color=colors[model],label=model)
    for _,r in d.iterrows():
        ax1.annotate(f"{r['EffortLabel']}\n{r['Index_score']:.1f}",(r['Launch_estimated_cost_USD'],r['Index_score']),xytext=(5,5),textcoords='offset points',fontsize=7.8,color=colors[model])
for model,marker in [('Claude Fable 5','X'),('Gemini 3.1 Pro Preview','v')]:
    d=hist_plot[hist_plot.Model==model]
    ax1.scatter(d['Launch_estimated_cost_USD'],d['Index_score'],marker=marker,s=75,color=colors[model],label=model)
ax1.set_xscale('log'); ax1.set_xlim(70,5000); ax1.set_ylim(34,82.5)
ticks1=[75,100,150,200,300,500,750,1000,1500,2000,3000,5000]
ax1.xaxis.set_major_locator(FixedLocator(ticks1)); ax1.xaxis.set_major_formatter(FuncFormatter(lambda x,pos:f'${x:,.0f}'))
ax1.grid(True,which='major',alpha=.35); ax1.grid(True,which='minor',alpha=.10)
ax1.set_xlabel('Estimated total API cost of historical v1.1 benchmark run (USD, log scale)')
ax1.set_ylabel('AA Coding Agent Index v1.1')
ax1.set_title('A — Historical Coding Agent Index v1.1 reconstruction',fontsize=15,pad=10)
ax1.legend(loc='lower right',fontsize=7.5,ncol=2)

ax2 = fig.add_axes([0.07,0.17,0.89,0.28])
ax2.set_xscale('log'); ax2.set_xlim(200,4500); ax2.set_ylim(5,51)
ticks2=[200,250,300,400,500,750,1000,1500,2000,2500,3000,3500,4000]
ax2.xaxis.set_major_locator(FixedLocator(ticks2)); ax2.xaxis.set_major_formatter(FuncFormatter(lambda x,pos:f'${x:,.0f}'))
ax2.grid(True,which='major',alpha=.30); ax2.grid(True,which='minor',alpha=.08)
for _,r in current.dropna(subset=['Total_Index_Cost_USD']).iterrows():
    model=r['Model']; x=float(r['Total_Index_Cost_USD']); y=float(r['Intelligence_Index']); c=colors[model]
    ax2.axhline(y,color=c,linewidth=1.45,alpha=.58)
    ax2.vlines(x,ymin=ax2.get_ylim()[0],ymax=y,color=c,linewidth=1.5,linestyle=':',alpha=.95)
    ax2.scatter([x],[y],s=105,color=c,edgecolor='black',linewidth=.6,zorder=5)
    ax2.annotate(f'{model}\nIndex {y:.0f} | total ${x:,.0f}',(x,y),xytext=(6,6),textcoords='offset points',fontsize=8.0,color=c,bbox=dict(boxstyle='round,pad=0.20',facecolor='white',edgecolor=c,alpha=.90))
qwen=current[current.Model=='Qwen3 Coder 30B A3B'].iloc[0]; qy=float(qwen.Intelligence_Index); qc=colors['Qwen3 Coder 30B A3B']
ax2.axhline(qy,color=qc,linewidth=1.5,linestyle='--',alpha=.75)
ax2.text(0.015,(qy-5)/(51-5)+0.012,'Qwen3 Coder 30B A3B — estimated Index 10; full v4.3 evaluation cost not published',transform=ax2.transAxes,fontsize=8.5,color=qc,ha='left',va='bottom',bbox=dict(boxstyle='round,pad=0.20',facecolor='white',edgecolor=qc,alpha=.90))
ax2.set_xlabel('Total cost to run Artificial Analysis Intelligence Index v4.3 (USD, log scale)')
ax2.set_ylabel('AA Intelligence Index v4.3')
ax2.set_title('B — Current Intelligence Index vs TOTAL evaluation cost (17 Sep 2026)\nhorizontal = index level; dotted vertical = total evaluation cost; point = measured intersection',fontsize=14,pad=9)

fig.text(0.07,0.100,'Correction from prior version: the previous lower panel used blended API price per 1M tokens. That is why Sol appeared near USD 3.08. Here the x-axis is TOTAL cost to run the full Artificial Analysis Intelligence Index. Sol Max is therefore about USD 3,465, Terra Max about USD 2,501, Luna Max about USD 320.',fontsize=8.8,va='top')
fig.text(0.07,0.062,'Sources: Artificial Analysis model pages / comparison pages, accessed 17 Sep 2026. Current measured totals: GLM-5.3-Flash USD 280.28; DeepSeek V4 Flash 0731 Max USD 474.19; GLM-5.3 Max USD 2,503.48; GPT-5.6 Luna Max USD 319.93; Terra Max USD 2,500.72; Sol Max USD 3,465. Qwen3 Coder 30B A3B has an estimated Intelligence Index of 10 but no published comparable full-index total cost.',fontsize=8.1,va='top')

png=OUT/'charts'/'latest'/'llm_cost_performance_latest.png'
pdf=OUT/'charts'/'latest'/'llm_cost_performance_latest.pdf'
svg=OUT/'charts'/'latest'/'llm_cost_performance_latest.svg'
fig.savefig(png,dpi=220,bbox_inches='tight'); fig.savefig(pdf,bbox_inches='tight'); fig.savefig(svg,bbox_inches='tight'); plt.close(fig)

print('\n'.join(map(str,[png,pdf,svg,OUT/'data'/'historical_coding_agent_index_v11.csv',OUT/'data'/'current_intelligence_index_v43.csv'])))
