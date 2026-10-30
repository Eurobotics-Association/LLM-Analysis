from pathlib import Path
import datetime
import re
import textwrap
from zoneinfo import ZoneInfo

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, LogLocator
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/eurobotics_v18_aa_v5_openrouter_nopromo_eurobotics_261030_1727.csv'
now = datetime.datetime.now(ZoneInfo('Europe/Paris'))
name = f'llm_cost_performance_latest_eurobotics_{now:%y%m%d_%H%M}'
output = ROOT / 'charts/latest' / name
df = pd.read_csv(DATA)
costed = df.AA_Total_Cost.notna()
if df.loc[~costed, 'Est_OR_Total_Cost'].notna().any():
    raise ValueError('Reference-only models cannot have an estimated cost')
aa = .7 * df.loc[costed, 'AA_Cache'] + .2 * df.loc[costed, 'AA_In'] + .1 * df.loc[costed, 'AA_Out']
orate = .7 * df.loc[costed, 'OR_Cache'] + .2 * df.loc[costed, 'OR_In'] + .1 * df.loc[costed, 'OR_Out']
if aa.isna().any() or orate.isna().any() or (aa <= 0).any():
    raise ValueError('Missing tariff or invalid AA blend')
for column, computed, tolerance in [('AA_Blend', aa, .00001), ('OR_Blend', orate, .00001), ('Ratio', orate / aa, .000002), ('Est_OR_Total_Cost', df.loc[costed, 'AA_Total_Cost'] * orate / aa, .011)]:
    if ((df.loc[costed, column] - computed).abs() > tolerance).any():
        raise ValueError(f'{column} does not match source tariffs')
    df.loc[costed, column] = computed

colors = ['#0072b2','#d55e00','#cc79a7','#009e73','#56b4e9','#e69f00','#332288','#882255','#44aa99','#117733','#aa4499','#999933','#666666']
fig, ax = plt.subplots(figsize=(16, 10.5))
curves = ['GPT-6.1 Terra', 'GPT-6.1 Sol', 'GPT-6 Astra', 'GPT-6 Luna']
effort_order = {'Low': 0, 'Medium': 1, 'High': 2, 'XHigh': 3, 'Max': 4}
for i, model in enumerate(curves):
    d = df[(df.Model == model) & costed].copy()
    d['order'] = d.Effort.map(effort_order)
    d = d.sort_values('order')
    # A missing effort does not imply an observed intermediate curve.
    for (_, a), (_, b) in zip(d.iloc[:-1].iterrows(), d.iloc[1:].iterrows()):
        if b['order'] == a['order'] + 1:
            ax.plot([a.Est_OR_Total_Cost, b.Est_OR_Total_Cost], [a.AA_Index, b.AA_Index], color=colors[i], linewidth=1.8, zorder=2)
    ax.scatter(d.Est_OR_Total_Cost, d.AA_Index, s=48, color=colors[i], label=model, zorder=3)
    for _, r in d.iterrows():
        offset = (4, 5)
        if model in {'GPT-6 Astra', 'GPT-6.1 Terra'} and r.Effort == 'XHigh':
            offset = (4, -12)
        ax.annotate(r.Effort, (r.Est_OR_Total_Cost, r.AA_Index), xytext=offset, textcoords='offset points', color=colors[i], fontsize=7)

for i, (_, r) in enumerate(df[costed & ~df.Model.isin(curves)].iterrows()):
    ax.scatter(r.Est_OR_Total_Cost, r.AA_Index, marker=['s','D','^','v','P','X','h','p','*'][i % 9], s=75, color=colors[(i+4) % len(colors)], edgecolor='white', linewidth=.6, label=r.Model, zorder=4)
for _, r in df[~costed].iterrows():
    ax.axhline(r.AA_Index, color='#777777', linewidth=.8, linestyle='--', alpha=.65)
    ax.text(0.01, r.AA_Index + .3, f'{r.Model}: {r.AA_Index:g} (intelligence reference only)', transform=ax.get_yaxis_transform(), fontsize=8, color='#555555', va='bottom', bbox={'facecolor':'white','edgecolor':'none','alpha':.8})

ax.set_xscale('log')
ax.set_xlim(5, 25000)
ax.set_ylim(4, 64)
ax.xaxis.set_major_locator(LogLocator(base=10, subs=(1, 2, 5)))
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f'${v:,.0f}'))
ax.grid(True, which='major', alpha=.25)
ax.set_xlabel('Estimated OpenRouter cost for the complete AA evaluation (USD, logarithmic scale)')
ax.set_ylabel('Artificial Analysis Intelligence Index v5')
ax.set_title('Eurobotics LLM Cost / Intelligence Map\nAA Index v5 × selected non-promotional OpenRouter provider prices', fontsize=16, pad=12)
ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1), frameon=False, fontsize=8.5, title='Models')
ax.text(.012, .98, 'Higher intelligence / lower cost ↖', transform=ax.transAxes, va='top', fontsize=9, bbox={'facecolor':'white','edgecolor':'none','alpha':.85})

repo='https://github.com/Eurobotics-Association/LLM-Analysis'
aa_url='https://artificialanalysis.ai/'
footers=[
'Methodology v1.8: AA Intelligence Index v5 and AA measured total evaluation cost, repriced with the ratio of selected non-promotional OpenRouter and AA 7:2:1 blends (70% cache read / 20% input / 10% output). Cache-write and tiered prices limit accuracy; this is an estimate, not an invoice.',
'GPT effort labels are measured points; missing Luna Medium is not interpolated. Rounded Astra High and XHigh scores are equal. Reference lines have no verified comparable OpenRouter cost. See methodology for omissions and pricing caveats.',
'Disclaimer: For informational use only; do not use for budgeting. Pricing and benchmark data change frequently. Verify prices and capability for your own requirements. Eurobotics.org provides this information without warranty.',
f'Sources: {aa_url} | OpenRouter audit: 30 October 2026 | Generated: {now:%Y-%m-%d %H:%M:%S %Z}',
f'Repository: {repo}'
]
lines=[line for f in footers for line in textwrap.wrap(f, 160)]
for i, line in enumerate(lines):
    t=fig.text(.055, .015 + .016*(len(lines)-i-1), line, fontsize=7.8, va='bottom')
    if repo in line: t.set_url(repo)
    elif aa_url in line: t.set_url(aa_url)
fig.subplots_adjust(left=.075, right=.80, top=.89, bottom=.10 + .016*len(lines))
for ext in ('png','pdf','svg'):
    fig.savefig(f'{output}.{ext}', dpi=200, bbox_inches='tight')
plt.close(fig)
readme_path=ROOT/'README.md'
readme=readme_path.read_text(encoding='utf-8')
for ext in ('svg','png','pdf'):
    readme=re.sub(rf'charts/latest/llm_cost_performance_latest(?:_eurobotics_\d{{6}}_\d{{4}})?\.{ext}', f'charts/latest/{name}.{ext}', readme)
readme_path.write_text(readme, encoding='utf-8')
print(name)
