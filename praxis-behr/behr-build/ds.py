from sys_ import *
import sub
c=sub.c
c.add('.bh-legal',SEC,{**box(["clamp(56px, 7vw, 96px)",PADX,"clamp(72px, 9vw, 128px)",PADX])})
c.add('.bh-legal-body',{"max-width":"72ch"})
c.add('.bh-lh2',{"margin-top":"48px","margin-bottom":"12px","font-family":HF,"font-weight":"700","font-size":"1.5rem","line-height":"1.25","color":INK})
c.add('.bh-lh3',{"margin-top":"24px","margin-bottom":"8px","font-family":HF,"font-weight":"600","font-size":"1.1875rem","line-height":"1.3","color":INK})
c.add('.bh-lp',{"margin-top":"0px","margin-bottom":"14px"})
c.add('.bh-lul',{"margin-top":"0px","margin-bottom":"14px","padding-left":"22px"})
c.add('.bh-lstand',{"margin-top":"40px","margin-bottom":"0px","font-size":"0.9375rem","color":MUTED})
def H(t): return f'<h2 class="bh-lh2">{t}</h2>'
def H3(t): return f'<h3 class="bh-lh3">{t}</h3>'
def P(t): return f'<p class="bh-lp">{t}</p>'
def UL(*xs): return '<ul class="bh-lul">'+''.join(f'<li>{x}</li>' for x in xs)+'</ul>'
body=''.join([
P('Diese Erklärung informiert Sie darüber, welche personenbezogenen Daten beim Besuch dieser Website und bei der Kontaktaufnahme verarbeitet werden. Für die Behandlung selbst gelten zusätzlich die berufsrechtliche Schweigepflicht und eigene Informationen, die Sie in der Praxis erhalten.'),
H('1. Verantwortliche'),
P('Antonia Behr, [Berufsbezeichnung laut Approbation]<br>[Straße und Hausnummer]<br>[PLZ] Berlin<br>Telefon: 030 [Nummer]<br>E-Mail: [E-Mail-Adresse]'),
P('Eine Pflicht zur Benennung einer oder eines Datenschutzbeauftragten besteht für diese Einzelpraxis nicht. Bei Fragen zum Datenschutz wenden Sie sich direkt an die oben genannte Adresse.'),
H('2. Hosting und Aufruf der Website'),
P('Diese Website wird bei Webflow, Inc., 398 11th Street, 2nd Floor, San Francisco, CA 94103, USA gehostet. Beim Aufruf der Seiten verarbeitet Webflow technisch notwendige Daten, insbesondere IP-Adresse, Datum und Uhrzeit des Zugriffs, aufgerufene Seite, übertragene Datenmenge, Browsertyp und Betriebssystem. Diese Daten sind erforderlich, um die Website auszuliefern, ihre Sicherheit zu gewährleisten und Angriffe abzuwehren.'),
P('Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Das berechtigte Interesse liegt im sicheren und stabilen Betrieb der Website. Mit Webflow besteht ein Vertrag zur Auftragsverarbeitung nach Art. 28 DSGVO. Eine Übermittlung in die USA stützt sich auf den Angemessenheitsbeschluss der EU-Kommission zum EU-US Data Privacy Framework, soweit Webflow danach zertifiziert ist, sowie ergänzend auf die EU-Standardvertragsklauseln.'),
H('3. Schriftarten'),
P('Die auf dieser Website verwendeten Schriftarten werden über die Server von Webflow ausgeliefert. Es findet keine Verbindung zu Google Fonts oder anderen externen Schriftanbietern statt.'),
H('4. Cookies, Analyse und Werbung'),
P('Diese Website setzt keine Analyse-, Tracking- oder Marketingdienste ein und verwendet keine Cookies, die nicht technisch notwendig sind. Es werden keine Nutzungsprofile erstellt. Eingebundene Karten oder Videos, die Daten an Dritte übertragen, gibt es nicht.'),
H('5. Kontakt per Telefon oder E-Mail'),
P('Wenn Sie anrufen oder eine E-Mail schreiben, werden Ihre Angaben verarbeitet, um Ihr Anliegen zu beantworten und gegebenenfalls einen Termin zu vereinbaren. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (Anbahnung eines Behandlungsvertrags). Soweit Sie dabei Angaben zur Gesundheit machen, erfolgt die Verarbeitung zusätzlich nach Art. 9 Abs. 2 lit. h DSGVO in Verbindung mit § 22 Abs. 1 Nr. 1 lit. b BDSG.'),
P('Bitte beachten Sie: Eine normale E-Mail wird in der Regel unverschlüsselt übertragen. Schreiben Sie deshalb bitte keine Einzelheiten zu Beschwerden, Diagnosen oder belastenden Erlebnissen per E-Mail. Darüber sprechen wir persönlich.'),
H('6. Rückrufformular'),
P('Über das Formular auf der Kontaktseite können Sie um einen Rückruf bitten. Dabei werden Ihr Name, Ihre Telefonnummer, freiwillig Ihre E-Mail-Adresse, das Alter Ihres Kindes, die Art der Versicherung und Ihre bevorzugte Rückrufzeit verarbeitet. Bitte machen Sie im Formular keine Angaben zu Beschwerden.'),
P('Das Formular wird über den Dienst Web3Forms übermittelt, der die Eingaben per E-Mail an die Praxis weiterleitet. Anbieter und Serverstandort: [laut Impressum und Datenschutzhinweisen von Web3Forms ergänzen]. Mit dem Anbieter besteht eine Vereinbarung zur Auftragsverarbeitung nach Art. 28 DSGVO [bitte vor Veröffentlichung abschließen und prüfen]. Findet eine Verarbeitung außerhalb der EU statt, erfolgt sie auf Grundlage von EU-Standardvertragsklauseln.'),
P('Schon die Bitte um einen Therapieplatz kann Rückschlüsse auf die Gesundheit zulassen. Die Verarbeitung erfolgt deshalb auf Grundlage Ihrer ausdrücklichen Einwilligung nach Art. 6 Abs. 1 lit. a und Art. 9 Abs. 2 lit. a DSGVO, die Sie mit dem Häkchen im Formular erteilen. Sie können die Einwilligung jederzeit mit Wirkung für die Zukunft widerrufen, etwa per Telefon oder E-Mail.'),
H('7. Speicherdauer'),
P('Anfragen per Telefon, E-Mail oder Formular werden gelöscht, sobald sie erledigt sind und kein Behandlungsverhältnis entsteht, spätestens jedoch nach sechs Monaten. Kommt eine Behandlung zustande, gelten die gesetzlichen Aufbewahrungspflichten für die Patientenakte, in der Regel zehn Jahre nach Abschluss der Behandlung (§ 630f Abs. 3 BGB). Die Protokolldaten des Hostinganbieters werden nach dessen Vorgaben kurzfristig gelöscht.'),
H('8. Empfänger'),
P('Ihre Daten werden nur an die oben genannten Dienstleister weitergegeben, soweit das für den Betrieb der Website und die Übermittlung Ihrer Anfrage erforderlich ist. Eine Weitergabe an sonstige Dritte, etwa Krankenkassen, erfolgt nur mit Ihrer Einwilligung oder aufgrund einer gesetzlichen Pflicht.'),
H('9. Ihre Rechte'),
P('Sie haben nach der DSGVO das Recht auf'),
UL('Auskunft über die gespeicherten Daten (Art. 15)','Berichtigung unrichtiger Daten (Art. 16)','Löschung (Art. 17) und Einschränkung der Verarbeitung (Art. 18)','Datenübertragbarkeit (Art. 20)','Widerspruch gegen Verarbeitungen auf Grundlage berechtigter Interessen (Art. 21)','Widerruf einer erteilten Einwilligung mit Wirkung für die Zukunft (Art. 7 Abs. 3)'),
P('Sie können sich außerdem bei einer Datenschutzaufsichtsbehörde beschweren. Zuständig ist die Berliner Beauftragte für Datenschutz und Informationsfreiheit, Alt-Moabit 59–61, 10555 Berlin, www.datenschutz-berlin.de.'),
H('10. Pflicht zur Bereitstellung'),
P('Sie sind nicht verpflichtet, über diese Website Daten anzugeben. Ohne Name und Telefonnummer ist ein Rückruf allerdings nicht möglich. Sie können die Praxis jederzeit auch zu den Telefonzeiten direkt anrufen.'),
'<p class="bh-lstand">Stand: September 2026</p>'])
DS=[('datenschutz',f'<section class="bh-legal"><h1 class="bh-ph1">Datenschutzerklärung</h1><div class="bh-legal-body">{body}</div></section>')]
