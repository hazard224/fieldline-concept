from common import *
from pages_home import VID_ALC, VID_CPG

S = ''

def video_card(thumb, title, text, live_url):
    thumb = local_img(thumb); live_url = "#"
    return f'''<a class="story-card is-feature reveal" href="{live_url}" rel="noopener">
  <div class="thumb" style="position:relative"><img src="{thumb}" alt="" loading="lazy"><span style="position:absolute;inset:0;display:grid;place-items:center"><span style="width:84px;height:84px;border-radius:50%;background:var(--white);display:grid;place-items:center;box-shadow:0 10px 30px rgba(0,0,0,.3)"><svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M8 5l11 7-11 7z" fill="#004181"/></svg></span></span></div>
  <div class="body"><small>Performance in practice</small><h3>{title}</h3><p>{text}</p><span class="more">Watch the video</span></div>
</a>'''

def img_fallback(src, fallback, alt=''):
    return f'<img src="{fallback}" alt="{alt}" loading="lazy">'

def section(inner, cls='', id=''):
    i = f' id="{id}"' if id else ''
    return f'<section class="section {cls}"{i}><div class="wrap">{inner}</div></section>'

# ---------------------------------------------------------------- Retail
def retail():
    icon = lambda n: f'{S}2026/09/Icon-{n}.png'
    feat = [
        ('Promotional effectiveness', 'Did the promotion achieve its objective and what did it change across the category and basket? Evaluate incremental lift, cannibalization, customer response and supplier investment to understand the full impact of your promotional strategy.', 'Promotion'),
        ('Category and assortment performance', 'Understand which products contribute to category growth, where assortment gaps exist and how changes in product mix influence demand, sales and category performance.', 'Categories'),
        ('Customer and basket behavior', 'See what customers buy together, how purchasing patterns change and which products and promotions influence basket size, purchase frequency and customer loyalty.', 'Basket'),
        ('Inventory and availability', 'Understand where out-of-stocks, excess inventory, spoilage and replenishment issues affect sales and store execution. Improve availability while reducing unnecessary inventory and waste.', 'Inventory'),
        ('Store-level performance', 'Understand why categories, promotions and products perform differently across stores, regions and markets, and where successful strategies can be applied elsewhere.', 'Store'),
        ('Supplier collaboration', 'Create a shared understanding of product, category and promotional performance to strengthen supplier relationships, improve promotional planning and support more effective investments.', 'Supplier-Relationship'),
    ]
    feat_cards = ''.join(f'<article class="card reveal"><div class="card-icon">{img_fallback(icon(k), "assets/brand/el-sws-blue.webp")}</div><h3>{t}</h3><p>{d}</p></article>' for t, d, k in feat)
    body = page_hero('Performance is decided beyond the shelf.', kicker='Retail, grocery and convenience',
        lede='Every product, promotion and customer interaction contributes to your retail business. Fieldline combines your organization\u2019s data and industry knowledge with proprietary technology to help the people responsible for results understand what\u2019s happening, why and where they can improve.',
        img='assets/img/hero-retail.webp', crumbs=[('industries.html', 'Industries'), (None, 'Retail, grocery and convenience')],
        buttons=btn('Explore what drives retail performance', '#visibility', 'accent') + btn('See how retail uses Fieldline', '#in-practice', 'ghost', arrow=False))
    body += section(head('Impact begins with visibility.', 'Seeing what moved is easy. Just look at the sales figures. Understanding performance requires a closer look at why customers buy, how promotions affect demand, which categories are growing and where store execution influences the result.') + f'<div class="card-grid">{feat_cards}</div>', id='visibility')
    body += section(f'''<div class="split">
      <div class="reveal"><p class="kicker">Promotional effectiveness</p><h2 class="h-section">A promotion isn\u2019t just a promotion.<span class="soft">Units moved isn\u2019t the same as value created.</span></h2>
      <div class="prose mt-2"><p>A promotion\u2019s impact can extend across the category, influence what customers buy together, affect inventory and change purchasing behavior well beyond the featured product.</p><p>Fieldline makes it possible for retailers to evaluate promotional effectiveness against their business objectives by connecting the information behind demand, category performance, customer behavior and store execution.</p><p><strong>Retailers and suppliers see what worked, what didn\u2019t and how to improve future investments.</strong></p></div></div>
      <div class="media-tile reveal">{img_fallback(S + '2026/09/Promotional-Value.jpg', 'assets/img/ind-retail.webp', 'Evaluating promotional value in a store')}</div>
    </div>''', 'bg-surface')
    grocery = ['Category management and assortment optimization', 'Promotional effectiveness and supplier programs', 'Private-label performance', 'Fresh inventory, spoilage and waste', 'Customer purchasing patterns and basket composition', 'Store-level performance and product availability']
    conv = ['Basket size and purchasing frequency', 'Foodservice and category performance', 'Promotional effectiveness', 'Store-level assortment and product availability', 'Customer behavior and product mix', 'Location-level performance and operational efficiency']
    body += section(head('Different retail environments.', 'From grocery stores and convenience chains to pharmacies, hardware stores and vending operations, Fieldline adapts to the way your organization defines and manages performance.', 'Retail environments we serve', 'Different measures of success.') + f'''
      <div class="card-grid cols-2">
        <article class="card reveal"><h3>Grocery retail</h3><p>Grocers manage extensive assortments, frequent promotions, changing customer preferences and inventory that moves at different rates. Fieldline helps category managers, merchandising teams and store operators decide based on the realities of their business.</p>{ticks(grocery)}</article>
        <article class="card reveal"><h3>Convenience retail</h3><p>Fast-moving assortments and significant variation across locations, from packaged beverages and snacks to foodservice. Fieldline helps operators evaluate category performance, customer behavior, promotions and store execution.</p>{ticks(conv)}</article>
      </div>
      <div class="card-grid mt-2">
        <article class="card reveal"><h3>Pharmacies and drug stores</h3><p>Front-of-store performance across health and wellness, personal care, food, beverages and everyday essentials.</p></article>
        <article class="card reveal"><h3>Vending and unattended retail</h3><p>Product performance, inventory and replenishment across distributed machines and unattended locations.</p></article>
        <article class="card reveal"><h3>Hardware and specialty retail</h3><p>Extensive assortments, seasonal demand and varying customer needs, down to store-level trends.</p></article>
      </div>
      <div class="band mt-3 reveal"><h2>Performance extends beyond the individual store.</h2><p>Grocery wholesalers and retail associations can bring retail data together across the retailers they serve to support category management, promotional planning, inventory decisions and supplier collaboration across their networks.</p><img class="element" src="assets/brand/el-steps-white.webp" alt=""></div>''', id='environments')
    body += section(head('Your retail business doesn\u2019t operate from one desk.', 'Category managers, merchandising teams, store operators and executives are responsible for different outcomes, but their decisions affect one another. Fieldline gives each role the information relevant to it while keeping a shared understanding of performance.', 'Performance at every level', 'Neither should your understanding of it.') + rows([
        ('Category and merchandising', 'Understand promotional performance, assortment, supplier programs and category trends to make better decisions about the products customers buy.'),
        ('Store and operations', 'Monitor store-level execution, inventory, availability and operational performance across locations.'),
        ('Marketing and loyalty', 'Evaluate customer behavior, basket composition, promotional response and purchasing patterns to see what influences engagement and customer value.'),
        ('Leadership and finance', 'Understand performance across categories, stores and functions, investigate the factors behind results and evaluate progress against business objectives.'),
    ]) + '<div class="band mt-3 reveal" style="background:var(--navy)"><h2>A starting point that doesn\u2019t limit where you can go.</h2><p>People get a relevant view of their responsibilities and can investigate beyond predefined reports as questions change. And because your business will keep evolving, Fieldline stays involved to refine measures and extend the environment.</p></div>', 'bg-surface')
    body += section(head('Technology matters.', 'Retail questions change quickly. The value of a partner is knowing enough about the business to understand why the answer matters and how it connects to what happens next.', 'Retail performance in practice', 'Understanding the business matters even more.') +
        video_card('', 'See how retailers use Fieldline', 'Hear from retail teams about category, promotion and store performance.', '#'), id='in-practice')
    return page('retail-grocery-convenience.html', 'Retail, grocery and convenience | Fieldline', 'Fieldline helps retail, grocery and convenience teams improve performance through unified data, faster decisions and stronger alignment across the business.', body,
        ('Your business has its own definition of performance. Fieldline will help you improve it.', 'From category management and promotional effectiveness to customer behavior and store execution, Fieldline brings your data, priorities and industry expertise together.'))

# ---------------------------------------------------------------- Alcoholic beverage
def alcoholic():
    body = page_hero('Performance doesn\u2019t pour itself.', 'Volume is only part of the story.', kicker='Alcoholic beverage',
        lede='Pricing, portfolio mix, promotions, inventory, route execution and cost-to-serve influence whether growth creates value or diminishes it. Fieldline connects the operational, financial and market context so your people can understand what\u2019s changing, investigate why and focus where it makes the greatest impact.',
        img='assets/img/hero-alc.webp', video=VID_ALC, poster='assets/img/hero-alc.webp', crumbs=[('industries.html', 'Industries'), (None, 'Alcoholic beverage')],
        buttons=btn('Explore what drives beverage performance', '#answers', 'accent') + btn('See Granite Distributing', '#in-practice', 'ghost', arrow=False))
    body += section(f'''<p class="kicker reveal">Trusted across alcoholic beverage</p>{logo_grid(['granite-distributing', 'riverbend-distributing', 'rosewood-beverage-house', 'blue-heron-distributors'] )}''', 'section-tight')
    body += section(f'''<div class="split top">
      <div class="reveal"><p class="kicker">Performance in a shifting market</p><h2 class="h-section">A shifting market changes more than demand.<span class="soft">It changes the economics of the business.</span></h2></div>
      <div class="prose reveal"><p>Alcoholic beverage organizations manage meaningful changes in category mix, consumer preferences, promotional pressure and operating costs. What creates value in one part of the portfolio may look completely different in another, and yesterday\u2019s assumptions don\u2019t always hold as the market moves.</p>
      <p>For suppliers, that means understanding if distribution gains translate into velocity, how pricing compares with expectations and whether joint business plans produce intended returns.</p>
      <p>For distributors, the questions move closer to the economics of execution: which customers and routes remain profitable, what the true cost-to-serve is and where inventory, delivery or promotional decisions put pressure on margin.</p>
      <p><strong>As the market evolves, the way performance is measured should too.</strong></p></div></div>''', 'bg-surface')
    sup = ['Compare suggested pricing against market conditions', 'Pinpoint where margin is gained or lost across distributors, channels, packages and geographies', 'Connect distributor execution to retail performance and market share', 'Understand where distribution gains translate into velocity and where they fall flat', 'Evaluate joint business plans against actual performance and identify where action is needed']
    dist = ['Calculate true dead-net cost by product, customer, route or territory', 'Identify the customers and products that create profitable growth', 'Understand where delivery requirements and service patterns erode margin', 'Quantify the financial impact of shrink, overstocks, out-of-stocks and excess inventory', 'Connect sales and incentive performance back to volume, margin and execution']
    body += section(head('Different responsibilities demand different performance answers.', 'Pricing structure, portfolio hierarchies, route economics, incentive programs and the way margin is defined vary significantly between organizations. Fieldline starts with how you create and measure value, then structures the data, business rules and technology around it.', 'Purpose-built in practice') + f'''
      <div class="card-grid cols-2">
        <article class="card reveal"><p class="kicker">For suppliers</p><h3>See what\u2019s happening beyond the shipment</h3><p>Shipment and depletion data only tell part of the story. Fieldline connects distributor activity with pricing, retailer performance, syndicated data and other market signals.</p>{ticks(sup)}</article>
        <article class="card reveal"><p class="kicker">For distributors</p><h3>Know what it really costs to move the business</h3><p>Route accounting captures the movement of product, but not always the full economics behind it. Fieldline connects sales with financial, payroll, inventory and routing data.</p>{ticks(dist)}</article>
      </div>''', id='answers')
    body += section(f'''<div class="split">
      <div class="reveal"><p class="kicker">Designed to go further</p><h2 class="h-section">A change in performance gives you a place to begin.<span class="soft">It doesn\u2019t tell you where to go next.</span></h2>
      <div class="prose mt-2"><p>The cause of a performance shift often sits several layers beneath the headline number, in a particular market, customer, package, route, price point or transaction. The path is different every time.</p><p>Fieldline gives business users the freedom to investigate as questions arise. Start with the variance, explore the factors contributing to it and keep moving into the underlying activity until the cause becomes clear.</p><p><strong>The goal isn\u2019t more reporting. It\u2019s the ability to follow the question as far as the business requires.</strong></p></div></div>
      <div class="media-tile reveal">{img_fallback(S + '2026/09/01.jpg', 'assets/img/story-platform.webp', 'Exploring performance data in Fieldline')}</div></div>''', 'bg-navy on-dark')
    body += section(head('Profitable growth is decided in the details.', 'From the price of a case to the cost of getting it to the customer. Fieldline brings each piece together around the measures, relationships and business rules your organization uses to define performance.', 'Built differently for a reason') + '''
      <div class="pillars">
        <div class="pillar reveal"><h3>What moved</h3><ul><li>Shipments</li><li>Depletions</li><li>Sales</li><li>Inventory</li></ul></div>
        <div class="pillar reveal"><h3>What it cost</h3><ul><li>Financial costs</li><li>Labor</li><li>Delivery</li><li>Cost-to-serve</li></ul></div>
        <div class="pillar reveal"><h3>What happened in the market</h3><ul><li>Pricing</li><li>Execution</li><li>Retail activity</li><li>Market trends</li></ul></div>
        <div class="pillar reveal"><h3>What it means to your business</h3><ul><li>Business rules</li><li>Targets and KPIs</li><li>Margin</li><li>Profitability</li></ul></div>
      </div>
      <p class="mt-2 reveal" style="font-weight:700;color:var(--brand-blue)">Your performance view should reflect how these factors work together. Not how your systems store them.</p>''', 'bg-surface')
    body += section(video_card('', 'See what purpose-built performance looks like at Granite Distributing', 'Fieldline gives Granite the ability to move beyond high-level reporting, investigate performance in greater detail and use that understanding to strengthen execution and protect margin.', '#'), id='in-practice')
    return page('alcoholic-beverage.html', 'Alcoholic beverage | Fieldline', 'Fieldline connects the operational, financial and market context behind alcoholic beverage performance for suppliers and distributors.', body,
        ('Ready for a better way to manage alcoholic beverage performance?', 'Bring measures, relationships and value creation together with Fieldline\u2019s alcoholic beverage expertise and proprietary technology.'))

# ---------------------------------------------------------------- Non-alcoholic beverage
def nonalcoholic():
    body = page_hero('Performance moves when decisions are aligned.', 'A shared view keeps execution, margin and momentum connected.', kicker='Non-alcoholic beverage',
        lede='Innovation cycles are constant, packaging changes quickly and promotions, pricing and execution shift by market, customer and route. Fieldline helps non-alcoholic beverage organizations run performance as a connected system across brands, bottlers and routes.',
        img='assets/img/hero-nonalc.webp', crumbs=[('industries.html', 'Industries'), (None, 'Non-alcoholic beverage')],
        buttons=btn('Connect with a beverage performance expert', 'connect.html', 'accent') + btn('See how beverage teams use Fieldline', '#in-practice', 'ghost', arrow=False))
    body += section(f'''<div class="split top">
      <div class="reveal"><h2 class="h-section">You don\u2019t run beverage performance from one office.<span class="soft">You align decisions across the organization.</span></h2>
      <div class="prose mt-2"><p>Performance is shaped by hundreds of decisions made every day by brand leaders, bottlers, planners and field teams. When responsibility is distributed but performance isn\u2019t managed from the same foundation, even strong strategies lose momentum.</p><p>Fieldline partners with beverage organizations to establish a shared foundation, so decisions made in the field, in planning and at the center move in the same direction.</p></div></div>
      <div class="card reveal"><h3>When decisions are aligned, momentum builds</h3>{ticks(['Field execution aligns with central strategy', 'Promotions reflect inventory, demand and route realities', 'Margin becomes easier to understand and protect', 'Collaboration improves across roles and regions', 'Performance compounds instead of fragmenting'])}</div></div>''')
    body += section(f'''<div class="split">
      <div class="media-tile reveal">{img_fallback('', 'assets/img/hero-connect.webp', 'Beverage leadership team meeting')}</div>
      <div class="reveal"><h2 class="h-section">When feedback connects the business, performance improves.</h2>
      <div class="prose mt-2"><p>Performance improvement depends on how effectively an organization learns from its decisions. When teams understand the downstream impact of their choices, they can adjust early and prevent small issues from becoming systemic problems.</p><p>Fieldline builds clear feedback loops and shared accountability into the way the business operates. AI-supported processes surface emerging risks and opportunities earlier so teams can respond before performance slips.</p></div>
      {ticks(['Pricing and promotions guided by real execution and demand signals', 'Route decisions anchored in true cost-to-serve and efficiency', 'Earlier course correction as volume and mix shifts emerge', 'Central decisions shaped by what\u2019s actually happening in the field', 'Consistent execution across brands, bottlers and territories'])}</div></div>''', 'bg-surface')
    body += section(f'<p class="kicker reveal">Trusted by beverage leaders obsessed with maximizing performance</p>{logo_grid(['clearwater-bottling-company', 'northern-spring-bottling', 'harbor-bottling-group', 'ridgeline-bottling-ventures', 'copper-kettle-beverage'])}', 'section-tight')
    body += section(head('Build performance that doesn\u2019t fall flat.', 'Fieldline helps non-alcoholic beverage organizations design alignment into the way decisions are made, so execution stays crisp, accountability is clear and results hold over time. With a shared foundation for performance, organizations can:') + cards([
        ('Coordinate pricing, promotions and execution', 'Keep markets moving in the same direction.', 'el-sws-blue.webp'),
        ('Understand true cost-to-serve', 'See route efficiency and what it costs to deliver.', 'el-sws-seagreen.webp'),
        ('Spot early signals', 'Catch changes that affect volume, mix and margin.', 'el-steps-blue.webp'),
        ('Reduce friction', 'Close the gap between central teams and the field.', 'el-asterisk-seablue.webp'),
        ('Keep local agility', 'Maintain consistency without losing flexibility.', 'el-tile-seagreen.webp'),
    ]), 'bg-navy on-dark')
    body += section(f'''<div class="split">
      <div class="reveal"><h2 class="h-section">Build confidence where execution happens.</h2>
      <div class="prose mt-2"><p>Planners, operators and field teams make decisions every day that directly affect bottling and distribution performance. For them to act with speed and accountability, expectations must be clear and performance must be understood.</p><p>Fieldline establishes shared measures, clear context and consistent feedback, giving individuals the confidence to take ownership of outcomes and act with intent.</p></div>
      {ticks(['Empower confident action in the field', 'Support planners and operators with timely, relevant guidance', 'Reduce second-guessing and manual reconciliation', 'Build accountability rooted in shared understanding', 'Foster a performance-driven culture focused on continuous improvement'])}
      <p class="mt-2"><strong>When individuals trust the foundation behind their decisions, confidence follows. And so does performance.</strong></p></div>
      <div class="media-tile reveal">{img_fallback('', 'assets/img/hero-wholesale.webp', 'Distribution staff in a beverage warehouse')}</div></div>''')
    body += section(head('Clear execution. Intentional performance.', 'Leading non-alcoholic beverage organizations partner with Fieldline to align teams across routes, markets and roles, from bottling to operations to distribution and delivery.') + video_card('', 'See what performance looks like when alignment drives execution', 'Hear from beverage teams using Fieldline across the plant, the warehouse and the last mile.', '#'), 'bg-surface', id='in-practice')
    return page('non-alcoholic-beverage.html', 'Non-alcoholic beverage | Fieldline', 'Fieldline helps non-alcoholic beverage organizations run performance as a connected system across brands, bottlers and routes.', body,
        ('From the plant to the last mile, performance depends on alignment.', 'Partner with a team that helps non-alcoholic beverage organizations manage performance as a system.', 'Connect with a beverage performance expert'))

# ---------------------------------------------------------------- Wholesale
def wholesale():
    body = page_hero('Performance moves when issues are identified and resolved quickly.', kicker='Wholesale distribution',
        lede='Tight margins, significant inventory investment and complex operations leave little room for error. Fieldline helps wholesale distributors shorten the distance between identifying issues and taking corrective action, before delays turn into losses.',
        img='assets/img/hero-wholesale.webp', crumbs=[('industries.html', 'Industries'), (None, 'Wholesale distribution')],
        buttons=btn('Connect with a wholesale expert', 'connect.html', 'accent') + btn('See how wholesalers use Fieldline', '#resolution', 'ghost', arrow=False))
    body += section(f'''<div class="split top">
      <div class="reveal"><h2 class="h-section">Wholesale decisions are measured in basis points,<span class="soft">not broad averages.</span></h2>
      <div class="prose mt-2"><p>Pricing adjustments, program changes and inventory commitments must align with actual movement and depletion timing. Each decision may seem minor in isolation, but together they determine whether quarterly profits are met or missed.</p><p>With teams working independently, coordination breaks down. By the time disconnects surface, margin is damaged and decisions become reactive.</p></div></div>
      <div class="card reveal"><h3>Fieldline partners with wholesale leaders to address issues before they become losses</h3>{ticks(['Margin erosion hidden inside vendor and customer programs', 'Pricing drift that\u2019s difficult to detect early', 'Program performance that\u2019s hard to compare or validate', 'Delayed visibility that turns manageable issues into financial exposure'])}</div></div>''')
    body += section(head('Wholesale performance depends on fast, coordinated resolution.') + cards([
        ('Identify margin leakage early', 'Surface pricing, program and customer-level issues before profitability weakens.', 'el-sws-blue.webp'),
        ('Manage inventory with intent', 'Spot short-dated and at-risk product early, align depletions to expiration windows and reduce write-offs before they happen.', 'el-sws-seagreen.webp'),
        ('Validate vendor and customer programs', 'Measure allowances, bill backs and survey programs consistently so performance can be corrected while programs are still active.', 'el-steps-blue.webp'),
        ('Improve service reliability', 'Monitor fill rates, delivery consistency and service-level execution to control cost-to-serve while protecting customer relationships.', 'el-asterisk-seablue.webp'),
        ('Move from issue to action quickly', 'Shorten the time between issue identification and corrective action, so small issues don\u2019t become financial liabilities.', 'el-tile-seagreen.webp'),
    ]), 'bg-surface', id='resolution')
    body += section(f'''<div class="split">
      <div class="media-tile reveal">{img_fallback('', 'assets/img/hero-wholesale.webp', 'Wholesale executive in a warehouse')}</div>
      <div class="reveal"><h2 class="h-section">Inventory is capital.<span class="soft">Performance depends on how fast you protect it.</span></h2>
      <div class="prose mt-2"><p>For wholesale operations, inventory is working capital, customer commitments and margin at risk, all moving at once. A seller plans six months of sell-through. The product expires in sixty days. By the time the disconnect becomes visible, the opportunity for action is gone.</p><p>Fieldline brings inventory, timing and execution together. When product age, demand and customer commitments are visible together, teams can intervene earlier, reallocate purposefully and prevent loss before it hits the P&amp;L.</p></div></div></div>''')
    body += section(f'''<div class="split top">
      <div class="reveal"><h2 class="h-section">Resolution works when every role is working from the same reality.</h2><p class="lede">Sales pursues commitments. Operations manages availability. Finance tracks margin after the fact. Fieldline helps teams align these priorities so decisions support the same outcomes, not competing ones.</p></div>
      <div class="reveal">{ticks(['Identify short-dated and at-risk inventory before it turns into out-of-dates', 'Align sellers, operations and leadership around realistic depletion windows', 'Improve program performance while adjustments are still possible', 'Connect service reliability to cost-to-serve and margin impact', 'Take corrective action early, not after losses are realized'])}</div></div>''', 'bg-navy on-dark')
    body += section(head('Built for wholesale.', 'Performance depends on how quickly teams can identify issues, understand impact and take corrective action across roles. Fieldline supports the way wholesale operations actually run, day to day.', soft='Designed for resolution.') + rows([
        ('Early detection of margin and risk', 'Surface basis-point pressure, short-dated exposure and service breakdowns before they become losses.'),
        ('Service reliability tied to cost-to-serve', 'Connect fill rates, delivery consistency and execution performance directly to margin and operational efficiency.'),
        ('Faster corrective action across roles', 'Enable sales, operations and finance to act together instead of reconciling after the fact.'),
        ('Flexibility across the distribution ecosystem', 'Scale performance management across supplier and retailer relationships as business models evolve.'),
    ]), 'bg-surface')
    return page('wholesale-distributors.html', 'Wholesale distribution | Fieldline', 'Fieldline helps wholesale distributors protect margin, inventory and service by shortening the distance between identifying issues and acting on them.', body,
        ('Align pricing, programs, inventory and service across the business.', 'Teams act faster, resolve issues earlier and keep performance moving.', 'Connect with a wholesale distribution expert'))

# ---------------------------------------------------------------- CPG
def cpg():
    body = page_hero('Performance starts long before the shelf.', 'Your market, customers and distributors as one connected system.', kicker='Consumer packaged goods',
        lede='For CPG suppliers that sell and distribute, performance is shaped by pricing, promotions, product mix, trade spend and distributor execution. Fieldline connects shipments, distributor activity, retail scans and syndicated data into a single performance context.',
        img='assets/img/hero-cpg.webp', video=VID_CPG, poster='assets/img/hero-cpg.webp', crumbs=[('industries.html', 'Industries'), (None, 'Consumer packaged goods')],
        buttons=btn('Connect with a CPG growth expert', 'connect.html', 'accent') + btn('See how Oakmont uses Fieldline', '#in-practice', 'ghost', arrow=False))
    body += section(f'''<div class="split top">
      <div class="reveal"><h2 class="h-section">Performance isn\u2019t a report.<span class="soft">It\u2019s a system.</span></h2></div>
      <div class="prose reveal"><p>Reporting only looks at the past. Fieldline partners with CPG suppliers to understand how pricing, promotions, product mix and distributor execution influence one another, and how yesterday\u2019s decisions set tomorrow\u2019s motion.</p><p>Fieldline brings together human expertise, advanced management discipline and AI-enabled systems to help organizations understand real performance. Why it shifted. What it means for what\u2019s ahead. And where small changes can improve margin, execution and growth.</p></div></div>''')
    body += section(f'''<div class="split top">
      <div class="reveal"><h2 class="h-section">CPG markets move fast.<span class="soft">Suppliers are expected to stay ahead of every variable.</span></h2>
      <div class="prose mt-2"><p>Pricing shifts. Promotions rise and fall. Distributor performance fluctuates. Retailers demand more support with fewer resources. Yet most suppliers still operate without a clear line of sight between decisions and outcomes.</p><p>Shipments don\u2019t show sell-through. Distributor reports don\u2019t explain retail behavior. And syndicated data reveals trends without the cause behind them.</p></div></div>
      <div class="card reveal"><h3>Fieldline partners with CPG suppliers to address</h3>{ticks(['Fragmented information that hides true demand and execution', 'Limited understanding of distributor performance and cost-to-serve', 'Promotions that are difficult to evaluate or justify', 'Reporting practices that keep decisions reactive instead of intentional'])}</div></div>''', 'bg-surface')
    body += section(head('Four drivers that shape CPG performance.', 'Suppliers don\u2019t need more reports. They need a disciplined way to understand why results occur and how to improve them, combining clean, unified information, AI-enabled decision support and ongoing partnership with experts.') + cards([
        ('Understand the impact behind every decision', 'Clarify how pricing, promotions, mix and trade spend contribute to performance so decisions are guided by value, not assumption.'),
        ('Reveal how products move across the value chain', 'Understand distribution gaps, delivery patterns and compliance to manage execution between shipment and shelf.'),
        ('Interpret what retailers and shoppers are telling you', 'Connect sell-through, velocity, out-of-stocks and trends to understand true demand and changing behavior.'),
        ('Align teams around one performance foundation', 'Ensure individuals across the organization operate from the same understanding of performance and priorities.'),
    ], icons=False), 'bg-navy on-dark')
    body += section(f'<p class="kicker reveal">Trusted by CPG brands shaping markets nationwide</p>{logo_grid(['oakmont-foods', 'hearthstone-bakeries', 'evergreen-brands', 'bluebird-creamery'])}', 'section-tight')
    body += section(head('Enable intentional, connected performance across the CPG value chain.') + rows([
        ('Identify true margin drivers', 'Understand how mix, cost-to-serve and trade spend influence profitability.'),
        ('Strengthen distributor partnerships', 'Analyze execution patterns and collaborate using shared insight.'),
        ('Improve promotion performance', 'Evaluate incrementality, timing and cannibalization to guide investment decisions.'),
        ('Recognize demand signals early', 'Spot emerging business patterns before issues compound.'),
        ('Guide pricing decisions', 'Understand how price changes affect volume, margin and customer behavior.'),
        ('Reduce costly blind spots', 'Connect cause and effect across the value chain.'),
        ('Align decisions across the organization', 'Give sales, revenue growth management, marketing, finance and supply chain a shared performance context.'),
        ('Move performance forward', 'Support decisions that improve margin, relationships and long-term growth.'),
    ]), 'bg-surface')
    body += section(head('Real CPG leaders. Real complexity.', soft='Real performance improvement.') + video_card('', 'See how Oakmont Foods uses Fieldline to improve performance across the value chain', 'Oakmont strengthens alignment, accelerates action and improves performance with Fieldline as a strategic partner.', '#'), id='in-practice')
    return page('consumer-packaged-goods.html', 'Consumer packaged goods | Fieldline', 'Fieldline connects shipments, distributor activity, retail scans and syndicated data so CPG suppliers understand what drives performance.', body,
        ('Move CPG performance forward with purpose.', 'Equip your organization with the structure and partnership needed to guide decisions, strengthen execution and deliver lasting improvement.', 'Connect with a CPG performance expert'))

# ---------------------------------------------------------------- Industries overview
def industries():
    items = [
        ('retail-grocery-convenience.html', 'assets/img/ind-retail.webp', 'Retail, grocery and convenience', 'Your margin story isn\u2019t contained in one dashboard. Connect pricing, promotion, category, inventory, supplier and financial performance.'),
        ('wholesale-distributors.html', 'assets/img/ind-wholesale.webp', 'Wholesale distribution', 'Your operation doesn\u2019t run from a summary. See performance customer by customer, route by route and delivery by delivery.'),
        ('non-alcoholic-beverage.html', 'assets/img/ind-nonalc.webp', 'Non-alcoholic beverage', 'Every customer, route and market contributes differently. Keep execution, margin and momentum connected.'),
        ('alcoholic-beverage.html', 'assets/img/ind-alc.webp', 'Alcoholic beverage', 'Performance doesn\u2019t pour itself. Understand supplier and distributor economics in detail.'),
        ('consumer-packaged-goods.html', 'assets/img/ind-cpg.webp', 'Consumer packaged goods', 'See what happens between shipment and shelf, from pricing and promotion to distributor execution.'),
        ('#', 'assets/img/hero-connect.webp', 'Healthcare', 'Bring clinical, operating and financial information together around the measures that matter. Visit Fieldline Health.'),
    ]
    grid = ''.join(story_card(h, i, 'Industry', t, d, 'Explore' if not h.startswith('http') else 'Visit Fieldline Health', external=h.startswith('http')) for h, i, t, d in items)
    body = page_hero('Performance works differently by industry.', 'So should the solution.', kicker='Industries we serve',
        lede='Fieldline brings decades of industry experience together with proprietary technology and performance expertise to build solutions around the way value is created, measured and influenced in your business.',
        img='assets/img/hero-industries.webp', crumbs=[(None, 'Industries')])
    body += section(f'<div class="story-grid">{grid}</div>')
    body += section('<div class="band reveal"><h2>Your business doesn\u2019t have to fit a predefined approach to performance.</h2><p>Fieldline brings your organization\u2019s data, priorities and industry expertise together to create a performance environment built around the way you operate.</p><div class="btn-row">' + btn('See how Fieldline connects it all together', 'how-we-work.html', 'accent') + '</div><img class="element" src="assets/brand/el-steps-white.webp" alt=""></div>', 'section-tight')
    return page('industries.html', 'Industries we serve | Fieldline', 'Fieldline serves retail, grocery and convenience, wholesale distribution, alcoholic and non-alcoholic beverage, consumer packaged goods and healthcare.', body,
        ('Ready for a better way to manage business performance?', 'Tell us about your industry, your priorities and the questions you can\u2019t answer today.'))
