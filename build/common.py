"""Shared layout pieces for the Salient static site.
Run build/build.py to regenerate every page from these templates."""

ARROW = '<svg class="arrow" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11M11 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHEV = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
EXT = '<svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true" style="display:inline;vertical-align:-1px"><path d="M6 3H3v10h10v-3M9 3h4v4M13 3L7 9" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def icon(path):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{path}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

ICONS = {
    'retail': icon('M3 4h2l2.4 11h10.2L20 8H6.2M9 20a1 1 0 100-2 1 1 0 000 2zm8 0a1 1 0 100-2 1 1 0 000 2z'),
    'alc': icon('M7 3h10l-1 7a4 4 0 01-8 0L7 3zm5 11v6m-4 0h8'),
    'nonalc': icon('M10 2h4v3l2 3v12a2 2 0 01-2 2h-4a2 2 0 01-2-2V8l2-3V2zm-2 9h8'),
    'wholesale': icon('M2 7h11v9H2zM13 10h4l3 3v3h-7M6 19a2 2 0 100-4 2 2 0 000 4zm11 0a2 2 0 100-4 2 2 0 000 4z'),
    'cpg': icon('M12 3l8 4.5v9L12 21l-8-4.5v-9L12 3zm0 0v18M4 7.5l8 4.5 8-4.5'),
    'health': icon('M12 21s-8-4.5-8-11a4.5 4.5 0 018-2.8A4.5 4.5 0 0120 10c0 6.5-8 11-8 11zM9 11h6M12 8v6'),
    'guide': icon('M4 4h7a3 3 0 013 3v13a2 2 0 00-2-2H4V4zm16 0h-4a3 3 0 00-3 3'),
    'blog': icon('M4 20h4L19 9l-4-4L4 16v4zM13 7l4 4'),
    'events': icon('M4 6h16v14H4zM4 10h16M8 3v4m8-4v4'),
    'about': icon('M4 21V8l8-5 8 5v13M9 21v-6h6v6'),
    'careers': icon('M8 11a3 3 0 100-6 3 3 0 000 6zm8 1a2.5 2.5 0 100-5 2.5 2.5 0 000 5zM2 20a6 6 0 0112 0m1-3a5 5 0 017 3'),
}

INDUSTRIES = [
    ('retail-grocery-convenience.html', 'Retail, grocery and convenience', 'Pricing, promotion, category and store performance', 'retail'),
    ('alcoholic-beverage.html', 'Alcoholic beverage', 'Supplier and distributor economics', 'alc'),
    ('non-alcoholic-beverage.html', 'Non-alcoholic beverage', 'Brands, bottlers and routes aligned', 'nonalc'),
    ('wholesale-distributors.html', 'Wholesale distribution', 'Margin, inventory and service in one place', 'wholesale'),
    ('consumer-packaged-goods.html', 'Consumer packaged goods', 'From shipment to shelf', 'cpg'),
]

def mega_link(href, title, desc, key, external=False):
    ext = f' {EXT}' if external else ''
    target = ' rel="noopener"' if external else ''
    return f'''<a class="mega-link" href="{href}"{target}><span class="mega-icon">{ICONS[key]}</span><span><strong>{title}{ext}</strong><span>{desc}</span></span></a>'''

def header(current):
    ind_links = ''.join(mega_link(h, t, d, k) for h, t, d, k in INDUSTRIES)
    ind_links += mega_link('https://www.salienthealth.com', 'Healthcare', 'Visit Salient Health', 'health', external=True)
    def cur(group):
        return ' is-current' if current in group else ''
    ind_pages = {h for h, *_ in INDUSTRIES} | {'industries.html'}
    def aria(page):
        return ' aria-current="page"' if current == page else ''
    return f'''
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header" data-header>
  <div class="wrap header-inner">
    <a class="brand" href="index.html" aria-label="Salient home"><img src="assets/brand/salient-logo.svg" alt="Salient" width="148" height="41"></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-nav-toggle><span class="nav-toggle-bars" aria-hidden="true"></span><span class="visually-hidden">Menu</span></button>
    <nav class="nav" id="site-nav" aria-label="Main" data-nav>
      <ul class="nav-list">
        <li class="nav-item{cur(ind_pages)}">
          <button class="nav-trigger" type="button" aria-expanded="false" aria-controls="mega-industries" data-mega-trigger>Industries {CHEV}</button>
          <div class="mega" id="mega-industries">
            <div class="wrap mega-inner">
              <div class="mega-grid cols-3">{ind_links}</div>
              <a class="mega-feature" href="industries.html">
                <img src="assets/img/hero-industries.webp" alt="" loading="lazy">
                <small>Industries we serve</small>
                <strong>Performance works differently by industry. So should the solution.</strong>
                <span class="text-link">Compare industries {ARROW}</span>
              </a>
            </div>
          </div>
        </li>
        <li class="nav-item"><a class="nav-link" href="how-we-work.html"{aria('how-we-work.html')}>How we work</a></li>
        <li class="nav-item"><a class="nav-link" href="customers.html"{aria('customers.html')}>Customers</a></li>
        <li class="nav-item{cur({'commercial-performance-guide.html', 'blog.html', 'events.html'})}">
          <button class="nav-trigger" type="button" aria-expanded="false" aria-controls="mega-resources" data-mega-trigger>Resources {CHEV}</button>
          <div class="mega" id="mega-resources">
            <div class="wrap mega-inner">
              <div class="mega-grid cols-3">
                {mega_link('commercial-performance-guide.html', 'Commercial performance guide', 'Why commercial performance breaks down', 'guide')}
                {mega_link('blog.html', 'Blog', 'Insight and perspective for commercial leaders', 'blog')}
                {mega_link('events.html', 'Events', 'Meet the team at industry events', 'events')}
              </div>
              <a class="mega-feature" href="commercial-performance-guide.html">
                <img src="assets/img/hero-guide.webp" alt="" loading="lazy">
                <small>Free guide</small>
                <strong>By the time you see it, margin has already moved.</strong>
                <span class="text-link">Get the guide {ARROW}</span>
              </a>
            </div>
          </div>
        </li>
        <li class="nav-item{cur({'about.html', 'careers.html'})}">
          <button class="nav-trigger" type="button" aria-expanded="false" aria-controls="mega-about" data-mega-trigger>About {CHEV}</button>
          <div class="mega" id="mega-about">
            <div class="wrap mega-inner">
              <div class="mega-grid">
                {mega_link('about.html', 'About Salient', 'Who we are, what we believe and our history since 1986', 'about')}
                {mega_link('careers.html', 'Careers', 'Performance isn\u2019t just what we deliver. It\u2019s how we work.', 'careers')}
              </div>
              <a class="mega-feature" href="about.html">
                <img src="assets/img/hero-about.webp" alt="" loading="lazy">
                <small>Since 1986</small>
                <strong>This is what performance looks like in motion.</strong>
                <span class="text-link">Meet Salient {ARROW}</span>
              </a>
            </div>
          </div>
        </li>
      </ul>
      <div class="nav-cta"><a class="btn btn-primary" href="connect.html">Connect with us</a></div>
    </nav>
  </div>
</header>'''

def cta_final(title, text, button='See what Salient can do for you', href='connect.html'):
    return f'''
<section class="cta-final" aria-labelledby="cta-title">
  <div class="wrap cta-grid">
    <div class="reveal">
      <p class="kicker" style="color:var(--bright-green)">Let\u2019s move performance forward, together</p>
      <h2 class="h-section" id="cta-title">{title}</h2>
      <p class="lede" style="color:rgba(255,255,255,.86)">{text}</p>
      <div class="btn-row"><a class="btn btn-accent btn-lg" href="{href}">{button} {ARROW}</a></div>
    </div>
    <address class="cta-contact">
      <span>88 E. Tioga Avenue<br>Corning, NY 14830</span>
      <a href="tel:+16077394511">(607) 739-4511</a>
    </address>
  </div>
  <img class="element" src="assets/brand/el-steps-white.webp" alt="" width="140" height="140" loading="lazy">
</section>'''

def footer():
    inds = ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t, *_ in INDUSTRIES)
    return f'''
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <img src="assets/brand/salient-logo-white.svg" alt="Salient" width="140" height="39" loading="lazy">
      <p>Data-driven decisions keep performance in motion.</p>
    </div>
    <nav aria-label="Industries"><h2>Industries</h2><ul>{inds}<li><a href="https://www.salienthealth.com">Healthcare {EXT}</a></li></ul></nav>
    <nav aria-label="Company"><h2>Company</h2><ul><li><a href="about.html">About Salient</a></li><li><a href="how-we-work.html">How we work</a></li><li><a href="customers.html">Customers</a></li><li><a href="careers.html">Careers</a></li></ul></nav>
    <nav aria-label="Resources"><h2>Resources</h2><ul><li><a href="commercial-performance-guide.html">Commercial performance guide</a></li><li><a href="blog.html">Blog</a></li><li><a href="events.html">Events</a></li></ul></nav>
    <nav aria-label="Contact"><h2>Contact</h2><ul><li><a href="connect.html">Connect with us</a></li><li><a href="tel:+16077394511">(607) 739-4511</a></li><li><a href="https://www.linkedin.com/company/salient-management/">LinkedIn {EXT}</a></li><li><a href="https://x.com/SalientMgmtComp/">X {EXT}</a></li></ul></nav>
  </div>
  <div class="wrap footer-legal">
    <span>&copy; <span data-year>2026</span> Salient. All rights reserved. 88 E. Tioga Avenue, Corning, NY 14830</span>
    <ul><li><a href="https://www.salient.com/privacy-policy/">Privacy policy</a></li><li><a href="https://www.salient.com/terms-of-use/">Terms of use</a></li></ul>
  </div>
</footer>'''

def page(slug, title, description, body, cta=None):
    cta_html = cta_final(*cta) if cta else ''
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <link rel="icon" href="assets/brand/salient-bug.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
{header(slug)}
<main id="main">
{body}
{cta_html}
</main>
{footer()}
<script src="js/main.js" defer></script>
</body>
</html>
'''

def page_hero(title, soft='', lede='', kicker='', img='', crumbs=None, buttons='', jumps=None, video=None, poster=None):
    crumb_html = ''
    if crumbs:
        parts = ['<a href="index.html">Home</a>'] + [f'<a href="{h}">{t}</a>' if h else f'<span aria-current="page">{t}</span>' for h, t in crumbs]
        sep = '<span aria-hidden="true">/</span>'
        crumb_html = '<nav class="crumb" aria-label="Breadcrumb">' + sep.join(parts) + '</nav>'
    bg = ''
    if video:
        bg = f'<video class="bg" autoplay muted loop playsinline preload="metadata" poster="{poster or img}" data-inview aria-hidden="true"><source src="{video}" type="video/mp4"></video>'
    elif img:
        bg = f'<img class="bg" src="{img}" alt="" fetchpriority="high">'
    soft_html = f'<span class="soft">{soft}</span>' if soft else ''
    kicker_html = f'<p class="kicker">{kicker}</p>' if kicker else ''
    lede_html = f'<p class="lede">{lede}</p>' if lede else ''
    jump_html = ''
    if jumps:
        jump_html = '<nav class="jump-links" aria-label="On this page">' + ''.join(f'<a href="#{a}">{t}</a>' for a, t in jumps) + '</nav>'
    btn_html = f'<div class="btn-row">{buttons}</div>' if buttons else ''
    return f'''
<section class="page-hero on-dark">
  {bg}
  <div class="wrap">
    {crumb_html}
    {kicker_html}
    <h1>{title}{soft_html}</h1>
    {lede_html}
    {btn_html}
    {jump_html}
  </div>
</section>'''

def btn(text, href, kind='primary', arrow=True, lg=True):
    size = ' btn-lg' if lg else ''
    return f'<a class="btn btn-{kind}{size}" href="{href}">{text}{" " + ARROW if arrow else ""}</a>'

def cards(items, cols='', icons=True):
    """items: list of (title, text, icon_file_or_None)"""
    out = []
    for i, it in enumerate(items):
        title, text = it[0], it[1]
        ic = it[2] if len(it) > 2 and icons else None
        ic_html = f'<div class="card-icon"><img src="assets/brand/{ic}" alt=""></div>' if ic else ''
        out.append(f'<article class="card reveal">{ic_html}<h3>{title}</h3><p>{text}</p></article>')
    if not cols:
        cols = 'five' if len(items) == 5 else 'four' if len(items) % 4 == 0 and len(items) >= 4 else ''
    return f'<div class="card-grid {cols}">{"".join(out)}</div>'

def rows(items):
    return '<div class="rows">' + ''.join(f'<div class="reveal"><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + '</div>'

def ticks(items, two_col=False):
    cls = 'ticks two-col-list' if two_col else 'ticks'
    return f'<ul class="{cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'

def head(title, lede='', kicker='', soft='', link=None):
    k = f'<p class="kicker">{kicker}</p>' if kicker else ''
    s = f'<span class="soft">{soft}</span>' if soft else ''
    l = f'<p class="lede">{lede}</p>' if lede else ''
    lk = f'<a class="text-link" href="{link[0]}">{link[1]} {ARROW}</a>' if link else ''
    return f'<div class="section-head reveal"><div>{k}<h2 class="h-section">{title}{s}</h2>{l}</div>{lk}</div>'

LOGOS = [
    ('ccu-disc', 'Coca-Cola Bottling Company United'), ('coca-cola-canada', 'Coca-Cola Canada Bottling'),
    ('liberty-coca-cola', 'Liberty Coca-Cola Beverages'), ('pepsi-bottling-ventures', 'Pepsi Bottling Ventures'),
    ('keurig-dr-pepper', 'Keurig Dr Pepper'), ('goya', 'Goya Foods'), ('fareway', 'Fareway Meat & Grocery'),
    ('silver-eagle', 'Silver Eagle Distributors'), ('associated-foods', 'Associated Food Stores'),
    ('bimbo', 'Bimbo Bakeries USA'), ('unilever', 'Unilever'), ('carvel', 'Carvel'),
    ('7g-distributing', '7G Distributing'), ('heidelberg', 'Heidelberg Distributing'),
    ('house-of-la-rose', 'The House of La Rose'), ('holiday-market', 'Holiday Market'),
    ('mothers-market', 'Mother\u2019s Market & Kitchen'), ('crickler', 'Crickler Vending'),
    ('nys-doh', 'New York State Department of Health'), ('maceys', 'Macey\u2019s'),
]

def logo_grid(keys=None):
    items = [l for l in LOGOS if not keys or l[0] in keys]
    cells = []
    for key, alt in items:
        ext = 'svg' if key == 'fareway' else 'webp'
        cells.append(f'<li class="logo-cell"><img src="assets/logos/{key}.{ext}" alt="{alt}" loading="lazy"></li>')
    return f'<ul class="logo-grid reveal" aria-label="Partners">{"".join(cells)}</ul>'

def story_card(href, img, small, title, text, more='Read the story', chips=None, feature=False, cat=None, external=False):
    chip_html = ''
    if chips:
        chip_html = '<div class="metric-chips">' + ''.join(f'<span>{c}</span>' for c in chips) + '</div>'
    f = ' is-feature' if feature else ''
    c = f' data-cat="{cat}"' if cat else ''
    rel = ' rel="noopener"' if external else ''
    return f'''<a class="story-card{f} reveal" href="{href}"{c}{rel}>
  <div class="thumb"><img src="{img}" alt="" loading="lazy"></div>
  <div class="body"><small>{small}</small><h3>{title}</h3><p>{text}</p>{chip_html}<span class="more">{more} {ARROW.replace('class="arrow"', '')}</span></div>
</a>'''

def accordion(items):
    return '<div class="accordion">' + ''.join(
        f'<details class="reveal"><summary>{q}<span class="plus" aria-hidden="true"></span></summary><div class="answer">{a}</div></details>' for q, a in items) + '</div>'

QUOTE_MARK = '<svg class="quote-mark" viewBox="0 0 54 40" aria-hidden="true"><path fill="currentColor" d="M0 40V24C0 10 7 2 21 0l2 6c-7 2-11 6-11 13h10v21H0zm31 0V24c0-14 7-22 21-24l2 6c-7 2-11 6-11 13h10v21H31z"/></svg>'
