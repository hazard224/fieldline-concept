# Fieldline website concept

A 15-page marketing website concept for **Fieldline**, a fictional business-performance software company. Designed and built by Dan Baroody in plain HTML, CSS and JavaScript, with no framework and no runtime build step.

Fieldline, its customers, people, quotes, logos, figures and contact details are all placeholders.

## Run it

```
python3 -m http.server 8000
```
Then open http://localhost:8000. Opening index.html directly also works.

## Pages

| Page | File |
| --- | --- |
| Home | index.html |
| Industries overview | industries.html |
| Retail, grocery and convenience | retail-grocery-convenience.html |
| Alcoholic beverage | alcoholic-beverage.html |
| Non-alcoholic beverage | non-alcoholic-beverage.html |
| Wholesale distribution | wholesale-distributors.html |
| Consumer packaged goods | consumer-packaged-goods.html |
| How we work | how-we-work.html |
| Customers | customers.html |
| About | about.html |
| Careers | careers.html |
| Commercial performance guide | commercial-performance-guide.html |
| Blog | blog.html |
| Events | events.html |
| Connect | connect.html |

## Editing

Pages are generated from Python templates so the header, mega menu and footer stay identical everywhere.

```
build/common.py            header, mega menu, footer, shared helpers, logo list
build/pages_home.py        home page
build/pages_industries.py  industries overview and the five industry pages
build/pages_other.py       how we work, customers, about, careers, guide, blog, events, connect
python3 build/build.py     regenerates every .html file
```

## Notes

- Hero video streams from Pexels (Jakub Zerdzicki, "Tablet Analysis of Financial Data"), free for commercial use. Save the 1080p file as `assets/video/hero.mp4` to serve it locally.
- Forms validate and show a confirmation but send nothing.
- Partner logos are generated placeholder wordmarks.
