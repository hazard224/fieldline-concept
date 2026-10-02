from common import *
from pages_industries import section, img_fallback, video_card
from pages_home import QUOTE_PHOTO

S = '#'
U = ''

# ---------------------------------------------------------------- How we work
def how():
    body = page_hero('There\u2019s a better way to manage business performance.', kicker='How we work',
        lede='We combine four decades of performance and industry expertise with proprietary technology to build solutions around your organization, your data and the way value is created across your business.',
        img='assets/img/hero-how.webp', crumbs=[(None, 'How we work')],
        jumps=[('what-we-do', 'What we do'), ('foundation', 'The foundation'), ('evolve', 'Built to change'), ('faq', 'Questions')])
    body += section(head('What working with Fieldline looks like.', 'We\u2019re not here to dictate decisions or replace key roles. We combine human expertise with advanced data technology to support distributed decision-making without losing alignment.', 'What we do') + cards([
        ('Align performance to purpose', 'We work with leaders to define what success looks like, where performance matters most and how responsibility should be distributed to drive outcomes.', 'el-sws-blue.webp'),
        ('Create an AI-ready data foundation', 'Fieldline integrates, organizes, normalizes and validates data across systems, teams and partners so performance can be measured consistently and trusted.', 'el-sws-seagreen.webp'),
        ('Make data meaningful to the business', 'We don\u2019t stop at moving data from one place to another. We connect it to value, responsibility and action so teams understand what it means.', 'el-steps-blue.webp'),
        ('Enable decision-making at every level', 'We put decision-ready information into the hands of the people closest to the work while maintaining visibility and accountability across the enterprise.', 'el-asterisk-seablue.webp'),
        ('Support investigation, not just reporting', 'We design for exploration, context and root cause so teams understand why performance changed and what to do next.', 'el-tile-seagreen.webp'),
        ('Connect performance intelligence to the AI ecosystem', 'Validated performance data, business context and interactive exploration become accessible to the people, systems and AI tools that need them.', 'el-sws-blue.webp'),
        ('Partner beyond implementation', 'We stay engaged as performance evolves, helping organizations adapt, expand and keep improving as priorities and conditions change.', 'el-sws-seagreen.webp'),
        ('Sustain accountability over time', 'Shared measures, transparent feedback loops and systems that reinforce ownership long after implementation.', 'el-steps-blue.webp'),
    ]), id='what-we-do')
    body += section(f'''<div class="split top">
      <div class="reveal"><p class="kicker">Built differently for a reason</p><h2 class="h-section">Purpose-built starts with a proven foundation.</h2><p class="lede">That experience shaped the technology itself, from how data is integrated and structured to how business users investigate performance, apply business rules and understand the impact of what happens next.</p><div class="btn-row">{btn('Try the drill-down demo', 'index.html#follow', 'accent')}</div></div>
      <div>{rows([
        ('Integrated performance data', 'Fieldline connects, cleans and transforms data from across your organization into a governed foundation designed to measure performance consistently and in detail.'),
        ('Business context and rules built into the data', 'Measures, definitions, hierarchies, relationships and business rules give the data meaning beyond the systems where it originated, including advanced allocations.'),
        ('Proprietary technology built for investigation', 'Move from summarized performance into detailed activity, change perspectives and follow questions without requiring every path to be predefined.'),
        ('AI built into the performance environment', 'Integrated AI helps users navigate, analyze, interpret change and identify where to investigate next, with the context of your measures and rules.'),
        ('Expertise that makes the technology specific to you', 'We define measures, structure business logic, build allocation rules and shape the environment around the outcomes you\u2019re aiming to improve.'),
      ])}</div></div>''', 'bg-navy on-dark', id='foundation')
    body += section(f'''<div class="split">
      <div class="reveal"><p class="kicker">Built to change with you</p><h2 class="h-section">Your business will change.<span class="soft">Your performance environment should change with it.</span></h2>
      <div class="prose mt-2"><p>New priorities emerge, markets change, organizations restructure and data sources expand. The measures that matter today may not tell the full story tomorrow.</p><p>A Fieldline solution is designed to evolve with those changes. We continuously improve based on the needs of the organization with new data, refined measures and business rules, visibility into new areas of the organization and new capabilities.</p><p>Because Fieldline combines proprietary technology with ongoing performance and industry expertise, the environment doesn\u2019t have to be rebuilt every time the business moves forward.</p></div></div>
      <div class="timeline reveal" style="grid-template-columns:1fr">
        <div class="phase"><h3>Start with what you want to improve</h3><p>Your priorities, your operating environment and the decisions your people need to make.</p></div>
        <div class="phase"><h3>Bring the pieces together</h3><p>Data, business rules, technology and expertise around your measures. Built to adapt. Designed to deliver.</p></div>
        <div class="phase"><h3>Keep earning its place</h3><p>New data, refined measures and new capabilities as your business moves forward.</p></div>
      </div></div>''', 'bg-surface', id='evolve')
    body += section(head('Questions leaders ask us', kicker='Questions') + accordion([
        ('Do we have to fit our business into your model?', '<p>No. We start with the realities of your operating environment instead of asking you to translate them into a generic application or predetermined model. Measures, hierarchies, business rules and allocations are built around the way your organization creates value.</p>'),
        ('What kinds of data can Fieldline bring together?', '<p>It depends on your business, but commonly shipments, depletions, sales, inventory, pricing, promotions, financial costs, labor, delivery and cost-to-serve, retail scans and syndicated market data. Fieldline connects, cleans and validates it into one governed foundation.</p>'),
        ('Who uses Fieldline day to day?', '<p>The people responsible for outcomes: category and merchandising teams, store and route operations, sales, finance, marketing and leadership. Each sees what\u2019s relevant to their role while working from a shared understanding of performance.</p>'),
        ('How does AI fit in?', '<p>Integrated AI helps users navigate, analyze, interpret change and find where to investigate next. Because it works inside an environment structured around your measures and business rules, it has the context to support relevant analysis. Fieldline also helps make validated performance data available to the broader AI tools your organization uses.</p>'),
        ('What happens after implementation?', '<p>We stay engaged. As priorities and conditions change, we incorporate new data, refine measures and business rules, extend visibility to new areas and introduce new capabilities.</p>'),
        ('Where do we start?', '<p>Whether you\u2019ve defined goals or have early questions, <a class="text-link" href="connect.html">start here</a>. We\u2019ll guide the path forward with you.</p>'),
    ]), id='faq')
    return page('how-we-work.html', 'How we work | Fieldline', 'Fieldline combines four decades of performance and industry expertise with proprietary technology built around your organization and data.', body,
        ('Every organization has room to improve how performance moves.', 'Let\u2019s explore what this means for your business.', 'Connect now'))

# ---------------------------------------------------------------- Customers
CASES = [
    ('lakeside-pharmacy', 'assets/img/case-pharmacy.webp', 'Retail', 'Lakeside Pharmacy',
     'A privately owned regional retailer with more than 75 stores across Northeast Ohio, operating as both a full-service pharmacy and a neighborhood department store with more than 40,000 items.',
     'Store managers, buyers and category leaders relied on IT to run reports. Simple questions often took days to answer, making it hard to compare stores, evaluate planograms, find out-of-stocks and negotiate confidently with vendors.',
     ['Faster responses to store-level issues', 'Better planogram and space decisions', 'Stronger negotiating leverage with vendors', 'More consistent margin management across stores'],
     S + 'case-study-discount-drug-mart/', None),
    ('pinecrest-grocers', 'assets/img/case-grocer.webp', 'Grocery', 'Pinecrest Grocers',
     'A specialty organic grocery and foodservice retailer built on quality.',
     'Teams logged into individual POS systems store by store, compiled spreadsheets by hand and waited days, sometimes a full week, for analysis.',
     ['Faster access to trustworthy information', 'Less manual work and fewer handoffs', 'Better questions, asked earlier', 'Clear ownership at every level'],
     S + 'case-study-mothers-market/', ('With all nine stores together, I can pull sales information in five minutes.', 'Vanessa Shelton', 'Foodservice Coordinator, Pinecrest Grocers')),
    ('bluebird-creamery', 'assets/img/case-creamery.webp', 'Consumer packaged goods', 'Bluebird Creamery',
     'The category leader in uniquely shaped ice cream cakes, with hundreds of franchised and foodservice locations and thousands of supermarket outlets.',
     'Timing, freshness and execution matter as much as demand. Bluebird Creamery needed a practical, flexible view of store-level performance that reflected how the business actually runs.',
     ['Performance by region, market, chain, route and product', 'Average per outlet as a relative measure of store health', 'True demand issues separated from execution gaps'],
     S + 'case-study-bluebird-creamery/', ('Average Per Outlet became an excellent way for us to tell, on a relative basis, how well a store is doing.', 'Gottlieb', 'Bluebird Creamery')),
    ('summit-food-coop', 'assets/img/hero-retail.webp', 'Wholesale and retail', 'Summit Food Cooperative',
     'SFC selected Fieldline to build a data sharing platform for vendor partners, its corporate team and, eventually, its independent grocers.',
     'SFC dedicated more resources to shopper data to drive decisions, engage shoppers and improve store profitability across both the wholesale and retail sides of the business.',
     ['Co-op, supplier and retail analytics', 'Views limited to the right users', 'Fast processing at high transaction volumes'],
     S + 'sfc-chooses-fieldline/', None),
]

def customers():
    body = page_hero('Purpose-built performance changes what people can see, understand and act on.', kicker='Customers',
        lede='Real organizations. Their way of thinking. See how retailers, distributors, bottlers and brands use Fieldline to move performance forward.',
        img='assets/img/hero-customers.webp', crumbs=[(None, 'Customers')],
        jumps=[(c[0], c[3]) for c in CASES])
    body += section(f'''<figure class="quote-block reveal">
      <div><blockquote>{QUOTE_MARK}<p>Not only does the solution provide information to make better decisions, the Fieldline team understand the questions we are asking and why answers to those questions matter to our business.</p></blockquote>
      <figcaption><img src="assets/logos/northgate-market.svg" alt="Northgate Market" width="150" height="33"><span><strong>Jordan Ellis</strong><small>Northgate Market</small></span></figcaption></div>
      <div class="quote-photo">{img_fallback(QUOTE_PHOTO, 'assets/img/case-grocer.webp', 'Jordan Ellis of Northgate Market')}</div></figure>''')
    for i, (key, img, cat, name, intro, challenge, outcomes, url, quote) in enumerate(CASES):
        q = ''
        if quote:
            q = f'<blockquote class="mt-2" style="margin-inline:0;padding-left:1.25rem;border-left:3px solid var(--sea-green)"><p style="font-size:1.15rem;font-weight:600;line-height:1.45">\u201c{quote[0]}\u201d</p><footer style="margin-top:.5rem;color:var(--muted);font-size:.95rem"><strong style="color:var(--darkness)">{quote[1]}</strong>, {quote[2]}</footer></blockquote>'
        order = ' style="order:-1"' if i % 2 else ''
        body += section(f'''<div class="split top">
          <div class="reveal"><p class="kicker">{cat}</p><h2 class="h-section" style="font-size:var(--fs-2xl)">{name}</h2><p class="lede">{intro}</p>
            <h3 class="mt-2" style="font-size:1.1rem">The challenge</h3><p style="color:var(--muted);margin-top:.4rem">{challenge}</p>{q}</div>
          <div class="reveal"{order}><div class="media-tile"><img src="{img}" alt="" loading="lazy"></div>
            <div class="card mt-1"><h3>The outcome</h3>{ticks(outcomes)}<a class="text-link mt-1" href="{url}" rel="noopener">Read the full story</a></div></div>
        </div>''', 'bg-surface' if i % 2 == 0 else '', id=key)
    body += section(video_card('', 'Oakmont Foods: transformation that moves performance forward', 'See how Oakmont Foods strengthens alignment, accelerates action and improves performance with Fieldline as a strategic partner.', S + 'consumer-packaged-goods-cpg/#CPGVideo'))
    body += section(head('Partners who count on Fieldline to keep performance in motion') + logo_grid(), 'bg-surface')
    return page('customers.html', 'Customers | Fieldline', 'Customer stories from retailers, distributors, bottlers and brands that use Fieldline to move performance forward.', body,
        ('Move performance forward with purpose.', 'Build a culture that supports informed decisions, aligned teams and continual improvement that compounds over time.', 'Connect now'))

# ---------------------------------------------------------------- About
def about():
    body = page_hero('This is what performance looks like in motion.', kicker='About Fieldline',
        lede='Fieldline partners with organizations to align decisions, accountability and outcomes to drive productivity across the enterprise.',
        img='assets/img/hero-about.webp', crumbs=[(None, 'About Fieldline')],
        jumps=[('who', 'Who we are'), ('beliefs', 'What we believe'), ('partners', 'Who we work with'), ('history', 'Our history')])
    body += section(f'''<div class="split">
      <div class="prose reveal"><p style="font-size:var(--fs-lg);line-height:1.55">In complex organizations, performance depends on thousands of decisions made every day across job functions, teams and locations. Too often, those decisions are made with partial information, inconsistent definitions or data that isn\u2019t trusted enough to guide meaningful action.</p>
      <p>That challenge grows in importance as organizations bring AI into the way they operate. AI can only create value when it works from data that\u2019s accurate, connected, normalized and validated, and that connects to the broader technology ecosystem.</p>
      <p><strong>Fieldline helps organizations build that platform.</strong> We align data, responsibility and outcomes so people, systems and AI-enabled tools can work from the same trusted understanding of the business.</p></div>
      <div class="media-tile reveal" style="background:var(--white)"><img src="assets/img/hero-about.webp" alt="" loading="lazy" style="aspect-ratio:16/9;object-fit:cover"></div></div>''')
    body += section(f'''<div class="split top">
      <div class="reveal"><p class="kicker">Who we are</p><h2 class="h-section">Built for organizations that expect performance to keep moving.</h2></div>
      <div class="prose reveal"><p>Fieldline is a process optimization partner built for organizations that operate at scale. We work with leaders and teams responsible for real outcomes in environments where static reporting won\u2019t cut it, because decisions can\u2019t wait.</p>
      <p>For nearly four decades, Fieldline has helped organizations manage complexity by aligning data with how work actually gets done. Our work is grounded in a simple belief: performance improves when responsibility is clear, information is shared and people understand the impact of their actions.</p>
      <p>Our solution brings together operationally aligned data, rapid exploration and trusted performance context so organizations can understand what\u2019s happening, why it\u2019s happening and where action can create value. The result is a system where improvement is built into the way teams work, not treated as a one-time initiative. That\u2019s why our relationships are designed to last.</p></div></div>''', 'bg-surface', id='who')
    body += section(head('What we believe', 'Performance improvement doesn\u2019t happen by accident. It improves when organizations are intentional about how decisions are made, who owns the outcome and how progress is measured over time.') + accordion([
        ('Performance improves when responsibility is distributed, not centralized.', '<p>The people closest to the work are best positioned to see what\u2019s happening and act on it. Organizations perform better when decision-making authority is accessible, not hierarchical.</p>'),
        ('Alignment matters as much as autonomy.', '<p>Distributed decision-making only works when teams share a common understanding of success. Shared measures, transparent data and consistent definitions ensure autonomy doesn\u2019t come at the expense of alignment.</p>'),
        ('Understanding drives better action than reporting alone.', '<p>Seeing what happened isn\u2019t enough. Teams need to understand why performance changed, what influenced the outcome and where action creates value. Information without context leads to hesitation. Understanding creates momentum.</p>'),
        ('Accountability depends on trust.', '<p>Trust is built when teams work from the same information and can trace outcomes back to real activity. The same is true in AI-enabled environments: if the data foundation isn\u2019t validated, AI can\u2019t reliably support decisions.</p>'),
        ('Technology should serve the way business actually runs.', '<p>The value of technology comes from how well it supports the decisions, responsibilities and outcomes that shape performance.</p>'),
        ('Improvement is a system, not an initiative.', '<p>Sustainable performance comes from systems designed to support learning, adjustment and accountability every day, not from one-time programs or periodic reviews.</p>'),
    ]), 'bg-blue on-dark', id='beliefs')
    body += section(head('Who we work with', 'Fieldline partners with organizations where performance depends on informed decisions made across teams, functions and locations.') + cards([
        ('Retail and wholesale', 'Organizations managing margin, pricing, inventory and execution across stores, regions, categories and partners.', 'el-sws-seagreen.webp'),
        ('Beverage and consumer goods', 'Brands, distributors and suppliers navigating complex routes to market, trade spend, execution variability and performance across partners.', 'el-sws-blue.webp'),
        ('Healthcare and government', 'Organizations operating in regulated, data-intensive environments where accountability, transparency and outcomes matter.', 'el-asterisk-seablue.webp'),
    ]) + f'''<div class="card-grid cols-2 mt-2">
        <article class="card reveal"><h3>The leaders we support</h3>{ticks(['Executive leadership responsible for performance and accountability', 'Operations and functional leaders managing day-to-day execution', 'Finance and strategy teams focused on outcomes, efficiency and measurement', 'Data and analytics teams supporting insight, access, governance and AI readiness', 'Technology leaders responsible for data quality, system integration and scalable infrastructure'])}</article>
        <article class="card reveal"><h3>What our partners have in common</h3>{ticks(['Performance depends on thousands of daily decisions, not a single dashboard', 'Data lives across systems and teams, creating fragmentation, delay and disagreement', 'Accountability is shared, but not everyone has access to the information that drives value', 'AI is part of the technology strategy, but the business foundation isn\u2019t always ready for it', 'Improvement must be sustained, not reintroduced quarterly'])}</article>
      </div>''', id='partners')
    body += section(head('Trusted by today\u2019s leading brands') + logo_grid(), 'bg-surface')
    body += section(head('Our history', kicker='Since 1991') + '''<div class="timeline">
        <div class="phase reveal"><h3>1991: a practical problem</h3><p>Fieldline was founded to align day-to-day decisions with organizational performance. The focus was never reporting for reporting\u2019s sake. It was helping people understand the impact of their actions where work actually happens.</p></div>
        <div class="phase reveal"><h3>Growing with complexity</h3><p>As organizations and their data grew more complex, Fieldline evolved to support industries operating at scale, from consumer goods and distribution to retail, healthcare and government, and beyond single-use applications to distributed decision-making.</p></div>
        <div class="phase reveal"><h3>Today and what\u2019s next</h3><p>We combine experience, perspective and modern technology, and help organizations create the trusted performance foundation that lets people, processes, systems and AI-enabled tools work from the same understanding of value.</p></div>
      </div>''', id='history')
    return page('about.html', 'About Fieldline | Fieldline', 'Since 1991, Fieldline has partnered with organizations to align decisions, accountability and outcomes across the enterprise.', body,
        ('Every organization has room to improve how performance moves.', 'Let\u2019s explore what this means for your business.', 'Connect now'))

# ---------------------------------------------------------------- Careers
def careers():
    benefits = ['Competitive compensation', '401(k) with company match', 'Healthcare benefits with HSA-eligible plans', 'Paid time off', 'Company holiday shutdown from December 25 to January 1', 'Flexible work environment', 'Distributed, remote-first workforce', 'Internet and phone reimbursement', 'Volunteer time off']
    body = page_hero('Performance isn\u2019t just what we deliver.', 'It\u2019s how we work.', kicker='Careers',
        lede='At Fieldline, performance improves when people have ownership, understanding and autonomy. We design our work environment the same way we design our partnerships.',
        img='assets/img/hero-careers.webp', crumbs=[(None, 'Careers')], buttons=btn('View open positions', '#positions', 'accent'))
    body += section(f'''<div class="split top">
      <div class="reveal"><p class="kicker">Who we are</p><h2 class="h-section">Clear thinking over hierarchy.<span class="soft">Outcomes over optics.</span></h2></div>
      <div class="prose reveal"><p>Fieldline is a performance optimization partner built on a simple belief: organizations perform better when responsibility is distributed, performance is transparent and people are trusted to act.</p>
      <p>For nearly four decades, we\u2019ve helped organizations across industries make better business decisions by pairing human expertise with the right tools and frameworks. That same mindset shapes how we work internally. Fieldline values clear thinking over hierarchy, progress over posturing and outcomes over optics.</p>
      <p>We hire people who want to understand the \u201cwhy,\u201d take ownership of their work and contribute to something that lasts.</p></div></div>''')
    body += section(f'''<div class="split">
      <div class="media-tile reveal">{img_fallback('', 'assets/img/team.webp', 'Fieldline team members working together')}</div>
      <div class="prose reveal"><h2 class="h-section" style="font-size:var(--fs-2xl)">Distributed by design.</h2><p class="mt-1">Most of our team works remotely, supported by clear expectations, shared accountability and alignment around outcomes. When life requires flexibility, we support it. When work requires focus, we protect it.</p><p>The leadership team is accessible and engaged. Ideas aren\u2019t gated by title, and some of our most impactful thinking comes from collaboration across teams.</p></div></div>''', 'bg-surface')
    body += section(head('What our team says') + '''<div class="voices">
        <blockquote class="voice reveal"><p>\u201cThe collaborative culture and commitment to creative problem-solving at Fieldline are truly exceptional. I consistently feel valued as a team member and have the opportunity to learn from colleagues with diverse skill sets, all working toward a shared goal.\u201d</p><footer><strong>Jennifer Shelp</strong><small>Solutions Architect</small></footer></blockquote>
        <blockquote class="voice reveal"><p>\u201cMy career at Fieldline has been a continuous journey of supported growth. This is a place where professional development is prioritized and innovation is part of the daily culture.\u201d</p><footer><strong>Tiffany Smith</strong><small>Director of Data Analysis Services</small></footer></blockquote>
        <blockquote class="voice reveal"><p>\u201cFieldline understands what it means to embrace family values as an organization while maintaining high levels of professionalism. It\u2019s a place where people genuinely feel part of something bigger.\u201d</p><footer><strong>Jerold Kochman</strong><small>Senior Software Engineer</small></footer></blockquote>
      </div>''', 'bg-navy on-dark')
    body += section(head('Benefits and support', 'People do their best work when they\u2019re supported in practical, meaningful ways.') + f'<div class="card reveal">{ticks(benefits, two_col=True)}</div>')
    body += section(f'''<div class="split top">
      <div class="reveal"><p class="kicker">Open positions</p><h2 class="h-section" style="font-size:var(--fs-2xl)">We post current openings on LinkedIn.</h2><p class="lede">We don\u2019t use a traditional applicant tracking system. Every resume and introduction is reviewed by our team.</p></div>
      <div class="reveal"><a class="story-card" href="#" rel="noopener" style="flex-direction:row;align-items:center"><div class="body"><small>Remote</small><h3>Healthcare Data Analyst</h3><span class="more">Apply on LinkedIn {EXT}</span></div></a>
        <div class="card mt-1"><h3>Don\u2019t see the right role?</h3><p>Not every great fit starts with a job posting. Share your resume or reach out directly. If there\u2019s a mutual fit, we\u2019ll find the right path forward.</p><div class="btn-row" style="margin-top:1.25rem">{btn('Email hr@fieldline.example', 'mailto:hr@fieldline.example', 'primary', lg=False)}</div></div></div></div>''', 'bg-surface', id='positions')
    body += section('''<div class="prose reveal" style="max-width:80ch"><h2 class="h-section" style="font-size:var(--fs-xl)">Equal opportunity employment</h2><p class="mt-1">Fieldline is an equal opportunity employer. Employment decisions are based on qualifications, merit and business needs. We do not tolerate discrimination or harassment of any kind.</p><p>Fieldline provides equal employment opportunities to all employees and applicants without regard to race, color, religion, creed, sex, sexual orientation, gender identity, marital status, military or veteran status, age, national origin, citizenship, ancestry, disability, genetic information, domestic violence victim status or any other status protected by applicable law. This policy applies to all aspects of employment, including recruitment, hiring, compensation, benefits, promotion, termination and all other terms and conditions of employment.</p></div>''', 'section-tight')
    return page('careers.html', 'Careers | Fieldline', 'Join a distributed, remote-first team that values ownership, understanding and autonomy.', body)

# ---------------------------------------------------------------- Guide
def form(fields, button, success, note='This demo form doesn\u2019t send anything yet.'):
    out = []
    for f in fields:
        if f[0] == 'row':
            out.append('<div class="form-row">' + ''.join(field(*x) for x in f[1]) + '</div>')
        else:
            out.append(field(*f))
    return f'''<form class="form reveal" novalidate data-demo-form>
  <div class="form-fields">{"".join(out)}<button class="btn btn-primary btn-lg" type="submit">{button}</button><p class="form-note">{note}</p></div>
  <div class="form-success" role="status">{success}</div>
</form>'''

def field(name, label, kind='text', required=True, options=None):
    req = ' required' if required else ''
    star = '' if required else ' <span style="font-weight:400;color:var(--muted)">(optional)</span>'
    if kind == 'select':
        opts = '<option value="">Choose one</option>' + ''.join(f'<option>{o}</option>' for o in options)
        ctrl = f'<select id="{name}" name="{name}"{req}>{opts}</select>'
    elif kind == 'textarea':
        ctrl = f'<textarea id="{name}" name="{name}"{req}></textarea>'
    else:
        auto = {'email': 'email', 'name': 'name', 'company': 'organization', 'phone': 'tel'}.get(name, 'off')
        ctrl = f'<input id="{name}" name="{name}" type="{kind}" autocomplete="{auto}"{req}>'
    return f'<div class="field"><label for="{name}">{label}{star}</label>{ctrl}<span class="error">Enter your {label.lower()}.</span></div>'

IND_OPTS = ['Retail, grocery and convenience', 'Wholesale distribution', 'Non-alcoholic beverage', 'Alcoholic beverage', 'Consumer packaged goods', 'Healthcare', 'Other']

def guide():
    body = page_hero('By the time you see it,', 'margin has already moved.', kicker='Free guide for commercial, sales and finance leaders',
        lede='Why Commercial Performance Breaks Down shows how decision infrastructure connects performance, business context, accountability and action, helping teams protect margin, strengthen execution and support growth while decisions still matter.',
        img='assets/img/hero-guide.webp', crumbs=[(None, 'Commercial performance guide')], buttons=btn('Get the guide', '#get', 'accent'))
    body += section('''<div class="stats">
      <div class="stat reveal"><b data-count="21">21</b><span>Pages of practical guidance</span></div>
      <div class="stat reveal"><b data-count="6" data-suffix="-step">6-step</b><span>Rapid performance feedback cycle</span></div>
      <div class="stat reveal"><b data-count="5">5</b><span>Commercial environments examined</span></div>
      <div class="stat reveal"><b data-count="1">1</b><span>Decision infrastructure self-assessment</span></div></div>''', 'section-tight')
    body += section(head('Commercial teams can see what happened.', kicker='The challenge', soft='The challenge is understanding why, and acting while it still matters.') + cards([
        ('Teams work from disconnected views', 'Sales, finance, category and operations may use different measures, systems and levels of detail. Each sees a valid part of the business, but shared understanding becomes harder to establish.'),
        ('The cause disappears beneath the summary', 'A margin shift or promotion result may be visible at the top level, while the customer, product, store, route or execution detail needed to explain it sits several steps away.'),
        ('The answer arrives after the opportunity', 'Teams wait on analysts, exports or the next reporting cycle. By then, the window to adjust pricing, spend, inventory or execution may have passed.'),
    ], icons=False), 'bg-surface')
    body += section(f'''<div class="split">
      <div class="reveal"><p class="kicker">What\u2019s inside</p><h2 class="h-section">A practical look at decision infrastructure.</h2>
      {ticks(['Why commercial teams remain stuck explaining results instead of improving them', 'How the six-step rapid performance feedback cycle turns reporting into an operating rhythm', 'Where decision friction appears across retail, CPG, beverage and DSD', 'A practical self-assessment to identify where your current foundation slows action'])}
      <p class="mt-2" style="color:var(--muted)">Built for commercial teams in retail, grocery and convenience, consumer packaged goods, alcoholic beverage, non-alcoholic beverage and wholesale and DSD distribution.</p></div>
      <div class="guide-cover reveal"><div class="book"><img class="logo" src="assets/brand/fieldline-logo.svg" alt=""><div><div class="bar"></div><h3 class="mt-1">Why commercial performance breaks down</h3></div><img class="el" src="assets/brand/el-sws-seagreen.webp" alt=""></div></div></div>''')
    body += section(f'''<div class="split top">
      <div class="reveal"><p class="kicker">Free PDF, immediate access</p><h2 class="h-section">Identify where your performance feedback cycle slows down.</h2><p class="lede">Use the guide to find where disconnected measures, fragmented data, delayed analysis or unclear accountability may be limiting margin, execution and growth, and what stronger decision infrastructure requires.</p></div>
      {form([('row', [('fname', 'First name'), ('lname', 'Last name')]), ('email', 'Work email', 'email'), ('company', 'Company'), ('industry', 'Industry', 'select', True, IND_OPTS)], 'Get the guide', 'Thanks. Your guide is on its way to your inbox.')}</div>''', 'bg-navy on-dark', id='get')
    return page('commercial-performance-guide.html', 'Commercial performance guide | Fieldline', 'Why Commercial Performance Breaks Down: a free guide for commercial, sales and finance leaders.', body)

# ---------------------------------------------------------------- Blog
POSTS = [
    ('data-integration-decision-infrastructure/', '2026/09/Fieldline-Blog-Images-2.png', 'Thought leadership', 'Data integration isn\u2019t the same as decision infrastructure', 'Most retail, wholesale, distribution and CPG organizations have tried to solve performance with integration alone.', 'thought'),
    ('kpi-alignment-competing-priorities/', '2026/08/KPI-Alignment.jpeg', 'Thought leadership', 'Do your KPIs create alignment or competing priorities?', 'Most organizations have no shortage of key performance indicators.', 'thought'),
    ('performance-feedback-cycle-decision-friction/', '2026/08/Decision-Friction-Performance-Cycle.jpeg', 'Thought leadership', '7 places decision friction enters the feedback cycle', 'Decision friction accumulates at different points in the performance feedback cycle.', 'thought'),
    ('decision-friction-commercial-teams/', '2026/08/decision-friction-commercial-performance.jpeg', 'Thought leadership', 'What\u2019s decision friction, and what does it cost commercial teams?', 'A commercial leader notices something in the business has changed.', 'thought'),
    ('commercial-performance-management-questions/', '2026/08/Commercial-performance-management-questions.jpeg', 'Thought leadership', '8 more questions every commercial leader should ask about performance', 'Commercial organizations can have extensive reporting and still struggle to act.', 'thought'),
    ('commercial-performance-feedback-cycle/', '2026/07/Feedback-Cycle-Better-Decisions.jpeg', 'Thought leadership', 'The feedback cycle behind better commercial decisions', 'Better commercial decisions depend on a structured performance feedback cycle.', 'thought'),
    ('commercial-performance-questions/', '2026/07/Commercial-Leaders-Executives-Business-Analyze-Questions.jpeg', 'Thought leadership', '8 questions every commercial leader should ask about performance', 'Commercial performance often slows because teams can see results but not the cause.', 'thought'),
    ('new-product-innovation-performance/', '2026/01/Rows-Coffee-Consumer-Packaged-Goods-Grocery-Store-Shelves-Shelving.jpeg', 'Consumer packaged goods', 'When innovation moves performance forward, and when it doesn\u2019t', 'Innovation is supposed to move performance forward. Most of the time, the results are mixed.', 'cpg'),
    ('beer-competitive-edge-alignment/', '2026/04/Beer-Glass-Taps-Aligned.jpeg', 'Beverage', 'Why beer\u2019s next competitive edge is better alignment', 'Over the past several years, beer leaders invested heavily in data and technology.', 'beverage'),
    ('why-technology-initiatives-fail/', '2026/01/Technology-Implementation-Frustration-Man-Laptop.jpeg', 'Thought leadership', '4 reasons technology initiatives fail to improve performance', 'Most technology initiatives begin with sound intent.', 'thought'),
    ('crestview-chooses-fieldline/', None, 'Customer news', 'Crestview Snacks brings cutting-edge profitability management into practice', 'Crestview Snacks implemented Margin Minder to track profitability at a very precise level.', 'news'),
    ('sfc-chooses-fieldline/', None, 'Customer news', 'SFC chooses Fieldline for co-op, supplier and retail analytics', 'Summit Food Cooperative selected Fieldline to build a data sharing platform.', 'news'),
]

def blog():
    fallback = {'news': 'assets/img/hero-retail.webp'}
    cards_html = ''
    for i, (slug, img, cat, title, text, key) in enumerate(POSTS):
        src = U + img if img else fallback.get(key, 'assets/img/hero-blog.webp')
        cards_html += story_card(S + slug, src, cat, title, text, 'Read the article', feature=(i == 0), cat=key, external=True)
    chips = ''.join(f'<button class="chip" type="button" data-cat="{k}" aria-pressed="{str(k == "all").lower()}">{t}</button>' for k, t in [('all', 'All'), ('thought', 'Thought leadership'), ('cpg', 'Consumer packaged goods'), ('beverage', 'Beverage'), ('news', 'Customer news')])
    body = page_hero('Insight and perspective', kicker='Blog',
        lede='For leaders navigating margin pressure, execution complexity and growth at scale. Topics range from margin to execution to data access, accountability and decision-making at scale.',
        img='assets/img/hero-blog.webp', crumbs=[(None, 'Blog')])
    body += section(f'<div class="filter-bar" data-filter=".story-grid [data-cat]" aria-label="Filter articles">{chips}</div><div class="story-grid">{cards_html}</div><p class="mt-2 form-note">Articles open.</p>')
    return page('blog.html', 'Blog | Fieldline', 'Fieldline\u2019s perspective on how organizations manage performance across complex, distributed environments.', body,
        ('Want these insights applied to your business?', 'Bring the question you can\u2019t answer today. We\u2019ll bring the expertise.', 'Connect with us'))

# ---------------------------------------------------------------- Events
def events():
    up = [('nbwa-annual-convention-2026/', '2026/08/Commercial-Event-Website-Images-800-x-500.jpg', 'Orlando, FL', 'NBWA 2026', 'National Beer Wholesalers Association annual convention.'),
          ('nacs-2026/', '2026/08/Commercial-Event-Website-Images-800-x-500-1.jpg', 'Las Vegas, NV', 'NACS 2026', 'The convenience and fuel retailing show.')]
    past = [('iddba-2026/', '2026/05/IDDBA-2026-Orlando-FL-Fieldline-Commercial-CPG-Alcoholic-NonAlcoholic-Beverage-Wholesale-Distributor.jpg', 'Orlando, FL', 'IDDBA 2026'),
            ('sweets-snacks-expo-2026/', '2026/04/Sweets-and-Snacks-Expo-Fieldline.jpg', 'Las Vegas, NV', 'Sweets & Snacks Expo'),
            ('nga-2026/', None, 'Las Vegas, NV', 'The NGA Show 2026'),
            ('expo-west-2026/', None, 'Anaheim, CA', 'Expo West')]
    past_imgs = {'nga-2026/': '', 'expo-west-2026/': ''}
    up_html = ''.join(story_card(S + s, U + i, loc, t, d, 'Explore and meet us', external=True) for s, i, loc, t, d in up)
    past_html = ''.join(story_card(S + s, (U + i) if i else past_imgs[s], loc, t, 'See the recap.', 'View event', external=True) for s, i, loc, t in past)
    body = page_hero('Performance moves faster when leaders meet.', kicker='Events',
        lede='From national conferences to targeted association meetings, our presence is intentional. Fieldline participates in industry events where leaders are responsible for outcomes: margin, execution, growth and accountability.',
        img='assets/img/hero-events.webp', crumbs=[(None, 'Events')])
    body += section(head('Upcoming events', 'Join Fieldline on the road as we connect with industry leaders to exchange perspectives on what drives performance forward.') + f'<div class="story-grid">{up_html}</div>')
    body += section(head('Past events') + f'<div class="story-grid">{past_html}</div>', 'bg-surface')
    return page('events.html', 'Events | Fieldline', 'Meet Fieldline at industry events across retail, beverage, wholesale and CPG.', body,
        ('Don\u2019t see an event that fits your schedule?', 'Connect with the Fieldline team directly.', 'Connect now'))

# ---------------------------------------------------------------- Connect
def connect():
    body = page_hero('Empower your team.', 'Move performance forward.', kicker='Connect',
        lede='Fieldline partners with you to strengthen alignment, support decisions and build momentum across your entire organization.',
        img='assets/img/hero-connect.webp', crumbs=[(None, 'Connect')])
    body += section(f'''<div class="split top">
      <div class="reveal"><h2 class="h-section">Strong partnerships begin with strong connections.</h2>
        <div class="prose mt-2"><p>Whether you\u2019ve defined goals or early questions, start here. We\u2019ll guide the path forward with you.</p><p>No matter where you are in your performance journey, Fieldline partners with your team to uncover obstacles, strengthen alignment and build processes that support better decisions across the organization. With tech-enabled insight and strategic guidance, we help teams identify challenges, focus on priorities and take confident action toward meaningful improvement.</p><p><strong style="color:var(--brand-blue);font-size:1.15rem">Wherever you\u2019re starting from, we\u2019ll meet you there.</strong></p></div>
        <div class="card mt-2"><h3>Prefer to talk now?</h3><p>Call <a class="text-link" href="tel:+15550100142">(555) 010-0142</a> or visit us at 100 Main Street, Anytown, USA.</p></div></div>
      {form([('row', [('fname', 'First name'), ('lname', 'Last name')]), ('row', [('email', 'Work email', 'email'), ('phone', 'Phone', 'tel', False)]), ('row', [('company', 'Company'), ('title', 'Job title', 'text', False)]), ('industry', 'Industry', 'select', True, IND_OPTS), ('message', 'What would you like to improve?', 'textarea', False)], 'Start the conversation', 'Thanks for reaching out. A member of the Fieldline team will be in touch soon.')}</div>''', id='form')
    body += section(head('Partners who count on Fieldline to keep performance in motion') + logo_grid(), 'bg-surface')
    body += section(video_card('', 'Transformation that moves performance forward', 'See how Oakmont Foods strengthens alignment, accelerates action and improves performance with Fieldline as a strategic partner.', S + 'consumer-packaged-goods-cpg/#CPGVideo'))
    return page('connect.html', 'Connect | Fieldline', 'Start a conversation with Fieldline about the performance questions you can\u2019t answer today.', body)
