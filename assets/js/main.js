/* Moavia SEO Pro — zero-dependency interactions, no tracking scripts */
(() => {
  'use strict';
  // For Netlify-managed lead capture, change to 'netlify' and deploy to Netlify.
  // Default 'whatsapp' works on GitHub Pages, Vercel, Netlify, and local static hosting.
  const FORM_PROVIDER = 'whatsapp';
  const WHATSAPP_NUMBER = '923234313869';
  const whatsappURL = message => `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;

  const themeButton = document.querySelector('[data-theme-toggle]');
  const updateThemeLabel = () => {
    if (themeButton) {
      const isLight = document.documentElement.dataset.theme === 'light';
      themeButton.textContent = isLight ? '☾' : '☀';
      themeButton.setAttribute('aria-label', isLight ? 'Switch to dark theme' : 'Switch to light theme');
      themeButton.setAttribute('title', isLight ? 'Dark theme' : 'Light theme');
    }
  };
  try {
    const saved = localStorage.getItem('msp-theme');
    if (saved === 'light' || saved === 'dark') document.documentElement.dataset.theme = saved;
  } catch (_) { /* Theme persists only where storage is available. */ }
  updateThemeLabel();
  themeButton?.addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem('msp-theme', next); } catch (_) { /* ignore */ }
    updateThemeLabel();
  });

  const menuButton = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('[data-nav-links]');
  const closeMenu = () => {
    nav?.classList.remove('is-open');
    menuButton?.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('menu-open');
  };
  menuButton?.addEventListener('click', () => {
    const open = !nav.classList.contains('is-open');
    nav.classList.toggle('is-open', open);
    menuButton.setAttribute('aria-expanded', String(open));
    document.body.classList.toggle('menu-open', open);
  });
  nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  window.addEventListener('resize', () => { if (window.innerWidth > 900) closeMenu(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });

  document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  // Preserve the selected pricing/service tier when opening Contact from a service page.
  const requestedService = new URLSearchParams(window.location.search).get('service');
  const serviceSelect = document.querySelector('#contact-form-service');
  if (requestedService && serviceSelect) {
    const option = [...serviceSelect.options].find(o => o.value === requestedService);
    if (option) serviceSelect.value = requestedService;
  }

  // Transparent scenario calculator: uplift is a relative change in conversion rate,
  // not a guaranteed return or a prediction of campaign outcomes.
  const roiForm = document.querySelector('[data-roi-calculator]');
  if (roiForm) {
    const output = document.querySelector('[data-roi-result]');
    const fmt = new Intl.NumberFormat('en-US', {style:'currency',currency:'USD',maximumFractionDigits:0});
    const calculate = () => {
      const visits = Math.max(0, Number(roiForm.elements.visits.value) || 0);
      const rate = Math.min(100, Math.max(0, Number(roiForm.elements.rate.value) || 0));
      const order = Math.max(0, Number(roiForm.elements.order.value) || 0);
      const lift = Math.max(0, Number(roiForm.elements.lift.value) || 0);
      const incremental = visits * (rate / 100) * (lift / 100) * order;
      output.textContent = fmt.format(incremental);
      const hidden = document.querySelector('input[name="scenario"]');
      if (hidden) hidden.value = `Monthly visits ${visits}, conversion rate ${rate}%, average order value $${order}, relative conversion lift ${lift}%; illustrative incremental monthly revenue ${fmt.format(incremental)}`;
    };
    roiForm.addEventListener('input', calculate);
    calculate();
  }

  // Lead forms transfer the prepared details to WhatsApp by default.
  // This deliberately avoids claiming to store leads without a configured backend.
  document.querySelectorAll('[data-lead-form]').forEach(form => {
    form.addEventListener('submit', async event => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const status = form.querySelector('[data-form-status]');
      const button = form.querySelector('button[type="submit"]');
      const data = new FormData(form);
      const content = [...data.entries()]
        .filter(([key,value]) => !['form-name','bot-field','consent'].includes(key) && String(value).trim())
        .map(([key,value]) => `${key.replace(/[-_]/g,' ')}: ${String(value).trim()}`);
      if (String(data.get('bot-field') || '').trim()) return; // spam honeypot
      if (FORM_PROVIDER === 'netlify') {
        button.disabled = true;
        status.textContent = 'Sending your inquiry…';
        try {
          const response = await fetch(form.getAttribute('action') || '/', {
            method:'POST',
            headers:{'Content-Type':'application/x-www-form-urlencoded'},
            body:new URLSearchParams(data).toString()
          });
          if (!response.ok) throw new Error(`HTTP ${response.status}`);
          status.textContent = 'Thank you. Your inquiry has been submitted.';
          form.reset();
        } catch (_) {
          status.textContent = 'Submission failed. Your details have not been saved; please use the WhatsApp contact link.';
        } finally { button.disabled = false; }
      } else {
        status.textContent = 'Opening WhatsApp with your prepared message. Press Send in WhatsApp to deliver it.';
        const url = whatsappURL(`Hello Moavia SEO Pro, I would like to inquire:\n\n${content.join('\n')}`);
        // Same-tab navigation works consistently even if popup blocking is enabled.
        window.location.href = url;
      }
    });
  });

  // Scripted FAQ support — deliberately not described as a generative AI service.
  // No user messages are sent to an external API or stored by this website.
  const panel = document.querySelector('[data-chat-panel]');
  const launcher = document.querySelector('[data-chat-launcher]');
  const closer = document.querySelector('[data-chat-close]');
  const messages = document.querySelector('[data-chat-messages]');
  const chatForm = document.querySelector('[data-chat-form]');
  const chatInput = document.querySelector('[data-chat-input]');
  const suggestions = document.querySelector('[data-chat-suggestions]');
  const replies = [
    {keys:['seo','keyword','backlink','ranking','audit'],reply:'SEO plans start at $300/month (Starter), $650/month (Growth), and $1,200/month (Scale). They can include audits, on-page work, technical SEO, and link outreach based on scope. See Services → SEO for details.'},
    {keys:['website','web','wordpress','development','landing','ecommerce','store'],reply:'Web development projects start at $600 for a landing page, $1,500 for a business website, and $3,000+ for custom or e-commerce projects. Final cost depends on design, pages, integrations, and content.'},
    {keys:['meta','facebook','instagram','pixel','capi','social ads'],reply:'Meta Ads management starts at $400/month, with Growth at $850/month and Scale from $1,500/month. Ad spend is separate. Services include campaign setup, audience testing, tracking, and reporting.'},
    {keys:['google','ppc','search ads','shopping','youtube','display'],reply:'Google Ads management starts at $450/month, Growth $900/month, and Scale from $1,600/month. Advertising spend is not included. We work on account structure, keywords, tracking, and optimization.'},
    {keys:['contact','whatsapp','call','phone','talk','consult'],reply:'You can reach us on WhatsApp at +92 323 4313869 or email moaviahassan124@gmail.com. Choose the WhatsApp link below to speak directly.'},
    {keys:['free','consultation','proposal','quote'],reply:'A free initial project review can be requested through the contact form or WhatsApp. An in-depth audit or implementation scope may be quoted separately.'},
    {keys:['price','pricing','cost','package','rate'],reply:'Starting prices (USD): SEO $300/month, Web Development $600/project, Meta Ads $400/month, Google Ads $450/month. These are indicative; scopes and media budgets are quoted separately.'}
  ];
  const addMessage = (text, sender) => {
    if (!messages) return;
    const bubble = document.createElement('div');
    bubble.className = `bubble ${sender}`;
    bubble.textContent = text; // textContent prevents HTML injection
    messages.appendChild(bubble);
    messages.scrollTop = messages.scrollHeight;
  };
  const replyTo = query => {
    addMessage(query, 'user');
    const normalized = query.toLowerCase();
    const match = replies.find(item => item.keys.some(key => normalized.includes(key)));
    addMessage(match ? match.reply : 'I can help with SEO, website development, Meta Ads, Google Ads, pricing, and contact information. For a detailed answer, use the WhatsApp link below.', 'bot');
  };
  const openChat = () => {
    if (!panel) return;
    panel.hidden = false;
    launcher?.setAttribute('aria-expanded','true');
    chatInput?.focus();
  };
  const closeChat = () => {
    if (!panel) return;
    panel.hidden = true;
    launcher?.setAttribute('aria-expanded','false');
    launcher?.focus();
  };
  launcher?.addEventListener('click', () => panel?.hidden ? openChat() : closeChat());
  closer?.addEventListener('click', closeChat);
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && panel && !panel.hidden) closeChat(); });
  chatForm?.addEventListener('submit', e => {
    e.preventDefault();
    const query = chatInput.value.trim();
    if (!query) return;
    replyTo(query);
    chatInput.value = '';
    chatInput.focus();
  });
  suggestions?.querySelectorAll('button').forEach(button => button.addEventListener('click', () => replyTo(button.textContent.trim())));
})();
