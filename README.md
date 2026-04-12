# IAAI Clone + Webflow API Helper

Statische Landingpage im Stil von iaai.de mit grundlegenden Interaktionen (mobile Navigation, Slider, FAQ, Formularvalidierung) sowie Hilfsskripten fuer die Webflow API v2.

## Schnellstart

1. Lokalen Server starten:

```bash
npm run start
```

2. Seite im Browser aufrufen:

```text
http://localhost:4173
```

## Webflow API einrichten

1. `.env` Datei auf Basis von `.env.example` erstellen:

```bash
cp .env.example .env
```

2. API-Key und Site-ID eintragen:

```dotenv
WEBFLOW_API_KEY=...
WEBFLOW_SITE_ID=...
```

## Webflow Skripte

Alle Befehle lesen den API-Key aus `WEBFLOW_API_KEY`.

Sites auflisten:

```bash
npm run webflow:list
```

Custom Domains fuer eine Site anzeigen:

```bash
npm run webflow:domains -- --site <siteId>
```

Site veroeffentlichen:

```bash
npm run webflow:publish -- --site <siteId> --subdomain true
```

Optional mit Custom Domains:

```bash
npm run webflow:publish -- --site <siteId> --domains <domainId1,domainId2> --subdomain false
```
