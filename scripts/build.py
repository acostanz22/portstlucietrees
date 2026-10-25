#!/usr/bin/env python3
"""Build the static Port St Lucie Tree Service site from the audited HTML."""

import html
import json
import re
from pathlib import Path

from content import (
    GOOGLE_PROFILE,
    HOME_CARDS,
    HOME_FAQS,
    HOME_INTRO,
    LOCATION_PAGES,
    META,
    PERMIT_URL,
    REVIEWS,
    SERVICE_PAGES,
)

def escape(value, quote=False):
    return html.escape("" if value is None else str(value), quote=quote)


unescape = html.unescape

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / ".audit" / "html"
SEO = json.loads((ROOT / ".audit" / "seo.json").read_text())

BASE = "https://www.portstlucietrees.com"
PHONE = "772-492-4436"
TEL = "tel:7724924436"
BUSINESS = "Port St Lucie Tree Service"
SITE_NAME = "Tree Service Port St Lucie"

SERVICES = [
    ("tree-removal.html", "Tree Removal"),
    ("emergency-tree-removal.html", "Emergency Tree Removal"),
    ("palm-tree-trimming.html", "Palm Tree Trimming & Removal"),
    ("tree-care-prevention.html", "Tree Trimming & Pruning"),
    ("stump-removal.html", "Stump Removal"),
    ("storm-damage-clean-up.html", "Storm Damage Clean Up"),
    ("land-lot-clearing.html", "Land & Lot Clearing"),
    ("brush-cleaning.html", "Brush Cleaning"),
    ("commercial-tree-service.html", "Commercial Tree Service"),
    ("large-tree-removal.html", "Large Tree Removal"),
    ("crane-assisted-tree-removal.html", "Crane-Assisted Tree Removal"),
    ("hazardous-dangerous-tree-removal.html", "Hazardous & Dangerous Tree Removal"),
    ("oak-tree-removal.html", "Oak Tree Removal"),
    ("dead-diseased-tree-removal.html", "Dead & Diseased Tree Removal"),
    ("tree-removal-near-houses-buildings.html", "Tree Removal Near Houses & Buildings"),
    ("tree-removal-for-construction.html", "Tree Removal for Construction"),
]
SERVICE_URL = {name: href for href, name in SERVICES}

PLACES = [
    ("port-st-lucie-flordia.html", "Port St Lucie, FL"),
    ("stuart-flordia.html", "Stuart, FL"),
    ("palm-city-florida.html", "Palm City, FL"),
    ("fort-pierce-florida.html", "Fort Pierce, FL"),
    ("florida-ridge-fl.html", "Florida Ridge, FL"),
    ("hobo-sound-fl.html", "Hobe Sound, FL"),
    ("vero-beach-florida.html", "Vero Beach, FL"),
    ("jupiter-florida.html", "Jupiter, FL"),
    ("palm-beach-gardens-florida.html", "Palm Beach Gardens, FL"),
    (None, "North Palm Beach, FL"),
    ("sebastian-florida.html", "Sebastian, FL"),
    (None, "Lake Park, FL"),
    ("riviera-beach-fl.html", "Riviera Beach, FL"),
    ("royal-palm-beach-florida.html", "Royal Palm Beach, FL"),
    ("mico-florida.html", "Mico, FL"),
]
PLACE_LOOKUP = {re.sub(r"\s+", " ", name).strip().lower(): href for href, name in PLACES}

NEIGHBORHOODS = [
    ("portstluciecarlton.html", "Port St Lucie - Carlton"),
    ("se-morningside-blvd.html", "SE PORT ST LUCIE BLVD & SE MORNINGSIDE BLVD"),
]

PAGES = [
    "index.html",
    "about.html",
    "services.html",
    "contact.html",
    "our-work.html",
    "tree-removal.html",
    "emergency-tree-removal.html",
    "palm-tree-trimming.html",
    "stump-removal.html",
    "commercial-tree-service.html",
    "tree-care-prevention.html",
    "brush-cleaning.html",
    "land-lot-clearing.html",
    "storm-damage-clean-up.html",
    "large-tree-removal.html",
    "crane-assisted-tree-removal.html",
    "hazardous-dangerous-tree-removal.html",
    "oak-tree-removal.html",
    "dead-diseased-tree-removal.html",
    "tree-removal-near-houses-buildings.html",
    "tree-removal-for-construction.html",
    "locations-port-st-lucie.html",
    "neighborhoods.html",
    "royal-palm-beach-florida.html",
    "fort-pierce-florida.html",
    "palm-city-florida.html",
    "riviera-beach-fl.html",
    "se-morningside-blvd.html",
    "port-st-lucie-flordia.html",
    "florida-ridge-fl.html",
    "portstluciecarlton.html",
    "mico-florida.html",
    "stuart-flordia.html",
    "vero-beach-florida.html",
    "sebastian-florida.html",
    "jupiter-florida.html",
    "hobo-sound-fl.html",
    "palm-beach-gardens-florida.html",
]

JUNK = {
    "* indicates required field",
    "name *",
    "first",
    "last",
    "phone number *",
    "email *",
    "comment *",
    "submit",
}

# Photos downloaded from the live site. Alt text matches the live page
# except the quote graphic, whose live alt was the generic word "Picture".
LOGO = ("/images/mark.svg", "Port St Lucie Tree Service logo", 64, 64)
HERO_PHOTO = "/images/live/background-images/209300239.jpg"
TREES_PHOTO = "/images/live/background-images/1436807259.jpg"
HOME_PHOTOS = {
    "Tree Removal": (
        "/images/live/tree-removal-pros-port-st-lucie-tree-removal-1_orig.jpg",
        "tree removal in progress",
        1067,
        800,
    ),
    "Stump Removal": (
        "/images/live/tree-removal-pros-port-st-lucie-stump-removal-1_orig.jpg",
        "tree stump got removed",
        1100,
        733,
    ),
    "Commercial Tree Service": (
        "/images/live/tree-removal-pros-port-st-lucie-commercial-tree-service-1_orig.jpg",
        "commercial tree service worker working",
        1059,
        800,
    ),
    "Tree Care Prevention": (
        "/images/live/tree-removal-pros-port-st-lucie-tree-care-prevention-1_orig.jpg",
        "tree care service in progress",
        1100,
        733,
    ),
    "Brush Cleaning": (
        "/images/live/tree-removal-pros-port-st-lucie-brush-cleaning-1_orig.jpg",
        "tree care worker working on brush cleaning",
        1100,
        728,
    ),
    "Storm Damage Clean Up": (
        "/images/live/tree-removal-pros-port-st-lucie-storm-damage-clean-up-1_orig.jpg",
        "tree fallen on car after storm",
        1100,
        733,
    ),
}
PAGE_PHOTOS = {
    "about.html": (
        "/images/live/tree-removal-pros-port-st-lucie-about_orig.jpg",
        "tree care expert during work",
        1100,
        734,
    ),
    "services.html": (
        "/images/live/tree-removal-pros-port-st-lucie-services_orig.jpg",
        "tree logs after removal",
        1100,
        733,
    ),
    "contact.html": (
        "/images/live/tree-removal-pros-port-st-lucie-contact_orig.jpg",
        "woman smiling taking phone call",
        1100,
        733,
    ),
    "tree-removal.html": (
        "/images/live/tree-removal-pros-port-st-lucie-tree-removal-2_orig.jpg",
        "tree removal in progress",
        1100,
        731,
    ),
    "stump-removal.html": (
        "/images/live/tree-removal-pros-port-st-lucie-stump-removal-2_orig.jpg",
        "stump left behind after tree got removed",
        1067,
        800,
    ),
    "commercial-tree-service.html": (
        "/images/live/tree-removal-pros-port-st-lucie-commercial-tree-service-2_orig.jpg",
        "tree care expert during work",
        1057,
        800,
    ),
    "brush-cleaning.html": (
        "/images/stock/brush-cleaning.jpg",
        "Brush and undergrowth cleared from a yard",
        1200,
        800,
    ),
    "palm-tree-trimming.html": (
        "/images/stock/palm-tree-trimming.jpg",
        "Palm tree trimming work",
        1200,
        901,
    ),
    "tree-care-prevention.html": (
        "/images/stock/tree-trimming.jpg",
        "Tree trimming and pruning in progress",
        1200,
        800,
    ),
    "land-lot-clearing.html": (
        "/images/stock/land-lot-clearing.jpg",
        "Land and lot clearing in progress",
        1200,
        675,
    ),
    "emergency-tree-removal.html": (
        "/images/live/tree-removal-pros-port-st-lucie-storm-damage-clean-up-2_orig.jpg",
        "Emergency tree removal after storm damage",
        1100,
        736,
    ),
    "large-tree-removal.html": (
        "/images/stock/large-tree-removal.jpg",
        "Large tree removal",
        1200,
        1797,
    ),
    "crane-assisted-tree-removal.html": (
        "/images/stock/crane-tree-removal.jpg",
        "Crane-assisted tree removal",
        1200,
        687,
    ),
    "hazardous-dangerous-tree-removal.html": (
        "/images/stock/hazardous-tree.jpg",
        "Hazardous tree near a property",
        1200,
        828,
    ),
    "oak-tree-removal.html": (
        "/images/stock/oak-tree.jpg",
        "Oak tree on a residential lot",
        1200,
        799,
    ),
    "dead-diseased-tree-removal.html": (
        "/images/stock/dead-diseased-tree.jpg",
        "Dead or diseased tree",
        1200,
        800,
    ),
    "tree-removal-near-houses-buildings.html": (
        "/images/stock/tree-near-house.jpg",
        "Tree close to a house",
        1200,
        800,
    ),
    "tree-removal-for-construction.html": (
        "/images/stock/construction-clearing.jpg",
        "Trees cleared for construction",
        1200,
        675,
    ),
    "storm-damage-clean-up.html": (
        "/images/live/tree-removal-pros-port-st-lucie-storm-damage-clean-up-2_orig.jpg",
        "tree damaged after storm",
        1100,
        736,
    ),
    "florida-ridge-fl.html": ("/images/live/flordia-ridge-tree-service_orig.jpg", "Picture", 331, 359),
    "fort-pierce-florida.html": ("/images/live/fort-pierce-fl-tree-service_orig.jpg", "Picture", 278, 326),
    "hobo-sound-fl.html": ("/images/live/hobe-sound-fl-tree-service_orig.jpg", "Picture", 310, 448),
    "jupiter-florida.html": ("/images/live/tree-service-jupiter-fl_orig.jpg", "Picture", 281, 285),
    "mico-florida.html": ("/images/live/tree-service-mico-fl_orig.jpg", "Picture", 258, 340),
    "palm-beach-gardens-florida.html": ("/images/live/palm-beach-gardens-tree-service_orig.jpg", "Picture", 265, 206),
    "palm-city-florida.html": ("/images/live/published/palm-city-fl-tree-service.jpg", "Picture", 413, 394),
    "port-st-lucie-flordia.html": ("/images/live/port-st-lucie_orig.jpg", "Picture", 300, 368),
    "riviera-beach-fl.html": ("/images/live/published/riviera-beach-fl-tree-service.jpg", "Picture", 252, 339),
    "royal-palm-beach-florida.html": ("/images/live/tree-service-mico-fl_1.jpg", "Picture", 258, 340),
    "sebastian-florida.html": ("/images/live/tree-service-sebastian-fl_orig.jpg", "Picture", 324, 484),
    "stuart-flordia.html": ("/images/live/concrete-contractors-stuart-fl_orig.jpg", "Picture", 305, 498),
    "vero-beach-florida.html": ("/images/live/published/tree-service-vero-beach-fl.jpg", "Picture", 296, 250),
}


def clean_text(fragment):
    fragment = re.sub(r"<br\s*/?>", " ", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = unescape(fragment).replace("\xa0", " ")
    return re.sub(r"\s+", " ", fragment).strip()


def is_junk(text):
    lowered = text.lower().strip()
    return lowered in JUNK or lowered.startswith("* indicates required")


def inline_html(fragment):
    holders = []

    def repl(match):
        href = unescape(match.group(1)).strip()
        text = clean_text(match.group(2))
        if not text:
            return ""
        internal = href.startswith("/") and "://" not in href
        if href.startswith("tel:") or internal:
            if href in ("/index.html", "/"):
                href = "/"
            token = f"\x00A{len(holders)}\x00"
            holders.append(f'<a href="{escape(href, quote=True)}">{escape(text)}</a>')
            return token
        return text

    fragment = re.sub(
        r'<a\b[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
        repl,
        fragment,
        flags=re.S | re.I,
    )
    fragment = re.sub(r"<br\s*/?>", " ", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = unescape(fragment).replace("\xa0", " ")
    fragment = re.sub(r"[ \t]+", " ", fragment)
    fragment = re.sub(r"\s+", " ", fragment).strip()
    for index, html in enumerate(holders):
        fragment = fragment.replace(f"\x00A{index}\x00", html)
    return fragment


def paragraph_blocks(inner):
    blocks = []
    parts = re.split(r"(<ul[\s\S]*?</ul>)", inner, flags=re.I)
    for part in parts:
        if part.lower().startswith("<ul"):
            items = []
            for item in re.findall(r"<li[^>]*>(.*?)</li>", part, flags=re.S | re.I):
                text = clean_text(item)
                if text:
                    items.append(text)
            if items:
                blocks.append(("ul", items))
            continue
        pieces = re.split(r"<strong>(.*?)</strong>", part, flags=re.S | re.I)
        for index, piece in enumerate(pieces):
            if index % 2 == 1:
                title = clean_text(piece)
                if title and not is_junk(title):
                    blocks.append(("h2", title))
                continue
            html = inline_html(piece)
            plain = re.sub(r"<[^>]+>", "", html).strip()
            if html and not is_junk(plain):
                blocks.append(("p", html))
    return blocks


def extract(filename):
    raw = (AUDIT / filename).read_text(encoding="utf-8", errors="replace")
    match = re.search(r'id="wsite-content"(.*?)(?=<div class="footer-wrap">)', raw, re.S)
    if not match:
        raise SystemExit(f"No content region in {filename}")
    chunk = re.sub(r"<script[\s\S]*?</script>", "", match.group(1), flags=re.I)
    chunk = re.sub(r"<style[\s\S]*?</style>", "", chunk, flags=re.I)
    h1 = None
    blocks = []
    pattern = re.compile(
        r"<h1[^>]*>(.*?)</h1>|<h2[^>]*>(.*?)</h2>|<div class=\"paragraph\"[^>]*>(.*?)</div>",
        re.S | re.I,
    )
    for found in pattern.finditer(chunk):
        if found.group(1) is not None:
            h1 = clean_text(found.group(1)) or h1
        elif found.group(2) is not None:
            title = clean_text(found.group(2))
            if title:
                blocks.append(("h2", title))
        else:
            blocks.extend(paragraph_blocks(found.group(3)))
    if not h1:
        for index, (kind, value) in enumerate(blocks):
            if kind == "h2":
                h1 = value
                del blocks[index]
                break
    return {"h1": h1, "blocks": blocks}


def render_ul(items):
    lis = []
    for item in items:
        key = re.sub(r"\s+", " ", item).strip().lower()
        href = PLACE_LOOKUP.get(key)
        if href:
            lis.append(f'<li><a href="/{href}">{escape(item)}</a></li>')
        else:
            lis.append(f"<li>{escape(item)}</li>")
    return '<ul class="place-list">' + "".join(lis) + "</ul>"


def render_blocks(blocks):
    html = []
    for kind, value in blocks:
        if kind == "h2":
            html.append(f"<h2>{escape(value)}</h2>")
        elif kind == "p":
            html.append(f"<p>{value}</p>")
        elif kind == "ul":
            html.append(render_ul(value))
    return "\n".join(html)


def canon(filename):
    if filename == "index.html":
        return BASE + "/"
    return f"{BASE}/{filename}"


def description_for(filename, extracted):
    seo = SEO[filename]
    if seo.get("description"):
        return re.sub(r"\s+", " ", seo["description"]).strip()
    for kind, value in extracted["blocks"]:
        if kind == "p":
            plain = re.sub(r"<[^>]+>", "", value)
            plain = re.sub(r"\s+", " ", plain).strip()
            if len(plain) <= 165:
                return plain
            cut = plain[:157]
            if " " in cut:
                cut = cut.rsplit(" ", 1)[0]
            return cut.rstrip(".,;:") + "."
    og = (seo.get("og") or {}).get("og:description") or [None]
    return og[0]


def picture(src, alt, width, height, lazy=True, cls=""):
    loading = "lazy" if lazy else "eager"
    class_attr = f' class="{cls}"' if cls else ""
    return (
        f'<img src="{src}" alt="{escape(alt, quote=True)}" width="{width}" height="{height}"'
        f'{class_attr} loading="{loading}" decoding="async">'
    )


def page_figure(filename):
    photo = PAGE_PHOTOS.get(filename)
    if not photo:
        return ""
    src, alt, width, height = photo
    return f'<figure class="page-photo">{picture(src, alt, width, height)}</figure>'


def tally():
    src = (
        "https://tally.so/embed/xX6B0y?alignLeft=1&hideTitle=1"
        "&transparentBackground=1&dynamicHeight=1&source=Port+St+Lucie+Tree+Service"
    )
    return f"""
    <div class="quote-card" id="quote">
      <small>Get a tree estimate</small>
      <p>{escape(BUSINESS)}</p>
      <iframe data-tally-src="{src}" loading="lazy" width="100%" height="552" frameborder="0" marginheight="0" marginwidth="0" title="Port St Lucie Tree Service quote form"></iframe>
    </div>"""


def tally_script():
    return """
<script>
var d=document,w="https://tally.so/widgets/embed.js",v=function(){if(typeof Tally!=="undefined"){Tally.loadEmbeds();}else{d.querySelectorAll("iframe[data-tally-src]:not([src])").forEach(function(e){e.src=e.dataset.tallySrc;});}};if(typeof Tally!=="undefined"){v();}else if(d.querySelector('script[src="'+w+'"]')==null){var s=d.createElement("script");s.src=w;s.onload=v;s.onerror=v;d.body.appendChild(s);}
</script>"""


def here(filename, href):
    path = href[1:] if href.startswith("/") else href
    if href == "/" and filename == "index.html":
        return ' aria-current="page"'
    if path == filename:
        return ' aria-current="page"'
    return ""


def nav(filename):
    service_links = "\n".join(
        f'<li><a href="/{href}"{here(filename, "/" + href)}>{escape(label)}</a></li>'
        for href, label in SERVICES
    )
    place_links = "\n".join(
        f'<li><a href="/{href}"{here(filename, "/" + href)}>{escape(label)}</a></li>'
        if href
        else f"<li><span>{escape(label)}</span></li>"
        for href, label in PLACES
    )
    neighborhood_links = "\n".join(
        f'<li><a href="/{href}"{here(filename, "/" + href)}>{escape(label)}</a></li>'
        for href, label in NEIGHBORHOODS
    )
    services_current = filename in {href for href, _ in SERVICES} or filename == "services.html"
    places_current = filename in {href for href, _ in PLACES if href} or filename in {
        "locations-port-st-lucie.html",
        "neighborhoods.html",
        "portstluciecarlton.html",
        "se-morningside-blvd.html",
    }
    estimate = "/#quote" if filename == "index.html" else "/contact.html#quote"
    return f"""
    <nav class="site-nav" id="site-nav" aria-label="Primary">
      <ul>
        <li><a href="/"{here(filename, "/")}>Home</a></li>
        <li class="has-sub">
          <a class="nav-parent" href="/services.html"{' aria-current="page"' if services_current else ""}>Services</a>
          <ul class="sub">
            <li><a href="/services.html"{here(filename, "/services.html")}>All services</a></li>
            {service_links}
          </ul>
        </li>
        <li class="has-sub">
          <a class="nav-parent" href="/locations-port-st-lucie.html"{' aria-current="page"' if places_current else ""}>Service area</a>
          <ul class="sub places-menu">
            <li><a href="/locations-port-st-lucie.html"{here(filename, "/locations-port-st-lucie.html")}>All locations</a></li>
            {place_links}
            <li><a href="/neighborhoods.html"{here(filename, "/neighborhoods.html")}>Neighborhoods</a></li>
            {neighborhood_links}
          </ul>
        </li>
        <li><a href="/about.html"{here(filename, "/about.html")}>About</a></li>
        <li><a href="/contact.html"{here(filename, "/contact.html")}>Contact</a></li>
      </ul>
    </nav>
    <div class="header-actions">
      <a class="btn btn-ghost btn-call" href="{TEL}">{PHONE_ICON}<strong>Call {PHONE}</strong></a>
      <a class="btn btn-solid" href="{estimate}">Request an estimate</a>
    </div>"""


OFFICE_HOURS = "Monday–Sunday: 7 am – 7 pm"
OFFICE_HOURS_DAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)
OFFICE_HOURS_TIME = "7 am – 7 pm"
PHONE_ICON = '<svg class="phone-icon" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1.1-.3 1.2.4 2.5.6 3.8.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.6.6 3.8.1.4 0 .8-.3 1.1L6.6 10.8z"/></svg>'


def phone_link(extra_class=""):
    cls = "phone-link" + (f" {extra_class}" if extra_class else "")
    return f'<a class="{cls}" href="{TEL}">{PHONE_ICON}<strong>{PHONE}</strong></a>'


def office_hours_block():
    rows = "".join(
        f"<div><span>{day}</span><span>{OFFICE_HOURS_TIME}</span></div>"
        for day in OFFICE_HOURS_DAYS
    )
    return f'<div class="hours-list">{rows}</div>'


def footer():
    services = "\n".join(
        f'<li><a href="/{href}">{escape(label)}</a></li>' for href, label in SERVICES
    )
    return f"""
  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <h2>Company</h2>
        <p>Tree removal and trimming for homeowners in Port St. Lucie and nearby towns.</p>
        <p>{phone_link()}</p>
        <ul>
          <li><a href="/about.html">About</a></li>
          <li><a href="/our-work.html">Our Work</a></li>
          <li><a href="/contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h2>Services</h2>
        <ul>{services}</ul>
      </div>
      <div>
        <h2>Quick Links</h2>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/services.html">All services</a></li>
          <li><a href="/locations-port-st-lucie.html">Service Areas</a></li>
          <li><a href="/neighborhoods.html">Neighborhoods</a></li>
          <li><a href="/contact.html#quote">Request an estimate</a></li>
        </ul>
      </div>
      <div>
        <h2>Office Hours</h2>
        {office_hours_block()}
      </div>
    </div>
    <div class="wrap legal">
      <p>{escape(BUSINESS)}. Port St. Lucie, Florida. {phone_link()}</p>
    </div>
  </footer>
  <div class="mobile-bar">
    <a class="btn btn-ghost" href="{TEL}">{PHONE_ICON} Call</a>
    <a class="btn btn-solid" href="/contact.html#quote">Request estimate</a>
  </div>"""


def crumbs(items):
    parts = []
    for href, label in items:
        if href:
            parts.append(f'<li><a href="{escape(href, quote=True)}">{escape(label)}</a></li>')
        else:
            parts.append(f"<li>{escape(label)}</li>")
    return f'<nav aria-label="Breadcrumb"><ol class="crumbs">{"".join(parts)}</ol></nav>'


def json_ld():
    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": BUSINESS,
        "telephone": "+1-772-492-4436",
        "url": BASE + "/",
    }
    return json.dumps(data, ensure_ascii=False)


def shell(filename, main, with_tally=False):
    meta = META[filename]
    title = meta["title"]
    description = meta["description"]
    canonical = canon(filename)
    desc_tag = f'\n<meta name="description" content="{escape(description, quote=True)}">'
    og_desc = f'\n<meta property="og:description" content="{escape(description, quote=True)}">'
    if filename in PAGE_PHOTOS:
        share = PAGE_PHOTOS[filename][0]
    elif filename == "index.html":
        share = HERO_PHOTO
    else:
        share = TREES_PHOTO
    og_image = f'\n<meta property="og:image" content="{BASE}{share}">'
    tally_js = tally_script() if with_tally else ""
    logo_src, logo_alt, logo_w, logo_h = LOGO
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>{desc_tag}
<link rel="canonical" href="{canonical}">
<meta property="og:site_name" content="{escape(SITE_NAME, quote=True)}">
<meta property="og:title" content="{escape(title, quote=True)}">{og_desc}
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">{og_image}
<meta name="theme-color" content="#1b3024">
<link rel="icon" href="/images/mark.svg" type="image/svg+xml">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">{json_ld()}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="utility">
  <div class="wrap utility-inner">
    <span>Port St. Lucie, Florida · {OFFICE_HOURS}</span>
    {phone_link()}
  </div>
</div>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/">
      {picture(logo_src, logo_alt, logo_w, logo_h, lazy=False)}
      <span>Port St Lucie<small>Tree Service</small></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    {nav(filename)}
  </div>
</header>
{main}
{footer()}
<script src="/js/site.js"></script>
{tally_js}
</body>
</html>
"""


def place_section():
    return f"""
    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <p class="kicker">Service area</p>
          <h2>Locations we serve</h2>
        </div>
        {render_ul([name for _, name in PLACES])}
        <p><a href="/neighborhoods.html">Neighborhoods</a></p>
      </div>
    </section>"""


def related_services(filename):
    links = "".join(
        f'<li><a href="/{href}">{escape(label)}</a></li>'
        for href, label in SERVICES
        if href != filename
    )
    return f"""
    <section class="section">
      <div class="wrap">
        <h2>Services</h2>
        <ul class="related">{links}</ul>
      </div>
    </section>"""


MAP_SRC = (
    "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d131340.077642477"
    "!2d-80.3924825!3d27.290052!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2"
    "!1s0x88deebae10c38979%3A0x34a1ee4d9dd96ba5!2sPort%20St%20Lucie%20Tree%20Service"
    "!5e1!3m2!1sen!2suk!4v1791843374669!5m2!1sen!2suk"
)


def map_embed():
    return f"""
    <div class="map-frame">
      <iframe src="{MAP_SRC}" width="600" height="450" style="border:0;" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin" title="Port St Lucie Tree Service on Google Maps"></iframe>
    </div>"""


def map_section():
    return f"""
    <section class="section map-section">
      <div class="wrap">
        {map_embed()}
      </div>
    </section>"""


def cta_band(intro="", heading="Call us today"):
    extra = f"<p>{intro}</p>" if intro else ""
    return f"""
    <section class="band">
      <div class="wrap band-inner">
        <div class="band-copy">
          <h2>{escape(heading)}</h2>
          {extra}
        </div>
        <div class="band-panel">
          <a class="band-phone" href="{TEL}">{PHONE}</a>
          <div class="cta-actions">
            <a class="btn btn-solid" href="{TEL}">CLICK TO CALL</a>
            <a class="btn btn-ghost" href="/contact.html#quote">Request an estimate</a>
          </div>
        </div>
      </div>
    </section>"""


def render_home(extracted):
    lede = about = intro = closing = None
    services = []
    mode = None
    current = None
    for kind, value in extracted["blocks"]:
        if kind == "h2" and value == "About Us":
            mode = "about"
        elif kind == "h2" and value == "Our Services":
            mode = "intro"
        elif kind == "h2" and value in SERVICE_URL:
            mode = "service"
            current = value
        elif kind == "h2" and value == "Call Us Today":
            mode = "close"
        elif kind == "p":
            if mode is None and lede is None:
                lede = value
            elif mode == "about" and about is None:
                about = value
            elif mode == "intro" and intro is None:
                intro = value
            elif mode == "service" and current:
                services.append((current, value))
                current = None
            elif mode == "close" and closing is None:
                closing = value
    by_name = dict(services)
    cards = []
    for name, paragraph in services:
        href = SERVICE_URL[name]
        src, alt, width, height = HOME_PHOTOS[name]
        cards.append(
            f"""<article class="service-card">
              {picture(src, alt, width, height)}
              <div>
                <h2><a href="/{href}">{escape(name)}</a></h2>
                <p>{paragraph}</p>
                <p><a class="details" href="/{href}">Details</a></p>
              </div>
            </article>"""
        )
    about_src, about_alt, about_w, about_h = PAGE_PHOTOS["about.html"]
    commercial_src, commercial_alt, commercial_w, commercial_h = PAGE_PHOTOS["commercial-tree-service.html"]
    main = f"""
<main id="main">
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="eyebrow">Port St Lucie Tree service</p>
        <h1>{escape(extracted["h1"])}</h1>
        <p class="lede">{lede}</p>
        <div class="hero-actions">
          <a class="btn btn-solid" href="#quote">Request an estimate</a>
          <a class="btn btn-ghost" href="{TEL}">CALL NOW</a>
        </div>
        <p class="hero-more"><a href="/services.html">LEARN MORE</a></p>
      </div>
      {tally()}
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">Our services</p>
        <h2>Our Services</h2>
        <p>{intro}</p>
      </div>
      <div class="service-list">
        {"".join(cards)}
      </div>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="wrap feature-grid">
      <article class="feature">
        {picture(about_src, about_alt, about_w, about_h)}
        <div>
          <p class="kicker">About us</p>
          <h2>About Us</h2>
          <p>{about}</p>
          <p><a class="details" href="/about.html">About</a></p>
        </div>
      </article>
      <article class="feature">
        {picture(commercial_src, commercial_alt, commercial_w, commercial_h)}
        <div>
          <p class="kicker">Commercial</p>
          <h2>Commercial Tree Service</h2>
          <p>{by_name["Commercial Tree Service"]}</p>
          <p><a class="details" href="/commercial-tree-service.html">Details</a></p>
        </div>
      </article>
    </div>
  </section>
  {place_section()}
  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">Questions</p>
        <h2>Questions before you call</h2>
      </div>
      <div class="faq">
        <details>
          <summary>Which tree services are offered?</summary>
          <p>{intro}</p>
        </details>
        <details>
          <summary>Can you remove a stump after a tree is already down?</summary>
          <p>{services[1][1]}</p>
        </details>
        <details>
          <summary>Do you work on commercial property?</summary>
          <p>{services[2][1]}</p>
        </details>
        <details>
          <summary>What should I do after a storm?</summary>
          <p>{services[5][1]}</p>
        </details>
        <details>
          <summary>How do I reach you?</summary>
          <p>{closing} <a href="{TEL}">{PHONE}</a></p>
        </details>
      </div>
    </div>
  </section>
  {map_section()}
  {cta_band(closing, "Call Us Today")}
</main>"""
    return shell("index.html", extracted, main, with_tally=True)


def crumb_for(filename, h1):
    if filename == "services.html":
        return crumbs([("/", "Home"), (None, "Services")])
    if filename == "our-work.html":
        return crumbs([("/", "Home"), (None, "Our Work")])
    if filename in {href for href, _ in SERVICES}:
        return crumbs([("/", "Home"), ("/services.html", "Services"), (None, h1)])
    if filename in {href for href, _ in NEIGHBORHOODS}:
        return crumbs([("/", "Home"), ("/neighborhoods.html", "Neighborhoods"), (None, h1)])
    if filename in {href for href, _ in PLACES if href}:
        return crumbs([("/", "Home"), ("/locations-port-st-lucie.html", "Locations"), (None, h1)])
    if filename == "locations-port-st-lucie.html":
        return crumbs([("/", "Home"), (None, "Locations")])
    if filename == "neighborhoods.html":
        return crumbs([("/", "Home"), (None, "Neighborhoods")])
    if filename == "about.html":
        return crumbs([("/", "Home"), (None, "About")])
    if filename == "contact.html":
        return crumbs([("/", "Home"), (None, "Contact")])
    return crumbs([("/", "Home"), (None, h1)])


def render_neighborhoods(extracted):
    links = "".join(
        f'<li><a href="/{href}">{escape(label)}</a></li>' for href, label in NEIGHBORHOODS
    )
    h1 = "Neighborhoods"
    main = f"""
<main id="main">
  <div class="page-hero photo-trees"><div class="wrap">{crumb_for("neighborhoods.html", h1)}<h1>{h1}</h1></div></div>
  <section class="section">
    <div class="wrap prose">
      <p>Neighborhood pages on this site:</p>
      <ul class="place-list">{links}</ul>
    </div>
  </section>
  {related_services("neighborhoods.html")}
  {map_section()}
  {cta_band()}
</main>"""
    extracted = {"h1": h1, "blocks": [("p", "Neighborhood pages on this site.")]}
    return shell("neighborhoods.html", extracted, main)


def render_page(filename, extracted):
    h1 = extracted["h1"] or SEO[filename]["title"]
    body = render_blocks(extracted["blocks"])
    extra = ""
    if filename in {href for href, _ in SERVICES} or filename == "services.html":
        extra = place_section() + related_services(filename)
    elif filename != "contact.html":
        extra = related_services(filename)
    figure = page_figure(filename)
    place_pages = {href for href, _ in PLACES if href} | {href for href, _ in NEIGHBORHOODS} | {
        "locations-port-st-lucie.html",
        "neighborhoods.html",
    }
    hero_class = "page-hero photo-trees" if filename in place_pages else "page-hero photo-work"
    if filename == "contact.html":
        content = f'<div class="contact-grid"><div>{figure}<div class="prose">{body}</div></div>{tally()}</div>'
    elif figure:
        content = f'<div class="story">{figure}<div class="prose">{body}</div></div>'
    else:
        content = f'<div class="prose">{body}</div>'
    main = f"""
<main id="main">
  <div class="{hero_class}"><div class="wrap">{crumb_for(filename, h1)}<h1>{escape(h1)}</h1></div></div>
  <section class="section"><div class="wrap">{content}</div></section>
  {extra}
  {map_section()}
  {"" if filename == "contact.html" else cta_band()}
</main>"""
    return shell(filename, extracted, main, with_tally=filename == "contact.html")


def write_sitemap():
    urls = [BASE + "/"] + [f"{BASE}/{name}" for name in PAGES if name != "index.html"]
    body = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in urls:
        body.append("  <url>")
        body.append(f"    <loc>{url}</loc>")
        body.append("  </url>")
    body.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(body) + "\n", encoding="utf-8")


def write_robots():
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: https://www.portstlucietrees.com/sitemap.xml\n",
        encoding="utf-8",
    )


def service_card_html(cards):
    parts = []
    for href, label, blurb, photo_key in cards:
        src, alt, width, height = PAGE_PHOTOS[photo_key]
        parts.append(
            f"""<article class="service-card">
              {picture(src, alt, width, height)}
              <div>
                <h2><a href="/{href}">{escape(label)}</a></h2>
                <p>{escape(blurb)}</p>
                <p class="card-link"><a class="details" href="/{href}">Details</a></p>
              </div>
            </article>"""
        )
    return "".join(parts)


def faq_html(items):
    blocks = []
    for question, answer in items:
        extra = ""
        if question.startswith("Do I need a permit"):
            extra = f' <a href="{PERMIT_URL}">City of Port St. Lucie tree rules</a>.'
        blocks.append(
            f"<details><summary>{escape(question)}</summary><p>{escape(answer)}{extra}</p></details>"
        )
    return f'<div class="faq">{"".join(blocks)}</div>'


def locations_home_section():
    links = "".join(
        f'<li><a href="/{href}">{escape(label)}</a></li>' if href else f"<li>{escape(label)}</li>"
        for href, label in PLACES
    )
    return f"""
  <section class="section locations-band" style="padding-top:0">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">Service area</p>
        <h2>Locations we serve</h2>
        <p>Tree removal and trimming across Port St. Lucie and nearby Treasure Coast towns.</p>
      </div>
      <ul class="place-list location-chips">{links}</ul>
      <p><a class="details" href="/locations-port-st-lucie.html">All service areas</a> · <a class="details" href="/neighborhoods.html">Neighborhoods</a></p>
    </div>
  </section>"""


def render_home_page():
    reviews = "".join(
        f"""<blockquote class="review">
              <h3>{escape(name)}</h3>
              <p class="stars" aria-label="5 out of 5 stars">★★★★★</p>
              <p>{escape(text)}</p>
              <footer>Google review</footer>
            </blockquote>"""
        for name, text in REVIEWS
    )
    main = f"""
<main id="main">
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="eyebrow">Port St. Lucie, Florida</p>
        <h1>Tree Removal in Port St. Lucie</h1>
        <p class="lede">{escape(HOME_INTRO)}</p>
        <div class="hero-actions">
          <a class="btn btn-solid" href="#quote">Request an estimate</a>
          <a class="btn btn-ghost btn-call" href="{TEL}">{PHONE_ICON}<strong>CALL NOW</strong></a>
        </div>
        <p class="hero-more"><a href="/services.html">LEARN MORE</a></p>
      </div>
      {tally()}
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">Our services</p>
        <h2>Our Services</h2>
      </div>
      <div class="service-list">
        {service_card_html(HOME_CARDS)}
      </div>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">Google reviews</p>
        <h2>What homeowners wrote</h2>
        <p class="stars section-stars" aria-label="5 out of 5 stars">★★★★★</p>
        <p>The Google listing shows 5.0 from 17 reviews. These three are from that listing.</p>
      </div>
      <div class="review-list">
        {reviews}
      </div>
      <p><a class="details" href="{GOOGLE_PROFILE}">Read the Google reviews</a></p>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="wrap work-note">
      <div>
        <p class="kicker">Our work</p>
        <h2>Recent jobs</h2>
        <p>Photos of finished jobs will go on the work page. Call if you want to ask what a similar tree looked like after the crew left.</p>
        <p><a class="details" href="/our-work.html">Our Work</a></p>
      </div>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">Questions</p>
        <h2>Questions before you call</h2>
      </div>
      {faq_html(HOME_FAQS)}
    </div>
  </section>
  {locations_home_section()}
  {map_section()}
</main>"""
    return shell("index.html", main, with_tally=True)


def service_related_links(filename, limit=4):
    items = []
    for href, label in SERVICES:
        if href == filename:
            continue
        items.append(f'<li><a href="/{href}">{escape(label)}</a></li>')
        if len(items) >= limit:
            break
    return "".join(items)


def service_gallery(photo_key, alt_fallback="Tree service work"):
    primary = PAGE_PHOTOS.get(photo_key) or PAGE_PHOTOS["tree-removal.html"]
    src, alt, width, height = primary
    # Pair with a second job photo when available for a Valdosta-style gallery
    secondary_keys = [
        "stump-removal.html",
        "storm-damage-clean-up.html",
        "tree-care-prevention.html",
        "brush-cleaning.html",
    ]
    second = None
    for key in secondary_keys:
        if key != photo_key and key in PAGE_PHOTOS:
            second = PAGE_PHOTOS[key]
            break
    figures = [
        f'<figure class="service-shot">{picture(src, alt or alt_fallback, width, height)}</figure>'
    ]
    if second:
        s_src, s_alt, s_w, s_h = second
        figures.append(
            f'<figure class="service-shot">{picture(s_src, s_alt, s_w, s_h)}</figure>'
        )
    return f'<div class="service-gallery">{"".join(figures)}</div>'


def render_service(filename):
    data = SERVICE_PAGES[filename]
    raw_h1 = data["h1"]
    if "Port St. Lucie" in raw_h1 or "Port St Lucie" in raw_h1:
        h1 = raw_h1
    else:
        h1 = f"{raw_h1} in Port St. Lucie, FL"
    eyebrow = data.get("eyebrow") or raw_h1
    lede = data.get("lede") or data.get("intro", "")
    story_h2 = data.get("story_h2") or f"Where {raw_h1.lower()} fits local properties"
    story = data.get("story") or data.get("intro", "")
    when = "".join(f"<li>{escape(item)}</li>" for item in data["when"])
    process = "".join(f"<li>{escape(item)}</li>" for item in data["process"])
    costs = "".join(f"<li>{escape(item)}</li>" for item in data["costs"])
    seo = data.get("seo_sections") or [
        (
            "What changes the job on Treasure Coast lots",
            "Sandy soil, tight setbacks, pool cages, and summer wind all change how a tree comes down. A photo of the trunk, the house, and the access path is enough to start an honest estimate.",
        ),
        (
            "What an estimate covers",
            "The estimate should include the tree size, how close it is to structures, equipment needs, haul-away, and stump grinding if you want it. We do not publish a flat price list.",
        ),
    ]
    seo_html = "".join(
        f"<h2>{escape(title)}</h2><p>{escape(body)}</p>" for title, body in seo
    )
    photo_key = filename if filename in PAGE_PHOTOS else "tree-removal.html"
    place_links = "".join(
        f'<li><a href="/{href}">{escape(label)}</a></li>' if href else f"<li>{escape(label)}</li>"
        for href, label in PLACES
        if href
    )
    main = f"""
<main id="main">
  <div class="crumb-bar">
    <div class="wrap">{crumb_for(filename, raw_h1)}</div>
  </div>
  <section class="hero slim-hero service-hero">
    <div class="wrap service-hero-inner">
      <p class="eyebrow">{escape(eyebrow)}</p>
      <h1>{escape(h1)}</h1>
      <p class="lede">{escape(lede)}</p>
      <div class="hero-actions">
        <a class="btn btn-solid" href="/contact.html#quote">Request an estimate</a>
        <a class="btn btn-ghost btn-call" href="{TEL}">{PHONE_ICON}<strong>Call {PHONE}</strong></a>
      </div>
    </div>
  </section>
  <section class="section service-body">
    <div class="wrap service-layout">
      <div class="service-main">
        {service_gallery(photo_key)}
        <div class="prose service-copy">
          <h2>{escape(story_h2)}</h2>
          <p>{escape(story)}</p>
          <h2>When to call</h2>
          <ul class="plain-list">{when}</ul>
          <h2>How the work goes</h2>
          <ol class="plain-list">{process}</ol>
          <h2>What changes the price</h2>
          <ul class="plain-list">{costs}</ul>
          {seo_html}
          <h2>Questions about this job</h2>
          {faq_html(data["faqs"])}
        </div>
      </div>
      <aside class="service-aside" aria-label="Estimate and related services">
        <div class="side-card" id="quote">
          <p class="side-kicker">Talk through the tree</p>
          <p>Call or send the property details. We will tell you if the job is a removal, a trim, or something that should wait for the utility.</p>
          <p class="side-phone">{phone_link("phone-link-lg")}</p>
          <p class="side-hours">{OFFICE_HOURS}</p>
          <p><a class="btn btn-solid" href="/contact.html#quote">Estimate form</a></p>
        </div>
        <div class="side-card side-card-muted">
          <p class="side-kicker">Related</p>
          <ul class="side-links">{service_related_links(filename)}</ul>
        </div>
      </aside>
    </div>
  </section>
  <section class="section section-towns" style="padding-top:0">
    <div class="wrap">
      <h2>Towns we serve</h2>
      <ul class="location-chips">{place_links}</ul>
      <p><a class="details" href="/locations-port-st-lucie.html">Service area</a> · <a class="details" href="/contact.html#quote">Request an estimate</a> · <a class="details" href="/services.html">All services</a></p>
    </div>
  </section>
</main>"""
    return shell(filename, main)


def render_location(filename):
    data = LOCATION_PAGES[filename]
    h1 = data["h1"]
    paragraphs = data["paragraphs"]
    lead = escape(paragraphs[0])
    rest = "".join(f"<p>{escape(paragraph)}</p>" for paragraph in paragraphs[1:])
    permit = ""
    if filename in {"port-st-lucie-flordia.html", "portstluciecarlton.html"}:
        permit = f'<p><a href="{PERMIT_URL}">Port St. Lucie protected-tree rules</a></p>'
    main = f"""
<main id="main">
  <section class="hero slim-hero location-hero">
    <div class="wrap hero-grid">
      <div>
        {crumb_for(filename, h1)}
        <p class="eyebrow">Service area</p>
        <h1>{escape(h1)}</h1>
        <p class="lede">{lead}</p>
        <div class="hero-actions">
          <a class="btn btn-solid" href="#quote">Request an estimate</a>
          <a class="btn btn-ghost btn-call" href="{TEL}">{PHONE_ICON}<strong>Call {PHONE}</strong></a>
        </div>
      </div>
      {tally()}
    </div>
  </section>
  <section class="section">
    <div class="wrap location-split">
      <div class="prose">
        {rest}
        {permit}
        <h2>Services for this property</h2>
        <ul>
          <li><a href="/tree-removal.html">Tree Removal</a></li>
          <li><a href="/large-tree-removal.html">Large Tree Removal</a></li>
          <li><a href="/tree-care-prevention.html">Tree Trimming &amp; Pruning</a></li>
          <li><a href="/palm-tree-trimming.html">Palm Tree Trimming &amp; Removal</a></li>
          <li><a href="/storm-damage-clean-up.html">Storm Damage Clean Up</a></li>
          <li><a href="/stump-removal.html">Stump Removal</a></li>
        </ul>
        <p>{phone_link("phone-link-lg")}</p>
      </div>
      {map_embed()}
    </div>
  </section>
</main>"""
    return shell(filename, main, with_tally=True)


def render_about_page():
    h1 = "About"
    main = f"""
<main id="main">
  <div class="page-hero photo-work"><div class="wrap">{crumb_for("about.html", h1)}<h1>{h1}</h1></div></div>
  <section class="section">
    <div class="wrap story">
      {page_figure("about.html")}
      <div class="prose">
        <p>Port St Lucie Tree Service removes, trims, and cleans up trees for homeowners. The work is the tree in your yard: how close it is to the house, whether it is dead, and what has to be hauled away.</p>
        <p>We do not publish awards, license numbers, or a street address on this site. Call {PHONE} and ask for the proof your property manager needs before the crew starts.</p>
        <p><a href="/services.html">Services</a> · <a href="/contact.html">Contact</a></p>
      </div>
    </div>
  </section>
  {map_section()}
  {cta_band()}
</main>"""
    return shell("about.html", main)


def render_services_index():
    h1 = "Services"
    main = f"""
<main id="main">
  <div class="page-hero photo-work"><div class="wrap">{crumb_for("services.html", h1)}<h1>{h1}</h1></div></div>
  <section class="section">
    <div class="wrap">
      <div class="prose">
        <p>Start with the problem. A tree on the house is not the same job as a stump in the lawn or brush along the fence.</p>
      </div>
      <div class="service-list">
        {service_card_html(HOME_CARDS)}
      </div>
    </div>
  </section>
  {map_section()}
  {cta_band()}
</main>"""
    return shell("services.html", main)


def render_contact_page():
    h1 = "Contact"
    main = f"""
<main id="main">
  <div class="page-hero photo-work"><div class="wrap">{crumb_for("contact.html", h1)}<h1>{h1}</h1></div></div>
  <section class="section">
    <div class="wrap contact-grid">
      <div class="prose">
        {page_figure("contact.html")}
        <p>Call {PHONE} or send the form. Say what the tree is doing, how close it is to the house, and whether a truck can reach the yard. A photo helps.</p>
        <p><a class="btn btn-dark" href="{TEL}">Call {PHONE}</a></p>
      </div>
      {tally()}
    </div>
  </section>
  {map_section()}
</main>"""
    return shell("contact.html", main, with_tally=True)


def render_our_work():
    h1 = "Our Work"
    main = f"""
<main id="main">
  <div class="page-hero photo-work"><div class="wrap">{crumb_for("our-work.html", h1)}<h1>{h1}</h1></div></div>
  <section class="section">
    <div class="wrap prose">
      <p>Photos of finished jobs will be added here. Until those are up, call {PHONE} and ask what a similar removal or trim looked like when the crew left.</p>
      <p><a class="btn btn-dark" href="{TEL}">Call {PHONE}</a></p>
    </div>
  </section>
  {map_section()}
  {cta_band()}
</main>"""
    return shell("our-work.html", main)


def render_locations_index():
    h1 = "Service Areas"
    links = render_ul([name for _, name in PLACES])
    main = f"""
<main id="main">
  <div class="page-hero photo-trees"><div class="wrap">{crumb_for("locations-port-st-lucie.html", h1)}<h1>{h1}</h1></div></div>
  <section class="section">
    <div class="wrap prose">
      <p>We take calls for homes in these towns. If your city is not linked, it does not have its own page yet. Call and ask before you assume the drive is too far.</p>
      {links}
      <p><a href="/neighborhoods.html">Neighborhoods</a></p>
    </div>
  </section>
  {map_section()}
  {cta_band()}
</main>"""
    return shell("locations-port-st-lucie.html", main)


def render_neighborhoods_page():
    links = "".join(
        f'<li><a href="/{href}">{escape(label)}</a></li>' for href, label in NEIGHBORHOODS
    )
    h1 = "Neighborhoods"
    main = f"""
<main id="main">
  <div class="page-hero photo-trees"><div class="wrap">{crumb_for("neighborhoods.html", h1)}<h1>{h1}</h1></div></div>
  <section class="section">
    <div class="wrap prose">
      <p>Neighborhood pages on this site:</p>
      <ul class="place-list">{links}</ul>
    </div>
  </section>
  {map_section()}
  {cta_band()}
</main>"""
    return shell("neighborhoods.html", main)


def validate():
    missing = [name for name in PAGES if not (ROOT / name).exists()]
    if missing:
        raise SystemExit(f"Missing pages: {missing}")
    problems = []
    for name in PAGES:
        text = (ROOT / name).read_text(encoding="utf-8")
        title = META[name]["title"]
        if f"<title>{escape(title)}</title>" not in text:
            problems.append(f"{name} title mismatch")
        if f'name="description" content="{escape(META[name]["description"], quote=True)}"' not in text:
            problems.append(f"{name} description mismatch")
        if f'rel="canonical" href="{canon(name)}"' not in text:
            problems.append(f"{name} canonical mismatch")
        if "<h1" not in text:
            problems.append(f"{name} missing h1")
        if text.count("<h1") != 1:
            problems.append(f"{name} h1 count {text.count('<h1')}")
        if name not in SERVICE_PAGES and "google.com/maps/embed" not in text:
            problems.append(f"{name} missing map")
        if "noindex" in text.lower():
            problems.append(f"{name} noindex")
        if "concretecolumbusga.com" in text or "Augusta" in text:
            problems.append(f"{name} stray claim")
        if "weebly.com" in text:
            problems.append(f"{name} weebly reference")
        for href in re.findall(r'href="(/[^"]*)"', text):
            path = href.split("#", 1)[0]
            if path in ("/", ""):
                continue
            target = ROOT / path.lstrip("/")
            if not target.exists():
                problems.append(f"{name} broken {href}")
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    contact = (ROOT / "contact.html").read_text(encoding="utf-8")
    if "source=Port+St+Lucie+Tree+Service" not in index or "source=Port+St+Lucie+Tree+Service" not in contact:
        problems.append("Tally source missing")
    if "number one" in index.lower() or "best tree company" in index.lower():
        problems.append("homepage still has an unverified claim")
    if problems:
        raise SystemExit("\n".join(problems))
    print(f"Built {len(PAGES)} pages")


def main():
    pages = {
        "index.html": render_home_page(),
        "about.html": render_about_page(),
        "services.html": render_services_index(),
        "contact.html": render_contact_page(),
        "our-work.html": render_our_work(),
        "locations-port-st-lucie.html": render_locations_index(),
        "neighborhoods.html": render_neighborhoods_page(),
    }
    for name in SERVICE_PAGES:
        pages[name] = render_service(name)
    for name in LOCATION_PAGES:
        pages[name] = render_location(name)
    missing = [name for name in PAGES if name not in pages]
    extra = [name for name in pages if name not in PAGES]
    if missing or extra:
        raise SystemExit(f"Page list mismatch missing={missing} extra={extra}")
    for name, html in pages.items():
        (ROOT / name).write_text(html, encoding="utf-8")
    write_sitemap()
    write_robots()
    validate()


if __name__ == "__main__":
    main()
