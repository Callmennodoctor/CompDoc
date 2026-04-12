#!/usr/bin/env node

import { mkdir, writeFile } from "node:fs/promises";
import { resolve } from "node:path";

const BASE_URL = "https://api.webflow.com/v2";
const SITE_ID = "686445e522a903cc9af42ef0";
const OUTPUT_PATH = resolve(process.cwd(), "data", "blog-posts.json");

function readEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing environment variable: ${name}`);
  }
  return value;
}

function decodeHtmlEntities(text) {
  return text
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">");
}

function stripHtml(text) {
  return decodeHtmlEntities(text.replace(/<[^>]+>/g, " "))
    .replace(/\s+/g, " ")
    .trim();
}

function excerpt(text, maxLength = 220) {
  if (text.length <= maxLength) {
    return text;
  }
  const short = text.slice(0, maxLength);
  const lastSpace = short.lastIndexOf(" ");
  return `${short.slice(0, Math.max(lastSpace, 120)).trim()}...`;
}

async function webflowRequest(path) {
  const token = readEnv("WEBFLOW_API_KEY");
  const response = await fetch(`${BASE_URL}${path}`, {
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
  });

  const raw = await response.text();
  let data = {};

  if (raw) {
    try {
      data = JSON.parse(raw);
    } catch {
      throw new Error(`Invalid JSON response for ${path}`);
    }
  }

  if (!response.ok) {
    throw new Error(
      `Webflow request failed (${response.status}) for ${path}: ${
        data.message || data.msg || "unknown error"
      }`
    );
  }

  return data;
}

function extractTextFromDom(domPayload) {
  const nodes = domPayload?.nodes || [];
  const texts = nodes
    .filter((node) => node.type === "text" && node.text)
    .map((node) => {
      if (node.text.text) return String(node.text.text).trim();
      if (node.text.html) return stripHtml(String(node.text.html));
      return "";
    })
    .filter(Boolean);

  const uniqueTexts = [...new Set(texts)];
  const longParagraphs = uniqueTexts.filter((line) => line.length > 80);
  const bodyText = longParagraphs.join(" ");

  return {
    bodyText,
    excerpt: excerpt(bodyText || uniqueTexts.join(" ")),
  };
}

function normalizePage(page, domInfo) {
  return {
    id: page.id,
    title: page.title,
    slug: page.slug,
    url: `https://www.compdocs.de${page.publishedPath}`,
    publishedPath: page.publishedPath,
    seoTitle: page.seo?.title || page.title,
    seoDescription: page.seo?.description || "",
    excerpt: domInfo.excerpt || page.seo?.description || "",
    fetchedAt: new Date().toISOString(),
  };
}

async function fetchAllPages() {
  const limit = 100;
  let offset = 0;
  let total = Infinity;
  const pages = [];

  while (offset < total) {
    const payload = await webflowRequest(
      `/sites/${SITE_ID}/pages?limit=${limit}&offset=${offset}`
    );
    const chunk = payload.pages || [];
    pages.push(...chunk);

    total = payload.pagination?.total ?? chunk.length;
    offset += chunk.length;

    if (chunk.length === 0) {
      break;
    }
  }

  return pages;
}

function isBlogPage(page) {
  return (
    typeof page.publishedPath === "string" &&
    page.publishedPath.startsWith("/blog/") &&
    !page.archived &&
    !page.draft
  );
}

async function main() {
  console.log("Lade Seitenliste von CompDocs...");
  const pages = await fetchAllPages();
  const blogPages = pages.filter(isBlogPage);

  if (blogPages.length === 0) {
    throw new Error("Keine Blogseiten gefunden.");
  }

  console.log(`Gefundene Blogseiten: ${blogPages.length}`);
  const records = [];

  for (const page of blogPages) {
    try {
      const dom = await webflowRequest(`/pages/${page.id}/dom`);
      const domInfo = extractTextFromDom(dom);
      records.push(normalizePage(page, domInfo));
      console.log(`OK: ${page.publishedPath}`);
    } catch (error) {
      console.warn(`Warnung bei ${page.publishedPath}: ${error.message}`);
      records.push(
        normalizePage(page, {
          excerpt: page.seo?.description || "",
        })
      );
    }
  }

  records.sort((a, b) => a.title.localeCompare(b.title, "de"));

  await mkdir(resolve(process.cwd(), "data"), { recursive: true });
  await writeFile(
    OUTPUT_PATH,
    JSON.stringify(
      {
        source: "Webflow API v2",
        siteId: SITE_ID,
        total: records.length,
        generatedAt: new Date().toISOString(),
        posts: records,
      },
      null,
      2
    ),
    "utf8"
  );

  console.log(`Export abgeschlossen: ${OUTPUT_PATH}`);
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
