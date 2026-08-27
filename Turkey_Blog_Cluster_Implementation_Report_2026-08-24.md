# Turkey Blog Cluster — English + Urdu Implementation Report

**Completed:** 24 August 2026  
**Management choices:** English + Urdu only · publish all now  
**Release bundle:** `releases/Path_Plaza_Turkey_Blog_Cluster_English_Urdu_2026-08-24.zip`

## Scope delivered

The cluster now contains **16 article pages** across eight topics:

| # | Topic | English | Urdu |
|---:|---|---|---|
| 1 | Turkey student visa document checklist | Existing, updated | Built/rebuilt |
| 2 | Turkey university fees 2026 | Existing, updated | Built/rebuilt |
| 3 | Study in Turkey without IELTS | Built | Built |
| 4 | Türkiye Scholarships 2027 planning guide | Built | Built |
| 5 | Turkey student visa processing time and fees | Built | Built |
| 6 | Student İkamet after arrival | Built | Built |
| 7 | Denklik and attestation | Built | Built |
| 8 | Istanbul vs Ankara vs Izmir budget fit | Built | Built |

Calendar rows #9 and #10 were not created as separate Roman-Urdu pages because management selected **English and Urdu only**. Their underlying topics are already covered by the English/Urdu pairs for #2 and #3.

## Visibility corrections applied

- Post #3 explains what replaces IELTS instead of implying no language requirement.
- Post #4 removes “honest odds,” acceptance percentages and unannounced 2027 dates.
- Post #5 avoids a universal processing-time or fee promise.
- Post #6 removes the blanket 30-day İkamet claim and uses current official residence-document guidance.
- Post #7 distinguishes Pakistan attestation, school equivalence, YÖK institution recognition and diploma equivalence.
- Post #8 does not declare a best city; it teaches a programme/housing/family decision model.
- Every new page displays the current calendar-mandated contact format `92315-500-9620`; technical WhatsApp URLs remain digits-only.

## Blog index

`blog.html` now contains:

- 16 visible article cards
- 8 English and 8 Urdu pages
- Featured post #3, with Urdu switch
- Filter counts: All 16 · Turkey 16 · Process 10 · Money 6 · Family 2 · Urdu 8
- Blog JSON-LD containing all 16 URLs with `en-PK`/`ur-PK`
- No template, empty-state or future-date content

## Sitemap

`sitemap.xml` now contains:

- All 16 article canonical URLs
- One URL entry per article
- `lastmod` 24 August 2026
- Reciprocal `en-PK`, `ur-PK` and `x-default` annotations for every pair
- 48 article hreflang annotations
- Full destination, legal, FAQ, profile-review and blog inventory

## QA summary

- Manifest: 16 rows
- New pages: 12
- English pages: 8 total
- Urdu pages: 8 total
- One H1 per page: passed
- Four visible FAQs and exact FAQPage parity per page: passed
- BlogPosting/Breadcrumb JSON-LD: passed
- Canonical and three hreflang links per page: passed
- Internal article-card targets: passed
- No template tokens: passed
- No prohibited internal contact patterns: passed
- No Path Plaza service/Roadmap fee: passed
- No “honest odds,” single-digit acceptance, universal 30-day clock or fixed processing promise: passed
- Largest Urdu page plus shared font: approximately 332 KB, under the 350 KB budget
- Blog index size: approximately 247 KB
- Sitemap XML parse: passed

## Release contents

- Root `blog.html`
- Root `sitemap.xml`
- 16 article HTML files
- 12 new post deployment guides plus existing post guides
- Noto Nastaliq Urdu WOFF2 and licence
- Article manifest CSV
- SHA-256 file manifest
- Deployment checklist

## Deployment order

1. Upload the Nastaleeq font.
2. Upload all 16 article HTML files in `blog/`.
3. Upload root `blog.html`.
4. Upload root `sitemap.xml`.
5. Purge LiteSpeed/CDN caches.
6. Verify all URLs from the manifest return their own article titles.
7. Check the blog filters and language switches.
8. Submit the sitemap only after every article returns HTTP 200.

The article, blog index and sitemap must always be deployed from the same release bundle.
