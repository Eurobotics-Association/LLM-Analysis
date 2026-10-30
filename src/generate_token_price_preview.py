#!/usr/bin/env python3
"""Render a review-only SVG: AA v5 score versus OpenRouter output tariff."""
import csv, json, math, sys
from datetime import datetime, timezone
from html import escape
from pathlib import Path

if len(sys.argv) != 4:
    raise SystemExit('Usage: generate.py AA_SNAPSHOT.csv ENDPOINT_SNAPSHOT.json OUTPUT_DIR')
source, endpoint_file, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
endpoint_snapshot = json.loads(endpoint_file.read_text(encoding='utf-8'))
out.mkdir(parents=True, exist_ok=True)
now = datetime.now(timezone.utc)
suffix = now.strftime('eurobotics_%y%m%d_%H%M')
stamp = now.strftime('%Y-%m-%d %H:%M:%S UTC')
records = list(csv.DictReader(source.open(encoding='utf-8', newline='')))
points, excluded = [], []
for row in records:
    if not row['OpenRouter_URL'] or not row['AA_Index']:
        excluded.append(row['Model'] + ': no linked endpoint or AA score')
        continue
    slug = row['OpenRouter_URL'].removeprefix('https://openrouter.ai/')
    if slug not in endpoint_snapshot['models']:
        excluded.append(row['Model'] + ': endpoint listing missing')
        continue
    data = endpoint_snapshot['models'][slug]['data']
    candidates = [e for e in data['endpoints'] if e.get('status') == 0
                  and e.get('pricing', {}).get('discount') == 0
                  and e.get('pricing', {}).get('completion') is not None
                  and float(e['pricing']['completion']) > 0
                  and 'reasoning_effort' in e.get('supported_parameters', [])]
    if not candidates:
        excluded.append(row['Model'] + ': no eligible non-promotional quoted output rate')
        continue
    chosen = min(candidates, key=lambda e: (float(e['pricing']['completion']), e['tag']))
    rate = chosen['pricing']
    def m(key):
        return '' if rate.get(key) is None else format(float(rate[key]) * 1_000_000, '.8g')
    points.append({'model':row['Model'], 'effort':row['Effort'], 'aa_index':row['AA_Index'],
                   'output_per_m':m('completion'), 'input_per_m':m('prompt'),
                   'cache_read_per_m':m('input_cache_read'), 'cache_write_per_m':m('input_cache_write'),
                   'endpoint':chosen['tag'], 'provider':chosen['provider_name'],
                   'quantization':chosen.get('quantization') or 'unknown',
                   'tier':chosen.get('service_tier') or 'standard',
                   'overrides':json.dumps(rate.get('overrides', []), separators=(',', ':')),
                   'aa_source':row['AA_Source'], 'endpoint_source':'https://openrouter.ai/api/v1/models/'+slug+'/endpoints',
                   'score_snapshot':'2026-10-30 (existing v1.8 AA v5 snapshot)',
                   'price_checked_utc':endpoint_snapshot['checked_utc'], 'rendered_at_utc':stamp})

csv_path = out / ('aa_v5_openrouter_output_rates_' + suffix + '.csv')
with csv_path.open('w', encoding='utf-8', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=list(points[0])); writer.writeheader(); writer.writerows(points)

W,H=1500,1070
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     '<rect width="100%" height="100%" fill="#f8fafc"/>',
     '<style>text{font-family:Arial,sans-serif;fill:#172438}.small{font-size:16px}.tiny{font-size:14px}.label{font-size:15px;font-weight:bold}.grid{stroke:#dce4ed;stroke-width:1}</style>',
     '<text x="75" y="56" font-size="32" font-weight="bold">AA intelligence vs OpenRouter output-token price</text>',
     '<text x="75" y="87" font-size="18">REVIEW PREVIEW · AA Intelligence Index v5 · lower output tariff is left · higher score is up</text>',
     '<text x="75" y="116" font-size="18" font-weight="bold" fill="#a22929">Token price ≠ cost per task: token use varies by model and effort.</text>']
L,R,T,B=100,1030,175,730
def xp(rate):return L+(math.log10(rate)-math.log10(.04))/(math.log10(80)-math.log10(.04))*(R-L)
def yp(score):return B-float(score)/65*(B-T)
for y in range(0,61,10):
    Y=yp(y); svg += [f'<line class="grid" x1="{L}" x2="{R}" y1="{Y}" y2="{Y}"/>',f'<text x="{L-15}" y="{Y+6}" text-anchor="end" class="small">{y}</text>']
for n in [.05,.1,.2,.5,1,2,5,10,20,50]:
    X=xp(n);svg += [f'<line class="grid" x1="{X}" x2="{X}" y1="{T}" y2="{B}"/>',f'<text x="{X}" y="{B+27}" text-anchor="middle" class="small">{n:g}</text>']
svg += [f'<text x="{(L+R)/2}" y="{B+58}" text-anchor="middle" font-size="18">USD per 1 million output tokens · logarithmic scale</text>',f'<text x="26" y="{(T+B)/2}" text-anchor="middle" font-size="18" transform="rotate(-90 26 {(T+B)/2})">AA Intelligence Index v5 (higher is better)</text>']
groups={}
for p in points: groups.setdefault(p['model'],[]).append(p)
colors=['#2563eb','#16a34a','#dc2626','#9333ea','#d97706','#0891b2','#e11d48','#4f46e5','#0f766e','#a16207','#7c3aed','#be123c','#475569','#0284c7']
svg += ['<text x="1080" y="168" font-size="20" font-weight="bold">Model / selected route</text>']
for i,(model,rows) in enumerate(groups.items()):
    color=colors[i%len(colors)]; X=xp(float(rows[0]['output_per_m'])); ys=[yp(r['aa_index']) for r in rows]
    if len(rows)>1:svg.append(f'<line x1="{X}" x2="{X}" y1="{min(ys)}" y2="{max(ys)}" stroke="{color}" stroke-width="3"/>')
    for p,y in zip(rows,ys):
        title=escape(f"{model} · {p['effort']} · score {p['aa_index']} · output ${p['output_per_m']}/M · {p['endpoint']}")
        svg.append(f'<circle cx="{X}" cy="{y}" r="7" fill="{color}" stroke="white" stroke-width="2"><title>{title}</title></circle>')
    if len(rows)>1:
        by_score = {}
        for p,y in zip(rows,ys): by_score.setdefault(y, []).append(p['effort'])
        for y,efforts in by_score.items():
            label='/'.join({'Low':'L','Medium':'M','High':'H','XHigh':'XH','Max':'Max'}.get(e,e) for e in efforts)
            svg.append(f'<text x="{X+12}" y="{y+5}" class="tiny" fill="{color}">{escape(label)}</text>')
    # Right-hand legend keeps overlapping model labels legible.
    Y=195+i*37; route=rows[0]['endpoint']; tier=rows[0]['tier'];quant=rows[0]['quantization']
    svg += [f'<circle cx="1085" cy="{Y-5}" r="6" fill="{color}"/>',f'<text x="1100" y="{Y}" class="label">{escape(model)}</text>',f'<text x="1100" y="{Y+16}" class="tiny">{escape(route)} · {escape(tier)} · {escape(quant)}</text>']
svg += [f'<text x="75" y="835" class="small">L / M / H / XH / Max are effort levels; hover SVG points for details. AA did not measure every priced route.</text>',
        '<text x="75" y="860" class="small">Prices are the lowest quoted eligible non-promotional output rate, not the lowest total workload cost. Flex may have restrictions.</text>',
        '<text x="75" y="885" class="small">Input, cache-read, cache-write, tier overrides, quantization and exact provider are in the companion CSV. Missing rates are blank.</text>',
        '<text x="75" y="910" class="small">Benchmark data are the existing 30 October AA v5 snapshot; tariff source is the supplied OpenRouter endpoint snapshot. Verify both.</text>',
        '<text x="75" y="935" class="small">Informational only, not for budgeting. Eurobotics provides no warranty; verify prices and suitability for your own use.</text>',
        f'<text x="75" y="964" class="small">Generated: {stamp} · USD per 1M tokens · no task-cost inference</text>',
        '<a xlink:href="https://github.com/Eurobotics-Association/LLM-Analysis"><text x="75" y="995" class="small" fill="#1d4ed8">Repository: github.com/Eurobotics-Association/LLM-Analysis</text></a>',
        '<a xlink:href="https://artificialanalysis.ai/"><text x="75" y="1021" class="small" fill="#1d4ed8">Benchmark: artificialanalysis.ai</text></a>',
        '</svg>']
svg_path=out/('aa_v5_output_price_preview_'+suffix+'.svg');svg_path.write_text('\n'.join(svg),encoding='utf-8')
print(json.dumps({'svg':str(svg_path),'csv':str(csv_path),'points':len(points),'models':len(groups),'excluded':sorted(set(excluded))}, indent=2))
