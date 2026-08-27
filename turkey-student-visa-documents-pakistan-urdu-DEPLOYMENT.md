# A1 Urdu Visa Checklist — Deployment & QA Guide

## Deliverables

- Urdu article: `/blog/turkey-student-visa-documents-pakistan-urdu.html`
- Visibility brief: `/seo/briefs/PP_VISIBILITY_A1_Turkey_Student_Visa_Checklist_Urdu_Brief.md`
- Shared Nastaleeq font: `/fonts/NotoNastaliqUrdu-Arabic.woff2`
- Font licence: `/fonts/NotoNastaliqUrdu-OFL.txt`
- Updated English A1 language signals
- Updated blog index, Blog JSON-LD and sitemap
- Updated Urdu A2 related link

**Language:** Urdu (`ur-PK`)  
**Direction:** RTL  
**Font:** Noto Nastaliq Urdu  
**Style:** plain, easy teaching Urdu with infographic-first explanations  
**Displayed reading time:** 8 minutes  
**Date used:** 21 August 2026

## Editorial and visibility approach

This is a natural Urdu teaching rewrite based on the A1 topic and current official-source review. It is not Roman Urdu and not a mechanical line-by-line translation.

The article deliberately treats the Pakistan visa file as a practical planning system rather than claiming that every applicant has one universal list. The current consular/mission checklist remains authoritative.

### Material visibility corrections

- Removed the universal US$800-per-month funds statement.
- Removed the blanket “apply for İkamet within 30 days” rule.
- Removed guaranteed 2–6-week processing language.
- Removed universal 5×5 visa-photo wording; readers are told to check the current mission specification.
- Used the current official e-İkamet requirement of two recent ICAO-compliant biometric photos for the student-residence file.
- Treated FRC, police certificate, translation and attestations as case/document-dependent.
- Retained the polio-certificate reminder using Pakistan Polio Programme guidance for outbound international travellers.
- Removed fixed visa-fee figures not verified on a current mission/authorised-centre page.

## Infographic system

The post includes nine major teaching visuals:

1. Four-card one-minute summary
2. Pakistan-to-Türkiye two-stage map
3. Five-folder visa-file system
4. Three commonly missed-item cards
5. Five-step attestation ladder
6. Clear-vs-weak sponsor file comparison
7. Six-step preparation flow
8. Seven-card student-residence file
9. Seven common-mistake warning grid

Exact details remain available in four responsive tables.

## Source ledger

Checked for the Urdu build:

1. Türkiye consular visa pre-application portal
2. Republic of Türkiye Ministry of Foreign Affairs
3. Official e-İkamet portal
4. Official student-residence required-documents page
5. Official residence-fee page
6. Pakistan Polio Programme travel-certificate guidance
7. HEC degree-attestation portal
8. IBCC attestation portal
9. MOFA Pakistan apostille/attestation portal

## Deployment order

1. Confirm the shared Nastaleeq font already exists at:

   ```text
   /fonts/NotoNastaliqUrdu-Arabic.woff2
   ```

2. Upload the Urdu article:

   ```text
   /blog/turkey-student-visa-documents-pakistan-urdu.html
   ```

3. Upload the updated English A1 article with reciprocal `ur-PK` hreflang and language switch.
4. Upload the updated Urdu A2 article so its related link points to the Urdu visa checklist.
5. Upload the updated `blog.html`.
6. Upload the updated `sitemap.xml`.
7. Purge LiteSpeed/CDN caches.
8. Test English ↔ Urdu language switching.
9. Confirm the article renders in Nastaleeq and all tables scroll on mobile.
10. Request indexing only after canonical, hreflang, schema and source checks pass.

## SEO and schema

- Urdu canonical and self hreflang: present
- Reciprocal `en-PK`, `ur-PK` and `x-default`: present
- BlogPosting schema with `inLanguage: ur-PK`: valid
- BreadcrumbList schema: valid
- Four visible Urdu FAQs: present
- FAQPage schema exactly matches visible Urdu answers
- Blog index links to the Urdu version
- Blog schema lists both Urdu posts
- Sitemap contains the Urdu A1 URL once

## Performance and accessibility

- Urdu HTML: approximately 93 KB
- Shared Nastaleeq WOFF2: approximately 239 KB
- Combined page + required font: approximately 332 KB
- Combined total remains under the 350 KB article budget
- One H1
- RTL document direction
- English names/URLs/numbers isolated for LTR rendering
- Desktop and mobile TOCs
- Four responsive table regions
- Keyboard-operable menu and FAQs
- Reduced-motion and print rules
- No essential fact requires JavaScript

## Pathfinder compliance

- Internal-only contact patterns: absent
- Approved public phone and plain email: present
- Path Plaza service/Roadmap fee: absent
- Admission/visa outcome guarantee: absent
- Fixed decision timeline: absent
- Unsupported universal funds amount: absent
- Universal 30-day residence claim: absent
- Global disclaimer appears in Urdu plus verbatim English
- Public form CTA does not ask for passport, bank or refusal documents

## Important English-source alignment note

The Urdu page uses a stricter source posture than the earlier English A1 build. Before treating both pages as a final translation pair, schedule a separate English A1 source-alignment patch for the funds benchmark, photo wording, processing estimate and residence-application timing. Do not copy the older English claims back into the Urdu page.

## GA4

The GA4 ID remains blank, so no tracker loads. The page is ready to emit language-labelled:

- `article_view`
- `cta_profile_click`
- `cta_whatsapp_click`

## Date rule

If publication occurs after 21 August 2026, update the visible date, BlogPosting dates, source-review date, blog-index date and sitemap `lastmod` before deployment.
