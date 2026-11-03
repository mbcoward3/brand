from pathlib import Path
import json

root = Path(__file__).parent
S = 'fill="none" stroke="currentColor" stroke-linecap="square" stroke-linejoin="miter"'
def line(d,w=12,extra=''):
    return f'<path d="{d}" {S} stroke-width="{w}" {extra}/>'

concepts = [
('01','Orbit','An open C embraces the M. A cleaner evolution of your existing mark.',
 line('M185 47 A76 76 0 1 0 185 153',11)+line('M76 137 V63 L120 115 L164 63 V137',11)),
('02','Shared stem','Two clear initials share a vertical. Precise, compact and versatile.',
 line('M38 151 V49 L84 111 L130 49 V151',13)+line('M201 59 Q181 43 160 52 Q130 64 130 100 Q130 137 160 148 Q181 157 201 141',13)),
('03','Counterform','A solid M and a C cut into its right-hand side. Bold at small sizes.',
 '<path fill="currentColor" d="M33 153 V47 H59 L104 105 L149 47 H207 V72 H184 Q155 72 155 100 Q155 128 184 128 H207 V153 H180 Q129 153 129 103 V91 L104 125 L59 68 V153 Z"/>'),
('04','One line','An angular M flows directly into an open C. Light and personal.',
 '<path d="M38 148 V54 L83 117 L128 54 V100 C128 38 187 38 205 68 M128 100 C128 162 187 162 205 132" fill="none" stroke="currentColor" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'),
('05','Editorial','A custom serif monogram with a generous open C. Quiet and established.',
 '<path fill="currentColor" d="M29 151 V146 H40 V54 H29 V49 H58 L94 126 L128 49 H151 V54 H141 V146 H152 V151 H118 V146 H129 V62 L91 151 H87 L48 65 V146 H61 V151 Z"/>'
 +'<path d="M207 60 Q194 47 178 49 C132 49 130 151 178 151 Q198 151 210 133 M207 50 V77" fill="none" stroke="currentColor" stroke-width="8"/>'),
('06','Open frame','An architectural C becomes the frame around a compact M.',
 line('M196 53 V35 H44 V165 H196 V147',9)+line('M76 132 V68 L120 112 L164 68 V132',10)),
('07','Soft arches','A lowercase mc drawn from rounded arches. Friendly and contemporary.',
 '<path d="M32 147 V78 Q32 59 53 59 Q76 59 76 85 V147 M76 85 Q76 59 98 59 Q121 59 121 85 V147 M205 74 Q193 59 176 59 Q144 59 144 103 Q144 147 176 147 Q193 147 205 133" fill="none" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>'),
('08','Interlace','A circular C threads through an M. Distinctive without extra symbols.',
 line('M185 53 A66 66 0 1 0 185 147',12)
 +'<path d="M65 151 V49 L120 115 L175 49 V151" fill="none" stroke="var(--paper, #f7f5f0)" stroke-width="24"/>'
 +line('M65 151 V49 L120 115 L175 49 V151',10)),
('09','Low profile','A wide lowercase ligature. Calm, practical and easy to pair with a name.',
 '<path d="M28 137 V70 M28 92 Q28 70 49 70 Q71 70 71 92 V137 M71 92 Q71 70 92 70 Q114 70 114 92 V137 M204 80 Q191 69 176 70 Q141 70 141 104 Q141 138 176 138 Q191 139 204 128" fill="none" stroke="currentColor" stroke-width="10"/>'),
('10','Chamfer','An angular C and peaked M. Technical, sharp and strong in one color.',
 line('M200 54 L177 37 H64 L37 64 V136 L64 163 H177 L200 146',11)
 +line('M72 133 V67 L120 111 L168 67 V133',11)),
('11','Seal','A small M nested in a circular C. A restrained personal stamp.',
 line('M192 60 A82 82 0 1 0 192 140',9)
 +line('M78 130 V70 L120 111 L162 70 V130',9)
 +'<circle cx="196" cy="100" r="5" fill="currentColor"/>'),
('12','Forward','An inclined MC with clipped terminals. Crisp and energetic.',
 '<g transform="translate(20 0) skewX(-11)">'
 +line('M41 150 V50 L85 111 L129 50 V150',12)
 +line('M207 60 Q195 50 180 50 Q148 50 148 100 Q148 150 180 150 Q195 150 207 140',12)
 +'</g>'),
]

def svg(c):
    n,name,desc,paths=c
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 200" role="img" aria-labelledby="title"><title id="title">{n} {name} — MC monogram</title>{paths}</svg>'

for c in concepts:
    (root/f'{c[0]}-{c[1].lower().replace(" ","-")}.svg').write_text(svg(c),encoding='utf-8')

cards=''
for c in concepts:
    n,name,desc,_=c
    fn=f'{n}-{name.lower().replace(" ","-")}.svg'
    cards+=f'<article><header><span>{n}</span><h2>{name}</h2></header><div class="mark">{svg(c)}</div><p>{desc}</p><footer><div class="tiny">{svg(c)}{svg(c)}</div><a href="{fn}" download>SVG ↓</a></footer></article>'

html='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>MC / Brand explorations</title><style>
*{box-sizing:border-box}body{--paper:#f7f5f0;--ink:#202a29;--line:#dcded7;margin:0;background:var(--paper);color:var(--ink);font-family:Arial,sans-serif}body.dark{--paper:#152321;--ink:#edece2;--line:#3a4944}main{max-width:1440px;margin:auto;padding:54px 56px 36px}.eyebrow{font-size:11px;letter-spacing:3px;text-transform:uppercase}h1{font-family:Georgia,serif;font-weight:normal;font-size:54px;margin:16px 0 12px;letter-spacing:-2px}.intro{color:var(--ink);opacity:.7;font-size:15px;line-height:1.6;max-width:670px}.toolbar{display:flex;gap:10px;margin:25px 0 30px}button{background:none;color:inherit;border:1px solid var(--line);border-radius:20px;padding:8px 16px;cursor:pointer}.grid{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line);border-left:1px solid var(--line)}article{padding:22px 26px 14px;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}header{display:flex;align-items:center;gap:12px}header span{font-size:10px;opacity:.5;letter-spacing:1px}h2{font-weight:400;font-size:15px;margin:0}.mark{height:188px;display:flex;align-items:center;justify-content:center}.mark svg{width:210px;height:175px;color:inherit}article p{font-size:12px;line-height:1.5;height:36px;opacity:.7;max-width:290px}footer{display:flex;align-items:center;justify-content:space-between;margin-top:14px}.tiny{display:flex;align-items:center;gap:12px}.tiny svg:first-child{width:24px;height:20px}.tiny svg:last-child{width:38px;height:32px}a{color:inherit;font-size:10px;text-decoration:none;opacity:.65}.note{font-size:11px;opacity:.6;margin-top:22px;letter-spacing:.25px}@media(max-width:800px){main{padding:28px 20px}.grid{grid-template-columns:repeat(2,1fr)}article{padding:18px}h1{font-size:40px}}@media(max-width:500px){.grid{grid-template-columns:1fr}}@media print{.toolbar{display:none}article{break-inside:avoid}}
</style><main><div class="eyebrow">Matthew Coward · matthewcoward.com</div><h1>A mark of your own.</h1><p class="intro">Twelve MC directions, from quiet and classical to compact and geometric.<br>One color first. Each concept includes a scalable SVG and small-size previews.</p><div class="toolbar"><button onclick="document.body.classList.toggle('dark')">Light / dark</button><button onclick="document.body.style.setProperty('--ink','#245b50')">Forest</button><button onclick="document.body.style.setProperty('--ink','#244d75')">Ink blue</button><button onclick="document.body.style.removeProperty('--ink')">Reset color</button></div><section class="grid">'''+cards+'''</section><p class="note">MC / CONCEPT STUDIES · NOVEMBER 2026 · Existing production logo retained. Concepts are original vector artwork.</p></main></html>'''
(root/'index.html').write_text(html,encoding='utf-8')

board='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 1690"><rect width="1440" height="1690" fill="#f7f5f0"/><g fill="#202a29" font-family="Arial, sans-serif"><text x="56" y="58" font-size="12" letter-spacing="3">MATTHEW COWARD / BRAND EXPLORATIONS</text><text x="56" y="128" font-size="56" font-family="Georgia, serif">A mark of your own.</text><text x="56" y="165" font-size="16">Twelve MC concepts for matthewcoward.com</text></g>'
for i,c in enumerate(concepts):
    n,name,desc,paths=c;x=56+(i%3)*442;y=210+(i//3)*354
    board+=f'<g transform="translate({x} {y})" style="color:#202a29;--paper:#f7f5f0"><rect width="442" height="354" fill="none" stroke="#dcded7"/><text x="24" y="34" fill="#777d75" font-size="11" font-family="Arial">{n}</text><text x="55" y="34" fill="#202a29" font-size="16" font-family="Arial">{name}</text><g transform="translate(101 62)">{paths}</g><g transform="translate(24 300) scale(.12)">{paths}</g><g transform="translate(65 293) scale(.19)">{paths}</g><text x="418" y="320" text-anchor="end" fill="#777d75" font-size="10" font-family="Arial">MC / {n}</text></g>'
board+='<text x="56" y="1660" fill="#777d75" font-size="12" font-family="Arial">ORIGINAL VECTOR CONCEPTS · Existing live logo retained · Choose by number</text></svg>'
(root/'comparison.svg').write_text(board,encoding='utf-8')
(root/'board.html').write_text('<html><body style="margin:0">'+board+'</body></html>',encoding='utf-8')
(root/'README.md').write_text('# MC logo concepts\n\nTwelve original SVG directions for matthewcoward.com. These are concepts for selection; existing production assets are unchanged.\n\n[Open the interactive gallery](index.html) · [Comparison sheet](comparison.svg)\n\n'+ '\n'.join(f'- **{n} {name}:** {desc}' for n,name,desc,_ in concepts)+'\n\nAll monogram geometry is drawn as editable SVG paths, with no font dependency. Color uses `currentColor`. Concept 08 uses `--paper` (default warm white) for its interlacing knockout; match this variable to the background. Gallery captions use system fonts. No image generation was used: the existing repo contains an SVG identity, so these explorations extend that vector system directly.\n',encoding='utf-8')
print(json.dumps([p.name for p in root.iterdir()]))
