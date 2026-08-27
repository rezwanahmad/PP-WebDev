# Deployment Notes — Study in Turkey from Pakistan Beginner Guide

**Release date:** 25 August 2026  
**Languages:** Plain English (`en-PK`) and simple Urdu (`ur-PK`)  
**English URL:** `https://pathplaza.com/blog/study-in-turkey-from-pakistan-beginner-guide-2026.html`  
**Urdu URL:** `https://pathplaza.com/blog/study-in-turkey-from-pakistan-beginner-guide-2026-urdu.html`  
**Status:** Built and QA-checked; not uploaded to production in this session.

## What changed

- Added a plain-English beginner guide for Pakistani students and parents.
- Added a complete matching Urdu guide in Urdu script, RTL layout and the local Noto Nastaliq Urdu font.
- Added responsive visual explainers and accessible tables for university types, degree levels, calendars, languages, application steps and complete-budget categories.
- Added BlogPosting, BreadcrumbList and FAQPage structured data to both pages.
- Added reciprocal English/Urdu hreflang, schema translation relationships and language-switch links.
- Added a 1200 × 630 branded OG image.
- Updated `blog.html` from 16 to 18 cards and 18 BlogPosting schema records; the English guide is featured and links to Urdu.
- Replaced the former generated `blog.html` with a clean 18-card baseline built from the real article files.
- Replaced the former generated `sitemap.xml` with a clean 34-URL baseline containing 18 reciprocal article URLs.
- These two files must now be kept and updated in place for every future article; normal publishing must not delete or regenerate them.
- Fixed two pre-existing defects in the linked IELTS pair:
  - removed the visible `{right_title}` token;
  - restored self-referencing canonical, Open Graph, schema and analytics-slug values in the English and Urdu files.

## Current fact decisions

- Used YÖK’s current count of **208 universities**.
- Used current direct-application and TR-YÖS wording; outdated advice that state universities run separate YÖS exams was not repeated.
- Used official duration ranges: associate 2 years, bachelor’s 4 years, master’s 1.5–2 years and doctorate 3–4 years.
- Published no tuition or universal total-cost figure.
- Explained Bologna alignment without promising automatic recognition.

## Files to upload

Upload in this order:

1. `images/blog/study-in-turkey-from-pakistan-beginner-guide-2026-og.jpg`
2. `blog/study-in-turkey-from-pakistan-beginner-guide-2026.html`
3. `blog/study-in-turkey-from-pakistan-beginner-guide-2026-urdu.html`
4. `blog/study-in-turkey-without-ielts-2026.html` — maintenance fix
5. `blog/study-in-turkey-without-ielts-2026-urdu.html` — maintenance fix
6. `blog.html`
7. `sitemap.xml`

## Existing dependencies

- `/images/Logo.png` must remain available.
- `/fonts/NotoNastaliqUrdu-Arabic.woff2` must remain available for the Urdu page.
- `PP_GA4_ID` remains blank; no analytics tracker loads until management supplies and approves an ID.

## Production integration

1. Back up every file that will be replaced.
2. Upload the OG image and both language pages first.
3. Upload the two maintenance files.
4. Upload `blog.html` and `sitemap.xml` last.
5. Purge page/CDN cache for both articles, the blog index and the sitemap.
6. Confirm both canonical URLs return HTTP 200.
7. Confirm each page links to the other language.
8. Confirm the Urdu body uses Nastaleeq and remains readable on mobile.
9. Confirm the blog index shows 18 cards and 18 schema records.
10. Confirm the sitemap contains 18 article URLs and reciprocal English/Urdu alternates.
11. Confirm both IELTS pages no longer show a template token and now have self canonicals.

## Rollback

Restore the backed-up `blog.html`, `sitemap.xml` and maintenance pages, then remove both new article files and the OG image. Purge cache again.

## Operational note

The separate production contact-release smoke test remains failed for unrelated shell and country-page issues. This bilingual blog package does not close that ticket. Human management approval and production access are still required.
