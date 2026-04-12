#!/usr/bin/env node

const BASE_URL = "https://api.webflow.com/v2";
const IAAI_SITE_ID = "69db6c1efbacd7363b1589fc";
const HOMEPAGE_PATH = "/";

function readEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing environment variable: ${name}`);
  }
  return value;
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

async function findHomepageId() {
  const payload = await webflowRequest(`/sites/${IAAI_SITE_ID}/pages?limit=100&offset=0`);
  const pages = payload?.pages || [];
  const home = pages.find((page) => page.publishedPath === HOMEPAGE_PATH);
  if (!home) {
    throw new Error("Homepage for IAAI site not found.");
  }
  return home.id;
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
      description:
        "Erfahrene Betriebsaerzte und Sicherheitsingenieure fuer Unternehmen in ganz Deutschland. Jetzt Angebot anfordern.",
    },
  };

  return webflowRequest(`/pages/${pageId}`, {
    method: "PATCH",
    body: JSON.stringify(body),
  });
}

async function main() {
  const pageId = await findHomepageId();
  console.log(`Homepage-ID gefunden: ${pageId}`);
  await updateHomepageSeo(pageId);
  console.log("SEO-Settings der IAAI-Homepage aktualisiert.");
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
