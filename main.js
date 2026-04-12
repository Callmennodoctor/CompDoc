const menuToggle = document.querySelector("#menu-toggle");
const siteNav = document.querySelector("#site-nav");
const navLinks = document.querySelectorAll("#site-nav a");
const testimonials = Array.from(document.querySelectorAll(".testimonial"));
const prevSlideBtn = document.querySelector(".slider-btn.prev");
const nextSlideBtn = document.querySelector(".slider-btn.next");
const faqItems = Array.from(document.querySelectorAll(".faq-item"));
const requestForm = document.querySelector("#request-form");
const formStatus = document.querySelector("#form-status");
const blogGrid = document.querySelector("#blog-grid");
const dguvForm = document.querySelector("#dguv-form");
const dguvStatus = document.querySelector("#dguv-status");
const dguvResult = document.querySelector("#dguv-result");
const resultTotal = document.querySelector("#result-total");
const resultDoctor = document.querySelector("#result-doctor");
const resultSafety = document.querySelector("#result-safety");

if (menuToggle && siteNav) {
  menuToggle.addEventListener("click", () => {
    const isExpanded = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isExpanded));
    siteNav.classList.toggle("is-open", !isExpanded);
  });
}

navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    if (!siteNav || !menuToggle) return;
    siteNav.classList.remove("is-open");
    menuToggle.setAttribute("aria-expanded", "false");
  });
});

let activeSlide = 0;

function renderSlide(index) {
  if (testimonials.length === 0) return;
  activeSlide = (index + testimonials.length) % testimonials.length;
  testimonials.forEach((slide, idx) => {
    slide.classList.toggle("is-active", idx === activeSlide);
  });
}

prevSlideBtn?.addEventListener("click", () => renderSlide(activeSlide - 1));
nextSlideBtn?.addEventListener("click", () => renderSlide(activeSlide + 1));

if (testimonials.length > 1) {
  setInterval(() => renderSlide(activeSlide + 1), 8000);
}

faqItems.forEach((item) => {
  const trigger = item.querySelector(".faq-trigger");
  const indicator = trigger?.querySelector("span:last-child");
  trigger?.setAttribute("aria-expanded", "false");

  trigger?.addEventListener("click", () => {
    const isOpen = item.classList.contains("open");

    faqItems.forEach((entry) => {
      entry.classList.remove("open");
      const entryTrigger = entry.querySelector(".faq-trigger");
      const entryIndicator = entryTrigger?.querySelector("span:last-child");
      entryTrigger?.setAttribute("aria-expanded", "false");
      if (entryIndicator) entryIndicator.textContent = "+";
    });

    if (!isOpen) {
      item.classList.add("open");
      trigger.setAttribute("aria-expanded", "true");
      if (indicator) indicator.textContent = "-";
    }
  });
});

requestForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  if (!formStatus) return;

  const data = new FormData(requestForm);
  const company = String(data.get("company") || "").trim();
  const name = String(data.get("name") || "").trim();
  const email = String(data.get("email") || "").trim();
  const inquiry = String(data.get("inquiry") || "").trim();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!company || !name || !email || !inquiry) {
    formStatus.textContent = "Bitte fuellen Sie alle Pflichtfelder aus.";
    formStatus.classList.remove("is-success");
    formStatus.classList.add("is-error");
    return;
  }

  if (!emailRegex.test(email)) {
    formStatus.textContent = "Bitte geben Sie eine gueltige E-Mail-Adresse ein.";
    formStatus.classList.remove("is-success");
    formStatus.classList.add("is-error");
    return;
  }

  formStatus.textContent =
    "Vielen Dank. Ihre Anfrage wurde lokal geprueft und kann jetzt an Ihr Backend gesendet werden.";
  formStatus.classList.remove("is-error");
  formStatus.classList.add("is-success");
  requestForm.reset();
});

function toDateLabel(value) {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "";
  return date.toLocaleDateString("de-DE", {
    year: "numeric",
    month: "short",
    day: "2-digit",
  });
}

async function loadBlogPosts() {
  if (!blogGrid) return;

  try {
    const response = await fetch("./data/blog-posts.json", { cache: "no-store" });
    if (!response.ok) {
      throw new Error("Blogdaten konnten nicht geladen werden.");
    }

    const payload = await response.json();
    const posts = Array.isArray(payload.posts) ? payload.posts : [];

    if (posts.length === 0) {
      blogGrid.innerHTML = '<p class="blog-loading">Keine Blogdaten verfuegbar.</p>';
      return;
    }

    const topPosts = posts.slice(0, 9);
    const fragment = document.createDocumentFragment();

    topPosts.forEach((post) => {
      const card = document.createElement("article");
      card.className = "blog-card";

      const heading = document.createElement("h3");
      heading.textContent = post.title || "Blogbeitrag";

      const meta = document.createElement("p");
      meta.className = "muted";
      meta.textContent = `${toDateLabel(post.fetchedAt)} | CompDocs`;

      const excerpt = document.createElement("p");
      excerpt.textContent = post.excerpt || post.seoDescription || "";

      const link = document.createElement("a");
      link.href = post.url || "#";
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.textContent = "Beitrag lesen";

      card.appendChild(heading);
      card.appendChild(meta);
      card.appendChild(excerpt);
      card.appendChild(link);
      fragment.appendChild(card);
    });

    blogGrid.innerHTML = "";
    blogGrid.appendChild(fragment);
  } catch (error) {
    blogGrid.innerHTML = `<p class="blog-loading">Fehler beim Laden: ${error.message}</p>`;
  }
}

function formatHours(value) {
  return Number(value).toLocaleString("de-DE", {
    minimumFractionDigits: 1,
    maximumFractionDigits: 1,
  });
}

function calculateDguv(group, employees) {
  const rates = {
    I: 2.5,
    II: 1.5,
    III: 0.5,
  };

  const rate = rates[group];
  if (!rate) {
    throw new Error("Bitte eine gueltige Betreuungsgruppe waehlen.");
  }

  const total = employees * rate;
  const minShare = Math.max(total * 0.2, employees * 0.2);
  const remaining = Math.max(total - 2 * minShare, 0);
  const doctor = minShare + remaining / 2;
  const safety = minShare + remaining / 2;

  return { total, doctor, safety };
}

dguvForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  if (!dguvStatus || !dguvResult) return;

  const data = new FormData(dguvForm);
  const group = String(data.get("group") || "");
  const employees = Number(data.get("employees"));

  if (!group || !Number.isFinite(employees) || employees < 1) {
    dguvStatus.textContent =
      "Bitte Betreuungsgruppe und mindestens 1 Mitarbeiter eintragen.";
    dguvStatus.classList.remove("is-success");
    dguvStatus.classList.add("is-error");
    return;
  }

  const result = calculateDguv(group, employees);
  resultTotal.textContent = `${formatHours(result.total)} h`;
  resultDoctor.textContent = `${formatHours(result.doctor)} h`;
  resultSafety.textContent = `${formatHours(result.safety)} h`;

  dguvStatus.textContent = "Berechnung erfolgreich.";
  dguvStatus.classList.remove("is-error");
  dguvStatus.classList.add("is-success");
  dguvResult.hidden = false;
});

renderSlide(0);
loadBlogPosts();
