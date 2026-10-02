from common import *

PEXELS_VIDEO = 'https://videos.pexels.com/video-files/36455152/15458588_1920_1080_25fps.mp4'
PEXELS_POSTER = 'https://images.pexels.com/videos/36455152/analysis-analytics-bar-business-36455152.jpeg?auto=compress&cs=tinysrgb&w=1920'
VID_ALC = ''
VID_CPG = ''
QUOTE_PHOTO = 'assets/img/case-grocer.webp'

TABS = [
    ('retail', 'Retail, grocery and convenience', 'Your margin story isn\u2019t contained in one dashboard.',
     'Connect pricing, promotion, category, inventory, supplier and financial performance around the way your organization manages the business.',
     'retail-grocery-convenience.html', 'Explore retail performance', 'img', 'assets/img/ind-retail.webp'),
    ('wholesale', 'Wholesale and DSD distribution', 'Your operation doesn\u2019t run from a summary.',
     'Understand performance customer by customer, product by product, route by route and delivery by delivery. Connect sales, inventory, service, cost-to-serve and profitability so the people closest to the business can see what\u2019s driving results.',
     'wholesale-distributors.html', 'Explore wholesale and distribution performance', 'img', 'assets/img/ind-wholesale.webp'),
    ('nonalc', 'Non-alcoholic beverage', 'Every customer, route and market contributes differently.',
     'Understand those differences without losing sight of the larger business, from pricing and product mix to route efficiency and profitability.',
     'non-alcoholic-beverage.html', 'Explore non-alcoholic performance', 'img', 'assets/img/ind-nonalc.webp'),
    ('alc', 'Alcoholic beverage', 'Performance doesn\u2019t pour itself.',
     'Pricing, portfolio mix, promotions, inventory, route execution and cost-to-serve influence whether growth creates value or diminishes it.',
     'alcoholic-beverage.html', 'Explore alcoholic performance', 'img', 'assets/img/ind-alc.webp'),
    ('cpg', 'Consumer packaged goods', 'See what happens between shipment and shelf.',
     'Connect internal, distributor, retailer and market information to understand how pricing, promotion, execution and product mix shape growth and margin.',
     'consumer-packaged-goods.html', 'Explore consumer goods performance', 'img', 'assets/img/ind-cpg.webp'),
    ('health', 'Healthcare', 'Build around the decisions that define healthcare performance.',
     'Bring clinical, operating and financial information together around the measures, responsibilities and priorities that matter to your organization.',
     '#', 'Explore Fieldline Health', 'img', 'assets/img/hero-connect.webp'),
]

def tabs_html():
    tab_btns, panels = [], []
    for i, (key, name, h, p, href, link, kind, src) in enumerate(TABS):
        sel = 'true' if i == 0 else 'false'
        tab_btns.append(f'<button class="tab" role="tab" id="tab-{key}" aria-controls="panel-{key}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">{name} {ARROW}</button>')
        if kind == 'video':
            poster = {'alc': 'assets/img/hero-alc.webp', 'cpg': 'assets/img/hero-cpg.webp'}[key]
            media = f'<video muted loop playsinline preload="none" poster="{poster}" aria-hidden="true"><source src="{src}" type="video/mp4"></video>'
        else:
            media = f'<img src="{src}" alt="" loading="lazy">'
        ext = f' {EXT}' if href.startswith('http') else ''
        panels.append(f'''<div class="tab-panel" role="tabpanel" id="panel-{key}" aria-labelledby="tab-{key}"{'' if i == 0 else ' hidden'}>
  <div class="tab-media">{media}</div>
  <div class="tab-copy"><small>{name}</small><h3>{h}</h3><p>{p}</p><a class="text-link" href="{href}">{link}{ext} {ARROW}</a></div>
</div>''')
    return f'''<div class="tabs" data-tabs>
  <div class="tab-list" role="tablist" aria-label="Industries">{"".join(tab_btns)}</div>
  <div>{"".join(panels)}</div>
</div>'''

def demo_html(step_items):
    steps = ''.join(f'''<li><button type="button" class="step" data-step="{i}"{' aria-current="step"' if i == 0 else ''}>
      <span class="step-num">{i + 1}</span><span class="step-text"><strong>{t}</strong><span>{d}</span></span></button></li>''' for i, (t, d) in enumerate(step_items))
    return steps, '''<div class="demo" data-demo>
  <div class="demo-bar"><nav class="crumbs" aria-label="Drill path" data-crumbs></nav><span class="demo-tag">Illustrative data</span></div>
  <div class="demo-head"><h3 class="demo-title" data-demo-title>Gross margin by region</h3><p class="demo-sub" data-demo-sub></p></div>
  <div class="demo-body" data-demo-body></div>
  <p class="demo-prompt" data-demo-prompt aria-live="polite"></p>
</div>'''

STEPS = [
    ('Start where it matters', 'Begin with the measures, outcomes and responsibilities relevant to the performance you influence.'),
    ('Follow the question', 'Move beyond the initial result and drill deeper into the detail behind it, across the dimensions and relationships in your business.'),
    ('Understand what\u2019s driving it', 'Connect detailed activity back to the broader business context to uncover the factors contributing to performance.'),
    ('Apply what you know', 'Bring your own business knowledge and experience to what the data reveals, and decide what happens next.'),
]

BLOG = [
    ('#', '', 'Data integration isn\u2019t the same as decision infrastructure', 'Most retail, wholesale, distribution and CPG organizations have tried to solve performance with integration alone.'),
    ('#', '', 'Do your KPIs create alignment or competing priorities?', 'Most organizations have no shortage of key performance indicators. Fewer have KPIs that pull in the same direction.'),
    ('#', '', '7 places decision friction enters the feedback cycle', 'Decision friction accumulates at different points in the performance feedback cycle.'),
]

def home():
    steps, demo = demo_html(STEPS)
    blog_cards = ''.join(story_card(h, i, 'Thought leadership', t, d, 'Read the article', external=True) for h, i, t, d in BLOG)
    body = f'''
<section class="hero-video on-dark" aria-labelledby="hero-title">
  <video data-hero-video autoplay muted loop playsinline preload="auto" poster="{PEXELS_POSTER}" aria-hidden="true">
    <source src="assets/video/hero.mp4" type="video/mp4">
    <source src="{PEXELS_VIDEO}" type="video/mp4">
  </video>
  <div class="wrap hero-inner">
    <h1 class="hero-title" id="hero-title"><span>Every result</span><span>has a reason.</span><span class="soft">We make sure you find it.</span></h1>
    <p class="hero-sub">Your business is complex. Getting to the root of performance shouldn\u2019t be. Fieldline helps complex organizations define what drives performance, put ownership closer to where outcomes can be influenced and create the visibility and feedback people need to improve.</p>
    <div class="btn-row">{btn('See what Fieldline can do for you', 'connect.html', 'accent')}{btn('Follow the question', '#follow', 'ghost', arrow=False)}</div>
    <div class="hero-foot">
      <div class="hero-proof">
        <div><b>Since 1991</b><span>Performance and industry expertise</span></div>
        <div><b>Five industries</b><span>Plus healthcare through Fieldline Health</span></div>
        <div><b>Billions of transactions</b><span>Queried at the speed of the question</span></div>
      </div>
      <div style="display:flex;align-items:center;gap:1rem">
        <span class="video-credit">Video: Jakub Zerdzicki on <a href="https://www.pexels.com/video/tablet-analysis-of-financial-data-36455152/">Pexels</a></span>
        <button class="icon-btn video-toggle" type="button" aria-pressed="false" data-video-toggle>
          <svg class="i-pause" viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>
          <svg class="i-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l11 7-11 7z"/></svg>
          <span class="visually-hidden">Pause background video</span>
        </button>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="people-title">
  <div class="wrap split">
    <div class="reveal">
      <p class="kicker">Purpose-built starts with people</p>
      <h2 class="h-section" id="people-title">Performance visibility belongs closer to the people who can change it.</h2>
      <div class="prose mt-2">
        <p>The people closest to the work often understand the context behind performance in a way no centralized report ever could. But experience alone isn\u2019t enough. To improve outcomes, they need clear measures, access to the detail behind the result and feedback that shows whether their decisions are moving performance in the right direction.</p>
        <p>Leadership gains transparency. Your people gain the context to investigate, act and understand the impact of what happens next.</p>
      </div>
    </div>
    <div class="pairing reveal">
      <div class="yours"><small>You bring</small><ul><li>Your knowledge.</li><li>Your performance.</li></ul></div>
      <div class="ours"><small>We bring</small><ul><li>Our expertise.</li><li>Our technology.</li></ul></div>
      <div class="pairing-foot">Built around your business.</div>
    </div>
  </div>
</section>

<section class="section-tight" aria-labelledby="logos-title">
  <div class="wrap">
    {head('Trusted by industry leaders', kicker='Our partners', link=('customers.html', 'See customer stories')).replace('<h2 class="h-section">', '<h2 class="h-section" id="logos-title" style="font-size:var(--fs-2xl)">')}
    {logo_grid()}
  </div>
</section>

<section class="section bg-surface" aria-labelledby="ind-title">
  <div class="wrap">
    <div class="section-head reveal"><div>
      <p class="kicker">Experience where it matters</p>
      <h2 class="h-section" id="ind-title">Performance works differently by industry.<span class="soft">So should the solution.</span></h2>
      <p class="lede">Fieldline brings decades of industry experience together with proprietary technology and performance expertise. We start with the realities of your operating environment, not ask you to translate them into a generic application or predetermined model.</p>
    </div></div>
    {tabs_html()}
  </div>
</section>

<section class="section bg-navy on-dark" id="follow" aria-labelledby="follow-title">
  <div class="wrap investigate-grid">
    <div class="reveal">
      <p class="kicker">Designed to go further</p>
      <h2 class="h-section" id="follow-title">What happened is only the beginning.<span class="soft">Understand what drives performance.</span></h2>
      <p class="lede">Traditional analytics and BI environments limit business users to the measures, views and interactions someone anticipated in advance. Fieldline\u2019s proprietary technology is designed for what happens after the first answer. Try it with illustrative numbers from a beverage distributor.</p>
      <ol class="steps">{steps}</ol>
    </div>
    {demo}
  </div>
</section>

<section class="section" aria-labelledby="built-title">
  <div class="wrap">
    {head('We didn\u2019t build technology to report on performance.', 'Fieldline\u2019s proprietary performance technology grew from decades of work helping complex organizations define value, distribute responsibility and give people the visibility and feedback they need to improve outcomes. That experience shaped the technology itself.', 'Built differently for a reason', 'We built it to help improve it.').replace('<h2 class="h-section">', '<h2 class="h-section" id="built-title">')}
    {cards([
        ('Integrated performance data', 'Fieldline connects, cleans and transforms data from across your organization into a governed foundation designed to measure performance consistently and in detail.', 'el-sws-blue.webp'),
        ('Business context and rules built into the data', 'Measures, definitions, hierarchies, relationships and business rules give the data meaning beyond the systems where it originated, including advanced allocations so measures such as margin reflect how value is actually created.', 'el-sws-seagreen.webp'),
        ('Proprietary technology built for investigation', 'Business users can move from summarized performance into detailed activity, change perspectives and follow questions without requiring every path to be predefined.', 'el-steps-blue.webp'),
        ('AI built into the performance environment', 'Integrated AI helps users navigate, analyze, interpret change and identify where to investigate next. It works within your measures, relationships and business rules, so it has the context to support more relevant analysis.', 'el-asterisk-seablue.webp'),
        ('Expertise that makes the technology specific to you', 'Fieldline works with your organization to define measures, structure business logic, build allocation rules and shape the performance environment around the outcomes you\u2019re aiming to improve.', 'el-tile-seagreen.webp'),
    ])}
    <p class="mt-3 reveal" style="font-size:var(--fs-xl);font-weight:700;letter-spacing:-0.02em;color:var(--brand-blue)">Technology built for performance. <span style="font-weight:300">Expertise that makes it yours.</span></p>
  </div>
</section>

<section class="section bg-surface" aria-labelledby="work-title">
  <div class="wrap">
    {head('Performance ownership belongs at every level of the business.', 'We don\u2019t layer another performance process on top of your organization. We start with the improvements you\u2019re looking to make, the way your business operates and what your people need to understand.', 'Built into the way you work', link=('how-we-work.html', 'See how we work')).replace('<h2 class="h-section">', '<h2 class="h-section" id="work-title">')}
    <div class="timeline">
      <div class="phase reveal"><h3>Start with what you want to improve</h3><p>We begin with your priorities, your operating environment and the decisions your people need to make, not a predetermined model.</p></div>
      <div class="phase reveal"><h3>Bring the pieces together</h3><p>Data, business rules, technology and expertise come together around your measures. Built to adapt. Designed to deliver.</p></div>
      <div class="phase reveal"><h3>Change with you</h3><p>New priorities emerge, markets change and data sources expand. We keep incorporating new data, refining measures and extending visibility, so the environment never has to be rebuilt.</p></div>
    </div>
    <div class="band mt-3 reveal">
      <h2>The goal isn\u2019t another finished application.</h2>
      <p>It\u2019s a performance environment that continues to earn its place in your business.</p>
      <img class="element" src="assets/brand/el-steps-white.webp" alt="">
    </div>
  </div>
</section>

<section class="section" aria-labelledby="proof-title">
  <div class="wrap">
    <p class="kicker reveal">Real organizations. Their way of thinking.</p>
    <h2 class="visually-hidden" id="proof-title">Customer stories</h2>
    <figure class="quote-block reveal">
      <div>
        <blockquote>{QUOTE_MARK}<p>Not only does the solution provide information to make better decisions, the Fieldline team understand the questions we are asking and why answers to those questions matter to our business.</p></blockquote>
        <figcaption><img src="assets/logos/northgate-market.svg" alt="Northgate Market" width="150" height="33"><span><strong>Jordan Ellis</strong><small>Northgate Market</small></span></figcaption>
      </div>
      <div class="quote-photo"><img src="{QUOTE_PHOTO}" alt="Jordan Ellis of Northgate Market" loading="lazy" onerror="this.src='assets/img/case-grocer.webp'"></div>
    </figure>
    <div class="story-grid mt-3">
      {story_card('customers.html#lakeside-pharmacy', 'assets/img/case-pharmacy.webp', 'Retail', 'Lakeside Pharmacy', 'A regional retailer with more than 75 stores moved from waiting days on IT reports to answering store questions quickly.', chips=['Faster store-level response', 'Better planogram decisions'])}
      {story_card('customers.html#pinecrest-grocers', 'assets/img/case-grocer.webp', 'Grocery', 'Pinecrest Grocers', 'Nine stores went from week-long manual analysis to pulling sales information in minutes.', chips=['Minutes, not days', 'Clear ownership'])}
      {story_card('customers.html#bluebird-creamery', 'assets/img/case-creamery.webp', 'Consumer packaged goods', 'Bluebird Creamery', 'A practical, flexible view of store-level performance that separates true demand issues from execution gaps.', chips=['Average per outlet', 'Region to route'])}
    </div>
  </div>
</section>

<section class="section bg-surface" aria-labelledby="res-title">
  <div class="wrap">
    <a class="story-card is-feature reveal" href="commercial-performance-guide.html">
      <div class="thumb"><img src="assets/img/hero-guide.webp" alt="" loading="lazy"></div>
      <div class="body"><small>Free guide for commercial, sales and finance leaders</small><h3 id="res-title">By the time you see it, margin has already moved.</h3><p>Why Commercial Performance Breaks Down covers the six-step rapid performance feedback cycle, where decision friction appears and a practical self-assessment.</p><span class="more">Get the guide {ARROW.replace('class="arrow"', '')}</span></div>
    </a>
    <div class="section-head reveal mt-3" style="margin-bottom:2rem"><div><h2 class="h-section" style="font-size:var(--fs-2xl)">Insight and perspective</h2></div><a class="text-link" href="blog.html">View all articles {ARROW}</a></div>
    <div class="story-grid">{blog_cards}</div>
  </div>
</section>
'''
    return page('index.html', 'Fieldline | Every result has a reason. We make sure you find it.',
                'Fieldline helps complex organizations define what drives performance, put ownership closer to where outcomes can be influenced and create the visibility and feedback people need to improve.',
                body, ('Ready for a better way to manage business performance?',
                       'Bring your people, performance priorities and data together with Fieldline\u2019s expertise, proven methodology and proprietary technology to create a performance solution built around the way value is created across your business.'))
