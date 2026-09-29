# Erstellungsprompt für Claude Design: Praxis Antonia Behr (Version 3, Impeccable)

> Vor dem Einfügen ersetzen: Schreibweise des Namens (Behr oder Bär), [Bezirk], [Berufsbezeichnung laut Approbation], [Verfahren], [Telefonzeiten], [Rhythmus der Elterngespräche].

---

Gestalte die Website der psychotherapeutischen Privatpraxis von Antonia Behr, [Berufsbezeichnung laut Approbation], in Berlin [Bezirk]. Die Praxis behandelt Kinder, Jugendliche und junge Erwachsene bis 21 und bezieht ihre Familien ein. Die Seite richtet sich zuerst an Eltern. Deren Entscheidung fällt aber auch davon, ob sich ihr Kind oder ihr jugendliches Kind darin wiederfindet.

Gestalte nicht nach Vorlage und nicht nach Branchengewohnheit. Das Ergebnis darf mit keiner anderen Therapieseite in Berlin verwechselbar sein.

## 1. Richtung: „Das Heft auf dem Küchentisch"

### These

Jede Familie mit Schulkind kennt diesen Tisch am Abend: Hefte mit farbigen, durchscheinenden Umschlägen, beschriftete Etiketten, ein Stundenplan, ein Textmarker. Diese Seite übernimmt genau diese Ordnung.

- Jede Zielgruppe hat ihre Umschlagfarbe, so wie jedes Fach seine hat.
- Das Wichtigste ist markiert wie mit Textmarker.
- Der Therapierhythmus ist als Stundenplan lesbar.

Damit verweigert die Seite zwei Muster: die übliche Therapieseite mit Salbeigrün, Blättern und Steinen im Wasser, und den KI Standardlook mit cremefarbenem Grund, kursiver Serifenschrift und Terrakotta Akzent.

### Welt (auch ohne Inhalt wiedererkennbar)

- Kühles, reines Papierweiß statt Creme, in einzelnen Abschnitten mit feinem 5 mm Karoraster
- Drei gesättigte, durchscheinende Farbflächen in Heftumschlag Optik. Wo sie sich überlagern, mischen sich die Farben wie echte Folie (Multiplikation).
- Weiße Etiketten mit dünnem Rahmen für Beschriftungen
- Eine Textmarker Markierung als einziges Hervorhebungsmittel für harte Fakten
- Keine Blätter, keine Wolken, keine Tiere, kein Regenbogen

### Geschichte der Seite

Ein Elternteil versteht in wenigen Sekunden, dass hier jemand für Kinder, Jugendliche und die Familie da ist. Es sieht sofort, ob gerade ein Platz frei ist, was eine Therapie kostet und wie oft Eltern dabei sind, und ruft zu den Telefonzeiten an. Eine Jugendliche findet ihren eigenen violetten Umschlag, liest dort in der Du Form, was ihre Eltern erfahren und was nicht, und fühlt sich nicht wie ein Kind behandelt.

### Erster Bildschirm (Desktop)

**Linke Hälfte**
- Name und Berufsbezeichnung in ruhiger Größe
- Die Hauptaussage groß: „Psychotherapie für Kinder, Jugendliche und junge Erwachsene. Und für die Familie drumherum."
- Darunter Bezirk und Altersspanne bis 21 als markierter Fakt
- Primärer Button in Heftblau: „Telefonzeiten ansehen"
- Sekundär als unterstrichener Textlink: „So läuft eine Therapie ab"

**Rechte Hälfte: der Heftstapel**
- Drei leicht aufgefächerte, durchscheinende Umschläge: Blau „Für Eltern", Grün „Für Kinder", Violett „Für dich"
- Jedes Etikett ist ein Link in den jeweiligen Bereich
- Auf dem obersten Umschlag klebt das Statusetikett, zum Beispiel „Stand 29.09.2026: Warteliste offen, derzeit etwa [X] Monate"

**Mobil**
- Der Stapel liegt als horizontal verschiebbare Reihe unter der Headline
- Das Statusetikett steht vor dem Stapel, direkt unter dem Button

## 2. Visuelles System

### Farbe

Strategie: volle Palette mit drei benannten Rollen plus Markierung. Werte in OKLCH, Hex nur als Näherung.

| Rolle | OKLCH | Hex ungefähr | Verwendung |
|---|---|---|---|
| Papier | oklch(98.5% 0.004 250) | #FAFBFD | Grundfläche |
| Karolinie | oklch(88% 0.03 240) | #CBD8E8 | Raster und Linien |
| Tinte | oklch(25% 0.05 260) | #1B2540 | Text und Überschriften |
| Heftblau | oklch(45% 0.13 255) | #2F5BA8 | Eltern, primäre Handlungen, Links |
| Heftgrün | oklch(62% 0.12 150) | #4E9A68 | Kinder |
| Heftviolett | oklch(45% 0.14 300) | #6A47A0 | Jugendliche und junge Erwachsene |
| Textmarker | oklch(92% 0.17 105) | #F2EA4A | nur als Markierung hinter Text, nie als Textfarbe |

Kontrastregeln:
- Auf Heftgrün steht Tinte, nicht Weiß.
- Auf Blau und Violett steht Papierweiß.
- Sekundärtext auf Farbflächen wird aus der Flächenfarbe getönt, nie grau.
- Alle Paare erfüllen WCAG 2.2 AA.

### Typografie (lokal eingebunden)

- **Überschriften und Etiketten: Gabarito.** Freundlich, klar und kräftig, eine Schrift, wie sie auf Heftetiketten und Schulmaterial zu Hause wäre, ohne kindlich zu wirken.
- **Fließtext: Atkinson Hyperlegible Next.** Die Schrift ist für Lesbarkeit entwickelt, das ist hier die eigentliche Begründung: Kinder, Menschen mit Leseschwäche und Eltern mit wenig Deutschkenntnissen lesen mit.
  - 18 px Basis, Zeilenlänge 65 bis 75 Zeichen
  - Tabellarische Ziffern bei Zeiten und Preisen
- **Skala:** modular 1,25, fluide über clamp(). Überschriften maximal 6rem und ausbalanciert umbrochen.
- **Nicht verwenden:** Inter, Roboto, Open Sans, Lato, Montserrat, Poppins, DM Sans, DM Serif, Fraunces, Playfair, Newsreader, Lora, Space Grotesk, Handschrift Fonts.
- Handschrift kommt nur als Scan der echten Handschrift der Therapeutin vor, an genau einer Stelle.

### Komposition

- Redaktionelles, asymmetrisches Raster. Die Gliederung entsteht über Farbflächen, Karopapier Abschnitte, Linien und Weißraum.
- Enge Gruppen, großzügige Trennung, mehr Abstand über einer Überschrift als darunter.

Verboten:
- gleich große Karten mit Icon, Überschrift und Text
- verschachtelte Karten
- kleine Vorzeilen (Eyebrows) über Überschriften
- Abschnittsnummern 01, 02, 03
- Verlaufstext
- Glaseffekte
- farbige Randbalken an Karten
- Kennzahlen Hero
- Emojis als Icons

Icons, falls überhaupt: eine einzige gezeichnete Linienfamilie in gleicher Strichstärke.

### Bewegung

Genau ein gestalteter Moment: Beim Laden fächert sich der Heftstapel leicht auf, wie wenn man Hefte auf dem Tisch auseinanderschiebt.
- Exponentiell auslaufend (ease out quart), aus einem bereits sichtbaren Ausgangszustand
- Keine Einblendanimation an jedem Abschnitt
- prefers-reduced-motion schaltet den Moment ab

### Browserflächen mitgestalten

- Textauswahl in Textmarker Gelb
- Fokusringe in Heftblau mit 2 px Versatz
- Unterstreichungsabstand der Links gesetzt
- Cursorfarbe in Formularfeldern in Heftblau

## 3. Signaturelemente

1. **Das Statusetikett.** Die Kapazitätsanzeige ist ein aufgeklebtes Heftetikett mit Datum.
   - Drei Zustände: „Erstgespräche möglich", „Warteliste offen, derzeit etwa [X] Monate", „Warteliste bis [Monat] geschlossen"
   - Gepflegt über ein Webflow CMS Feld
   - Es erscheint im Hero und auf der Kontaktseite.
2. **Der Stundenplan.** Der Ablauf der Therapie ist als Wochenraster dargestellt und macht einen echten Fakt sichtbar: wöchentliche Sitzung, dazu regelmäßige Elterngespräche im Rhythmus von [Rhythmus]. Davor stehen die Schritte Anrufen, Erstgespräch und Kennenlernphase, gleiche Grammatik, schlicht und ohne Verzierung.
3. **Drei Umschläge, drei Stimmen.** Jeder Bereich hat seine Umschlagfarbe und seine Tonlage:
   - Eltern: Blau, Sie Form
   - Kinder: Grün, sehr einfache Sätze, zum Vorlesen gedacht
   - Jugendliche: Violett, Du Form, im Collegeblock Stil mit perforierter Kante
4. **Textmarker für Fakten.** Nur harte Fakten werden markiert: Altersgrenze, Wartezeit, Kosten, Telefonzeiten, Notfallnummern. Nie Werbesätze.

## 4. Sitemap

1. Start
2. Für Eltern
3. Für Kinder
4. Für dich (ab 14)
5. Ablauf und Kosten
   - Private Krankenversicherung und Beihilfe
   - Selbstzahler nach GOP
   - Kostenerstattung nach § 13 Abs. 3 SGB V als Schrittfolge
6. Über mich: Werdegang, Approbation, [Verfahren], Haltung, Kammer
7. Häufige Fragen
8. Aktuelles
9. Kontakt und Anfahrt
10. Im Notfall
11. Impressum, Datenschutz, Erklärung zur Barrierefreiheit

## 5. Startseite nach dem ersten Bildschirm

1. **Wobei ich begleite:** eine sachliche Liste von Anliegen auf Karopapier, ohne Diagnosenkatalog und ohne Versprechen.
2. **Der Stundenplan** mit den Schritten davor.
3. **Kosten** als linierte Tabelle mit drei Zeilen. Die Beträge sind markiert, sofern sie feststehen.
4. **Kurzporträt** mit Foto und einem handschriftlichen Satz der Therapeutin als Scan.
5. **Fünf häufige Fragen** als liniertes Akkordeon.
6. **Kontakt:**
   - Telefonzeiten groß
   - Rückrufformular sekundär
7. **Footer** mit dauerhaft sichtbarem Notfallhinweis: „Diese Praxis bietet keinen Notfalldienst. In akuten Krisen: 112, Berliner Krisendienst, Nummer gegen Kummer 116 111."

## 6. Bildsprache

- **Stil:** Tageslichtfotografie mit kühler, klarer Weißbalance, ruhig und nah.
- **Motive:** Hefte und Stifte auf einem Tisch, Hände an Bauklötzen, ein Rucksack an der Garderobe, der Praxisraum.
- **Kinder und Jugendliche:** nie mit Gesicht, nur angeschnitten oder über Hände und Gegenstände.
- **Porträt:** die Therapeutin sitzend und auf Augenhöhe, im Raum.
- **Synthetische Platzhalter:** deutlich kennzeichnen und als Liste zum Austausch mitliefern.

## 7. Texte, Recht und Formular

**Knöpfe und Rückmeldungen**
- Knöpfe benennen ihre Handlung: „Rückruf anfragen", „Telefonzeiten ansehen". Nie „Mehr erfahren".
- Fehlermeldungen nennen das Problem und den Ausweg.
- Die Bestätigung ist konkret: „Danke. Ich rufe Sie innerhalb von drei Werktagen an."

**Berufsrecht**
- Keine Heilversprechen, Erfolgsquoten oder Superlative
- Keine Patientenstimmen
- Keine Dringlichkeitsrhetorik
- Maßstab sind das Merkblatt der Psychotherapeutenkammer Berlin und das Heilmittelwerbegesetz.

**Formular**
- Nur Name, Telefon, E-Mail, Alter des Kindes, Versicherungsart, Rückrufzeit und Datenschutz
- Kein Freitext zu Beschwerden, stattdessen der Hinweis: „Bitte schreiben Sie hier noch nichts zu Beschwerden, darüber sprechen wir persönlich."

**Jugendbereich**
Er beantwortet ehrlich: Erfahren meine Eltern alles? Muss ich reden, wenn ich nicht will? Bin ich zu alt oder nicht krank genug?

## 8. Ehrliches Risiko und Leitplanken

- **Assoziation Schule.** Schule ist für viele Kinder dieser Praxis selbst die Belastung. Deshalb gibt es keinerlei Noten, Rotstift, Zeugnis, Tafel oder Prüfungsmotive. Verwendet werden nur die neutralen Dinge des Küchentischs: Umschläge, Etiketten, Karopapier, Stundenplan, Textmarker.
- **Kindlicher Eindruck.** Die Farben bleiben flächig und gesättigt, die Typografie erwachsen. Der violette Bereich muss für eine 17 Jährige funktionieren.

## 9. Übergabe an Webflow

**Komponenten**
- Navigation
- Footer mit Notfallhinweis
- Statusetikett
- Heftstapel
- Stundenplan
- Kostentabelle
- Akkordeon
- Kontaktblock

**Technik**
- Abstände im 8 px Raster mit variiertem Rhythmus
- Mobile First, mit Telefon Button im Daumenbereich
- Semantische Überschriften und Alt Texte
- Klickflächen ab 44 px
- Zustände für Hover, Fokus, Fehler, Laden und Leer

**Lieferumfang**
- Desktop und Mobil für Start, Für dich, Ablauf und Kosten sowie Kontakt
- Ein Styleguide Blatt mit Farbtokens, Schriftskala, Buttons, Formularzuständen und den drei Etikettvarianten

## 10. Selbstprüfung vor der Abgabe

Einmal gebündelt prüfen, Desktop und Mobil zusammen, alles in einem Durchgang beheben, dann aufhören:

1. Könnte man die Ästhetik allein aus der Branche erraten? Wenn ja, überarbeiten.
2. Gibt es irgendwo Creme, Serifenkursive oder Terrakotta? Entfernen.
3. Steht Textmarker nur hinter harten Fakten?
4. Findet ein erschöpfter Elternteil am Smartphone Status, Kosten und Telefonzeiten ohne Suchen?
5. Fühlt sich eine 16 Jährige im violetten Bereich ernst genommen?
6. Kommt irgendwo Schulstress als Motiv vor? Entfernen.
