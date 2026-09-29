# Praxis Antonia Behr (Webflow)

Baukasten für die Webflow Site „Praxis Antonia Behr“ (Site ID 6a2135bd7da18f68d3f5142d, Staging praxis-antonia-behr.webflow.io).

`behr-src/` enthält die Claude Design Vorlage (`bundle.html`), Renderings und die Webfonts Gabarito und Atkinson Hyperlegible Next.

`behr-build/` enthält die Python Module, die HTML und CSS für den Webflow whtml Builder erzeugen: `sys_.py` (Tokens und Mixins), `start.py` (Startseite), `sub.py` (Für dich, Ablauf und Kosten, Kontakt), `ds.py` (Datenschutz), `faqp.py` (FAQ mit JSON LD), `um.py` (Über mich), `ek.py` (Für Eltern, Für Kinder). `act_*.json` sind die zuletzt gesendeten Builder Aktionen, `*_preview.html` und `*_d.png`/`*_m.png` lokale Vorschauen, `consent.html` das Einwilligungsbanner aus dem Site Head.

`PRODUCT.md` und `claude-design-prompt-praxis-behr.md` sind Produktkontext und Designprompt.

Keine API Keys in diesem Ordner. Der Web3Forms Access Key im Kontaktformular ist öffentlich und steht ohnehin im Seitenquelltext.
