# Contact Release — Crawl Smoke Test

**Run:** 2026-08-24T09:18:16+00:00  
**Base:** https://pathplaza.com/  
**Overall:** **FAIL**  
**URLs requested:** 38 · **Discovered internal links checked:** 37 · **Broken:** 4

## Executive summary

- Shared header and footer were fetched directly to test the released contact patch.
- Home, blog, destination, legal and profile-review groups were crawled from production.
- Every article URL found in the live sitemap was included.
- Responses were scanned for the internal UK contact, obsolete Pakistan-number formats and template tokens.
- Plain email, WhatsApp links, canonicals, H1 counts and cache headers were recorded.
- Internal same-site links discovered during the crawl were smoke-tested.
- No cache-status response header is not treated as a failure when fresh public content is visible.

## Release gates

| Gate | Result |
|---|---|
| Header HTTP 200 | PASS |
| Footer HTTP 200 | PASS |
| Approved contact visible in header | FAIL |
| Approved contact visible in footer | FAIL |
| No prohibited contact across crawl | FAIL |
| No template placeholders | PASS |
| All requested URLs HTTP 200 | PASS |
| No broken discovered internal links | FAIL |
| Blog index contains 16 cards | PASS |
| Blog sitemap contains 16 article URLs | PASS |

## Issue register

| Severity | URL | Evidence |
|---|---|---|
| P1 | `https://pathplaza.com/header.html` | Contact formatting mismatch: displays 923155009620 instead of 92315-500-9620 |
| P1 | `https://pathplaza.com/footer.html` | Contact formatting mismatch: displays 923155009620 instead of 92315-500-9620 |
| P1 | `https://pathplaza.com/destinations.html` | Contact formatting mismatch: displays 923155009620 instead of 92315-500-9620 |
| P0 | `https://pathplaza.com/study-in-uk.html` | Prohibited contact pattern(s): +92 315 5009620 |
| P2 | `https://pathplaza.com/study-in-uk.html` | Cloudflare email obfuscation present |
| P0 | `https://pathplaza.com/study-in-ireland.html` | Prohibited contact pattern(s): +92 315 5009620 |
| P0 | `https://pathplaza.com/study-in-malaysia.html` | Prohibited contact pattern(s): +92 315 5009620 |
| P0 | `https://pathplaza.com/study-in-turkey.html` | Prohibited contact pattern(s): +92 315 5009620 |
| P2 | `https://pathplaza.com/privacy-policy.html` | canonical missing |
| P2 | `https://pathplaza.com/terms.html` | canonical missing |
| P1 | `https://pathplaza.com/disclaimer.html` | Contact formatting mismatch: displays 923155009620 instead of 92315-500-9620 |
| P2 | `https://pathplaza.com/disclaimer.html` | canonical missing |
| P2 | `https://pathplaza.com/service-scope-and-refund-policy.html` | canonical missing |
| P2 | `https://pathplaza.com/FAQs.html` | canonical missing |
| P1 | `https://pathplaza.com/cdn-cgi/l/email-protection` | Internal link returned 404 |
| P1 | `https://pathplaza.com/faqs.html` | Internal link returned 404 |
| P1 | `https://pathplaza.com/privacy-policy` | Internal link returned 404 |
| P1 | `https://pathplaza.com/terms-of-use` | Internal link returned 404 |

## Crawl results

| Group | HTTP | Result | Title/asset | Contact | Email | Notes |
|---|---:|---|---|---:|---:|---|
| Shell | 200 | FAIL | header.html | 0 | 1 | Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Shell | 200 | FAIL | footer.html | 0 | 1 | Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Home | 200 | PASS | Path Plaza | Study Abroad Consultancy for UK, Turkey, Ireland & Malaysia | 0 | 0 | No cache-status header |
| Home | 200 | PASS | Path Plaza | Study Abroad Consultancy for UK, Turkey, Ireland & Malaysia | 0 | 0 | No cache-status header |
| Home | 200 | PASS | About Us | Path Plaza — Study Abroad Consultancy Pakistan | 0 | 0 | No cache-status header |
| Home | 200 | PASS | Our Services | Path Plaza — Study Abroad Consultancy Pakistan | 0 | 0 | No cache-status header |
| Home | 200 | PASS | Partner Universities | Path Plaza — Study Abroad Consultancy Pakistan | 0 | 0 | No cache-status header |
| Destinations | 200 | FAIL | Study Abroad Destinations: UK, Ireland, Malaysia & Turkey | 0 | 2 | Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Destinations | 200 | FAIL | Study in UK from Pakistan 2026 — Requirements, Fees, Intakes | Path Plaza | 0 | 0 | Cloudflare email obfuscation present |
| Destinations | 200 | FAIL | Study in Ireland from Pakistan — Requirements, Costs & Visa (2026) | Path Plaza | 0 | 3 | No cache-status header |
| Destinations | 200 | FAIL | Study in Malaysia from Pakistan — Fees, Requirements & Visa (2026) | Path Plaza | 0 | 3 | No cache-status header |
| Destinations | 200 | FAIL | Study in Turkey from Pakistan — Fees, Requirements & Visa (2026) | Path Plaza | 0 | 3 | No cache-status header |
| Legal | 200 | FAIL | Privacy Policy | Path Plaza — Education & Visa Consultants | 3 | 5 | canonical missing |
| Legal | 200 | FAIL | Terms of Use | Path Plaza — Education & Visa Consultants | 0 | 3 | canonical missing |
| Legal | 200 | FAIL | Disclaimer | Path Plaza — Education & Visa Consultants | 0 | 1 | canonical missing; Displayed contact is compact 923155009620; expected 92315-500-9620 |
| Legal | 200 | FAIL | Service Scope & Refund Policy | Path Plaza — Education & Visa Consultants | 2 | 2 | canonical missing |
| Legal | 200 | FAIL | Service Scope & Refund Policy | Path Plaza — Education & Visa Consultants | 2 | 2 | canonical missing |
| Profile Review | 200 | PASS | Initial Profile Review | Path Plaza — Study Abroad Consultancy Pakistan | 1 | 1 | No cache-status header |
| Blog | 200 | PASS | Study Abroad Blog — UK, Turkey, Ireland, Malaysia | Path Plaza | 2 | 2 | No cache-status header |
| Blog | 200 | PASS | Study in Turkey Without IELTS: Routes That Actually Exist (2026) | Path Plaza | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | IELTS کے بغیر ترکی میں تعلیم: اصل راستے 2026 | پاتھ پلازا | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | Türkiye Scholarships 2027 Guide for Pakistani Students | Path Plaza | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | Türkiye Scholarships 2027: پاکستانی طلبہ کی آسان اردو گائیڈ | پاتھ پلازا | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | Turkey Student Visa Processing Time & Fees from Pakistan (2026) | Path Plaza | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | پاکستان سے ترکی اسٹوڈنٹ ویزا: وقت اور فیس کی آسان گائیڈ 2026 | پاتھ پلازا | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | İkamet for Students in Turkey: Residence Permit Guide 2026 | Path Plaza | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | ترکی میں طالب علم کی اقامت: آسان اردو گائیڈ 2026 | پاتھ پلازا | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | Denklik & Attestation for Pakistani Students in Turkey | Path Plaza | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | ترکی کے لیے Denklik اور اٹیسٹیشن: پاکستانی طلبہ کی اردو گائیڈ | پاتھ پلازا | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | Istanbul vs Ankara vs Izmir for Pakistani Students | Path Plaza | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | استنبول، انقرہ یا ازمیر: پاکستانی طالب علم کے بجٹ کی اردو گائیڈ | پاتھ پلازا | 3 | 3 | No cache-status header |
| Blog | 200 | PASS | Turkey Student Visa Documents for Pakistani Applicants (2026) | Path Plaza Blog | 4 | 3 | No cache-status header |
| Blog | 200 | PASS | ترکی اسٹوڈنٹ ویزا دستاویزات: پاکستانی طلبہ کی چیک لسٹ | پاتھ پلازا | 2 | 3 | No cache-status header |
| Blog | 200 | PASS | Turkey University Fees for Pakistani Students 2026 | Path Plaza | 2 | 3 | No cache-status header |
| Blog | 200 | PASS | ترکی یونیورسٹی فیس 2026: پاکستانی طلبہ کے لیے | پاتھ پلازا | 2 | 3 | No cache-status header |
| Crawl Assets | 200 | PASS | robots.txt | 0 | 0 | No cache-status header |
| Crawl Assets | 200 | PASS | sitemap.xml | 0 | 0 | No cache-status header |
| Crawl Assets | 200 | PASS | NotoNastaliqUrdu-Arabic.woff2 | 0 | 0 | No cache-status header |

## Internal-link check

- Unique same-site links checked: 37
- Broken/non-success links: 4
- `404` — https://pathplaza.com/cdn-cgi/l/email-protection — HTTP Error 404: Not Found
- `404` — https://pathplaza.com/faqs.html — HTTP Error 404: Not Found
- `404` — https://pathplaza.com/privacy-policy — HTTP Error 404: Not Found
- `404` — https://pathplaza.com/terms-of-use — HTTP Error 404: Not Found

## Cache verification note

The crawler sent `Cache-Control: no-cache` and `Pragma: no-cache`. No Cloudflare/LiteSpeed cache-status headers were returned, so cache purge cannot be proven from response headers alone. Because the normal public URLs still expose contact-format mismatches and prohibited obsolete contact text, purge/deployment success is not established.

## Evidence files

- `Contact_Release_Crawl_Smoke_Test_2026-08-24.csv` — row-level crawl export
- `run_contact_release_smoke_test.py` — reproducible test script (workspace execution artifact)

---

**Conclusion:** Contact release smoke test failed; resolve the issue register before further releases.