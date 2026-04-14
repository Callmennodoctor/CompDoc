#!/usr/bin/env node

import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { stitch } from "@google/stitch-sdk";

const OUT_DIR = resolve(process.cwd(), "stitch-output");
const HTML_PATH = resolve(OUT_DIR, "iaai-stitch.html");
const META_PATH = resolve(OUT_DIR, "iaai-stitch-meta.json");

function requiredEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing environment variable: ${name}`);
  }
  return value;
}

async function fetchText(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Download failed (${response.status}) for ${url}`);
  }
  return response.text();
}

async function main() {
  requiredEnv("STITCH_API_KEY");

  const project = await stitch.createProject("IAAI 1zu1 Website Clone");
  const prompt = [
    "Erstelle eine Website als hochaufloesende Desktop-Landingpage im Stil von https://www.iaai.de.",
    "Ziel ist ein visuell sehr nahes Ergebnis (Abstaende, Typografie-Hierarchie, Section-Reihenfolge, CTA-Stil).",
    "Sektionen: Header/Navi, Hero, Leistungen, Warum IAAI, Testimonials, FAQ, Kontaktformular, Footer.",
    "Texte in Deutsch, professioneller B2B-Ton, arbeitsmedizinischer Kontext.",
    "Farbschema blau/weiss, sachlich und vertrauensvoll.",
    "Bitte semantisches HTML erzeugen und responsive CSS-Struktur vorbereiten.",
  ].join(" ");

  const screen = await project.generate(prompt, "DESKTOP");
  const htmlUrl = await screen.getHtml();
  const imageUrl = await screen.getImage();
  const html = await fetchText(htmlUrl);

  await writeFile(HTML_PATH, html, "utf8");
  await writeFile(
    META_PATH,
    JSON.stringify(
      {
        generatedAt: new Date().toISOString(),
        projectId: project.id,
        screenId: screen.id,
        htmlUrl,
        imageUrl,
      },
      null,
      2
    ),
    "utf8"
  );

  console.log(`Stitch HTML gespeichert: ${HTML_PATH}`);
  console.log(`Stitch Metadaten gespeichert: ${META_PATH}`);
  console.log(`Screenshot URL: ${imageUrl}`);
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});

