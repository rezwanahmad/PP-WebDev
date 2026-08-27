#!/usr/bin/env python3
"""Production smoke test for the Path Plaza contact and coordinated blog release.

The expected blog inventory is read from the retained local blog.html and sitemap.xml
baselines. Future article releases therefore update those two files—not this crawler.
"""
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
from datetime import datetime
from zoneinfo import ZoneInfo
import csv
import json
import re
import ssl

BASE = "https://pathplaza.com/"
SCRIPT = Path(__file__).resolve()
SITE_ROOT = SCRIPT.parents[2]
OUT = SITE_ROOT / "seo"
OUT.mkdir(parents=True, exist_ok=True)
NOW = datetime.now(ZoneInfo("Asia/Karachi"))
RUN_DATE = NOW.date().isoformat()
UA = f"Mozilla/5.0 (compatible; PathPlaza-Production-SmokeTest/{RUN_DATE})"
APPROVED = "92315-500-9620"
COMPACT = "923155009620"
WHATSAPP = "https://wa.me/923155009620"
PLAIN_EMAIL = "info@pathplaza.com"

# Full contact patterns only. A bare +44 is not treated as a failure because it may
# appear in unrelated editorial content.
PROHIBITED_PATTERNS = {
    "internal UK number": re.compile(r"(?:\+?44[\s-]*)?7577[\s-]*439[\s-]*898|wa\.me/447577439898", re.I),
    "obsolete Pakistan +92 315 5009620": re.compile(r"\+92[\s-]*315[\s-]*500[\s-]*9620", re.I),
    "obsolete Pakistan 0315 5009620": re.compile(r"(?<!\d)0315[\s-]*500[\s-]*9620(?!\d)", re.I),
}
PLACEHOLDER_RE = re.compile(
    r"\{\{\s*[^{}]+\s*\}\}|\{[A-Za-z_][A-Za-z0-9_]*\}|"
    r"ARTICLE TITLE|APPROVED_PARAGRAPH_COPY|META_TITLE",
    re.I,
)


def fetch(url):
    req = Request(
        url,
        headers={
            "User-Agent": UA,
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    try:
        with urlopen(req, timeout=30, context=ssl.create_default_context()) as response:
            body = response.read()
            return {
                "url": url,
                "status": response.status,
                "final": response.geturl(),
                "body": body,
                "headers": dict(response.headers.items()),
                "error": "",
            }
    except HTTPError as error:
        try:
            body = error.read()
        except Exception:
            body = b""
        return {
            "url": url,
            "status": error.code,
            "final": error.geturl(),
            "body": body,
            "headers": dict(error.headers.items()) if error.headers else {},
            "error": str(error),
        }
    except Exception as error:
        return {
            "url": url,
            "status": 0,
            "final": "",
            "body": b"",
            "headers": {},
            "error": repr(error),
        }


def sitemap_locs(payload):
    root = ET.fromstring(payload)
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [node.text.strip() for node in root.findall(".//s:loc", ns) if node.text]


def local_release_inventory():
    local_sitemap = SITE_ROOT / "sitemap.xml"
    local_blog = SITE_ROOT / "blog.html"
    if not local_sitemap.is_file() or not local_blog.is_file():
        raise RuntimeError("Retained local blog.html and sitemap.xml baselines are required")

    expected_urls = sitemap_locs(local_sitemap.read_bytes())
    expected_articles = {url for url in expected_urls if "/blog/" in url}

    blog_text = local_blog.read_text(encoding="utf-8")
    soup = BeautifulSoup(blog_text, "html.parser")
    expected_cards = len(soup.select("#posts-grid > .post-card"))
    expected_schema = 0
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
        except Exception:
            continue
        if isinstance(data, dict) and data.get("@type") == "Blog":
            expected_schema = len(data.get("blogPost", []))
            break

    if not expected_articles or expected_cards != len(expected_articles) or expected_schema != len(expected_articles):
        raise RuntimeError(
            "Local release inventory is inconsistent: "
            f"cards={expected_cards}, schema={expected_schema}, sitemap articles={len(expected_articles)}"
        )
    return expected_articles, expected_cards, expected_schema


EXPECTED_ARTICLES, EXPECTED_CARDS, EXPECTED_SCHEMA = local_release_inventory()

# Read the live sitemap, then request both the live inventory and every URL expected
# by the retained release baseline. Missing new release URLs are therefore visible as
# HTTP failures rather than being hidden by an old live sitemap.
sm = fetch(urljoin(BASE, "sitemap.xml"))
live_urls = sitemap_locs(sm["body"]) if sm["status"] == 200 else []
live_articles = {url for url in live_urls if "/blog/" in url}
blog_urls_to_request = sorted(live_articles | EXPECTED_ARTICLES)

requested = {
    "Shell": [urljoin(BASE, "header.html"), urljoin(BASE, "footer.html")],
    "Home": [
        BASE,
        urljoin(BASE, "index.html"),
        urljoin(BASE, "about.html"),
        urljoin(BASE, "services.html"),
        urljoin(BASE, "universities.html"),
    ],
    "Destinations": [
        urljoin(BASE, "destinations.html"),
        urljoin(BASE, "study-in-uk.html"),
        urljoin(BASE, "study-in-ireland.html"),
        urljoin(BASE, "study-in-malaysia.html"),
        urljoin(BASE, "study-in-turkey.html"),
    ],
    "Legal": [
        urljoin(BASE, "privacy-policy.html"),
        urljoin(BASE, "terms.html"),
        urljoin(BASE, "disclaimer.html"),
        urljoin(BASE, "service-scope-and-refund-policy.html"),
        urljoin(BASE, "FAQs.html"),
    ],
    "Profile Review": [urljoin(BASE, "initial-profile-review.html")],
    "Blog": [urljoin(BASE, "blog.html")] + blog_urls_to_request,
    "Crawl Assets": [
        urljoin(BASE, "robots.txt"),
        urljoin(BASE, "sitemap.xml"),
        urljoin(BASE, "fonts/NotoNastaliqUrdu-Arabic.woff2"),
    ],
}

# Dedupe while retaining the first assigned group.
entries = []
seen = set()
for group, group_urls in requested.items():
    for url in group_urls:
        if url in seen:
            continue
        seen.add(url)
        entries.append((group, url))

results = {}
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(fetch, url): (group, url) for group, url in entries}
    for future in as_completed(futures):
        group, url = futures[future]
        results[url] = (group, future.result())

rows = []
internal_links = set()
issues = []

for group, url in entries:
    response = results[url][1]
    body = response["body"]
    text = body.decode("utf-8", "replace")
    content_type = response["headers"].get("Content-Type", "")
    is_html = "text/html" in content_type or url.endswith(".html") or url == BASE
    title = ""
    h1 = ""
    canonical = ""
    placeholder = False
    plain_email = 0
    cloudflare_email = 0
    approved = 0
    compact_display = 0
    whatsapp = 0
    prohibited = []
    notes = []

    if is_html and body:
        soup = BeautifulSoup(text, "html.parser")
        title = soup.title.get_text(" ", strip=True) if soup.title else ""
        visible = soup.get_text(" ", strip=True)
        h1 = len(soup.find_all("h1"))
        canonical_link = soup.find("link", rel="canonical")
        canonical = canonical_link.get("href", "") if canonical_link else ""
        placeholder = bool(PLACEHOLDER_RE.search(text))
        plain_email = text.count("mailto:info@pathplaza.com")
        cloudflare_email = text.count("/cdn-cgi/l/email-protection")
        approved = visible.count(APPROVED)
        compact_display = visible.count(COMPACT)
        whatsapp = text.count("wa.me/923155009620")
        prohibited = [name for name, pattern in PROHIBITED_PATTERNS.items() if pattern.search(text)]

        for anchor in soup.find_all("a", href=True):
            href = anchor["href"].strip()
            if href.startswith(("#", "mailto:", "tel:", "javascript:")) or "wa.me/" in href:
                continue
            target = urljoin(url, href)
            parsed = urlparse(target)
            if parsed.netloc.lower() in {"pathplaza.com", "www.pathplaza.com"}:
                internal_links.add(target.split("#", 1)[0])

        if group not in ("Shell", "Crawl Assets") and h1 != 1:
            notes.append(f"H1 count {h1}")
        if group not in ("Shell", "Crawl Assets") and not canonical:
            notes.append("canonical missing")
        elif group == "Blog" and "/blog/" in urlparse(url).path and canonical.rstrip("/") != url.rstrip("/"):
            notes.append(f"canonical mismatch: {canonical}")
        if cloudflare_email:
            notes.append("Cloudflare email obfuscation present")
        if compact_display and not approved:
            notes.append(f"Displayed contact is compact {COMPACT}; expected {APPROVED}")

    status_ok = response["status"] == 200
    if not status_ok:
        issues.append(("P0", url, f'HTTP {response["status"]}: {response["error"]}'))
    if prohibited:
        issues.append(("P0", url, "Prohibited contact pattern(s): " + ", ".join(prohibited)))
    if cloudflare_email:
        issues.append(("P0", url, f"Email is protected/obfuscated; keep plain {PLAIN_EMAIL}"))
    if compact_display and not approved:
        severity = "P0" if group == "Shell" else "P1"
        issues.append((severity, url, f"Displays {COMPACT} instead of {APPROVED}"))
    if placeholder:
        issues.append(("P0", url, "Template/placeholder token visible"))
    if notes and group not in ("Shell", "Crawl Assets"):
        for note in notes:
            if note.startswith("Displayed contact is compact") or "Cloudflare" in note:
                continue
            issues.append(("P2", url, note))

    cache = "; ".join(
        filter(
            None,
            [
                response["headers"].get("CF-Cache-Status", ""),
                response["headers"].get("X-LiteSpeed-Cache", ""),
                response["headers"].get("Age", "") and "Age=" + response["headers"].get("Age", ""),
            ],
        )
    ) or "No cache-status header"
    result = "PASS" if status_ok and not prohibited and not placeholder and not notes else "FAIL"
    rows.append(
        {
            "Group": group,
            "URL": url,
            "Expected release URL": url in EXPECTED_ARTICLES,
            "In live sitemap": url in live_articles,
            "HTTP": response["status"],
            "Final URL": response["final"],
            "Title": title,
            "Bytes": len(body),
            "H1": h1 if is_html else "",
            "Canonical": canonical,
            "Approved display count": approved,
            "Compact display count": compact_display,
            "WhatsApp link count": whatsapp,
            "Plain email count": plain_email,
            "Cloudflare email obfuscation": cloudflare_email,
            "Prohibited patterns": ", ".join(prohibited),
            "Placeholder": placeholder,
            "Cache header": cache,
            "Result": result,
            "Notes": "; ".join(notes or ([response["error"]] if response["error"] else [])),
        }
    )

# Parse the live blog index for release-level inventory checks.
blog_url = urljoin(BASE, "blog.html")
blog_response = results.get(blog_url, (None, {"body": b""}))[1]
blog_text = blog_response.get("body", b"").decode("utf-8", "replace")
blog_soup = BeautifulSoup(blog_text, "html.parser") if blog_text else BeautifulSoup("", "html.parser")
live_card_count = len(blog_soup.select("#posts-grid > .post-card"))
live_schema_count = 0
for script in blog_soup.find_all("script", type="application/ld+json"):
    try:
        data = json.loads(script.string or "")
    except Exception:
        continue
    if isinstance(data, dict) and data.get("@type") == "Blog":
        live_schema_count = len(data.get("blogPost", []))
        break

missing_release_articles = sorted(EXPECTED_ARTICLES - live_articles)
extra_live_articles = sorted(live_articles - EXPECTED_ARTICLES)
if missing_release_articles:
    for url in missing_release_articles:
        issues.append(("P0", url, "Expected release article is missing from the live sitemap"))
if extra_live_articles:
    for url in extra_live_articles:
        issues.append(("P1", url, "Live sitemap article is not in the retained release baseline"))
if live_card_count != EXPECTED_CARDS:
    issues.append(("P0", blog_url, f"Blog has {live_card_count} cards; expected {EXPECTED_CARDS}"))
if live_schema_count != EXPECTED_SCHEMA:
    issues.append(("P0", blog_url, f"Blog schema has {live_schema_count} posts; expected {EXPECTED_SCHEMA}"))

# Check every discovered same-site link.
link_results = {}
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(fetch, url): url for url in sorted(internal_links)}
    for future in as_completed(futures):
        link_results[futures[future]] = future.result()

broken = []
for url, response in link_results.items():
    if not 200 <= response["status"] < 400:
        broken.append((url, response["status"], response["error"]))
        issues.append(("P1", url, f'Internal link returned {response["status"]}'))

header = next((row for row in rows if row["URL"].endswith("/header.html")), None)
footer = next((row for row in rows if row["URL"].endswith("/footer.html")), None)
gates = [
    ("Header HTTP 200", bool(header and header["HTTP"] == 200)),
    ("Footer HTTP 200", bool(footer and footer["HTTP"] == 200)),
    (f"Approved contact visible in header ({APPROVED})", bool(header and header["Approved display count"] >= 1)),
    (f"Approved contact visible in footer ({APPROVED})", bool(footer and footer["Approved display count"] >= 1)),
    ("Plain email remains unprotected", not any(row["Cloudflare email obfuscation"] for row in rows)),
    ("No prohibited contact across crawl", not any(row["Prohibited patterns"] for row in rows)),
    ("No template placeholders", not any(row["Placeholder"] for row in rows)),
    ("All requested URLs HTTP 200", all(row["HTTP"] == 200 for row in rows)),
    ("No broken discovered internal links", not broken),
    (f"Blog index contains {EXPECTED_CARDS} cards", live_card_count == EXPECTED_CARDS),
    (f"Blog schema contains {EXPECTED_SCHEMA} posts", live_schema_count == EXPECTED_SCHEMA),
    (f"Blog sitemap contains {len(EXPECTED_ARTICLES)} article URLs", len(live_articles) == len(EXPECTED_ARTICLES)),
    ("Live article sitemap matches retained baseline", live_articles == EXPECTED_ARTICLES),
]

csv_path = OUT / f"Production_Crawl_Smoke_Test_{RUN_DATE}.csv"
with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

passed = sum(value for _, value in gates)
blocking_issues = [issue for issue in issues if issue[0] in ("P0", "P1")]
overall = "PASS" if passed == len(gates) and not blocking_issues else "FAIL"

md = [
    "# Path Plaza — Production Crawl Smoke Test",
    "",
    f'**Run:** {NOW.isoformat(timespec="seconds")}  ',
    f"**Base:** {BASE}  ",
    f"**Expected release inventory:** {EXPECTED_CARDS} cards · {EXPECTED_SCHEMA} schema posts · {len(EXPECTED_ARTICLES)} sitemap articles  ",
    f"**Overall:** **{overall}**  ",
    f"**URLs requested:** {len(rows)} · **Discovered internal links checked:** {len(link_results)} · **Broken:** {len(broken)}",
    "",
    "## Executive summary",
    "",
    "- Shared header and footer were fetched directly.",
    "- Home, destination, legal, profile-review, blog and crawl-asset groups were requested from production.",
    "- Both the live sitemap inventory and every article expected by the retained local release baseline were requested.",
    "- Visible contact formatting, WhatsApp targets, plain email, Cloudflare obfuscation, canonicals, H1 counts and template tokens were checked.",
    "- Blog cards, BlogPosting schema and live sitemap articles were compared with the retained local blog.html and sitemap.xml baselines.",
    "- Discovered same-site links were smoke-tested.",
    "",
    "## Release gates",
    "",
    "| Gate | Result |",
    "|---|---|",
]
for name, value in gates:
    md.append(f'| {name} | {"PASS" if value else "FAIL"} |')

md += ["", "## Blog inventory comparison", ""]
md += [
    f"- Retained baseline cards/schema/articles: {EXPECTED_CARDS}/{EXPECTED_SCHEMA}/{len(EXPECTED_ARTICLES)}",
    f"- Live cards/schema/articles: {live_card_count}/{live_schema_count}/{len(live_articles)}",
    f"- Missing expected live sitemap articles: {len(missing_release_articles)}",
    f"- Extra live sitemap articles: {len(extra_live_articles)}",
]
for url in missing_release_articles:
    md.append(f"- Missing: `{url}`")
for url in extra_live_articles:
    md.append(f"- Extra: `{url}`")

md += ["", "## Issue register", ""]
if issues:
    md += ["| Severity | URL | Evidence |", "|---|---|---|"]
    for severity, url, evidence in issues:
        md.append(f"| {severity} | `{url}` | {evidence} |")
else:
    md.append("No P0–P2 smoke-test issues were found.")

md += [
    "",
    "## Crawl results",
    "",
    "| Group | HTTP | Result | Title/asset | Contact | Email | Notes |",
    "|---|---:|---|---|---:|---:|---|",
]
for row in rows:
    md.append(
        f'| {row["Group"]} | {row["HTTP"]} | {row["Result"]} | '
        f'{row["Title"] or Path(row["URL"]).name or "/"} | '
        f'{row["Approved display count"]} | {row["Plain email count"]} | '
        f'{row["Notes"] or row["Cache header"]} |'
    )

md += [
    "",
    "## Internal-link check",
    "",
    f"- Unique same-site links checked: {len(link_results)}",
    f"- Broken/non-success links: {len(broken)}",
]
for url, status, error in sorted(broken):
    md.append(f"- `{status}` — {url} — {error}")

cache_text = (
    "The crawler sent `Cache-Control: no-cache` and `Pragma: no-cache`. "
    "No Cloudflare/LiteSpeed cache-status header was exposed, so a cache purge cannot be proven from headers alone. "
)
if overall == "PASS":
    cache_text += "The normal public URLs nevertheless matched the retained release baseline."
else:
    cache_text += "Because public responses do not yet match the retained release baseline, deployment and purge success are not established."

md += [
    "",
    "## Cache verification note",
    "",
    cache_text,
    "",
    "## Evidence files",
    "",
    f"- `{csv_path.name}` — row-level crawl export",
    f"- `{SCRIPT.name}` — reproducible crawler",
    "",
    "---",
    "",
    f'**Conclusion:** {"Production smoke test passed." if overall == "PASS" else "Production smoke test failed; resolve the issue register and rerun before closing the release."}',
]

md_path = OUT / f"Production_Crawl_Smoke_Test_{RUN_DATE}.md"
md_path.write_text("\n".join(md), encoding="utf-8")
print(md_path)
print(csv_path)
print(
    "overall", overall,
    "gates", passed, "/", len(gates),
    "issues", len(issues),
    "rows", len(rows),
    "links", len(link_results),
    "live_cards", live_card_count,
    "live_schema", live_schema_count,
    "live_articles", len(live_articles),
    "expected_articles", len(EXPECTED_ARTICLES),
)
