# Blog Index and Sitemap Maintenance Rule

**Baseline recreated:** 25 August 2026  
**Canonical working files:**

- `/home/user/Path_Plaza_Website/blog.html`
- `/home/user/Path_Plaza_Website/sitemap.xml`

## Standing rule

These two files are now the retained baseline. **Do not delete or regenerate them during normal article publishing.** When a new article is created, edit these existing files in place.

## Required update for every new article

### `blog.html`

1. Add one visible card for each language page actually published.
2. Add the matching BlogPosting item to the existing Blog JSON-LD.
3. Use the real publication and modification dates.
4. Update visible filter totals.
5. Update the Blog `dateModified` value.
6. Add a language link only when the counterpart page exists.
7. Preserve every existing real article card and schema record.

### `sitemap.xml`

1. Add one `<url>` entry for each new article file.
2. Add reciprocal `en-PK` and `ur-PK` alternates when both language pages exist.
3. Keep `x-default` pointed to the English page for a bilingual pair.
4. Add only languages actually published; never create ghost URLs.
5. Use the real `lastmod` date.
6. Preserve all existing core and article URLs.
7. Update the existing `blog.html` sitemap entry when the blog index changes.

## Required QA after each update

- Article files, blog cards, BlogPosting records and sitemap article URLs must describe the same inventory.
- No duplicate card, schema URL or sitemap URL.
- JSON-LD and XML must parse successfully.
- Reciprocal hreflang must be complete for every bilingual pair.
- Visible contact must remain `92315-500-9620`.
- WhatsApp target must remain `https://wa.me/923155009620`.
- Email must remain visible as plain `info@pathplaza.com` with `mailto:info@pathplaza.com`.
- Do not protect, encode, obfuscate or replace the email with Cloudflare `/cdn-cgi/l/email-protection` output.
- No template token, invented article, invented date or unpublished language URL.

## Current baseline inventory

- 18 real article files
- 9 English pages
- 9 Urdu pages
- 9 reciprocal bilingual pairs
- 18 visible blog cards
- 18 BlogPosting records
- 18 sitemap article URLs
- 34 total sitemap URLs, including 16 core/legal/index URLs

This baseline replaces the former generated `blog.html` and `sitemap.xml` files.
