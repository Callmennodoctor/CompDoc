import importlib,sys
mod=importlib.import_module(sys.argv[1])
F='../behr-src/fonts/'
html=f"""<!doctype html><html lang=de><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><style>
@font-face{{font-family:Gabarito;src:url({F}Gabarito-400_900-normal-34236.woff2) format('woff2');font-weight:400 900}}
@font-face{{font-family:'Atkinson Hyperlegible Next';src:url({F}AtkinsonHyperlegibleNext-200_800-normal-33996.woff2) format('woff2');font-weight:200 800}}
body{{margin:0;background:#FAFBFD;color:#1B2540;font-family:'Atkinson Hyperlegible Next'}} *{{box-sizing:border-box}} h1,h2,h3,p{{margin:0}}
{mod.c.all()}
</style></head><body>{''.join(h for _,h in mod.S)}</body></html>"""
open(sys.argv[1]+'_preview.html','w').write(html)
