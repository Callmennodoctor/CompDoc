# Style system: one class per element (Webflow treats extra classes as combos)
INK="#1B2540"; PAPER="#FAFBFD"; LINE="#CBD8E8"; BLUE="#2F5BA8"; GREEN="#4E9A68"; VIOLET="#6A47A0"; MARK="#F2EA4A"; MUTED="#48536B"
HF="Gabarito, system-ui, sans-serif"; BF="'Atkinson Hyperlegible Next', system-ui, sans-serif"
PADX="clamp(20px, 5vw, 80px)"
SM="screen and (max-width: 767px)"; TAB="screen and (max-width: 991px)"
def box(p): return {f"padding-{k}":v for k,v in zip(["top","right","bottom","left"],p)}
def rad(r): return {f"border-{a}-radius":r for a in ["top-left","top-right","bottom-left","bottom-right"]}
def brd(b): return {f"border-{s}":b for s in ["top","right","bottom","left"]}
SEC={"font-family":BF,"font-size":"1.125rem","line-height":"1.55","color":INK,"background-color":PAPER,**box(["clamp(72px, 9vw, 128px)",PADX,"0px",PADX])}
GRIDBG={"background-image":"linear-gradient(rgba(203,216,232,0.55) 1px, transparent 1px), linear-gradient(90deg, rgba(203,216,232,0.55) 1px, transparent 1px)","background-size":"5mm 5mm"}
MARKS={"background-image":f"linear-gradient(transparent 12%, {MARK} 12%, {MARK} 88%, transparent 88%)","padding-right":"0.18em","padding-left":"0.18em","-webkit-box-decoration-break":"clone","box-decoration-break":"clone","color":INK}
H2={"margin-top":"0px","margin-bottom":"24px","font-family":HF,"font-weight":"700","font-size":"clamp(1.9rem, 2vw + 1.2rem, 2.75rem)","line-height":"1.1","text-wrap":"balance","color":INK}
H3={"margin-top":"0px","margin-bottom":"8px","font-family":HF,"font-weight":"600","font-size":"1.3125rem","line-height":"1.25","color":INK}
P={"margin-top":"0px","margin-bottom":"16px","max-width":"62ch"}
BTN={"display":"inline-flex","align-items":"center","justify-content":"center","min-height":"52px",**box(["0px","24px","0px","24px"]),"background-color":BLUE,"color":PAPER,**rad("6px"),"font-family":HF,"font-weight":"600","font-size":"1.0625rem","text-decoration":"none","font-variant-numeric":"tabular-nums"}
BTN_H={"background-color":INK,"color":PAPER}
TLINK={"display":"inline-flex","align-items":"center","min-height":"44px","font-family":HF,"font-weight":"500","font-size":"1.0625rem","color":INK,"text-decoration-line":"underline","text-decoration-color":BLUE,"text-decoration-thickness":"2px","text-underline-offset":"0.25em"}
TLINK_H={"color":BLUE}
FOCUS={"outline-color":BLUE,"outline-width":"2px","outline-style":"solid","outline-offset":"2px"}
LABEL={"display":"block",**box(["14px","18px","14px","18px"]),"background-color":"#FFFFFF",**brd(f"1.5px solid {INK}"),**rad("4px")}
PH={"display":"flex","align-items":"center","justify-content":"center",**box(["24px"]*4),"background-color":"#EEF1F5",**brd("1px solid #9AA3B5"),**rad("4px"),"color":MUTED,"font-size":"0.9375rem","text-align":"center"}
CHIP={"display":"block",**box(["6px","10px","6px","10px"]),**rad("3px"),"font-size":"0.9375rem"}

class CSS:
    def __init__(s): s.rules={}; s.order=[]
    def add(s, sel, *dicts, media=None, **kw):
        d={}
        for x in dicts: d.update(x)
        d.update({k.replace('_','-'):v for k,v in kw.items()})
        key=(sel,media)
        if key not in s.rules: s.order.append(key); s.rules[key]={}
        s.rules[key].update(d)
        return s
    def only(s, classes):
        # css text for rules whose class is in `classes`
        out=[];meds={}
        for sel,med in s.order:
            cls=sel.split(':')[0].lstrip('.')
            if cls not in classes: continue
            body=';'.join(f'{k}:{v}' for k,v in s.rules[(sel,med)].items())
            if med: meds.setdefault(med,[]).append(f'{sel}{{{body}}}')
            else: out.append(f'{sel}{{{body}}}')
        for med,rs in meds.items(): out.append(f'@media {med}{{{" ".join(rs)}}}')
        return ' '.join(out)
    def all(s):
        return s.only({sel.split(':')[0].lstrip('.') for sel,_ in s.order})
