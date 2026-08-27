# A2 Urdu Edition — Deployment & QA Guide

## Deliverables

- Urdu article: `/blog/turkey-university-fees-pakistani-students-2026-urdu.html`
- Nastaleeq webfont: `/fonts/NotoNastaliqUrdu-Arabic.woff2`
- Font licence: `/fonts/NotoNastaliqUrdu-OFL.txt`
- Updated English article with reciprocal Urdu hreflang/language switch
- Updated blog index with Urdu links
- Updated Blog JSON-LD and sitemap

**Language:** Urdu (`ur-PK`)  
**Direction:** RTL  
**Font:** Noto Nastaliq Urdu  
**Style:** plain teaching Urdu with infographic-first explanations  
**Displayed reading time:** 8 minutes  
**Date used:** 21 August 2026

## Language and editorial approach

This is an Urdu-script rewrite of the visibility-reviewed English A2 article, not a Roman-Urdu transliteration and not a word-for-word machine translation. It preserves the same official-source examples, currency assumptions, compliance caveats and calculation model.

The revised edition uses short sentences, everyday Urdu and a lesson-by-lesson teaching sequence. Dense explanations were converted into visual teaching blocks while the responsive tables remain available for exact comparison.

English university names, currencies, source URLs and numeric strings use isolated LTR rendering so that values remain readable inside the RTL page.

## Nastaleeq implementation

The page uses a local Arabic-subset WOFF2 file:

```css
@font-face {
  font-family: "Noto Nastaliq Urdu";
  src: url("/fonts/NotoNastaliqUrdu-Arabic.woff2") format("woff2");
  font-display: swap;
}
```

Fallbacks are:

```css
"Jameel Noori Nastaleeq", "Nafees Nastaleeq", serif
```

The WOFF2 file is distributed under the SIL Open Font License supplied in `NotoNastaliqUrdu-OFL.txt`.

The approved Path Plaza logo was resized proportionally for page performance without redrawing, recolouring or changing its aspect ratio.

## Deployment order

1. Upload the font:

   ```text
   /fonts/NotoNastaliqUrdu-Arabic.woff2
   ```

2. Upload the font licence outside user navigation but retain it in the deployment package.
3. Upload the Urdu article:

   ```text
   /blog/turkey-university-fees-pakistani-students-2026-urdu.html
   ```

4. Upload the updated English A2 article.
5. Upload the updated `blog.html`.
6. Upload the updated `sitemap.xml`.
7. Purge LiteSpeed/CDN caches.
8. Confirm the Urdu article loads in Nastaleeq rather than a generic Arabic font.
9. Test language switching in both directions.
10. Request indexing only after hreflang and canonical checks pass.

## SEO and language signals

The Urdu page includes:

- `<html lang="ur-PK" dir="rtl">`
- Self-referencing Urdu canonical
- `ur-PK`, `en-PK` and `x-default` hreflang links
- Urdu title, description, H1 and visible breadcrumbs
- `BlogPosting` schema with `inLanguage: ur-PK`
- `translationOfWork` pointing to the English article
- Urdu FAQPage schema matching visible FAQs
- Urdu article entry in Blog JSON-LD and sitemap

The English article now includes a reciprocal `ur-PK` hreflang link, a visible Urdu-language switch and `workTranslation` schema.

## Infographic system

The rebuilt article contains twelve CSS-only teaching visuals:

1. Four-card one-minute summary
2. Complete-budget formula flow
3. USD-to-PKR worked calculation
4. Three-university comparison cards
5. Four fee-tier cards
6. Tuition-band bar chart
7. City-cost bars
8. One-time cost tiles
9. Four-year/six-year timeline
10. Three first-year budget cards
11. Four-step cost-reduction flow
12. Seven red-flag cards

All numbers also remain available in six accessible responsive tables.

## Performance

- Urdu HTML: approximately 89 KB
- Noto Nastaliq Urdu WOFF2: approximately 239 KB
- Combined article + required font: approximately 328 KB
- Combined total remains below the governed 350 KB article budget
- Font uses `font-display: swap`
- No Google Fonts, CDN icon library or external stylesheet is required

## Accessibility and RTL QA

- Skip link: present
- One H1: required and verified
- RTL document direction: present
- Numeric/currency values isolated with `bdi`/LTR styling
- Mobile navigation: keyboard-operable
- Desktop and mobile TOCs: present
- Six responsive table regions: present
- FAQ accordions: keyboard-operable
- Visible focus, reduced-motion and print rules: present
- Key facts and sources remain available without JavaScript

## Content and compliance QA

- Official examples and SBP rate mirror the visibility-reviewed English article
- All changing figures are dated or labelled indicative
- Scholarship acceptance probability: absent
- Unsupported weekly work-hours figure: absent
- Path Plaza service/Roadmap fee: absent
- Internal-only contact patterns: absent
- Public phone and plain email: present
- Global disclaimer appears in Urdu and verbatim English
- Four visible Urdu FAQs match FAQPage schema exactly
- No guarantee of admission, scholarship, visa, work or settlement outcome

## Index and sitemap changes

- The English A2 featured slot and card now include an “اردو میں پڑھیں” link.
- Blog schema lists the Urdu translation separately with `inLanguage: ur-PK`.
- Sitemap contains the Urdu canonical URL once.

## GA4

The GA4 ID remains blank. No tracker loads. The Urdu page is ready to emit language-labelled:

- `article_view`
- `cta_profile_click`
- `cta_whatsapp_click`

## Date rule

If deployment occurs after 21 August 2026, update:

- Visible publication/review date
- BlogPosting dates
- FAQ/source review note where applicable
- English and Urdu index-card dates
- Sitemap `lastmod`

Do not auto-create a Roman-Urdu version from this Urdu page. Any Roman-Urdu edition requires a separately approved natural rewrite.
