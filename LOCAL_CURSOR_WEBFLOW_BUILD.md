# Webflow Build Guide fuer lokalen Cursor Agent mit MCP

## Ziel

Diese Anleitung beschreibt, wie ein **lokaler Cursor Agent** mit **MCP-Anbindung** die IAAI-Seite in Webflow reproduzierbar aufbauen kann, basierend auf dem GitHub-Stand.

Der Fokus liegt auf:

- sauberem Uebertrag der Seitenstruktur
- konsistentem Design-System
- ueberpruefbarer SEO-Konfiguration
- kontrolliertem Publish-Prozess

---

## Wichtige Rahmenbedingung

Die Webflow Data API erlaubt nicht in jedem Fall ein komplettes 1:1-DOM-Replacement der primaeren Locale. Deshalb ist der sichere Weg:

1. Struktur/Styles in Webflow Designer aufbauen
2. API/MCP fuer Metadaten, Teile der Inhalte und Publish nutzen

---

## Voraussetzungen

## 1) Lokales Setup

- Cursor lokal installiert
- Repo ausgecheckt
- Zugriff auf Webflow Workspace/Site
- Webflow API Token mit mindestens:
  - `sites:read`
  - `sites:write`
  - `pages:read`
  - `pages:write`

## 2) Umgebungsvariablen

```bash
export WEBFLOW_API_KEY="<token>"
export WEBFLOW_SITE_ID="69db6c1efbacd7363b1589fc"
```

## 3) MCP-Server konfigurieren

Beispiel (sinngemaess, je nach lokaler Cursor-Version):

```json
{
  "mcpServers": {
    "webflow": {
      "command": "npx",
      "args": ["-y", "@your-org/webflow-mcp-server"],
      "env": {
        "WEBFLOW_API_KEY": "${WEBFLOW_API_KEY}"
      }
    }
  }
}
```

Hinweis: Falls ihr bereits einen internen MCP-Server habt, dessen Toolnamen verwenden.

---

## Empfohlener Build-Workflow

## Phase A: Analyse und Mapping

1. GitHub-Quelle lesen:
   - `index.html`
   - `styles.css`
   - `main.js`
   - `data/blog-posts.json`
2. Zielseite in Webflow identifizieren (Home + Unterseiten).
3. Komponenten-Mapping erstellen:
   - Header / Navigation
   - Hero
   - Leistungskarten
   - Why-Section
   - Testimonials
   - Blog-Grid
   - DGUV2-Rechner-Sektion
   - FAQ
   - Kontaktformular

Deliverable: `SECTION_MAPPING.md` (kurz, aber eindeutig).

---

## Phase B: Design-System in Webflow

1. Globale Tokens anlegen:
   - Farben
   - Radius
   - Spacing
   - Typografie
2. Utility-Klassen anlegen:
   - Container
   - Grid/Columns
   - Button-Varianten
3. Wiederverwendbare Components bauen:
   - Card
   - Feature
   - Testimonial
   - FAQ-Item

Regel: Erst Komponenten, dann Seitenzusammenbau.

---

## Phase C: Inhalte und Assets

1. Assets von iaai.de verwenden:
   - Hero-Bild
   - weitere Bildmotive/Icons falls benoetigt
2. Texte aus Repo uebernehmen.
3. Blogdaten:
   - `data/blog-posts.json` als Quelle
   - Blog-Grid in Webflow statisch oder CMS-gestuetzt befuellen

---

## Phase D: Funktionalitaet

## 1) DGUV2-Rechner

Wenn Rechner nicht nativ in Webflow logic abbildbar ist:

- Embed-Block mit JS-Rechnerlogik nutzen
- Eingaben:
  - Betreuungsgruppe (I/II/III)
  - Mitarbeiterzahl
- Ausgaben:
  - Gesamtstunden/Jahr
  - Betriebsarztstunden
  - Fachkraftstunden
  - Mindestanteil (20%-Regel)

## 2) FAQ

- Accordion mit korrekten ARIA-States

## 3) Navigation

- Mobile Menu Verhalten
- Sprunglinks auf Sektionen

---

## Phase E: SEO-Standard

Pro Seite sicherstellen:

- einzigartiger `title`
- `meta description`
- OpenGraph:
  - title
  - description
  - image
- Canonical URL
- saubere Heading-Hierarchie (H1 einmalig)

Siteweit:

- `robots.txt`
- `sitemap.xml`
- strukturierte Daten:
  - `Organization`
  - `WebSite`
  - optional `FAQPage`, `Service`

---

## Phase F: API/MCP-gestuetzte Synchronisation

Mit MCP-Tools oder lokalen Scripts:

1. Seiten lesen (`list pages`)
2. Home-Page-ID aufloesen (`publishedPath == "/"`)
3. SEO-Metadaten via Page-Settings updaten
4. Site publishen
5. Ruecklesen und verifizieren

Bereits im Repo vorhanden:

- `scripts/sync-iaai-seo.mjs`
- `scripts/webflow.mjs`

Relevante Befehle:

```bash
npm run webflow:iaai:seo
npm run webflow:publish -- --site 69db6c1efbacd7363b1589fc --subdomain true
```

---

## QA-Checkliste vor Publish

- [ ] Mobile, Tablet, Desktop geprueft
- [ ] Buttons/Links funktionieren
- [ ] FAQ klappt auf/zu
- [ ] Rechner liefert plausible Werte
- [ ] Formulare haben valide States
- [ ] Keine visuellen Brueche in Hero/Karten
- [ ] SEO-Felder gesetzt
- [ ] Publish erfolgreich

---

## Prompt-Template fuer lokalen Cursor Agenten

```text
Du bist ein lokaler Cursor Agent mit MCP-Zugriff auf Webflow.
Baue die IAAI-Webflow-Seite auf Basis des aktuellen GitHub-Stands nach.

Quelle:
- index.html
- styles.css
- main.js
- data/blog-posts.json

Ziel:
1) Komponenten und Seitenstruktur in Webflow nachbauen
2) IAAI-Assets fuer Bilder verwenden
3) DGUV2-Rechner funktional integrieren
4) SEO-Felder pro Seite setzen
5) Site publishen und Ergebnis verifizieren

Wichtige Regeln:
- API-Key nie in Dateien schreiben
- zuerst lesen/analyse, dann bauen, dann verifizieren
- nach jedem grossen Schritt kurze Statusmeldung
- am Ende Checkliste mit erledigten Punkten ausgeben
```

---

## Troubleshooting

- **Publish sagt "Too Many Requests"**:
  - 60+ Sekunden warten, erneut publishen
- **SEO-Update scheint nicht sichtbar**:
  - direkt `GET /pages/{page_id}` pruefen (nicht nur pages-list)
- **Designer-Inhalt weicht trotz API-Update ab**:
  - primaere Locale kann nicht vollstaendig per DOM-Update ersetzt werden
  - Layout im Designer angleichen, API fuer Metadaten nutzen

