# IAAI Clone + CompDocs Import + DGUV2 Rechner

Statische Landingpage im Stil von iaai.de mit:

- verfeinertem UI/UX (Header, Hero, Karten, FAQ, Testimonials, Formular)
- dynamischer Blog-Sektion aus CompDocs-Daten
- integriertem DGUV2-Einsatzzeitenrechner (Grundbetreuung)
- Webflow API v2 Hilfsskripten

## Schnellstart

```bash
npm run start
```

Im Browser:

```text
http://localhost:4173
```

## Webflow API einrichten

1. `.env` aus Vorlage erstellen:

```bash
cp .env.example .env
```

2. Werte eintragen:

```dotenv
WEBFLOW_API_KEY=...
WEBFLOW_SITE_ID=...
```

## Skripte

### Webflow Basisbefehle

```bash
npm run webflow:list
npm run webflow:domains -- --site <siteId>
npm run webflow:publish -- --site <siteId> --subdomain true
```

### CompDocs Blog-Import

Exportiert Blogbeiträge aus CompDocs via:

- `GET /v2/sites/{siteId}/pages`
- `GET /v2/pages/{pageId}/dom`

und schreibt nach `data/blog-posts.json`.

```bash
WEBFLOW_API_KEY=... npm run compdocs:import
```

Die Startseite lädt diese Datei dann dynamisch und rendert die Blogkarten.

## DGUV2 Rechner-Logik

Der Rechner bildet die Grundbetreuung nach DGUV Vorschrift 2 über Gruppenfaktoren ab:

- Gruppe I: 2.5 Stunden pro Mitarbeiter/Jahr
- Gruppe II: 1.5 Stunden pro Mitarbeiter/Jahr
- Gruppe III: 0.5 Stunden pro Mitarbeiter/Jahr

Berechnung:

- Gesamtstunden = Mitarbeiterzahl * Gruppenfaktor
- Mindestanteil je Leistungs­erbringer = `max(20% von Gesamtstunden, 0.2 * Mitarbeiterzahl)`
- Betriebsarztstunden = Mindestanteil
- Fachkraftstunden = Gesamtstunden - Mindestanteil

Hinweis: Für eine realvertragliche Ausgestaltung muss die betriebs­spezifische Betreuung zusätzlich bewertet werden.

## SEO-Setup

Die Landingpage enthält technische und inhaltliche SEO-Grundlagen:

- eindeutige `title` und `meta description`
- Canonical-URL
- OpenGraph- und Twitter-Metadaten
- strukturierte Daten (Schema.org: `Organization`, `WebSite`, `FAQPage`)
- semantische Struktur mit klarer Heading-Hierarchie und `main`/`nav`/`section`-Landmarks
- `robots.txt` und `sitemap.xml`

Dateien:

- `robots.txt`
- `sitemap.xml`
