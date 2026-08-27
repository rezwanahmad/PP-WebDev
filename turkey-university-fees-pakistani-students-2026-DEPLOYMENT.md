# A2 Turkey University Fees — Deployment & QA Guide

## Deliverables

- Article: `/blog/turkey-university-fees-pakistani-students-2026.html`
- PP-VISIBILITY brief: `/seo/briefs/PP_VISIBILITY_A2_Turkey_University_Fees_2026_Build_Brief.md`
- Updated index: `/blog.html`
- Updated reciprocal article: `/blog/turkey-student-visa-documents-pakistan.html`
- Updated sitemap: `/sitemap.xml`

**Build/publication date used:** 21 August 2026  
**Category:** Turkey · Money & Scholarships  
**Primary keyword:** turkey university fees pakistani students  
**Visible article length:** approximately 1,597 words  
**Computed reading time:** 9 minutes

## Visibility review applied before build

The supplied copy deck was not rendered blindly. PP-VISIBILITY checked its major cost, scholarship and work-right claims against current official sources and issued a build brief before implementation.

### Material corrections

- Replaced “think in dollars, never in lira” with a currency-verification rule because public institutions may publish TRY schedules.
- Replaced the supplied clinical tuition ceiling with current Okan and İstinye 2026–27 examples reaching US$29,000.
- Replaced market-wide “common discount” wording with institution-specific, written-offer language.
- Removed single-digit scholarship-acceptance/probability claims.
- Removed the unsupported 24-hours-per-week work statement.
- Removed the unannounced 2027 scholarship-window prediction.
- Removed the 24–48-hour service turnaround statement.
- Rebuilt first-year and complete-degree calculations from disclosed assumptions at PKR 280/US$.

## Source ledger

Checked 21 August 2026:

1. State Bank of Pakistan — USD/PKR rate page
2. Istanbul Okan University — 2026–27 tuition
3. Istanbul Ticaret University — 2026–27 tuition and payment plans
4. İstinye University — 2026–27 quotas and tuition
5. Türkiye Scholarships official portal
6. Türkiye Scholarships 2026 programme announcement
7. Türkiye Law on Foreigners and International Protection
8. Republic of Türkiye Ministry of Foreign Affairs

The SBP page showed an M2M rate of 277.5604 on 21 August 2026. The article uses PKR 280/US$ as a clearly labelled rounded planning anchor.

Living, travel and one-time costs remain indicative family-planning models from the approved deck. They are not described as official national rates.

## Deployment order

1. Upload the new A2 article to:

   ```text
   /blog/turkey-university-fees-pakistani-students-2026.html
   ```

2. Upload the updated A1 article so its reciprocal A2 related link works.
3. Upload the updated `blog.html`.
4. Upload the updated `sitemap.xml`.
5. Do **not** upload `_article-template.html`.
6. Purge LiteSpeed/CDN caches.
7. Fetch the live blog page as a crawler and confirm no empty-state or manual-template text appears.
8. Confirm A2, A1, the Turkey destination guide and Profile Review links return valid pages.
9. Submit the updated sitemap and request indexing after production QA.

## Blog-index changes

- A2 is now the featured article.
- A2 appears as a Turkey + Money card.
- A1 remains live and links back to A2.
- Filter counts now represent two real articles.
- The public empty-state and manual card `<template>` were removed because crawler extraction exposed their placeholder text.
- Blog JSON-LD lists both live posts.

## SEO/AEO/GEO QA

- Title: 63 characters; logged exception to the ≤60 target to preserve keyword + brand
- Meta description: 142 characters
- One H1: passed
- Direct answer capsule: 46 words
- BlogPosting schema: valid JSON
- Breadcrumb schema: valid JSON
- FAQPage schema: valid JSON
- Four visible FAQs exactly match schema
- Six responsive tables: passed
- One accessible tuition-band visual: passed
- Eight official-source links: passed
- Canonical and article Open Graph metadata: passed
- Real visible and schema dates match

## Engineering and accessibility QA

- Self-contained file size: approximately 241 KB, below 350 KB
- Desktop and mobile TOCs: present
- Keyboard-focus styles: present
- Scrollable tables: present
- Reduced-motion and print rules: present
- Key facts remain visible without JavaScript
- No external font/icon stylesheet
- Every external `target="_blank"` link uses `rel="noopener"`

## Pathfinder compliance QA

- Internal-only contact patterns: absent
- Public WhatsApp and plain email: present
- Path Plaza service/Roadmap fee: absent
- Scholarship probability and guarantee language: absent
- Unsupported partnership wording: absent
- Part-time work is not presented as a funding solution
- Global disclaimer: present verbatim
- All PKR conversions state the planning rate and date
- Offer/current university page remains authoritative

The PKR 5,000–10,000 figure concerns indicative third-party document-attestation costs; it is not a Path Plaza fee.

## GA4

`window.PP_GA4_ID` remains blank. No tracker loads until management approves and supplies an ID. The page is ready for:

- `article_view`
- `cta_profile_click`
- `cta_whatsapp_click`

## Follow-up internal links

In the next Turkey-cluster release:

- Add a contextual link from `/study-in-turkey.html` to A2.
- Keep A2 linked to A1 and the Turkey guide.
- Add the future “Study in Turkey Without IELTS” related card only after that article exists.

If deployment occurs after 21 August 2026, update visible dates, schema dates, sitemap `lastmod`, index dates and source-check dates before upload.
