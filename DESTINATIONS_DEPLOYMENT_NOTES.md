# Destinations Page — Deployment Notes

**Page:** `destinations.html`  
**Prepared:** 17 August 2026  
**Conversion target:** Free Initial Profile Check  
**Primary keyword target:** study abroad destinations  
**Supporting intent:** compare study in the UK, Ireland, Malaysia and Turkey

## What changed

- Redesigned the page with the Path Plaza navy, blue, teal and gold identity, a split hero, destination matchboard, trust rail, destination cards, comparison board, cost-planning panel and verification workflow.
- Added icon-based social-media buttons in the top strip, a dedicated Follow Path Plaza panel and the footer, plus a floating WhatsApp button. All links use the approved Path Plaza profiles.
- Rebuilt the supplied page against PP-WEBDEV/Pathfinder compliance and the current uploaded site inventory.
- Added a corrected two-tier responsive header, destination dropdown, mobile navigation and five-column footer.
- Embedded the approved `Logo.png` as a data URI without redrawing, recolouring or changing its aspect ratio.
- Kept one H1 and added a 57-character title, 147-character meta description, canonical URL, Open Graph/Twitter metadata, `WebPage`, `EducationalOrganization`, `BreadcrumbList` and matching `FAQPage` JSON-LD.
- Replaced blanket cost bands, PKR conversions, “cheapest” labels and unsupported destination superlatives with a course-specific total-cost framework.
- Replaced broad claims about employment, post-study status, flexibility and test waivers with verification-first wording.
- Added official-source gateway links for the UK, Ireland, Malaysia and Turkey. Gateway links were checked on 17 August 2026; programme, fee, intake and case-specific immigration details still require a fresh check before use.
- Used plain-text `info@pathplaza.com` with `mailto:` links and only the approved public phone/WhatsApp contact.
- Removed Cloudflare email-obfuscation and challenge scripts, external fonts and icon-library dependencies.
- Added keyboard focus styles, a skip link, accessible mobile-menu controls, 44px+ navigation targets, reduced-motion handling and print CSS.
- Added the global disclaimer verbatim, followed by a separate page-specific August 2026 review caveat.

## Link strategy

The uploaded baseline does not include deployed country-detail pages. To prevent dropdown and footer 404s, destination links currently point to these in-page sections:

- `destinations.html#uk`
- `destinations.html#ireland`
- `destinations.html#malaysia`
- `destinations.html#turkey`

Replace those anchors with the corresponding country-guide URLs only after each guide is deployed and claim-checked.

The uploaded FAQ filename is case-sensitive, so the footer correctly uses `FAQs.html`.

## Verification status

No course-register figures, institution fee bands, exchange-rate conversions, scholarship figures or university logos are published on this page. No aggregator data was used. The page intentionally directs visitors to a profile-led, official-source verification process before application or payment.

## Pre-publish checks completed

- One H1: passed
- Title length: 57 characters
- Meta description: 147 characters
- Canonical: passed
- JSON-LD parses as valid JSON
- Internal fragment targets: passed
- Local page links match the uploaded baseline
- `target="_blank"` links use `rel="noopener"`
- Verbatim global disclaimer: passed
- Public contact and email rules: passed
- Banned outcome/statistic/fee wording scan: passed
- No form or credential collection added

## Deployment actions

1. Upload `destinations.html` to the site root.
2. Add this entry to `sitemap.xml`:

```xml
<url>
  <loc>https://pathplaza.com/destinations.html</loc>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

3. Add the Destinations dropdown to the shared site header after its separate compliance fix.
4. Add internal links to `destinations.html` from the home, about and services pages.
5. Do not replace this page's corrected embedded shell with the current uploaded shared header/footer until the internal-only contact line in those shared files has been removed and the footer disclaimer/navigation have been brought up to the same standard.
