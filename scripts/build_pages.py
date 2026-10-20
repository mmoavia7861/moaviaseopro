#!/usr/bin/env python3
"""Build standalone static HTML pages. No third-party templates or runtime dependencies.

Edit SITE_URL or page content here, then run: python scripts/build_pages.py
Generated HTML remains independently deployable on GitHub Pages, Netlify, or Vercel.
"""
from __future__ import annotations
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# A known project URL is the non-speculative default until an owned .com is connected.
SITE_URL = 'https://mmoavia7861.github.io/moaviaseopro/'
PHONE_DISPLAY = '+92 323 4313869'
PHONE = '+923234313869'
WA = 'https://wa.me/923234313869'
EMAIL = 'moaviahassan124@gmail.com'
LINKEDIN = 'https://www.linkedin.com/in/moavia-hassan-seo/'
FACEBOOK = 'https://www.facebook.com/profile.php?id=61594226902693'


def esc(s: object) -> str:
    return html.escape(str(s), quote=True)


def home_rel(path: str, depth: int) -> str:
    return ('../' * depth) + path


def b(url: str, label: str, css: str = 'btn-primary', external: bool = False) -> str:
    extra = ' target="_blank" rel="noopener noreferrer"' if external else ''
    return f'<a class="btn {css}" href="{esc(url)}"{extra}>{esc(label)}</a>'

SERVICES = {
    'seo': {
        'file': 'services/seo.html', 'name':'SEO Services','short':'Search Engine Optimization',
        'title':'SEO Services: Technical, On-Page & Local SEO | Moavia SEO Pro',
        'description':'Practical SEO services for global businesses: technical audits, keyword research, on-page SEO, local SEO and ethical outreach. View transparent USD plans.',
        'headline':'SEO services built for sustainable organic growth',
        'lead':'Improve the way search engines discover, understand, and present your website. We prioritize fixes and content opportunities according to business value, not vanity metrics.',
        'icon':'↗','deliverables':[
            ('Complete SEO audits','A prioritized analysis of index coverage, site architecture, metadata, internal links, structured data, competitors, and search-intent gaps. Every audit concludes with an actionable issue list.'),
            ('On-page optimization','Search-intent mapping, titles, descriptions, helpful page copy, header structure, internal linking, alt attributes, and content refreshes for priority URLs.'),
            ('Technical SEO','Core Web Vitals diagnostics, crawling and rendering checks, robots directives, canonicals, redirects, XML sitemaps, schema validation, and mobile usability.'),
            ('Off-page SEO & high-authority backlinks','Link-gap research, relevant publisher prospecting, digital PR and manual outreach for editorial backlinks. Domain Authority is a third-party score, not a Google ranking guarantee; we prioritize contextual relevance and quality.'),
            ('Keyword and competitor research','Keyword clustering by intent and opportunity, competitor content comparisons, SERP feature review, and a practical content roadmap.'),
            ('Local SEO','Google Business Profile guidance, local landing pages, NAP consistency checks where applicable, location-focused keyword research, and review-process recommendations.'),
            ('E-commerce SEO','Category taxonomy, faceted navigation guidance, product schema, product page optimization, internal link flow, and large-catalog crawl control.'),
            ('Measurement and reporting','Measurement plans using Google Search Console and Google Analytics where access is provided, including visibility, conversions, and completed deliverables.')
        ],
        'tiers':[
            ('Starter',300,'/ month','For small websites building strong SEO foundations.', ['Initial technical and content audit','Up to 5 priority pages optimized','Keyword map for core services','Monthly progress summary'],False),
            ('Growth',650,'/ month','For growing sites with content and technical opportunities.',['Ongoing technical issue resolution','Up to 15 priority pages','Keyword and competitor roadmap','Content briefs and internal linking','Monthly performance reporting'],True),
            ('Scale',1200,'/ month','For larger sites or multi-location growth programs.',['Technical and content workstreams','Up to 30 priority pages','E-commerce or local SEO support','Editorial outreach planning','Fortnightly status updates'],False)
        ],
        'faqs':[
            ('How long does SEO take?','SEO timelines vary by site condition, competition, resources, and search demand. Technical fixes may be seen sooner, while organic growth often requires months of consistent work.'),
            ('Do SEO packages include backlinks?','They include appropriate off-page analysis and outreach planning where scoped. Paid placements, third-party publishing fees, and guaranteed links are not included by default.'),
            ('Can you guarantee first-page rankings?','No. Search rankings depend on search engine systems and competitive factors beyond any agency’s control. We commit to transparent work and measurable reporting.'),
            ('Which tools do you use?','Depending on access and project scope, audits can use Google Search Console, GA4, Screaming Frog, Semrush, Ahrefs and manual checks.')
        ],
        'steps':[('Discover','Review goals, search demand, and website access.'),('Prioritize','Create a roadmap ordered by impact and effort.'),('Optimize','Implement fixes, content changes, and agreed outreach.'),('Measure','Report completed work, search trends, and leads.')]
    },
    'web-development': {
        'file':'services/web-development.html','name':'Web Development','short':'Web Development',
        'title':'Web Development & WordPress Services | Moavia SEO Pro',
        'description':'Fast, mobile-friendly WordPress sites, custom websites, landing pages, e-commerce development, security and ongoing maintenance. Explore project pricing.',
        'headline':'Modern websites designed to convert and perform',
        'lead':'Get a website that balances clear user journeys, accessibility, search-friendly architecture, and maintainable code—without unnecessary bloat or plugins.',
        'icon':'</>','deliverables':[
            ('Custom WordPress websites','Responsive WordPress builds, block-based editing, child themes or custom themes, flexible page layouts, and intuitive content management.'),
            ('WordPress speed optimization','Asset compression, caching strategy, efficient CSS and JavaScript, database hygiene, and Core Web Vitals diagnostics before and after changes.'),
            ('Security and reliability','HTTPS configuration guidance, backups, update schedules, least-privilege access, sensible form anti-spam and website recovery preparation.'),
            ('Modern custom websites','Lightweight HTML/CSS/JavaScript builds with optional AI-assisted development followed by human code review, testing and accessibility checks.'),
            ('Conversion-focused landing pages','Campaign-specific content, compelling CTAs, readable forms, performance-friendly layouts, tracking plans and mobile-first design.'),
            ('E-commerce stores','WooCommerce or custom storefront planning, category and product structures, cart and checkout UX, payment provider integration as scoped.'),
            ('Web maintenance','Routine updates, uptime review, backups, content updates, bug fixes, and accessibility/performance refinements.'),
            ('Technical SEO foundations','Clean headings, metadata, structured data where valid, descriptive URLs, internal links, sitemaps and launch-time redirect checks.')
        ],
        'tiers':[
            ('Launch',600,'/ project','A focused online presence for a new service.',['Up to 3 responsive pages','Lead/contact form integration','Basic on-page SEO setup','One revision round'],False),
            ('Business',1500,'/ project','A polished, editable website for a growing team.',['Up to 10 responsive pages','WordPress or static-site build','Speed and technical SEO setup','Analytics integration (access required)','Two revision rounds'],True),
            ('Custom / Store',3000,'+ / project','Advanced features or e-commerce scope.',['Custom information architecture','Store or application integrations','Performance and security review','Launch testing and documentation','Scoped post-launch support'],False)
        ],
        'faqs':[
            ('Is hosting or a domain included?','No. Domain registrations, hosting, premium plugins, paid themes, transaction fees, and third-party subscriptions are quoted separately.'),
            ('Can you build with WordPress?','Yes. We can use WordPress for editable business sites and WooCommerce stores, or lightweight static technologies when those fit the requirements better.'),
            ('Will my site work on mobile?','Responsive design and mobile usability checks are included in all listed packages.'),
            ('Can you maintain my existing website?','Yes. A maintenance scope can cover updates, backups, bugs, security hygiene and ongoing improvements.')
        ],
        'steps':[('Plan','Confirm pages, target audience, integrations, and content.'),('Design','Define layouts, design tokens and conversion paths.'),('Develop','Build responsive pages and relevant integrations.'),('Launch','Test speed, SEO, forms, and browser compatibility.')]
    },
    'meta-ads': {
        'file':'services/meta-ads.html','name':'Meta Ads','short':'Facebook & Instagram Ads',
        'title':'Meta Ads Management: Facebook & Instagram | Moavia SEO Pro',
        'description':'Meta Ads management for leads and e-commerce, including Facebook and Instagram campaigns, creative testing, retargeting, Pixel and Conversions API setup.',
        'headline':'Meta Ads campaigns focused on qualified outcomes',
        'lead':'Turn Facebook and Instagram advertising into a deliberate testing and optimization process with better event tracking, creative strategy and clearer reporting.',
        'icon':'◎','deliverables':[
            ('Facebook and Instagram campaigns','Full-funnel planning for awareness, lead generation, website conversions, catalog sales, and remarketing using suitable Meta campaign objectives.'),
            ('Lead generation ads','Instant forms or website conversion flows designed around lead quality, clear qualification and a fast follow-up process.'),
            ('Dynamic product ads','Catalog setup guidance and dynamic product ad structures for product discovery, remarketing and e-commerce sales.'),
            ('Audience strategy','Broad targeting, custom audiences, lookalikes where eligible, exclusions and remarketing based on data quality and current platform capability.'),
            ('Creative and copy testing','Creative hypotheses, hooks, primary text, headlines, formats and iterative testing to identify messaging that resonates.'),
            ('Meta Pixel and CAPI','Pixel installation reviews, event mapping, deduplication checks, and Conversions API integration when the website and server support it.'),
            ('Budget and performance management','Pacing, placement analysis, conversion-quality feedback, frequency monitoring and iterative changes tied to business goals.'),
            ('Clear monthly reporting','Performance recaps with spend, leads or purchase events, cost measures and next testing priorities based on available attribution data.')
        ],
        'tiers':[
            ('Starter',400,'/ month','For one market and a focused offer.',['Initial account review and setup','Up to 2 active campaigns','Core Pixel event verification','Monthly performance report'],False),
            ('Growth',850,'/ month','For businesses running recurring acquisition tests.',['Up to 5 active campaigns','Retargeting and audience testing','Creative test plan and review','Pixel/CAPI assessment','Twice-monthly optimization review'],True),
            ('Scale',1500,'+ / month','For multiple offers, markets, or larger budgets.',['Multi-campaign funnel strategy','Catalog and advanced audience support','Detailed tracking QA','Weekly optimization touchpoints','Custom reporting framework'],False)
        ],
        'faqs':[
            ('Is Meta advertising spend included?','No. Management fees are separate from the advertising budget charged by Meta.'),
            ('Do you provide ad designs?','Creative direction and copy testing are included as described per plan. High-volume design, video production and third-party assets may require a separate scope.'),
            ('Can you set up the Meta Pixel and CAPI?','We can configure or review supported integrations, given sufficient permissions and website or server access.'),
            ('Are lead or sales results guaranteed?','No. Results depend on the product, offer, budgets, competition, landing pages and tracking quality.')
        ],
        'steps':[('Audit','Review account access, events, offers, and funnel.'),('Launch','Build campaign structure, creative tests and tracking.'),('Learn','Collect performance and lead-quality feedback.'),('Scale','Adjust targeting, messaging, and spend responsibly.')]
    },
    'google-ads': {
        'file':'services/google-ads.html','name':'Google Ads','short':'Google Ads / PPC',
        'title':'Google Ads Management & PPC Services | Moavia SEO Pro',
        'description':'Google Search, Shopping, Display and YouTube Ads management, conversion tracking, keyword refinement and budget optimization. Transparent monthly packages.',
        'headline':'Capture high-intent demand with smarter Google Ads',
        'lead':'From search keyword strategy to measurement and bid optimization, we build manageable Google Ads accounts around conversions and efficient use of budget.',
        'icon':'⌕','deliverables':[
            ('Search Ads and PPC','Keyword research, match-type planning, search ad copy, landing page alignment and structured campaigns for high-intent searches.'),
            ('Google Display Network','Context and audience considerations, placements and creative testing for awareness or remarketing use cases with controls.'),
            ('Shopping and Merchant Center','Product feed health checks, listing optimization guidance, Merchant Center setup support and appropriate Shopping campaign structures.'),
            ('YouTube video advertising','Audience and creative recommendations, video campaign setup and performance analysis matched to defined campaign goals.'),
            ('Conversion tracking','Google Ads conversion actions, GA4 and Tag Manager coordination, enhanced conversions when appropriate, and event testing.'),
            ('Negative keyword management','Search term reviews, negative keyword lists and ongoing intent filtering to reduce irrelevant spend.'),
            ('Budget, bids and ROI analysis','Budget allocation, bidding review, cost per lead or acquisition trends and lead-quality feedback, mindful of attribution limitations.'),
            ('Reporting and improvement backlog','Plain-language results summaries, change logs and prioritized experiments for the next cycle.')
        ],
        'tiers':[
            ('Starter',450,'/ month','For a single core service or search market.',['Search campaign setup/review','Keyword and negative keyword lists','Basic conversion tracking QA','Monthly report'],False),
            ('Growth',900,'/ month','For several campaigns or product categories.',['Search + additional eligible campaign type','Up to 5 active campaigns','Conversion and query optimization','Twice-monthly performance review','Landing-page recommendations'],True),
            ('Scale',1600,'+ / month','For multi-market or higher-complexity accounts.',['Multi-channel Google Ads planning','Shopping/YouTube support as scoped','Advanced tracking coordination','Weekly optimization review','Custom attribution-focused reporting'],False)
        ],
        'faqs':[
            ('Does the monthly fee include ad spend?','No. You pay Google directly for ad spend, separately from the management fee.'),
            ('Do you work with existing Google Ads accounts?','Yes. We can audit, restructure and optimize existing accounts with appropriate access.'),
            ('Can you set up conversion tracking?','Yes, subject to website permissions, analytics consent requirements and supported integrations.'),
            ('Can Google Ads guarantee a return on investment?','No. Performance depends on commercial factors, campaign data, market competition, budgets and website conversion experience.')
        ],
        'steps':[('Diagnose','Review conversion definitions, search terms and offers.'),('Structure','Align campaigns, keywords, ads and landing pages.'),('Optimize','Refine bids, budgets, queries and tracking.'),('Report','Review conversion quality and next experiments.')]
    }
}

HOME_FAQ = [
    ('Which services does Moavia SEO Pro offer?','We offer SEO, modern website development, Meta Ads management, and Google Ads management. Services can be combined depending on your business goals.'),
    ('Do you work with clients outside Pakistan?','Yes. Moavia SEO Pro supports remote projects for clients internationally, with project scope, availability and communication arrangements agreed before work begins.'),
    ('Are the prices final?','Displayed prices are indicative starting rates in USD. Final proposals depend on project size, deliverables, timelines, and integrations. Ad spend, paid tools and third-party fees are separate.'),
    ('What happens after I submit an inquiry?','By default, the form opens WhatsApp with a prepared message. You must press Send in WhatsApp for the inquiry to be delivered. On Netlify, the site can be configured to submit to Netlify Forms.'),
]


def schema_for(page: str, config: dict | None, faqs: list) -> str:
    orgid = SITE_URL + '#organization'
    agencyid = SITE_URL + '#professional-service'
    url = SITE_URL + (config['file'] if config else ('' if page == 'home' else page + '.html'))
    graph = [
        {'@type':'Organization','@id':orgid,'name':'Moavia SEO Pro','url':SITE_URL,
         'logo':{'@type':'ImageObject','url':SITE_URL+'assets/images/moavia-logo-256.png'},
         'email':EMAIL,'sameAs':[LINKEDIN,FACEBOOK]},
        {'@type':['ProfessionalService','LocalBusiness'],'@id':agencyid,'name':'Moavia SEO Pro',
         'url':SITE_URL,'image':SITE_URL+'assets/images/moavia-logo-256.png','telephone':PHONE,
         'email':EMAIL,'priceRange':'$$',
         'areaServed':{'@type':'Place','name':'Worldwide'},
         'parentOrganization':{'@id':orgid},
         'hasOfferCatalog':{'@type':'OfferCatalog','name':'Digital Marketing and Web Services',
          'itemListElement':[{'@type':'OfferCatalog','name':v['name'],'url':SITE_URL+v['file']} for v in SERVICES.values()]}},
        {'@type':'WebPage','@id':url+'#webpage','url':url,
         'name':config['title'] if config else {'home':'Moavia SEO Pro | SEO, Websites & Ads','about':'About Moavia SEO Pro','contact':'Contact Moavia SEO Pro','privacy':'Privacy Policy | Moavia SEO Pro'}[page],
         'isPartOf':{'@id':SITE_URL+'#website'},'about':{'@id':agencyid}},
    ]
    graph.append({'@type':'WebSite','@id':SITE_URL+'#website','url':SITE_URL,'name':'Moavia SEO Pro','publisher':{'@id':orgid}})
    if page in ('about','contact'):
        graph.append({'@type':'ContactPoint','contactType':'customer service','telephone':PHONE,'email':EMAIL,'availableLanguage':['English','Urdu']})
    if config:
        graph += [
            {'@type':'Service','@id':url+'#service','name':config['name'],'serviceType':config['short'],
             'description':config['lead'],'provider':{'@id':agencyid},
             'areaServed':{'@type':'Place','name':'Worldwide'},
             'offers':[{'@type':'Offer','name':tier[0], 'priceCurrency':'USD','price':str(tier[1]),
                        'url':url} for tier in config['tiers']]},
            {'@type':'BreadcrumbList','itemListElement':[
                {'@type':'ListItem','position':1,'name':'Home','item':SITE_URL},
                {'@type':'ListItem','position':2,'name':config['name'],'item':url}]}
        ]
    if faqs:
        graph.append({'@type':'FAQPage','@id':url+'#faq','mainEntity':[
            {'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in faqs]})
    return json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False,indent=2).replace('</','<\\/')


def nav(depth: int, active: str) -> str:
    image = home_rel('assets/images/moavia-logo.webp',depth)
    def link(path: str,label: str,key: str):
        a = ' aria-current="page"' if active == key else ''
        return f'<a href="{esc(home_rel(path,depth))}"{a}>{esc(label)}</a>'
    return f'''<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="site-header">
  <div class="container nav-shell">
    <a class="brand" href="{esc(home_rel('index.html',depth))}" aria-label="Moavia SEO Pro home">
      <img src="{esc(image)}" alt="Moavia SEO Pro logo" width="53" height="53" decoding="async">
      <span class="brand-name">moavia<span>SEO PRO</span></span>
    </a>
    <nav class="nav-links" id="primary-navigation" data-nav-links aria-label="Primary navigation">
      {link('index.html','Home','home')}
      {link('services/seo.html','SEO','seo')}
      {link('services/web-development.html','Web Development','web-development')}
      {link('services/meta-ads.html','Meta Ads','meta-ads')}
      {link('services/google-ads.html','Google Ads','google-ads')}
      {link('about.html','About','about')}
      {link('contact.html','Contact','contact')}
      <a class="btn btn-primary nav-cta" href="{esc(home_rel('contact.html',depth))}">Get Free Consultation</a>
    </nav>
    <div class="nav-actions">
      <button class="icon-btn" type="button" data-theme-toggle title="Light theme" aria-label="Switch to light theme">☀</button>
      <a class="btn btn-primary" href="{esc(home_rel('contact.html',depth))}">Let's Talk</a>
      <button class="icon-btn menu-toggle" type="button" aria-label="Toggle menu" aria-controls="primary-navigation" aria-expanded="false" data-menu-toggle>☰</button>
    </div>
  </div>
</header>'''


def footer(depth: int) -> str:
    def li(href,label): return f'<li><a href="{esc(href)}">{esc(label)}</a></li>'
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand"><div class="brand-name">moavia<span>SEO PRO</span></div>
        <p>SEO, conversion-focused websites, and paid advertising managed with clarity and measurable priorities.</p>
        <div class="chip-row"><a class="chip" href="{esc(LINKEDIN)}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><a class="chip" href="{esc(FACEBOOK)}" target="_blank" rel="noopener noreferrer">Facebook ↗</a></div>
      </div>
      <div><h3>Explore</h3><ul>
        {li(home_rel('index.html',depth),'Home')}{li(home_rel('about.html',depth),'About Us')}{li(home_rel('contact.html',depth),'Contact')}
      </ul></div>
      <div><h3>Services</h3><ul>
        {''.join(li(home_rel(v['file'],depth),v['name']) for v in SERVICES.values())}
      </ul></div>
      <div><h3>Get in touch</h3><ul>
        {li('mailto:'+EMAIL,EMAIL)}{li('tel:'+PHONE,PHONE_DISPLAY)}
        {li(WA,'WhatsApp Business')}
      </ul><p class="small text-muted">Remote services for clients worldwide. All pricing shown in USD.</p></div>
    </div>
    <div class="footer-bottom"><span>© <span data-year>2026</span> Moavia SEO Pro. All rights reserved.</span>
      <span>Practical growth. Transparent work. <a href="{esc(home_rel('privacy.html',depth))}">Privacy policy</a></span></div>
  </div>
</footer>
<a class="floating-whatsapp" href="{WA}?text=Hello%20Moavia%20SEO%20Pro%2C%20I%27d%20like%20to%20discuss%20a%20project." target="_blank" rel="noopener noreferrer" aria-label="Contact Moavia SEO Pro via WhatsApp"><span aria-hidden="true">✆</span> WhatsApp</a>
<button type="button" class="chat-launcher" data-chat-launcher aria-controls="support-chat" aria-expanded="false" aria-label="Open support assistant">✦ <span>Ask us</span></button>
<section id="support-chat" class="chat-panel" data-chat-panel aria-label="Automated support assistant" hidden>
  <div class="chat-head"><div><strong>Moavia SEO Pro Support</strong><small>Instant automated answers · not a live agent</small></div><button type="button" class="chat-close" data-chat-close aria-label="Close assistant">✕</button></div>
  <div class="chat-messages" data-chat-messages role="log" aria-live="polite" aria-relevant="additions"><div class="bubble bot">Hello! I can explain our SEO, website, Meta Ads and Google Ads services, starting rates, and how to contact us.</div></div>
  <div class="chat-suggestions" data-chat-suggestions><button type="button">SEO pricing</button><button type="button">Web development</button><button type="button">Meta Ads</button><button type="button">Google Ads</button></div>
  <form class="chat-form" data-chat-form><label for="chat-question" class="sr-only">Ask a question</label><input id="chat-question" data-chat-input maxlength="400" placeholder="Ask about a service…" required><button type="submit">Send</button></form>
  <div class="chat-bottom"><a href="{WA}" target="_blank" rel="noopener noreferrer">Transfer to WhatsApp →</a><div class="text-muted">Scripted FAQs only. Do not share sensitive information.</div></div>
</section>'''


def shell(page: str,title: str,description: str,content: str,faqs: list|None=None,config:dict|None=None) -> str:
    depth = 1 if config else 0
    path = config['file'] if config else ('index.html' if page == 'home' else f'{page}.html')
    canonical = SITE_URL + ('' if page == 'home' else path)
    brand_img = SITE_URL+'assets/images/moavia-logo-256.png'
    social_title = title
    jsonld = schema_for(page,config,faqs or [])
    return f'''<!doctype html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#081320">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="canonical" href="{esc(canonical)}">
  <link rel="icon" type="image/png" href="{esc(home_rel('assets/images/favicon.png',depth))}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Moavia SEO Pro">
  <meta property="og:title" content="{esc(social_title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{esc(canonical)}">
  <meta property="og:image" content="{esc(brand_img)}">
  <meta property="og:image:alt" content="Moavia SEO Pro digital marketing logo">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(social_title)}">
  <meta name="twitter:description" content="{esc(description)}">
  <meta name="twitter:image" content="{esc(brand_img)}">
  <link rel="preload" href="{esc(home_rel('assets/css/styles.css',depth))}" as="style">
  <link rel="stylesheet" href="{esc(home_rel('assets/css/styles.css',depth))}">
  <!-- Structured data: edit business details only with verified information. -->
  <script type="application/ld+json">{jsonld}</script>
  <script src="{esc(home_rel('assets/js/main.js',depth))}" defer></script>
</head>
<body>
{nav(depth,page)}
<main id="main-content">
{content}
</main>
{footer(depth)}
</body>
</html>
'''


def faq_section(faqs: list) -> str:
    inner = '\n'.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in faqs)
    return f'''<section class="section section-muted" id="faq"><div class="container"><div class="section-head align-center" style="margin-inline:auto"><div class="eyebrow">Good to know</div><h2>Frequently asked questions</h2></div><div class="faq-list">{inner}</div></div></section>'''


def cta(depth: int=0) -> str:
    return f'''<section class="section"><div class="container"><div class="cta-banner"><div><div class="eyebrow">Start with clarity</div><h2>Ready to discuss your next growth project?</h2><p class="text-muted mb-0">Tell us what you want to achieve. We’ll review the scope and outline an appropriate next step.</p></div><div class="cta-row">{b(home_rel('contact.html',depth),'Request a Consultation')}{b(WA,'WhatsApp Us','btn-secondary',True)}</div></div></div></section>'''


def tiers_section(v: dict, depth: int=1) -> str:
    rows=[]
    for label,price,suffix,desc,items,featured in v['tiers']:
        featureclass = ' featured' if featured else ''
        featuretag = '<span class="tag">Most popular</span>' if featured else ''
        bullets=''.join(f'<li>{esc(x)}</li>' for x in items)
        rows.append(f'''<article class="price-card{featureclass}">{featuretag}<span class="price-label">{esc(label)}</span><h3>{esc(label)} plan</h3><p class="small text-muted">{esc(desc)}</p><div class="price">${price:,}<small> {esc(suffix)}</small></div><ul class="check-list">{bullets}</ul>{b(home_rel('contact.html',depth)+'?service='+esc(v['name']),'Discuss This Plan','btn-primary btn-block')}</article>''')
    return f'''<section class="section section-muted" id="pricing"><div class="container"><div class="section-head"><div class="eyebrow">Straightforward packages</div><h2>{esc(v['name'])} pricing</h2><p>Indicative starting rates in USD. Final pricing, schedules and deliverables are confirmed in a written scope.</p></div><div class="pricing-grid">{''.join(rows)}</div><p class="price-note">Packages are illustrative starting scopes, not binding quotes. Ad spend, paid tools, hosting, third-party fees, taxes, and exceptional requirements are not included unless agreed in writing. No results or rankings are guaranteed.</p></div></section>'''


def service_page(key: str, v: dict) -> str:
    cards = '\n'.join(f'<article class="card"><span class="service-icon" aria-hidden="true">{esc(str(i+1)).zfill(2)}</span><h3>{esc(title)}</h3><p>{esc(detail)}</p></article>' for i,(title,detail) in enumerate(v['deliverables']))
    steps='\n'.join(f'<article class="card"><span class="step-number">STEP 0{i+1}</span><h3>{esc(name)}</h3><p>{esc(text)}</p></article>' for i,(name,text) in enumerate(v['steps']))
    body=f'''<section class="page-hero"><div class="container"><nav aria-label="Breadcrumb" class="breadcrumb"><a href="../index.html">Home</a><span aria-hidden="true">/</span><span>{esc(v['name'])}</span></nav><div class="eyebrow">{esc(v['short'])} · Global service</div><h1>{esc(v['headline'])}</h1><p class="lead">{esc(v['lead'])}</p><div class="cta-row">{b('../contact.html','Request a Project Review')}{b(WA,'Chat on WhatsApp','btn-secondary',True)}</div></div></section>
<section class="section" id="solutions"><div class="container"><div class="section-head"><div class="eyebrow">Our capabilities</div><h2>What's included in our {esc(v['name'].lower())} work</h2><p>We tailor the following capabilities to the business model, available access and agreed package.</p></div><div class="grid grid-2">{cards}</div></div></section>
<section class="section section-muted"><div class="container"><div class="section-head"><div class="eyebrow">How delivery works</div><h2>A transparent four-step process</h2></div><div class="grid grid-4">{steps}</div></div></section>
{tiers_section(v)}{faq_section(v['faqs'])}{cta(1)}'''
    # Keep package title and description unique across URLs.
    return shell(key,v['title'],v['description'],body,v['faqs'],v)


def form_fields(form_id='contact-form',service_default='') -> str:
    return f'''<form id="{form_id}" name="{form_id}" method="POST" action="/" data-netlify="true" netlify-honeypot="bot-field" data-lead-form>
  <input type="hidden" name="form-name" value="{form_id}">
  <p class="sr-only"><label>Leave this blank: <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
  <div class="form-grid"><div class="form-field"><label for="{form_id}-name">Your name <span class="required">*</span></label><input id="{form_id}-name" name="name" autocomplete="name" maxlength="90" required placeholder="Full name"></div>
  <div class="form-field"><label for="{form_id}-email">Email address <span class="required">*</span></label><input id="{form_id}-email" type="email" name="email" autocomplete="email" maxlength="140" required placeholder="you@company.com"></div></div>
  <div class="form-grid"><div class="form-field"><label for="{form_id}-service">Service of interest</label><select id="{form_id}-service" name="service"><option value="Not specified">Select a service</option>{''.join(f'<option value="{esc(v["name"])}"'+(' selected' if service_default == v['name'] else '')+f'>{esc(v["name"])}</option>' for v in SERVICES.values())}</select></div>
  <div class="form-field"><label for="{form_id}-site">Website (optional)</label><input id="{form_id}-site" name="website" type="url" placeholder="https://example.com" maxlength="250"></div></div>
  <div class="form-field"><label for="{form_id}-message">Project details <span class="required">*</span></label><textarea id="{form_id}-message" name="message" maxlength="2500" minlength="10" required placeholder="Tell us about your goals, target audience and timeline..."></textarea></div>
  <label class="checkbox-row"><input type="checkbox" name="consent" value="yes" required><span>I agree to share these details with Moavia SEO Pro for a response to my inquiry. <span class="required">*</span></span></label>
  <button class="btn btn-primary" type="submit">Prepare My Inquiry →</button><div class="form-status" aria-live="polite" role="status" data-form-status></div>
  <p class="policy-note">By default this form opens WhatsApp with your details; it does not silently submit them. You must press Send in WhatsApp. Read the <a href="privacy.html">privacy policy</a>.</p>
</form>'''


def home_page() -> str:
    cards = '\n'.join(f'''<article class="card"><span class="service-icon" aria-hidden="true">{esc(v['icon'])}</span><h3>{esc(v['name'])}</h3><p>{esc(v['lead'])}</p><a class="card-link" href="{esc(v['file'])}">Explore {esc(v['name'])} →</a></article>''' for v in SERVICES.values())
    mini = '\n'.join(f'<tr><td><strong><a href="{esc(v["file"])}">{esc(v["name"])}</a></strong></td><td>From ${v["tiers"][0][1]:,} {esc(v["tiers"][0][2])}</td><td>{esc(v["tiers"][0][3])}</td></tr>' for v in SERVICES.values())
    stepcards=''.join(f'<article class="card"><span class="step-number">0{i+1} / 03</span><h3>{esc(title)}</h3><p>{esc(desc)}</p></article>' for i,(title,desc) in enumerate([
        ('Understand your goals','We start with commercial priorities, site or account access, and what success should mean.'),
        ('Build an actionable plan','You receive a clear scope covering deliverables, estimated fees, and a practical timeline.'),
        ('Execute and communicate','Work is tracked against agreed actions, with transparent reviews and relevant performance metrics.')]))
    body = f'''<section class="hero"><div class="container hero-grid"><div><div class="eyebrow">Moavia SEO Pro · Growth-focused digital services</div><h1>Turn your online presence into a <span class="text-accent">growth engine.</span></h1><p class="lead">SEO, modern website development, Meta Ads, and Google Ads for businesses that value measurable priorities, fast websites, and straightforward communication.</p><div class="cta-row">{b('contact.html','Get Free Audit Review')}{b(WA,'Chat on WhatsApp','btn-secondary',True)}</div><div class="proof"><span class="chip"><span class="chip-dot"></span> Search-first approach</span><span class="chip"><span class="chip-dot"></span> Transparent packages</span><span class="chip"><span class="chip-dot"></span> Global remote services</span></div></div>
  <div class="hero-visual" aria-label="Example growth strategy dashboard, illustrative values only"><div class="visual-top"><span class="mini-title">Digital growth framework</span><span class="status">● Plan → Execute → Learn</span></div>
  <div class="metric"><div class="metric-label"><span>Technical SEO readiness</span><span>Audit & improve</span></div><div class="bar-track"><div class="bar-fill" style="width:75%"></div></div></div>
  <div class="metric"><div class="metric-label"><span>Conversion experience</span><span>Test & refine</span></div><div class="bar-track"><div class="bar-fill" style="width:63%"></div></div></div>
  <div class="metric"><div class="metric-label"><span>Ad measurement</span><span>Track & report</span></div><div class="bar-track"><div class="bar-fill" style="width:87%"></div></div></div>
  <div class="metric-result"><div><strong>SEO</strong><span>Organic visibility</span></div><div><strong>WEB</strong><span>User experience</span></div><div><strong>ADS</strong><span>Paid acquisition</span></div></div><p class="hero-note">Illustrative design only; bars are not actual client performance results.</p></div></div></section>
<section class="section" id="services"><div class="container"><div class="section-head"><div class="eyebrow">What we do</div><h2>Four connected services. One clearer strategy.</h2><p>Build visibility, strengthen your website, and reach qualified audiences through well-scoped, measurable marketing work.</p></div><div class="grid grid-2">{cards}</div></div></section>
<section class="section section-muted"><div class="container"><div class="section-head"><div class="eyebrow">Our approach</div><h2>Thoughtful work, without the unnecessary complexity</h2></div><div class="grid grid-3">{stepcards}</div></div></section>
<section class="section"><div class="container"><div class="section-head"><div class="eyebrow">Simple scenario tool</div><h2>Explore potential conversion upside</h2><p>Adjust the inputs to model additional monthly revenue if your website improves its conversion rate. This is a mathematical scenario, not a forecast or promise.</p></div><div class="split"><div class="form-panel"><form data-roi-calculator><div class="form-grid"><div class="form-field"><label for="roi-visits">Monthly website visits</label><input id="roi-visits" name="visits" type="number" min="0" max="100000000" value="5000" required></div><div class="form-field"><label for="roi-rate">Current conversion rate (%)</label><input id="roi-rate" name="rate" type="number" min="0" max="100" step="0.1" value="1.8" required></div><div class="form-field"><label for="roi-order">Average order/lead value (USD)</label><input id="roi-order" name="order" type="number" min="0" max="100000000" step="1" value="80" required></div><div class="form-field"><label for="roi-lift">Relative conversion uplift (%)</label><input id="roi-lift" name="lift" type="number" min="0" max="10000" step="1" value="20" required></div></div></form><div class="roi-result"><span class="eyebrow">Illustrative additional monthly revenue</span><output data-roi-result aria-live="polite">$1,440</output><p>Monthly visits × current conversion rate × relative uplift × value. Excludes acquisition cost, margin and fees.</p></div></div>
  <div><div class="eyebrow">Request an initial review</div><h3>Talk through your growth opportunities</h3><p class="text-muted">Share your website and what you want to achieve. We can discuss a suitable first review and whether a full paid audit would be useful.</p><form id="roi-lead" name="roi-lead" method="POST" action="/" data-netlify="true" netlify-honeypot="bot-field" data-lead-form><input type="hidden" name="form-name" value="roi-lead"><input type="hidden" name="scenario" value=""><p class="sr-only"><label>Leave blank <input name="bot-field" autocomplete="off" tabindex="-1"></label></p><div class="form-field"><label for="roi-name">Your name <span class="required">*</span></label><input id="roi-name" name="name" autocomplete="name" placeholder="Full name" maxlength="90" required></div><div class="form-field"><label for="roi-email">Work email <span class="required">*</span></label><input id="roi-email" name="email" type="email" autocomplete="email" placeholder="you@company.com" maxlength="140" required></div><div class="form-field"><label for="roi-website">Your website (optional)</label><input id="roi-website" name="website" type="url" placeholder="https://example.com" maxlength="250"></div><label class="checkbox-row"><input type="checkbox" name="consent" value="yes" required><span>I agree to share this inquiry with Moavia SEO Pro.</span></label><button type="submit" class="btn btn-primary">Request Free Audit Review →</button><div class="form-status" data-form-status role="status" aria-live="polite"></div><p class="policy-note">Opens WhatsApp with your details and ROI scenario. Press Send to deliver. <a href="privacy.html">Privacy policy</a>.</p></form><p class="small text-muted mt-24">No performance outcome can be guaranteed. Actual results depend on your market, offer, website, and execution.</p></div></div></div></section>
<section class="section section-muted" id="pricing"><div class="container"><div class="section-head"><div class="eyebrow">Clear starting points</div><h2>Pricing overview</h2><p>Competitive starting rates for a defined scope. View each service page for its full three-tier package comparison.</p></div><div class="table-scroll"><table class="comparison-table"><thead><tr><th scope="col">Service</th><th scope="col">Starting price (USD)</th><th scope="col">Suitable for</th></tr></thead><tbody>{mini}</tbody></table></div><p class="price-note">Paid media budgets, software, domains, hosting and third-party expenses are excluded. Prices are indicative.</p></div></section>
<section class="section"><div class="container"><div class="section-head"><div class="eyebrow">Example workstreams</div><h2>What a focused engagement can look like</h2><p>These are illustrative project scenarios—not client case studies or verified results.</p></div><div class="grid grid-3"><article class="card"><h3>Local service visibility</h3><p>Map service-area keywords, fix crawlability issues, improve location-specific pages and establish a reporting baseline.</p><span class="chip">SEO · Example scenario</span></article><article class="card"><h3>Lead generation funnel</h3><p>Develop a focused landing page, verify conversion events, and test a campaign with lead-quality feedback.</p><span class="chip">Web + Ads · Example scenario</span></article><article class="card"><h3>E-commerce acquisition</h3><p>Review product feed health, category architecture, analytics events and acquisition campaign structure.</p><span class="chip">Store + PPC · Example scenario</span></article></div>
  <div class="feature-banner mt-32"><div class="eyebrow">Client testimonials</div><h3>Verified feedback, when available</h3><p class="text-muted mb-0">We only publish genuine client testimonials with permission. No unverified quotes or invented performance claims are displayed.</p></div></div></section>
{faq_section(HOME_FAQ)}{cta()}'''
    return shell('home','Moavia SEO Pro | SEO, Web Development & Paid Ads','Grow with Moavia SEO Pro: strategic SEO, fast website development, Meta Ads and Google Ads services. Transparent starting prices and direct consultation.',body,HOME_FAQ)


def about_page() -> str:
    values=[('Transparency','We define deliverables, costs and dependencies before work begins, and report against what was actually done.'),('Practical performance','We favor clean technology, relevant search intent and useful conversion data over empty buzzwords.'),('Responsible marketing','We avoid fake reviews, manufactured case studies, misleading ad claims and guaranteed rankings.'),('Long-term maintainability','Websites and campaigns should be understandable, accessible and easy to improve over time.')]
    cards=''.join(f'<article class="card"><h3>{esc(t)}</h3><p>{esc(p)}</p></article>' for t,p in values)
    body=f'''<section class="page-hero"><div class="container"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a> / About</nav><div class="eyebrow">Our company</div><h1>A focused digital partner for sustainable growth</h1><p class="lead">Moavia SEO Pro brings together SEO, web development and paid advertising to help businesses build a clearer path from online discovery to meaningful customer actions.</p></div></section>
<section class="section"><div class="container split"><div><div class="eyebrow">Our story</div><h2>Built around quality work and direct communication</h2><p>Moavia SEO Pro is a digital services brand focused on helping entrepreneurs, service providers and online stores strengthen their digital foundations. We approach each assignment with an agreed scope, practical priorities and readable reporting.</p><p>Our work spans technical search visibility, accessible websites, conversion tracking, and Facebook, Instagram and Google advertising. We do not claim outcomes that cannot be verified.</p></div><div class="feature-banner"><div class="eyebrow">Our mission</div><h3>Make digital growth work easier to understand—and easier to measure.</h3><p class="text-muted">We aim to combine sound technical implementation, clear campaigns and useful business reporting without unnecessary complexity.</p><ul class="check-list"><li>Search-ready website structure</li><li>Measurable marketing workstreams</li><li>Transparent packages and delivery</li></ul></div></div></section>
<section class="section section-muted"><div class="container"><div class="section-head"><div class="eyebrow">Our principles</div><h2>What guides every project</h2></div><div class="grid grid-2">{cards}</div></div></section>
<section class="section"><div class="container"><div class="section-head"><div class="eyebrow">Areas of expertise</div><h2>Connected skill areas</h2><p>Technical SEO and content structure, WordPress and lightweight frontends, measurement plans, Meta campaign management, and Google Ads execution.</p></div><div class="chip-row"><span class="chip">Technical SEO</span><span class="chip">WordPress</span><span class="chip">Performance optimization</span><span class="chip">Google Ads</span><span class="chip">Meta Ads</span><span class="chip">Conversion tracking</span></div></div></section>{cta()}'''
    return shell('about','About Moavia SEO Pro | Our Story & Mission','Learn about Moavia SEO Pro, a digital services brand focused on transparent SEO, website development, Meta Ads, Google Ads and measurable project delivery.',body)


def contact_page() -> str:
    body=f'''<section class="page-hero"><div class="container"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a> / Contact</nav><div class="eyebrow">Start a conversation</div><h1>Let's discuss your next digital project</h1><p class="lead">Tell us about your website, marketing goals and preferred service. You'll receive a clear next step after your message is sent.</p></div></section>
<section class="section"><div class="container split" style="align-items:start"><div class="form-panel"><h2 style="font-size:1.8rem">Project inquiry</h2><p class="text-muted">Complete the form and review your message before sending it on WhatsApp.</p>{form_fields()}</div><div><div class="eyebrow">Direct contact</div><h2>Reach Moavia SEO Pro</h2><p class="text-muted">Use whichever channel works best for you. All inquiries relate to our SEO, website and advertising services.</p><div class="grid"><div class="contact-method"><span class="service-icon" aria-hidden="true">@</span><div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></div><div class="contact-method"><span class="service-icon" aria-hidden="true">✆</span><div><strong>Phone / WhatsApp</strong><a href="tel:{PHONE}">{PHONE_DISPLAY}</a><p class="small mb-0"><a href="{WA}" target="_blank" rel="noopener noreferrer">Start WhatsApp chat →</a></p></div></div><div class="contact-method"><span class="service-icon" aria-hidden="true">↗</span><div><strong>Social profiles</strong><a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a> · <a href="{FACEBOOK}" target="_blank" rel="noopener noreferrer">Facebook</a></div></div></div>
  <div class="map-placeholder mt-32"><div><strong>Google Maps placeholder</strong><p class="small">No physical office address has been provided or verified. Add a genuine business location and embed map only after verification.</p></div></div></div></div></section>'''
    return shell('contact','Contact Moavia SEO Pro | SEO, Websites & Ads Inquiry','Contact Moavia SEO Pro about SEO, WordPress websites, Meta Ads and Google Ads. Email moaviahassan124@gmail.com or WhatsApp +92 323 4313869.',body)


def privacy_page() -> str:
    body=f'''<section class="page-hero"><div class="container"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a> / Privacy</nav><h1>Privacy policy</h1><p class="lead">How this static website handles messages and basic site preferences.</p></div></section>
<section class="section"><div class="container" style="max-width:850px"><h2>Information you choose to share</h2><p>Inquiry forms request your name, email, optional website, selected service and project details. The default form mode prepares a WhatsApp message on your device. The website itself does not receive or store that form data in this mode. The message is transmitted to Moavia SEO Pro only if you choose to press Send in WhatsApp, and WhatsApp's own terms and privacy practices apply.</p><h2>Netlify form hosting (optional)</h2><p>If the owner changes the site to Netlify Forms mode and deploys there, form submissions are handled by Netlify and made available to the site owner. Any hosting provider may process standard service logs as described in its policies.</p><h2>Support assistant</h2><p>Our support assistant uses locally scripted replies. Chat text is processed in your browser; we do not send it to an AI model or store it on this website. Only a separate click on the WhatsApp link moves you to an external service.</p><h2>Local storage and third-party links</h2><p>The website may save a dark/light theme preference in browser local storage. Social, email and WhatsApp links lead to third-party platforms which apply their own policies. The website includes no analytics or advertising trackers by default.</p><h2>Purpose and contact</h2><p>Information you send us is used to respond to your inquiry, scope a service and communicate about it. For privacy questions, contact <a class="text-accent" href="mailto:{EMAIL}">{EMAIL}</a>.</p><p class="small text-muted">Last updated: 20 October 2026. Replace or expand this policy when your actual hosting, analytics, consent, or form-processing arrangements change.</p></div></section>'''
    return shell('privacy','Privacy Policy | Moavia SEO Pro','Read the Moavia SEO Pro privacy policy covering inquiry forms, the scripted support assistant, external links and theme preferences.',body)


def main() -> None:
    pages={'index.html':home_page(),'about.html':about_page(),'contact.html':contact_page(),'privacy.html':privacy_page()}
    pages.update({v['file']:service_page(k,v) for k,v in SERVICES.items()})
    for pathname, content in pages.items():
        dest=ROOT/pathname
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(content, encoding='utf-8')
        print('wrote', pathname)
    urls=[SITE_URL,SITE_URL+'about.html',SITE_URL+'contact.html',
          *(SITE_URL+v['file'] for v in SERVICES.values()),SITE_URL+'privacy.html']
    site_map='''<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''+''.join('  <url><loc>'+esc(url)+'</loc></url>\n' for url in urls)+'</urlset>\n'
    (ROOT/'sitemap.xml').write_text(site_map,encoding='utf-8')
    (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+SITE_URL+'sitemap.xml\n',encoding='utf-8')
    print('wrote sitemap.xml and robots.txt')

if __name__ == '__main__':
    main()
