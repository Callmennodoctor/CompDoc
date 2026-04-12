#!/usr/bin/env node

const BASE_URL = "https://api.webflow.com/v2";

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

  const text = await response.text();
  let data = null;
  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      data = { raw: text };
    }
  }

  if (!response.ok) {
    const message =
      data?.message || data?.msg || `Request failed with status ${response.status}`;
    throw new Error(message);
  }

  return data;
}

function parseArgs(argv) {
  const [command, ...rest] = argv;
  const flags = {};
  for (let i = 0; i < rest.length; i += 1) {
    const token = rest[i];
    if (token.startsWith("--")) {
      const key = token.slice(2);
      const next = rest[i + 1];
      if (!next || next.startsWith("--")) {
        flags[key] = true;
      } else {
        flags[key] = next;
        i += 1;
      }
    }
  }
  return { command, flags };
}

async function listSites() {
  const payload = await webflowRequest("/sites");
  const sites = payload?.sites || [];
  if (sites.length === 0) {
    console.log("No sites found for this token.");
    return;
  }

  for (const site of sites) {
    console.log(`${site.id} | ${site.displayName || site.shortName || "Unnamed Site"}`);
  }
}

async function listDomains(flags) {
  const siteId = flags.site || process.env.WEBFLOW_SITE_ID;
  if (!siteId) {
    throw new Error("Please provide --site <siteId> or set WEBFLOW_SITE_ID.");
  }

  const payload = await webflowRequest(`/sites/${siteId}/custom-domains`);
  const domains = payload?.customDomains || [];
  if (domains.length === 0) {
    console.log("No custom domains found for this site.");
    return;
  }

  for (const domain of domains) {
    console.log(`${domain.id} | ${domain.url || domain.host || "Unknown Domain"}`);
  }
}

async function publishSite(flags) {
  const siteId = flags.site || process.env.WEBFLOW_SITE_ID;
  if (!siteId) {
    throw new Error("Please provide --site <siteId> or set WEBFLOW_SITE_ID.");
  }

  const publishToSubdomain =
    String(flags.subdomain || "true").toLowerCase() === "true";

  let customDomains = undefined;
  if (flags.domains) {
    customDomains = String(flags.domains)
      .split(",")
      .map((entry) => entry.trim())
      .filter(Boolean);
  }

  const body = {
    publishToWebflowSubdomain: publishToSubdomain,
  };

  if (customDomains && customDomains.length > 0) {
    body.customDomains = customDomains;
  }

  const result = await webflowRequest(`/sites/${siteId}/publish`, {
    method: "POST",
    body: JSON.stringify(body),
  });
  console.log("Publish triggered successfully.");
  console.log(JSON.stringify(result, null, 2));
}

async function main() {
  const { command, flags } = parseArgs(process.argv.slice(2));
  switch (command) {
    case "list-sites":
      await listSites();
      break;
    case "list-domains":
      await listDomains(flags);
      break;
    case "publish-site":
      await publishSite(flags);
      break;
    default:
      console.log("Usage:");
      console.log("  npm run webflow:list");
      console.log("  npm run webflow:domains -- --site <siteId>");
      console.log(
        "  npm run webflow:publish -- --site <siteId> [--subdomain true|false] [--domains id1,id2]"
      );
  }
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
