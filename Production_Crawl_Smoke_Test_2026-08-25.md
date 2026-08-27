# Path Plaza — Production Crawl Smoke Test

**Run:** 2026-08-25T16:23:18+05:00  
**Base:** https://pathplaza.com/  
**Expected release inventory:** 18 cards · 18 schema posts · 18 sitemap articles  
**Overall:** **FAIL**  
**URLs requested:** 40 · **Discovered internal links checked:** 39 · **Broken:** 4

## Executive summary

- Shared header and footer were fetched directly.
- Home, destination, legal, profile-review, blog and crawl-asset groups were requested from production.
- Both the live sitemap inventory and every article expected by the retained local release baseline were requested.
- Visible contact formatting, WhatsApp targets, plain email, Cloudflare obfuscation, canonicals, H1 counts and template tokens were checked.
- Blog cards, BlogPosting schema and live sitemap articles were compared with the retained local blog.html and sitemap.xml baselines.
- Discovered same-site links were smoke-tested.

## Release gates

| Gate | Result |
|---|---|
| Header HTTP 200 | PASS |
| Footer HTTP 200 | PASS |
| Approved contact visible in header (92315-500-9620) | FAIL |
| Approved contact visible in footer (92315-500-9620) | FAIL |
| Plain email remains unprotected | FAIL |
| No prohibited contact across crawl | FAIL |
| No template placeholders | FAIL |
| All requested URLs HTTP 200 | PASS |
| No broken discovered internal links | FAIL |
| Blog index contains 18 cards | PASS |
| Blog schema contains 18 posts | PASS |
| Blog sitemap contains 18 article URLs | PASS |
| Live article sitemap matches retained baseline | PASS |

## Blog inventory comparison

- Retained baseline cards/schema/articles: 18/18/18
- Live cards/schema/articles: 18/18/18
- Missing expected live sitemap articles: 0
- Extra live sitemap articles: 0

## Issue register

| Severity | URL | Evidence |
|---|---|---|
| P0 | `https://pathplaza.com/header.html` | Displays 923155009620 instead of 92315-500-9620 |
| P0 | `https://pathplaza.com/footer.html` | Displays 923155009620 instead of 92315-500-9620 |
| P0 | `https://pathplaza.com/` | Prohibited contact pattern(s): obsolete Pakistan +92 315 5009620 |
| P0 | `https://pathplaza.com/index.html` | Prohibited contact pattern(s): obsolete Pakistan +92 315 5009620 |
| P0 | `https://pathplaza.com/destinations.html` | Prohibited contact pattern(s): obsolete Pakistan +92 315 5009620 |
| P1 | `https://pathplaza.com/destinations.html` | Displays 923155009620 instead of 92315-500-9620 |
| P0 | `https://pathplaza.com/study-in-uk.html` | Prohibited contact pattern(s): obsolete Pakistan +92 315 5009620 |
| P0 | `https://pathplaza.com/study-in-uk.html` | Email is protected/obfuscated; keep plain info@pathplaza.com |
| P1 | `https://pathplaza.com/study-in-uk.html` | Displays 923155009620 instead of 92315-500-9620 |
| P0 | `https://pathplaza.com/study-in-ireland.html` | Prohibited contact pattern(s): obsolete Pakistan +92 315 5009620 |
| P1 | `https://pathplaza.com/study-in-ireland.html` | Displays 923155009620 instead of 92315-500-9620 |
| P0 | `https://pathplaza.com/study-in-malaysia.html` | Prohibited contact pattern(s): obsolete Pakistan +92 315 5009620 |
| P1 | `https://pathplaza.com/study-in-malaysia.html` | Displays 923155009620 instead of 92315-500-9620 |
| P0 | `https://pathplaza.com/study-in-turkey.html` | Prohibited contact pattern(s): obsolete Pakistan +92 315 5009620 |
| P1 | `https://pathplaza.com/study-in-turkey.html` | Displays 923155009620 instead of 92315-500-9620 |
| P0 | `https://pathplaza.com/privacy-policy.html` | Prohibited contact pattern(s): obsolete Pakistan +92 315 5009620 |
| P2 | `https://pathplaza.com/privacy-policy.html` | canonical missing |
| P2 | `https://pathplaza.com/terms.html` | canonical missing |
| P0 | `https://pathplaza.com/disclaimer.html` | Prohibited contact pattern(s): obsolete Pakistan +92 315 5009620 |
| P1 | `https://pathplaza.com/disclaimer.html` | Displays 923155009620 instead of 92315-500-9620 |
| P2 | `https://pathplaza.com/disclaimer.html` | canonical missing |
| P0 | `https://pathplaza.com/service-scope-and-refund-policy.html` | Prohibited contact pattern(s): obsolete Pakistan +92 315 5009620 |
| P2 | `https://pathplaza.com/service-scope-and-refund-policy.html` | canonical missing |
| P0 | `https://pathplaza.com/FAQs.html` | Prohibited contact pattern(s): obsolete Pakistan +92 315 5009620 |
| P2 | `https://pathplaza.com/FAQs.html` | canonical missing |
| P0 | `https://pathplaza.com/blog.html` | Email is protected/obfuscated; keep plain info@pathplaza.com |
| P0 | `https://pathplaza.com/blog/best-cities-turkey-pakistani-students-urdu.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/best-cities-turkey-pakistani-students-urdu.html` | canonical mismatch: https://pathplaza.com/blog/best-cities-turkey-pakistani-students.html |
| P0 | `https://pathplaza.com/blog/best-cities-turkey-pakistani-students.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/best-cities-turkey-pakistani-students.html` | canonical mismatch: https://pathplaza.com/blog/best-cities-turkey-pakistani-students-urdu.html |
| P0 | `https://pathplaza.com/blog/denklik-attestation-documents-turkey-pakistani-students-urdu.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/denklik-attestation-documents-turkey-pakistani-students-urdu.html` | canonical mismatch: https://pathplaza.com/blog/denklik-attestation-documents-turkey-pakistani-students.html |
| P0 | `https://pathplaza.com/blog/denklik-attestation-documents-turkey-pakistani-students.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/denklik-attestation-documents-turkey-pakistani-students.html` | canonical mismatch: https://pathplaza.com/blog/denklik-attestation-documents-turkey-pakistani-students-urdu.html |
| P0 | `https://pathplaza.com/blog/ikamet-student-residence-permit-turkey-guide-urdu.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/ikamet-student-residence-permit-turkey-guide-urdu.html` | canonical mismatch: https://pathplaza.com/blog/ikamet-student-residence-permit-turkey-guide.html |
| P0 | `https://pathplaza.com/blog/ikamet-student-residence-permit-turkey-guide.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/ikamet-student-residence-permit-turkey-guide.html` | canonical mismatch: https://pathplaza.com/blog/ikamet-student-residence-permit-turkey-guide-urdu.html |
| P0 | `https://pathplaza.com/blog/study-in-turkey-from-pakistan-beginner-guide-2026-urdu.html` | Email is protected/obfuscated; keep plain info@pathplaza.com |
| P0 | `https://pathplaza.com/blog/study-in-turkey-without-ielts-2026-urdu.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/study-in-turkey-without-ielts-2026-urdu.html` | canonical mismatch: https://pathplaza.com/blog/study-in-turkey-without-ielts-2026.html |
| P0 | `https://pathplaza.com/blog/study-in-turkey-without-ielts-2026.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/study-in-turkey-without-ielts-2026.html` | canonical mismatch: https://pathplaza.com/blog/study-in-turkey-without-ielts-2026-urdu.html |
| P0 | `https://pathplaza.com/blog/turkey-student-visa-processing-time-fees-pakistan-urdu.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/turkey-student-visa-processing-time-fees-pakistan-urdu.html` | canonical mismatch: https://pathplaza.com/blog/turkey-student-visa-processing-time-fees-pakistan.html |
| P0 | `https://pathplaza.com/blog/turkey-student-visa-processing-time-fees-pakistan.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/turkey-student-visa-processing-time-fees-pakistan.html` | canonical mismatch: https://pathplaza.com/blog/turkey-student-visa-processing-time-fees-pakistan-urdu.html |
| P0 | `https://pathplaza.com/blog/turkiye-burslari-2027-guide-pakistani-students-urdu.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/turkiye-burslari-2027-guide-pakistani-students-urdu.html` | canonical mismatch: https://pathplaza.com/blog/turkiye-burslari-2027-guide-pakistani-students.html |
| P0 | `https://pathplaza.com/blog/turkiye-burslari-2027-guide-pakistani-students.html` | Template/placeholder token visible |
| P2 | `https://pathplaza.com/blog/turkiye-burslari-2027-guide-pakistani-students.html` | canonical mismatch: https://pathplaza.com/blog/turkiye-burslari-2027-guide-pakistani-students-urdu.html |
| P1 | `https://pathplaza.com/cdn-cgi/l/email-protection` | Internal link returned 404 |
| P1 | `https://pathplaza.com/faqs.html` | Internal link returned 404 |
| P1 | `https://pathplaza.com/privacy-policy` | Internal link returned 404 |
| P1 | `https://pathplaza.com/terms-of-use` | Internal link returned 404 |

## Crawl results

| Group | HTTP | Result | Title/asset | Contact | Email | Notes |
|---|---:|---|---|---:|---:|---|
| Shell | 200 | FAIL | header.html | 0 | 1 | Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Shell | 200 | FAIL | footer.html | 0 | 1 | Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Home | 200 | FAIL | Path Plaza | Study Abroad Consultancy for UK, Turkey, Ireland & Malaysia | 0 | 0 | No cache-status header |
| Home | 200 | FAIL | Path Plaza | Study Abroad Consultancy for UK, Turkey, Ireland & Malaysia | 0 | 0 | No cache-status header |
| Home | 200 | PASS | About Us | Path Plaza — Study Abroad Consultancy Pakistan | 0 | 0 | No cache-status header |
| Home | 200 | PASS | Our Services | Path Plaza — Study Abroad Consultancy Pakistan | 0 | 0 | No cache-status header |
| Home | 200 | PASS | Partner Universities | Path Plaza — Study Abroad Consultancy Pakistan | 0 | 0 | No cache-status header |
| Destinations | 200 | FAIL | Study Abroad Destinations: UK, Ireland, Malaysia & Turkey | 0 | 2 | Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Destinations | 200 | FAIL | Study in UK from Pakistan 2026 — Requirements, Fees, Intakes | Path Plaza | 0 | 2 | Cloudflare email obfuscation present; Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Destinations | 200 | FAIL | Study in Ireland from Pakistan — Requirements, Costs & Visa (2026) | Path Plaza | 0 | 3 | Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Destinations | 200 | FAIL | Study in Malaysia from Pakistan — Fees, Requirements & Visa (2026) | Path Plaza | 0 | 3 | Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Destinations | 200 | FAIL | Study in Turkey from Pakistan — Fees, Requirements & Visa (2026) | Path Plaza | 0 | 3 | Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Legal | 200 | FAIL | Privacy Policy | Path Plaza — Education & Visa Consultants | 3 | 5 | canonical missing |
| Legal | 200 | FAIL | Terms of Use | Path Plaza — Education & Visa Consultants | 0 | 3 | canonical missing |
| Legal | 200 | FAIL | Disclaimer | Path Plaza — Education & Visa Consultants | 0 | 1 | canonical missing; Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Legal | 200 | FAIL | Service Scope & Refund Policy | Path Plaza — Education & Visa Consultants | 2 | 2 | canonical missing |
| Legal | 200 | FAIL | Service Scope & Refund Policy | Path Plaza — Education & Visa Consultants | 2 | 2 | canonical missing |
| Profile Review | 200 | PASS | Initial Profile Review | Path Plaza — Study Abroad Consultancy Pakistan | 1 | 1 | No cache-status header |
| Blog | 200 | FAIL | Study Abroad Blog — Turkey Guides for Pakistan | Path Plaza | 2 | 0 | Cloudflare email obfuscation present |
| Blog | 200 | FAIL | استنبول، انقرہ یا ازمیر: پاکستانی طالب علم کے بجٹ کی اردو گائیڈ | پاتھ پلازا | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/best-cities-turkey-pakistani-students.html |
| Blog | 200 | FAIL | Istanbul vs Ankara vs Izmir for Pakistani Students | Path Plaza | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/best-cities-turkey-pakistani-students-urdu.html |
| Blog | 200 | FAIL | ترکی کے لیے Denklik اور اٹیسٹیشن: پاکستانی طلبہ کی اردو گائیڈ | پاتھ پلازا | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/denklik-attestation-documents-turkey-pakistani-students.html |
| Blog | 200 | FAIL | Denklik & Attestation for Pakistani Students in Turkey | Path Plaza | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/denklik-attestation-documents-turkey-pakistani-students-urdu.html |
| Blog | 200 | FAIL | ترکی میں طالب علم کی اقامت: آسان اردو گائیڈ 2026 | پاتھ پلازا | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/ikamet-student-residence-permit-turkey-guide.html |
| Blog | 200 | FAIL | İkamet for Students in Turkey: Residence Permit Guide 2026 | Path Plaza | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/ikamet-student-residence-permit-turkey-guide-urdu.html |
| Blog | 200 | FAIL | ترکی میں تعلیم: پاکستانی طلبہ کے لیے آسان گائیڈ 2026 | 4 | 0 | Cloudflare email obfuscation present |
| Blog | 200 | PASS | Study in Turkey from Pakistan: Complete Beginner Guide 2026 | 4 | 3 | No cache-status header |
| Blog | 200 | FAIL | IELTS کے بغیر ترکی میں تعلیم: اصل راستے 2026 | پاتھ پلازا | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/study-in-turkey-without-ielts-2026.html |
| Blog | 200 | FAIL | Study in Turkey Without IELTS: Routes That Actually Exist (2026) | Path Plaza | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/study-in-turkey-without-ielts-2026-urdu.html |
| Blog | 200 | PASS | ترکی اسٹوڈنٹ ویزا دستاویزات: پاکستانی طلبہ کی چیک لسٹ | پاتھ پلازا | 2 | 3 | No cache-status header |
| Blog | 200 | PASS | Turkey Student Visa Documents for Pakistani Applicants (2026) | Path Plaza Blog | 4 | 3 | No cache-status header |
| Blog | 200 | FAIL | پاکستان سے ترکی اسٹوڈنٹ ویزا: وقت اور فیس کی آسان گائیڈ 2026 | پاتھ پلازا | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/turkey-student-visa-processing-time-fees-pakistan.html |
| Blog | 200 | FAIL | Turkey Student Visa Processing Time & Fees from Pakistan (2026) | Path Plaza | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/turkey-student-visa-processing-time-fees-pakistan-urdu.html |
| Blog | 200 | PASS | ترکی یونیورسٹی فیس 2026: پاکستانی طلبہ کے لیے | پاتھ پلازا | 2 | 3 | No cache-status header |
| Blog | 200 | PASS | Turkey University Fees for Pakistani Students 2026 | Path Plaza | 2 | 3 | No cache-status header |
| Blog | 200 | FAIL | Türkiye Scholarships 2027: پاکستانی طلبہ کی آسان اردو گائیڈ | پاتھ پلازا | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/turkiye-burslari-2027-guide-pakistani-students.html |
| Blog | 200 | FAIL | Türkiye Scholarships 2027 Guide for Pakistani Students | Path Plaza | 3 | 3 | canonical mismatch: https://pathplaza.com/blog/turkiye-burslari-2027-guide-pakistani-students-urdu.html |
| Crawl Assets | 200 | PASS | robots.txt | 0 | 0 | No cache-status header |
| Crawl Assets | 200 | PASS | sitemap.xml | 0 | 0 | No cache-status header |
| Crawl Assets | 200 | PASS | NotoNastaliqUrdu-Arabic.woff2 | 0 | 0 | No cache-status header |

## Internal-link check

- Unique same-site links checked: 39
- Broken/non-success links: 4
- `404` — https://pathplaza.com/cdn-cgi/l/email-protection — HTTP Error 404: Not Found
- `404` — https://pathplaza.com/faqs.html — HTTP Error 404: Not Found
- `404` — https://pathplaza.com/privacy-policy — HTTP Error 404: Not Found
- `404` — https://pathplaza.com/terms-of-use — HTTP Error 404: Not Found

## Cache verification note

The crawler sent `Cache-Control: no-cache` and `Pragma: no-cache`. No Cloudflare/LiteSpeed cache-status header was exposed, so a cache purge cannot be proven from headers alone. Because public responses do not yet match the retained release baseline, deployment and purge success are not established.

## Evidence files

- `Production_Crawl_Smoke_Test_2026-08-25.csv` — row-level crawl export
- `run_contact_release_smoke_test.py` — reproducible crawler

---

**Conclusion:** Production smoke test failed; resolve the issue register and rerun before closing the release.