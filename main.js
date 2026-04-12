const menuToggle = document.querySelector("#menu-toggle");
const siteNav = document.querySelector("#site-nav");
const navLinks = document.querySelectorAll("#site-nav a");
const testimonials = Array.from(document.querySelectorAll(".testimonial"));
const prevSlideBtn = document.querySelector(".slider-btn.prev");
const nextSlideBtn = document.querySelector(".slider-btn.next");
const faqItems = Array.from(document.querySelectorAll(".faq-item"));
const requestForm = document.querySelector("#request-form");
const formStatus = document.querySelector(".form-status");

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
    "Vielen Dank. Ihre Anfrage wurde lokal geprueft und kann jetzt an Webflow gesendet werden.";
  formStatus.classList.remove("is-error");
  formStatus.classList.add("is-success");
  requestForm.reset();
});

renderSlide(0);
