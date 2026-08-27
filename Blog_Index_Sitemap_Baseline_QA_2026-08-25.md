# Blog Index and Sitemap Baseline QA

**Date:** 25 August 2026  
**Result:** **PASS**  
**Scope:** Newly recreated `blog.html` and `sitemap.xml`

## Build result

- Former generated `blog.html` deleted locally and replaced with a clean file.
- Former generated `sitemap.xml` deleted locally and replaced with a clean file.
- The replacement files were built from the 18 real article HTML files in `/blog/`; `_article-template.html` was excluded.
- No production upload or cache purge was performed.

## Inventory checks

- [x] 18 real article files
- [x] 18 visible blog cards
- [x] 18 BlogPosting schema records
- [x] 18 sitemap article URLs
- [x] 9 English cards and 9 Urdu cards
- [x] 9 reciprocal English/Urdu article pairs
- [x] Cards, schema records, sitemap URLs and files describe the same inventory
- [x] No duplicate card, schema URL or sitemap URL
- [x] 34 total sitemap URLs: 16 core/legal/index URLs plus 18 articles

## SEO and technical checks

- [x] Blog title: 59 characters
- [x] Blog meta description: 149 characters
- [x] Self-referencing blog canonical
- [x] Blog JSON-LD parses successfully
- [x] Sitemap XML parses successfully
- [x] Blog JavaScript passes syntax checking
- [x] Every bilingual sitemap pair has `en-PK`, `ur-PK` and `x-default`
- [x] Current filter totals: All 18, Turkey 18, Process 12, Money 6, Family 4, Urdu 9
- [x] Blog file size: 42,940 bytes
- [x] Sitemap file size: 13,924 bytes

## Brand, contact and accessibility checks

- [x] Approved Path Plaza logo reference retained
- [x] Approved social links retained
- [x] Visible contact remains `92315-500-9620`
- [x] WhatsApp target remains `https://wa.me/923155009620`
- [x] No prohibited old contact format
- [x] Urdu cards use the local Nastaleeq font
- [x] Responsive desktop, tablet and mobile layouts included
- [x] Keyboard focus, skip link and reduced-motion support included
- [x] No template variable or ghost article inventory

## Future maintenance decision

The new `blog.html` and `sitemap.xml` are now permanent working baselines. Future article releases must update these two files in place rather than deleting or rebuilding them.

## Operational note

This replacement is workspace-only. Human hosting access is required to upload the files and purge cache. The separate failed production contact-release smoke test remains unresolved and is not closed by this blog-index maintenance.
