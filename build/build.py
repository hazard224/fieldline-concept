"""Regenerate every page: python3 build/build.py (from the site root)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages_home import home
from pages_industries import retail, alcoholic, nonalcoholic, wholesale, cpg, industries
from pages_other import how, customers, about, careers, guide, blog, events, connect
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = {
    'index.html': home, 'industries.html': industries,
    'retail-grocery-convenience.html': retail, 'alcoholic-beverage.html': alcoholic,
    'non-alcoholic-beverage.html': nonalcoholic, 'wholesale-distributors.html': wholesale,
    'consumer-packaged-goods.html': cpg, 'how-we-work.html': how, 'customers.html': customers,
    'about.html': about, 'careers.html': careers, 'commercial-performance-guide.html': guide,
    'blog.html': blog, 'events.html': events, 'connect.html': connect,
}
for name, fn in PAGES.items():
    with open(os.path.join(ROOT, name), 'w', encoding='utf-8') as f:
        f.write(fn())
    print('built', name)
