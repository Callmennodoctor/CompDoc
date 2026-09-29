# Übergabe: Webflow Site Praxis Antonia Behr

Stand 29.09.2026. Auftraggeber ist Johannes F. Angerer (IAAI Arbeitssicherheit GmbH). Er möchte Antworten auf Deutsch, knapp, als Fließtext, ohne Gedankenstriche, mit kritischem Blick auf seine Thesen. Alle Texte für die Site werden nach dem Humanizer Skill geschrieben.

## Projekt

Website einer Kinder und Jugendlichenpsychotherapeutin in Berlin Mitte. Webflow Workspace IAAI, Site „Praxis Antonia Behr“, Site ID `6a2135bd7da18f68d3f5142d`, veröffentlicht auf `https://praxis-antonia-behr.webflow.io/`. Eine eigene Domain gibt es noch nicht. Die Schreibweise des Namens ist ungeklärt: Der Nutzer schrieb „Bär“, Webflow sagt „Behr“, gebaut ist „Behr“.

Das Design folgt der Claude Design Vorlage „Praxis Behr.dc.html“ (Leitidee „Das Heft auf dem Küchentisch“, siehe `claude-design-prompt-praxis-behr.md` und `behr-src/bundle.html`).

## Designsystem

Schriften sind Gabarito (Überschriften) und Atkinson Hyperlegible Next (Text), beide als Custom Fonts in Webflow hochgeladen. Die Farben sind Tinte `#1B2540`, Papier `#FAFBFD`, Linie `#CBD8E8`, Blau `#2F5BA8`, Grün `#4E9A68` (darauf Tintentext), Violett `#6A47A0`, Marker `#F2EA4A` und Gedämpft `#48536B`. Dazu kommen ein 5 mm Karoraster als Hintergrund und Markerstriche. Tokens und Mixins liegen in `behr-build/sys_.py`.

## Seiten

| Seite | Slug | Page ID |
|---|---|---|
| Start | / | 6a2135bf7da18f68d3f51430 |
| Für Eltern | /fuer-eltern | 6abb693b8f93f7d01b155c35 |
| Für Kinder | /fuer-kinder | 6abb693b514ffb39e5b6b33e |
| Für dich (Jugendliche, auch Notfallhinweise) | /fuer-dich | 6abb572d0aac203f67f178de |
| Ablauf und Kosten | /ablauf-und-kosten | 6a2135c97da18f68d3f515cd |
| Über mich | /ueber-mich | 6a2135c97da18f68d3f515ce |
| Kontakt und Anfahrt | /kontakt | 6a2135c97da18f68d3f515cf |
| Häufige Fragen (29 Fragen, FAQPage JSON LD) | /haeufige-fragen | 6abb64b9f2dafbf0a105f406 |
| Datenschutz | /datenschutz | 6abb572d9a5c5bb1cd15adad |
| Impressum | /impressum | 6abb58618945d9a572504468 |

Aktuelles, Style Guide und vier Sicherungskopien (`backup-*-juni`) sind Entwürfe. Die Navigation ist Komponente `6a2135e7adf392ef963d3558`, der Footer `6a2135e7adf392ef963d3559`.

## Technik

Das Kontaktformular auf /kontakt sendet an Web3Forms (`https://api.web3forms.com/submit`, POST). Der Access Key steht als verstecktes Feld im Formular und ist öffentlich. Action und Method mussten über `data_element_settings_tool` gesetzt werden, weil der whtml Builder sie ignoriert.

Im Site Head stehen das Ahrefs Verifikations Meta Tag und das Einwilligungsbanner (`behr-build/consent.html`). Das Banner lädt Ahrefs Web Analytics erst nach Zustimmung und speichert die Wahl in localStorage. Der Footerlink „Datenschutz-Einstellungen“ (`#datenschutz-einstellungen`) öffnet es erneut. Abschnitt 4 der Datenschutzerklärung beschreibt das.

Beim Bauen mit dem Webflow MCP (`data_whtml_builder`) gilt:
- eine Klasse pro Element
- Media Queries nur `screen and (max-width: 991px|767px|479px)`
- Pseudoklassen nur hover, focus und active
- Inline Styles werden verworfen
- Klassen auf `details` gehen verloren, daher ein umschließendes div
- bei 429 Fehlern 45 bis 60 Sekunden warten

Aus der Cloud Umgebung blockiert der Proxy webflow.io und api.webflow.com, die Live Site ließ sich dort nicht prüfen.

## Ahrefs

Projekt 10448481 zeigt Health 33 bei nur 3 URLs. Das liegt an der Crawl Konfiguration und sagt nichts über die Inhalte. Die robots.txt von webflow.io sperrt Crawler, und der Umfang enthält die nicht existierende www Subdomain. Der Nutzer muss in Ahrefs:
- den Umfang auf die exakte URL setzen
- „robots.txt ignorieren“ aktivieren, was dank der Verifikation erlaubt ist
- neu crawlen

Danach das Audit ziehen und abarbeiten.

## Offen

1. **Bilder mit Nano Banana (Gemini).** Das ist der zuletzt gewünschte Schritt. In der Cloud Umgebung fehlte ein Gemini Key, und der Zugriff auf Cerberos wurde blockiert. Empfohlen ist ein eigener Key für dieses Projekt als `GEMINI_API_KEY`, nicht der Produktionskey aus Cerberos. Vorgeschlagene Motive:
   - Spielregal und Tisch im Praxisraum
   - Wartebereich
   - Elternpaar von hinten am Küchentisch
   - Rucksack mit Notizheft
   - Open Graph Bild

   Stil: gedämpftes Tageslicht, Papierstruktur, keine Gesichter. Porträt und Handschrift von Frau Behr bleiben echte Fotos, weil ein erzeugtes Gesicht irreführend wäre. Die Bilder als Webflow Assets hochladen (`data_assets_tool` mit presigned S3 Upload), Alt Texte setzen, die Platzhalter ersetzen und veröffentlichen.
2. **Inhalte von der Praxis.** Es fehlen:
   - Adresse, Telefonnummer (der Link `tel:+4930` wählt nur die Vorwahl), E Mail
   - Werdegang und Berufsbezeichnung laut Approbation
   - Fotos
   - Ausfallhonorar, Videotermine, Intervision oder Supervision
3. **Rechtliches.** Offen sind:
   - Auftragsverarbeitungsvertrag mit Web3Forms
   - Anschrift und Standardvertragsklauseln von Ahrefs in der Datenschutzerklärung
   - nach dem Absenden landen Nutzer auf der englischen Web3Forms Erfolgsseite; eine eigene deutsche Danke Seite als Redirect fehlt
4. **SEO.** Es fehlen:
   - Open Graph Bild
   - LocalBusiness bzw. Psychotherapist Schema, sobald die Adresse steht
   - Seite zur Barrierefreiheit
   - Google Search Console Code
   - noindex für webflow.io, sobald die eigene Domain aktiv ist
5. **Pull Request.** [Callmennodoctor/CompDoc#3](https://github.com/Callmennodoctor/CompDoc/pull/3) enthält diesen Ordner. Er ist ein Entwurf, mergebar und hat kein CI.

## Arbeitsweise

HTML und CSS in den Python Modulen unter `behr-build/` erzeugen, lokal mit Playwright rendern (`shot.js`), prüfen und dann als `act_*.json` über `data_whtml_builder` einspielen. Anschließend mit `data_sites_tool` veröffentlichen (`publishToWebflowSubdomain: true`).
