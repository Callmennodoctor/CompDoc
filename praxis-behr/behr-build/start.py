from sys_ import *
c=CSS()
# shared
c.add('.bh-mark',MARKS)
c.add('.bh-markb',MARKS,{"font-weight":"700"})
c.add('.bh-h2',H2)
c.add('.bh-p',P)
c.add('.bh-btn',BTN); c.add('.bh-btn:hover',BTN_H); c.add('.bh-btn:focus',FOCUS)
c.add('.bh-tlink',TLINK); c.add('.bh-tlink:hover',TLINK_H); c.add('.bh-tlink:focus',FOCUS)
c.add('.bh-ph',PH)
c.add('.bh-lbl',LABEL); c.add('.bh-lbl-date',{"margin-top":"0px","margin-bottom":"0px","font-size":"0.875rem","font-variant-numeric":"tabular-nums","color":MUTED})
c.add('.bh-lbl-state',{"margin-top":"4px","margin-bottom":"0px","font-family":HF,"font-weight":"700","font-size":"1.25rem","line-height":"1.25"})

S=[]
# 1 HERO
c.add('.bh-hero',SEC,{"display":"grid","grid-template-columns":"minmax(0px, 1fr) minmax(0px, 1.1fr)","column-gap":"48px","row-gap":"48px","align-items":"center",**box(["56px",PADX,"96px",PADX])})
c.add('.bh-hero',{"grid-template-columns":"1fr",**box(["24px","20px","48px","20px"]),"row-gap":"0px"},media=SM)
c.add('.bh-hero-copy',{"display":"flex","flex-direction":"column","align-items":"flex-start"})
c.add('.bh-hero-name',{"margin-top":"0px","margin-bottom":"0px","font-family":HF,"font-weight":"600","font-size":"1.125rem"})
c.add('.bh-hero-role',{"margin-top":"0px","margin-bottom":"0px","font-size":"1rem","color":MUTED})
c.add('.bh-h1',{"margin-top":"40px","margin-bottom":"0px","font-family":HF,"font-weight":"700","font-size":"clamp(2.4rem, 3.3vw + 1rem, 4.4rem)","line-height":"1.05","letter-spacing":"-0.015em","text-wrap":"balance","color":INK})
c.add('.bh-h1',{"margin-top":"28px","font-size":"2.25rem","line-height":"1.08"},media=SM)
c.add('.bh-hero-fact',{"margin-top":"28px","margin-bottom":"0px","font-size":"1.25rem"})
c.add('.bh-hero-ctas',{"display":"flex","flex-wrap":"wrap","align-items":"center","column-gap":"28px","row-gap":"16px","margin-top":"40px"})
c.add('.bh-hero-ctas',{"flex-direction":"column","align-items":"stretch","row-gap":"8px","margin-top":"28px"},media=SM)
c.add('.bh-stack',{"position":"relative","height":"560px"})
c.add('.bh-stack',{"display":"none"},media=SM)
cov={"position":"absolute","left":"6%","top":"22%","width":"60%","height":"66%","border-top-left-radius":"4px","border-bottom-left-radius":"4px","border-top-right-radius":"10px","border-bottom-right-radius":"10px","mix-blend-mode":"multiply"}
c.add('.bh-cov-v',cov,{"background-color":"rgba(106,71,160,0.62)","transform":"translate(34%, -28%) rotate(3deg)"})
c.add('.bh-cov-g',cov,{"background-color":"rgba(78,154,104,0.66)","transform":"translate(16%, -12%) rotate(1deg)"})
c.add('.bh-cov-b',cov,{"background-color":"rgba(47,91,168,0.72)","transform":"translate(-2%, 8%) rotate(-4deg)"})
ov={"position":"absolute","left":"6%","top":"22%","width":"60%","height":"66%"}
c.add('.bh-ov-v',ov,{"transform":"translate(34%, -28%) rotate(3deg)"})
c.add('.bh-ov-g',ov,{"transform":"translate(16%, -12%) rotate(1deg)"})
c.add('.bh-ov-b',ov,{"transform":"translate(-2%, 8%) rotate(-4deg)"})
tag={"position":"absolute","display":"flex","align-items":"baseline","column-gap":"8px","min-height":"44px",**box(["10px","16px","10px","16px"]),"background-color":"#FFFFFF",**brd(f"1.5px solid {INK}"),**rad("4px"),"color":INK,"text-decoration":"none","mix-blend-mode":"normal"}
c.add('.bh-tag-v',tag,{"top":"14px","right":"20px"}); c.add('.bh-tag-g',tag,{"top":"14px","left":"20px"}); c.add('.bh-tag-b',tag,{"top":"18px","left":"22px"})
for t in ['v','g','b']: c.add(f'.bh-tag-{t}:hover',{"background-color":"#F2F5FA"}); c.add(f'.bh-tag-{t}:focus',FOCUS)
c.add('.bh-tag-t',{"font-family":HF,"font-weight":"700","font-size":"1.125rem"})
c.add('.bh-tag-sv',{"font-size":"0.875rem","color":"#5A3F8C"}); c.add('.bh-tag-sg',{"font-size":"0.875rem","color":"#2E6344"}); c.add('.bh-tag-sb',{"font-size":"0.875rem","color":"#2C4F8F"})
c.add('.bh-stack-lbl',LABEL,{"position":"absolute","left":"22px","right":"22px","bottom":"26px","max-width":"330px","transform":"rotate(1.5deg)","box-shadow":"0 1px 0 rgba(27,37,64,0.12)"})
# mobile only
c.add('.bh-hero-m',{"display":"none"}); c.add('.bh-hero-m',{"display":"block"},media=SM)
c.add('.bh-m-lbl',LABEL,{"margin-top":"20px"})
c.add('.bh-strip',{"display":"flex","column-gap":"12px","overflow-x":"auto","scroll-snap-type":"x mandatory","margin-top":"32px","margin-right":"-20px","margin-left":"-20px",**box(["4px","20px","12px","20px"])})
strip={"flex":"0 0 72%","scroll-snap-align":"start","height":"170px",**box(["16px"]*4),"border-top-left-radius":"4px","border-bottom-left-radius":"4px","border-top-right-radius":"10px","border-bottom-right-radius":"10px","text-decoration":"none","display":"flex","align-items":"flex-start"}
c.add('.bh-strip-b',strip,{"background-color":BLUE}); c.add('.bh-strip-g',strip,{"background-color":GREEN}); c.add('.bh-strip-v',strip,{"background-color":VIOLET})
c.add('.bh-strip-tag',{"display":"inline-flex","flex-direction":"column","min-height":"44px",**box(["8px","14px","8px","14px"]),"background-color":"#FFFFFF",**brd(f"1.5px solid {INK}"),**rad("4px"),"color":INK})
c.add('.bh-strip-sub',{"font-size":"0.8125rem","color":MUTED})

def status(cls='bh-lbl'):
    return f'<div class="{cls}"><p class="bh-lbl-date">Stand 29.09.2026</p><p class="bh-lbl-state"><span class="bh-mark">Erstgespräche möglich</span></p></div>'

S.append(('hero', f'''<section class="bh-hero" aria-label="Einstieg"><div class="bh-hero-copy"><p class="bh-hero-name">Antonia Behr</p><p class="bh-hero-role">Kinder- und Jugendlichenpsychotherapeutin</p><h1 class="bh-h1">Psychotherapie für Kinder, Jugendliche und junge Erwachsene. Und für die Familie drumherum.</h1><p class="bh-hero-fact"><span class="bh-mark">Berlin-Mitte, bis 21 Jahre</span></p><div class="bh-hero-ctas"><a href="/kontakt" class="bh-btn">Telefonzeiten ansehen</a><a href="/ablauf-und-kosten" class="bh-tlink">So läuft eine Therapie ab</a></div></div><div class="bh-stack"><div class="bh-cov-v"></div><div class="bh-cov-g"></div><div class="bh-cov-b"></div><div class="bh-ov-v"><a href="/fuer-dich" class="bh-tag-v"><span class="bh-tag-t">Für dich</span><span class="bh-tag-sv">ab 14</span></a></div><div class="bh-ov-g"><a href="/ablauf-und-kosten" class="bh-tag-g"><span class="bh-tag-t">Für Kinder</span><span class="bh-tag-sg">zum Vorlesen</span></a></div><div class="bh-ov-b"><a href="/ablauf-und-kosten" class="bh-tag-b"><span class="bh-tag-t">Für Eltern</span><span class="bh-tag-sb">Ablauf, Kosten, Elterngespräche</span></a>{status('bh-stack-lbl')}</div></div><div class="bh-hero-m">{status('bh-m-lbl')}<div class="bh-strip"><a href="/ablauf-und-kosten" class="bh-strip-b"><span class="bh-strip-tag"><span class="bh-tag-t">Für Eltern</span><span class="bh-strip-sub">Ablauf, Kosten, Elterngespräche</span></span></a><a href="/ablauf-und-kosten" class="bh-strip-g"><span class="bh-strip-tag"><span class="bh-tag-t">Für Kinder</span><span class="bh-strip-sub">zum Vorlesen</span></span></a><a href="/fuer-dich" class="bh-strip-v"><span class="bh-strip-tag"><span class="bh-tag-t">Für dich</span><span class="bh-strip-sub">ab 14</span></span></a></div></div></section>'''))

# 2 ANLIEGEN
c.add('.bh-anl',SEC,GRIDBG,{**box(["clamp(56px, 8vw, 112px)",PADX,"clamp(56px, 8vw, 112px)",PADX])})
c.add('.bh-anl-list',{"list-style-type":"none","margin-top":"0px","margin-bottom":"0px",**box(["0px"]*4),"display":"grid","grid-template-columns":"repeat(auto-fit, minmax(min(100%, 300px), 1fr))","column-gap":"48px","max-width":"980px"})
c.add('.bh-anl-li',{**box(["14px","0px","14px","0px"]),"border-top":f"1.5px solid {INK}","margin-bottom":"0px"})
c.add('.bh-anl-close',{"margin-top":"28px","margin-bottom":"0px","max-width":"62ch"})
items=["Ihr Kind hat oft Angst und meidet vieles, was früher ging.","Zu Hause gibt es viel Streit, und alle sind erschöpft.","Ihr Kind zieht sich zurück oder wirkt seit Wochen traurig.","Nach einer Trennung, einem Umzug oder einem Verlust.","Essen, Schlaf oder der eigene Körper sind zum Dauerthema geworden.","Sie sind als Eltern unsicher, was Ihr Kind gerade braucht."]
S.append(('anliegen', '<section class="bh-anl" aria-labelledby="h-anliegen"><h2 id="h-anliegen" class="bh-h2">Wobei ich begleite</h2><ul class="bh-anl-list">'+''.join(f'<li class="bh-anl-li">{t}</li>' for t in items)+'</ul><p class="bh-anl-close">Ob eine Therapie der passende Weg ist, klären wir gemeinsam im Erstgespräch.</p></section>'))

# 3 ABLAUF + Stundenplan
c.add('.bh-abl',SEC,{"display":"grid","grid-template-columns":"repeat(auto-fit, minmax(min(100%, 340px), 1fr))","column-gap":"64px","row-gap":"40px"})
c.add('.bh-plan',{"font-variant-numeric":"tabular-nums"})
row={"display":"grid","grid-template-columns":"minmax(92px, 0.7fr) minmax(0px, 1fr) minmax(0px, 1fr)","column-gap":"8px","align-items":"center","min-height":"52px","border-bottom":f"1px solid {LINE}"}
c.add('.bh-plan-head',row,{"min-height":"0px","padding-bottom":"10px","border-bottom":f"1.5px solid {INK}","font-family":HF,"font-weight":"600","font-size":"1rem"})
c.add('.bh-plan-row',row); c.add('.bh-plan-rowend',row,{"border-bottom":f"1.5px solid {INK}"})
c.add('.bh-plan-rh',{"font-family":HF,"font-weight":"600","font-size":"0.9375rem"})
c.add('.bh-chip-b',CHIP,{"background-color":BLUE,"color":PAPER}); c.add('.bh-chip-g',CHIP,{"background-color":GREEN,"color":INK})
c.add('.bh-chip-w',CHIP,{"background-color":"#FFFFFF","border":f"1.5px solid {INK}","grid-column-start":"2","grid-column-end":"4"})
c.add('.bh-plan-note',{"margin-top":"12px","margin-bottom":"0px","font-size":"1rem","color":MUTED})
def prow(h,a,b,cls='bh-plan-row'):
    return f'<div class="{cls}" role="row"><span class="bh-plan-rh" role="rowheader">{h}</span>{a}{b}</div>'
E0='<span role="cell"></span>'
def G(t): return f'<span class="bh-chip-g" role="cell">{t}</span>'
def B(t): return f'<span class="bh-chip-b" role="cell">{t}</span>'
def plan(weeks=4, note=True):
    h='<div class="bh-plan" role="table" aria-label="Stundenplan der Therapie"><div class="bh-plan-head" role="row"><span role="columnheader"></span><span role="columnheader">Ihr Kind</span><span role="columnheader">Sie als Eltern</span></div>'
    h+=prow('Anrufen',E0,B('Telefonat'))
    h+=f'<div class="bh-plan-row" role="row"><span class="bh-plan-rh" role="rowheader">Erstgespräch</span><span class="bh-chip-w" role="cell">Gemeinsam, 50 Minuten</span></div>'
    h+=prow('Kennenlernen',G('Einige Sitzungen'),B('Rückmeldung'),'bh-plan-rowend')
    for w in range(1,weeks+1): h+=prow(f'Woche {w}',G('Sitzung, 50 Min.'),B('Elterngespräch') if w%4==0 else E0)
    if note: h+='<p class="bh-plan-note">und so weiter, im gleichen Rhythmus</p>'
    return h+'</div>'
S.append(('ablauf', f'<section class="bh-abl" aria-labelledby="h-ablauf"><div><h2 id="h-ablauf" class="bh-h2">So läuft eine Therapie ab</h2><p class="bh-p">Nach einem Anruf und dem Erstgespräch lernen wir uns in einigen Sitzungen kennen. Danach sieht Ihr Kind mich <span class="bh-mark">einmal pro Woche für 50 Minuten</span>.</p><p class="bh-p">Sie als Eltern sind <span class="bh-mark">alle vier Sitzungen</span> zu einem eigenen Gespräch da.</p><a href="/ablauf-und-kosten" class="bh-tlink">Ablauf und Kosten im Einzelnen</a></div>{plan()}</section>'))

# 4 KOSTEN
c.add('.bh-kost',SEC)
c.add('.bh-cost',{"max-width":"1040px","border-top":f"1.5px solid {INK}"})
c.add('.bh-cost-row',{"display":"grid","grid-template-columns":"repeat(auto-fit, minmax(min(100%, 240px), 1fr))","column-gap":"32px","row-gap":"4px",**box(["18px","0px","18px","0px"]),"border-bottom":f"1px solid {LINE}"})
c.add('.bh-cost-h',{"font-family":HF,"font-weight":"600","font-size":"1.1875rem"})
c.add('.bh-cost-v',{"font-variant-numeric":"tabular-nums"})
c.add('.bh-cost-link',{"display":"inline-flex","align-items":"center","min-height":"44px","font-family":HF,"font-weight":"500","color":BLUE,"text-decoration-line":"underline","text-underline-offset":"0.22em"})
def costs(link=True):
    r=lambda h,d,v: f'<div class="bh-cost-row" role="row"><span class="bh-cost-h" role="rowheader">{h}</span><span role="cell">{d}</span><span class="bh-cost-v" role="cell">{v}</span></div>'
    price='<span class="bh-markb">100,55 €</span> je Sitzung, 50 Minuten'
    last='<a href="/ablauf-und-kosten#kostenerstattung" class="bh-cost-link">Die Schritte zum Antrag</a>' if link else 'Rechnung wie oben, Erstattung durch die Kasse'
    return '<div class="bh-cost" role="table" aria-label="Kosten">'+r('Private Krankenversicherung und Beihilfe','Sie erhalten eine Rechnung und reichen sie bei Versicherung und Beihilfestelle ein.',price)+r('Selbstzahler nach GOP','Abrechnung nach der Gebührenordnung für Psychotherapeuten, 2,3-facher Satz.',price)+r('Kostenerstattung nach § 13 Abs. 3 SGB V','Für gesetzlich Versicherte, nur mit Genehmigung Ihrer Krankenkasse vor Beginn.',last)+'</div>'
S.append(('kosten', f'<section class="bh-kost" aria-labelledby="h-kosten"><h2 id="h-kosten" class="bh-h2">Was eine Sitzung kostet</h2>{costs()}</section>'))

# 5 UEBER
c.add('.bh-ueber',SEC,{"display":"grid","grid-template-columns":"repeat(auto-fit, minmax(min(100%, 320px), 1fr))","column-gap":"72px","row-gap":"40px","align-items":"end"})
c.add('.bh-portrait',PH,{"aspect-ratio":"4 / 5","max-width":"520px","width":"100%"})
c.add('.bh-ueber-txt',{"max-width":"58ch","padding-bottom":"8px"})
c.add('.bh-hand',PH,{"height":"120px","max-width":"440px","margin-top":"12px","margin-bottom":"20px"})
S.append(('ueber', '<section class="bh-ueber" aria-labelledby="h-ueber"><div class="bh-portrait" role="img" aria-label="Platzhalter Porträt">Platzhalter: Porträt, Frau Behr sitzend auf Augenhöhe im Praxisraum, Tageslicht</div><div class="bh-ueber-txt"><h2 id="h-ueber" class="bh-h2">Antonia Behr</h2><p class="bh-p">Ich bin Kinder- und Jugendlichenpsychotherapeutin mit Approbation im Verfahren Verhaltenstherapie. [Werdegang in einem Satz.]</p><p class="bh-p">Ich arbeite mit Kindern, Jugendlichen und jungen Erwachsenen bis 21 und beziehe die Familie ein, so viel wie hilfreich ist.</p><div class="bh-hand">Platzhalter: Scan, ein Satz in Frau Behrs Handschrift</div><a href="/ueber-mich" class="bh-tlink">Werdegang und Haltung</a></div></section>'))

# 6 FAQ (details/summary, no JS)
c.add('.bh-faq',SEC)
c.add('.bh-faq-list',{"max-width":"880px","border-top":f"1.5px solid {INK}"})
c.add('.bh-faq-item',{"border-bottom":f"1px solid {LINE}"})
c.add('.bh-faq-q',{"display":"flex","align-items":"center","justify-content":"space-between","column-gap":"16px","min-height":"60px",**box(["12px","0px","12px","0px"]),"font-family":HF,"font-weight":"600","font-size":"1.1875rem","color":INK,"cursor":"pointer","list-style-type":"none"})
c.add('.bh-faq-q:focus',FOCUS)
c.add('.bh-faq-a',{"margin-top":"0px","margin-bottom":"0px","padding-bottom":"20px","max-width":"64ch"})
faqs=[("Wie lange dauert eine Therapie?","Das hängt vom Anliegen ab. Nach der Kennenlernphase schlage ich Ihnen einen Umfang vor, und wir prüfen regelmäßig gemeinsam, wie es weitergeht."),("Muss mein Kind schon wissen, dass wir anrufen?","Nein. Das erste Telefonat führen meist die Eltern. Wie Sie Ihrem Kind vom Erstgespräch erzählen können, besprechen wir dabei."),("Übernimmt meine Krankenkasse die Kosten?","Private Versicherungen und Beihilfe erstatten je nach Tarif. Gesetzliche Kassen übernehmen die Kosten nur über eine Kostenerstattung, die vor Beginn genehmigt sein muss."),("Sind die Eltern bei jeder Sitzung dabei?","Nein. Ihr Kind hat seine Sitzungen allein mit mir. Alle vier Sitzungen gibt es ein Gespräch mit Ihnen."),("Was passiert mit dem, was mein Kind erzählt?","Ich habe Schweigepflicht, auch gegenüber den Eltern. Was ich im Elterngespräch weitergebe, spreche ich vorher mit Ihrem Kind ab. Ausnahme ist eine ernste Gefahr für Ihr Kind oder andere.")]
S.append(('faq', '<section class="bh-faq" aria-labelledby="h-faq"><h2 id="h-faq" class="bh-h2">Häufige Fragen</h2><div class="bh-faq-list">'+''.join(f'<div class="bh-faq-item"><details{" open" if i==0 else ""}><summary class="bh-faq-q">{q}<span aria-hidden="true">+</span></summary><p class="bh-faq-a">{a}</p></details></div>' for i,(q,a) in enumerate(faqs))+'</div></section>'))

# 7 TELEFON
c.add('.bh-tel',SEC,{"display":"grid","grid-template-columns":"repeat(auto-fit, minmax(min(100%, 340px), 1fr))","column-gap":"72px","row-gap":"32px","align-items":"end",**box(["clamp(72px, 9vw, 128px)",PADX,"clamp(72px, 9vw, 128px)",PADX])})
c.add('.bh-tel-big',{"margin-top":"0px","margin-bottom":"0px","font-family":HF,"font-weight":"700","font-size":"clamp(1.9rem, 3vw + 1rem, 3.4rem)","line-height":"1.15","font-variant-numeric":"tabular-nums"})
c.add('.bh-tel-note',{"margin-top":"20px","margin-bottom":"0px","max-width":"52ch"})
c.add('.bh-tel-act',{"display":"flex","flex-direction":"column","align-items":"flex-start","row-gap":"12px"})
c.add('.bh-btn-l',BTN,{"min-height":"56px","font-size":"1.25rem"}); c.add('.bh-btn-l:hover',BTN_H); c.add('.bh-btn-l:focus',FOCUS)
S.append(('telefon', '<section class="bh-tel" aria-labelledby="h-kontakt"><div><h2 id="h-kontakt" class="bh-h2">Telefonzeiten</h2><p class="bh-tel-big"><span class="bh-mark">Montag bis Donnerstag, 08:45 bis 10:00 Uhr</span></p><p class="bh-tel-note">In dieser Zeit gehe ich selbst ans Telefon. Sonst hören Sie den Anrufbeantworter.</p></div><div class="bh-tel-act"><a href="tel:+4930" class="bh-btn-l">030 [Nummer] anrufen</a><a href="/kontakt#rueckruf" class="bh-tlink">Rückruf anfragen</a></div></section>'))
