from sys_ import *
import ds
c=ds.c
c.add('.bh-faqp',SEC,{**box(["clamp(56px, 7vw, 96px)",PADX,"clamp(72px, 9vw, 128px)",PADX])})
c.add('.bh-toc',{"display":"flex","flex-wrap":"wrap","column-gap":"8px","row-gap":"8px","margin-top":"32px","max-width":"880px"})
c.add('.bh-toc-link',{"display":"inline-flex","align-items":"center","min-height":"44px",**box(["0px","14px","0px","14px"]),"background-color":"#FFFFFF",**brd(f"1.5px solid {INK}"),**rad("4px"),"font-family":HF,"font-weight":"600","font-size":"0.9375rem","color":INK,"text-decoration":"none"})
c.add('.bh-toc-link:hover',{"background-color":MARK})
c.add('.bh-toc-link:focus',FOCUS)
c.add('.bh-faq-group',{"margin-top":"64px","max-width":"880px"})
c.add('.bh-faq-gh',{"margin-top":"0px","margin-bottom":"16px","font-family":HF,"font-weight":"700","font-size":"clamp(1.6rem, 1.5vw + 1rem, 2.1rem)","line-height":"1.15","color":INK})
c.add('.bh-faq-gh-v',{"margin-top":"0px","margin-bottom":"16px","font-family":HF,"font-weight":"700","font-size":"clamp(1.6rem, 1.5vw + 1rem, 2.1rem)","line-height":"1.15","color":VIOLET})
c.add('.bh-faq-more',{"margin-top":"56px","margin-bottom":"0px","max-width":"62ch"})

G=[
("erstkontakt","Erster Kontakt und Wartezeit",[
("Wie bekomme ich einen ersten Termin?",'Am einfachsten rufen Sie zu den Telefonzeiten an, <span class="bh-mark">Montag bis Donnerstag, 08:45 bis 10:00 Uhr</span>. In dieser Zeit gehe ich selbst ans Telefon. Wenn Sie die Zeiten nicht schaffen, können Sie auf der Kontaktseite um einen Rückruf bitten.'),
("Wie lange muss ich auf einen Platz warten?","Das ändert sich laufend. Den aktuellen Stand finden Sie auf dem Etikett auf der Startseite und auf der Kontaktseite, jeweils mit Datum. Am Telefon sage ich Ihnen offen, ob und wann ein Erstgespräch möglich ist."),
("Brauche ich eine Überweisung?","Für das Erstgespräch nicht. Bevor die eigentliche Therapie beginnt, ist ein kurzer ärztlicher Bericht nötig, der sogenannte Konsiliarbericht. Er stellt sicher, dass körperliche Ursachen abgeklärt sind. Den stellt zum Beispiel die Kinderärztin oder der Hausarzt aus."),
("Muss mein Kind schon wissen, dass wir anrufen?","Nein. Das erste Telefonat führen meist die Eltern. Wie Sie Ihrem Kind vom Erstgespräch erzählen können, besprechen wir dabei."),
("Kann ich mich auch melden, wenn ich unsicher bin, ob Therapie nötig ist?","Ja, gerade dann. Im Erstgespräch schauen wir gemeinsam, ob eine Therapie der passende Weg ist oder ob etwas anderes besser hilft. Wenn eine andere Stelle besser passt, sage ich Ihnen das."),
]),
("ablauf","Ablauf und Therapie",[
("Wie läuft das Erstgespräch ab?","Sie kommen gemeinsam mit Ihrem Kind. Wir sprechen darüber, was Sie gerade beschäftigt und was Sie sich wünschen. Bei Jugendlichen spreche ich auch einen Teil der Zeit allein mit ihnen."),
("Was passiert in der Kennenlernphase?","In einigen Sitzungen klären wir, ob die Therapie passt, woran wir arbeiten wollen und wie lange es voraussichtlich dauert. Danach bekommen Sie eine Rückmeldung von mir und entscheiden, ob Sie weitermachen möchten."),
("Wie oft und wie lange sind die Sitzungen?",'In der Regel <span class="bh-mark">einmal pro Woche für 50 Minuten</span>, in meinem Praxisraum in Berlin-Mitte.'),
("Wie arbeiten Sie?","Ich arbeite verhaltenstherapeutisch. Das heißt, wir schauen gemeinsam, was im Alltag schwierig ist, und probieren Schritt für Schritt aus, was hilft. Mit jüngeren Kindern geschieht das viel über Spiel, Malen und Geschichten, mit Jugendlichen eher im Gespräch."),
("Wie lange dauert eine Therapie?","Das hängt vom Anliegen ab. Nach der Kennenlernphase schlage ich Ihnen einen Umfang vor, und wir prüfen regelmäßig gemeinsam, wie es weitergeht. Eine Therapie kann jederzeit beendet werden."),
("Was ist, wenn mein Kind nicht hingehen möchte?","Das kommt vor und ist kein Hindernis für ein erstes Gespräch. Oft hilft es, wenn Ihr Kind mich einmal unverbindlich kennenlernt. Gegen den ausdrücklichen Willen eines Kindes oder Jugendlichen lässt sich keine sinnvolle Therapie machen, aber wir finden meist gemeinsam einen Weg."),
("Was passiert, wenn wir einen Termin absagen müssen?","Bitte sagen Sie so früh wie möglich ab. Die genaue Regelung zu kurzfristigen Absagen besprechen wir vor Beginn und halten sie schriftlich fest. [Regelung zum Ausfallhonorar ergänzen]"),
]),
("kosten","Kosten und Versicherung",[
("Was kostet eine Sitzung?",'Die Abrechnung erfolgt nach der Gebührenordnung für Psychotherapeuten (GOP). Eine Sitzung von 50 Minuten kostet beim 2,3-fachen Satz <span class="bh-markb">100,55 €</span>. Eine Übersicht finden Sie unter Ablauf und Kosten.'),
("Übernimmt meine private Krankenversicherung die Kosten?","Das hängt von Ihrem Tarif ab. Fragen Sie bitte vor Beginn bei Ihrer Versicherung nach, ob eine Genehmigung nötig ist, wie viele Sitzungen Ihr Tarif vorsieht und welcher Anteil erstattet wird. Bei Beihilfe gilt dasselbe für die Beihilfestelle."),
("Wir sind gesetzlich versichert. Geht das trotzdem?",'Unter Umständen ja, über die Kostenerstattung nach § 13 Abs. 3 SGB V. Voraussetzung ist, dass Ihre Krankenkasse in zumutbarer Zeit keinen Therapieplatz bei einer Praxis mit Kassenzulassung vermitteln kann. Die Kasse muss vor Beginn zustimmen. Die einzelnen Schritte stehen auf der Seite Ablauf und Kosten.'),
("Können wir die Therapie auch selbst bezahlen?","Ja. Dann erfährt keine Versicherung davon. Die Rechnung kommt monatlich."),
("Erfährt die Versicherung, worum es in der Therapie geht?","Wenn Sie die Kosten erstattet bekommen möchten, braucht die Versicherung eine Diagnose und bei Antragsverfahren einen Bericht. Inhalte der Sitzungen gibt es dort nicht. Wenn Sie selbst zahlen, bekommt keine Versicherung Informationen."),
]),
("eltern","Eltern, Schweigepflicht und Einwilligung",[
("Sind die Eltern bei jeder Sitzung dabei?",'Nein. Ihr Kind hat seine Sitzungen allein mit mir. <span class="bh-mark">Alle vier Sitzungen</span> gibt es ein eigenes Gespräch mit Ihnen als Eltern. Bei jüngeren Kindern können Sie auch einmal in eine Stunde mit hineinkommen.'),
("Was erfahre ich als Elternteil?","Sie erfahren, wie es insgesamt läuft, woran wir arbeiten und wie Sie Ihr Kind zu Hause unterstützen können. Einzelheiten aus den Stunden gebe ich nur weiter, wenn Ihr Kind einverstanden ist. Das schützt das Vertrauen, ohne das Therapie nicht wirkt."),
("Gilt die Schweigepflicht auch gegenüber den Eltern?","Ja, soweit ein Kind oder Jugendlicher die Tragweite selbst verstehen kann. Bei Jugendlichen ist das in der Regel der Fall. Was ich im Elterngespräch weitergebe, spreche ich vorher mit Ihrem Kind ab. Ausnahme ist eine ernste Gefahr für Ihr Kind oder andere. Dann handle ich und sage das Ihrem Kind vorher."),
("Müssen beide Elternteile zustimmen?","Wenn Sie das Sorgerecht gemeinsam haben, braucht es für eine Psychotherapie in der Regel die Zustimmung beider Elternteile. Das gilt auch, wenn Sie getrennt leben. Sprechen Sie mich gern an, wenn das schwierig ist, wir finden meist einen Weg."),
("Geben Sie Auskünfte an Schule, Kita oder Jugendamt?","Nur mit Ihrer ausdrücklichen Zustimmung und, bei älteren Kindern, auch mit der Ihres Kindes. Manchmal ist ein Austausch mit der Schule hilfreich. Wir besprechen vorher gemeinsam, was weitergegeben wird."),
]),
("jugendliche","Für Jugendliche und junge Erwachsene",[
("Bis zu welchem Alter behandeln Sie?",'Ich arbeite mit Kindern, Jugendlichen und jungen Erwachsenen <span class="bh-mark">bis 21 Jahre</span>. Maßgeblich ist, dass die Therapie vor dem 21. Geburtstag beginnt.'),
("Kann ich mich als Jugendliche oder Jugendlicher selbst melden?","Ja. Ruf einfach zu den Telefonzeiten an. Ab 18 entscheidest du allein. Wenn du jünger bist, brauchen wir für die Therapie meistens auch deine Eltern. Wie das gut gehen kann, klären wir zusammen. Mehr dazu steht auf der Seite Für dich."),
("Muss ich richtig krank sein, um zu kommen?","Nein. Wenn dich etwas seit längerer Zeit belastet, ist das Grund genug für ein Gespräch."),
]),
("praktisches","Praktisches und Abgrenzung",[
("Was ist der Unterschied zu einem Kinderpsychiater?","Kinder- und Jugendpsychiaterinnen und psychiater sind Ärztinnen und Ärzte. Sie können zusätzlich Medikamente verordnen. Psychotherapeutinnen behandeln mit Gesprächen, Übungen und Spiel. Manchmal ist eine Zusammenarbeit sinnvoll, das besprechen wir dann gemeinsam."),
("Ist die Praxis barrierefrei erreichbar?","[Angaben zu Etage, Aufzug und Stufen ergänzen]. Wenn Sie besondere Anforderungen haben, sagen Sie es mir bitte am Telefon."),
("Bieten Sie auch Termine per Video an?","[Angabe ergänzen, ob und in welchen Fällen Videotermine möglich sind]."),
("Was tun wir in einer akuten Krise?",'Diese Praxis bietet keinen Notfalldienst. In akuten Krisen wählen Sie bitte <span class="bh-markb">112</span> oder wenden sich an den Berliner Krisendienst. Jugendliche erreichen die Nummer gegen Kummer anonym und kostenlos unter <span class="bh-markb">116 111</span>.'),
]),
]
toc='<nav class="bh-toc" aria-label="Themen">'+''.join(f'<a href="#{i}" class="bh-toc-link">{t}</a>' for i,t,_ in G)+'</nav>'
groups=''
for i,t,qs in G:
    gh='bh-faq-gh-v' if i=='jugendliche' else 'bh-faq-gh'
    groups+=f'<div id="{i}" class="bh-faq-group"><h2 class="{gh}">{t}</h2><div class="bh-faq-list">'+''.join(f'<div class="bh-faq-item"><details><summary class="bh-faq-q">{q}<span aria-hidden="true">+</span></summary><p class="bh-faq-a">{a}</p></details></div>' for q,a in qs)+'</div></div>'
html=f'<section class="bh-faqp" aria-labelledby="h-faqp"><h1 id="h-faqp" class="bh-ph1">Häufige Fragen</h1><p class="bh-plead">Antworten auf das, was Eltern, Kinder und Jugendliche vor dem ersten Anruf am häufigsten wissen möchten.</p>{toc}{groups}<p class="bh-faq-more">Ihre Frage ist nicht dabei? Rufen Sie gern zu den Telefonzeiten an. <a href="/kontakt" class="bh-tlink">Kontakt und Telefonzeiten</a></p></section>'
FAQ=[('faq',html)]
import re,json
def strip(s): return re.sub(r'<[^>]+>','',s)
ents=[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for _,_,qs in G for q,a in qs if '[' not in a]
LD={"@context":"https://schema.org","@type":"FAQPage","mainEntity":ents}
print(sum(len(q) for _,_,q in G),'Fragen,',len(ents),'im Schema')
