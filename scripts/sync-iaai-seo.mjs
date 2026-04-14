#!/usr/bin/env node

const BASE_URL = "https://api.webflow.com/v2";
const DEFAULT_SITE_ID = "69db6c1efbacd7363b1589fc";

function readEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing environment variable: ${name}`);
  }
  return value;
}

function siteIdFromEnv() {
  return process.env.WEBFLOW_SITE_ID || DEFAULT_SITE_ID;
}

async function webflowRequest(path, options = {}) {
  const token = readEnv("WEBFLOW_API_KEY");
  const response = await fetch(`${BASE_URL}${path}`, {
    ...options,
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
  });

  const raw = await response.text();
  let data = null;
  if (raw) {
    try {
      data = JSON.parse(raw);
    } catch {
      data = { raw };
    }
  }

  if (!response.ok) {
    throw new Error(
      `${response.status} ${path}: ${data?.message || data?.msg || "unknown error"}`
    );
  }

  return data;
}

async function findHomepage(siteId) {
  const payload = await webflowRequest(`/sites/${siteId}/pages?limit=100&offset=0`);
  const pages = payload?.pages || [];
  const home = pages.find((page) => page.publishedPath === "/");
  if (!home) {
    throw new Error("Homepage in Webflow site not found.");
  }
  return home;
}

async function updateHomepageSeo(pageId) {
  const body = {
    seo: {
      title: "IAAI Arbeitssicherheit GmbH | Arbeitsmedizin, Arbeitssicherheit und DGUV2 Rechner",
      description:
        "IAAI bietet bundesweit arbeitsmedizinische und sicherheitstechnische Betreuung. Mit DGUV2-Einsatzzeitenrechner, FAQ und aktuellen Fachinhalten.",
    },
    openGraph: {
      title: "IAAI Arbeitssicherheit GmbH | Betreuung fuer Ihr Unternehmen",
      titleCopied: false,
      description:
        "Erfahrene Betriebsaerzte und Sicherheitsingenieure fuer Unternehmen in ganz Deutschland. Jetzt Angebot anfordern.",
      descriptionCopied: false,
    },
  };

  return webflowRequest(`/pages/${pageId}`, {
    method: "PUT",
    body: JSON.stringify(body),
  });
}

async function main() {
  const siteId = siteIdFromEnv();
  const home = await findHomepage(siteId);
  console.log(`Homepage-ID gefunden: ${home.id}`);
  const result = await updateHomepageSeo(home.id);
  console.log("SEO-Settings der IAAI-Homepage aktualisiert.");
  console.log(
    JSON.stringify(
      {
        pageId: result.id,
        seo: result.seo,
        openGraph: result.openGraph,
      },
      null,
      2
    )
  );
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
