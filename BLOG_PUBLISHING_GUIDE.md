# Path Plaza Blog — Manual Publishing Guide

**Build date:** 21 August 2026  
**Files:** `blog.html` and `blog/_article-template.html`

## Current publication state

The blog shell and article template are complete. No article is displayed as live because the three approved Phase-A Markdown copy decks were not supplied. This preserves the brief's rule against editorial improvisation, ghost inventory and invented publication dates.

## Publish a new article

1. Duplicate `blog/_article-template.html`.
2. Rename the duplicate using the approved lowercase, hyphenated slug:

   ```text
   blog/turkey-student-visa-documents-pakistan.html
   ```

3. Replace every `{{TOKEN}}` in the duplicate.
4. Replace the sample body structure with the approved Markdown copy.
5. Keep at least two official sources and record the real date each was checked.
6. If numbers are used, date and label each figure and add the required table.
7. Change:

   ```html
   <meta name="robots" content="noindex,nofollow">
   ```

   to:

   ```html
   <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
   ```

8. Confirm the canonical, Open Graph URL, dates and BlogPosting schema all use the final slug.
9. Add one card to `blog.html` inside:

   ```html
   <div class="posts-grid" id="posts-grid">
     <!-- Add published cards here -->
   </div>
   ```

10. Replace the honest featured empty state when the first live article is ready.
11. Add the article to `sitemap.xml` with its real `lastmod` date.
12. Run the final compliance and link checks before upload.

## Blog card format

```html
<article
  class="post-card"
  data-category="turkey process"
  style="--accent:#0B1F3A;--chip:#EEF1F5"
>
  <div class="post-body">
    <div class="post-top">
      <span class="category-chip">Turkey</span>
      <span class="flag" aria-hidden="true">🇹🇷</span>
    </div>

    <h2>
      <a href="/blog/turkey-student-visa-documents-pakistan.html">
        Turkey Student Visa: A Document Checklist for Pakistani Applicants (2026)
      </a>
    </h2>

    <p class="excerpt">
      Add the approved two-line excerpt from the article copy deck.
    </p>

    <div class="post-meta">
      <time datetime="2026-08-21">21 August 2026</time>
      <span>8 min read</span>
    </div>

    <a
      class="read-link"
      href="/blog/turkey-student-visa-documents-pakistan.html"
    >
      Read →
    </a>
  </div>
</article>
```

The filter script calculates counts from `data-category`. Multiple categories are separated by spaces, for example:

```html
data-category="malaysia money"
```

## Category values and colours

| Visible category | `data-category` value | Accent |
|---|---|---|
| United Kingdom | `uk` | `#1E51C7` |
| Ireland | `ireland` | `#1C7C7D` |
| Malaysia | `malaysia` | `#C9A227` |
| Turkey | `turkey` | `#0B1F3A` |
| Process & Visa Files | `process` | `#1E51C7` |
| Money & Scholarships | `money` | `#C9A227` |
| Parents & Family | `family` | `#1C7C7D` |

## Replace the featured slot

Delete the existing `#featured-slot` empty-state block and replace it with a linked featured article using the same real title, excerpt, date and reading time as the post card. Do not leave a featured placeholder visible after articles are published.

## Sitemap entry per article

```xml
<url>
  <loc>https://pathplaza.com/blog/ARTICLE-SLUG.html</loc>
  <lastmod>YYYY-MM-DD</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.7</priority>
</url>
```

## GA4 setup

Both files contain:

```js
window.PP_GA4_ID='';
```

Leave it blank until management approves and supplies the GA4 measurement ID. While blank, no tracking script is loaded. After configuration, the article template emits:

- `article_view`
- `cta_profile_click`
- `cta_whatsapp_click`

## Pre-publish compliance check

- Only approved public Path Plaza contact details appear.
- No admission, scholarship, visa, employment or settlement outcome claim.
- No probability or “approval chances” language.
- No public Path Plaza service-fee amount.
- No unsupported direct-partnership wording.
- All changeable figures are dated and re-verified within 30 days.
- Two or more official sources are included and reachable.
- The real publication and modification dates match visible metadata and schema.
- Related-post and previous/next links resolve; remove any unused placeholder links.
- The article has one H1, ordered headings, keyboard focus and a working mobile TOC.
- Add optional FAQPage schema only when matching FAQs are visibly published.
- The article stays below the 350 KB all-in limit.

## Phase-A publication state

**Built from approved copy:**

- `blog/turkey-student-visa-documents-pakistan.html` — English build dated 21 August 2026
- `blog/turkey-student-visa-documents-pakistan-urdu.html` — simple-Urdu, RTL Nastaleeq teaching edition dated 21 August 2026
- `blog/turkey-university-fees-pakistani-students-2026.html` — visibility-reviewed English build dated 21 August 2026
- `blog/turkey-university-fees-pakistani-students-2026-urdu.html` — Urdu-script, RTL Nastaleeq edition dated 21 August 2026

**Awaiting approved copy decks:**

- `blog/pte-vs-ielts-2026-which-test.html`

The newer A2 Turkey-fees deck supersedes the earlier working assumption that A2 would be the Malaysia-fees article. Any Malaysia-fees post remains a separate planned asset until management supplies an approved deck and slug.

Build remaining articles only after their approved Markdown copy decks and real publication dates are supplied.
