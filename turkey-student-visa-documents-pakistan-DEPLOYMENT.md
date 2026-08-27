# A1 Deployment & Publishing Guide

## Deliverable

`/blog/turkey-student-visa-documents-pakistan.html`

**Publication date:** 21 August 2026  
**Updated date:** 21 August 2026  
**Category:** Turkey  
**Primary keyword:** turkey student visa pakistan documents  
**Computed length:** approximately 1,445 visible article words  
**Displayed reading time:** 8 minutes

## Files updated

- `blog/turkey-student-visa-documents-pakistan.html` — new article
- `blog.html` — featured slot, live card and Blog schema updated
- `sitemap.xml` — article URL and real `lastmod` added

## Build decisions

- The approved A1 copy deck was rendered into the binding article template.
- The supplied meta description was shortened to 144 characters to meet the article-template requirement while preserving the keyword intent.
- The seven-mistakes list was rendered as the fourth responsive table, matching the copy deck's build note.
- The Turkey category uses the public navy/blue treatment rather than the internal-only crimson token.
- Four visible FAQs were added with matching FAQPage schema text.
- Six official-source links are shown. The three deck sources were retained and current official consular, residence-type and residence-fee pages were added.
- Only the live Turkey destination guide is shown under related guidance. The two unpublished Phase-A articles were not linked, preventing deliberate 404s and ghost inventory.
- No hero photograph was introduced; the page remains self-contained and uses the approved embedded Path Plaza logo.

## Required deployment order

1. Upload the `blog/` directory so the live path is:

   ```text
   https://pathplaza.com/blog/turkey-student-visa-documents-pakistan.html
   ```

2. Upload the updated root `blog.html`.
3. Upload the updated `sitemap.xml`.
4. Confirm `study-in-turkey.html` is already live because the article's related-guidance card links to it.
5. Open the article at 360px, 768px and desktop width.
6. Test the mobile menu, desktop TOC, mobile TOC, all table scroll regions, four FAQs and both CTA locations.
7. Confirm each official source opens on the publish-day network.
8. Submit the updated sitemap in Google Search Console after deployment.

## Source-status note

The Ministry of Foreign Affairs, consular portal, e-İkamet portal, residence-permit-types page and 2026 residence-fee page were reachable during build QA on 21 August 2026. The Turkish Embassy Islamabad hostname could not be resolved from the sandbox network even though it is the approved source in the copy deck. Manually confirm that link from the production network before publication; if it remains unavailable, replace it with the mission's current official page rather than a third-party copy.

The numerical visa, attestation, insurance, airfare, processing and funds benchmarks were supplied by the approved copy deck and are visibly labelled indicative. They must still be re-verified for an individual client within 30 days of filing.

## SEO and schema QA

- Canonical: passed
- One H1: passed
- Meta description: 144 characters
- BlogPosting schema: valid JSON
- BreadcrumbList schema: valid JSON
- FAQPage schema: valid JSON
- Visible FAQ and FAQ schema text: exact match
- Real publication and modification dates: passed
- Blog index card date and article date: matched
- Sitemap article count: one

## Structure and accessibility QA

- Article wrapper and ordered heading structure: passed
- Eight numbered body H2 sections: passed
- Desktop TOC and collapsible mobile TOC: passed
- Four responsive table wrappers: passed
- Key-facts box: passed
- Mandatory change caveat: passed
- Mid-article CTA placed after section 5: passed
- End CTA: passed
- Six official-source links use `rel="noopener"`: passed
- Visible keyboard focus, reduced-motion and print rules: passed
- File size approximately 236 KB, below the 350 KB cap

## Pathfinder compliance scan

- Internal-only contact patterns: absent
- Approved public phone and plain email: present
- Outcome/probability and banned-statistic phrases: absent
- Public Path Plaza Roadmap/service fee: absent
- Unsupported partnership wording: absent
- Global disclaimer: present verbatim
- Password, OTP or credential requests: absent

The references to PKR 5,000–10,000 concern indicative third-party document-attestation costs from the approved copy deck; they are not a Path Plaza service or Roadmap fee.

## GA4

`window.PP_GA4_ID` remains blank. No tracker loads until management provides and approves the measurement ID. Once configured, this article is ready to emit:

- `article_view`
- `cta_profile_click`
- `cta_whatsapp_click` with location values

## Future related-post update

After A2 and A3 are approved and deployed, add these related cards and previous/next links:

- `/blog/malaysia-university-fees-pakistani-students-2026.html`
- `/blog/pte-vs-ielts-2026-which-test.html`

Then re-run the link, schema and compliance checks and update the article's modification date.
