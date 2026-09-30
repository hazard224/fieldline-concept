# Salient website concept (v2)

A 15-page static redesign of salient.com in plain HTML, CSS and JavaScript. No framework and no runtime build step.

## Run it

```
python3 -m http.server 8000
```
Then open http://localhost:8000. Opening index.html directly also works.

## Publish on GitHub Pages

Push this folder to the repo root (or `/docs`), then set Settings > Pages to that branch and folder.

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

Healthcare links out to salienthealth.com. Privacy and terms link to the live site.

## Editing content

Pages are generated from Python templates so the header, mega menu and footer stay identical everywhere.

```
build/common.py            header, mega menu, footer, shared helpers, logo list
build/pages_home.py        home page
build/pages_industries.py  industries overview and the five industry pages
build/pages_other.py       how we work, customers, about, careers, guide, blog, events, connect
python3 build/build.py     regenerates every .html file
```
You can also edit the .html files directly; just don't run the build afterward or it will overwrite them.

## Before sharing

- **Hero video.** Streams from Pexels (Jakub Zerdzicki, "Tablet Analysis of Financial Data"). The Pexels license allows free commercial use without attribution. Download the 1080p file from https://www.pexels.com/video/tablet-analysis-of-financial-data-36455152/ and save it as `assets/video/hero.mp4`. The page tries the local file first.
- **Hotlinked salient.com assets.** Industry videos, Vidyard thumbnails, blog and event images, retail icons, the Fareway photo and the animated logo load from salient.com. Most have local fallbacks. For production, copy them into `assets/`.
- **Forms** validate and show a confirmation but send nothing. Connect them to your HubSpot (or other) form endpoint.
- **Proof points** in the home hero ("Since 1986", "Five industries", "Billions of transactions") come from existing Salient copy and press releases. Confirm before publishing.
- **Partner logos** include Macey's, Unilever, Reyes and Carvel, which appear in the asset library but not all on today's site. Confirm permissions.
- **FAQ answers** on How we work are assembled from existing site copy. Have marketing review them.
- **Stock licenses.** Confirm Adobe Stock and iStock licenses cover a public demo.

## Content fixes applied from the live site

- "quarterly profits or met" to "are met"; "See how Wholesalers uses" to "use"; "Salient supports that way" to "the way"
- "the way business operations" to "the way the business operates"
- "See how Salient connect it all together" to "connects"
- "professionalism.The" spacing; missing period after "distribution performance"
- "margin already moved" to "has already moved"; "into" and "you're" typos from the home page
- Duplicated sections removed on About and CPG
- Careers "more than 30 years" changed to "nearly four decades" to match the rest of the site
- ALL CAPS labels converted to sentence case, Oxford commas removed, per the brand guide

## Flagged, not changed

- About says "process optimization partner"; Careers says "performance optimization partner." Pick one.
- On the live Events page, the IDDBA image links to the American Bakers Association page.
- The live Wholesale page has a stray "Connect with a CPG Growth Expert" button.

## Brand rules applied

Montserrat (website font), Salient Blue and Darkness as primaries, Sea Green for calls to action, Sunshine and Bright Green only as line accents, 14px button radius, the rounded-corner tile shape on media, sentence case, no emojis, no Oxford comma, contractions.
