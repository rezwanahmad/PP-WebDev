# Turkey Blog Cluster — 30-Day Publishing Calendar · RECTIFIED V2
**Window: 19 Aug – 19 Sep 2026 · Owner: Pathfinder (content) × PP-WEBDEV (build) · Cadence: 2 posts/week (Wed + Sat)**
Authority: Blog Developer Brief (18 Aug) · SEO Guide Part 6 · Pathfinder v4.0 — compliance guardrails apply to every post.

**Why this sprint exists:** Turkey is the build-priority destination (Türkiye Burslari window ~Jan–Feb 2027), the dropdown link currently 404s, and Turkey carries our biggest Roman-Urdu search tail. This cluster builds topical authority *before* the master editorial calendar hits its October Turkey slot ("Turkey admission timeline" — unchanged, follows this sprint).

---

## Rectification log — 24 Aug 2026 (Growth desk)
| # | Change | Reason |
|---|---|---|
| R1 | **All dates from post #4 onward corrected to real Wednesdays/Saturdays** (#4 → Sat 29 Aug, #5 → Wed 2 Sep, #6 → Sat 5 Sep, #7 → Wed 9 Sep, #8 → Sat 12 Sep, #9 → Wed 16 Sep, #10 → Sat 19 Sep) | Calendar listed e.g. "Sat 30 Aug 2026" — 30 Aug 2026 is a **Sunday**; the Wed/Sat cadence broke after 26 Aug. Window end corrected 17 Sep → **19 Sep** to cover post #10. |
| R2 | Post #1 marked **LIVE (19 Aug)** with a live-page fix ticket | Article fetched live 24 Aug: it displays the **obsolete contact `+92 315 5009620`** (header + bottom CTA). Fix routed to PP-WEBDEV (see Webdev Brief 24 Aug, P1-48h). |
| R3 | Compliance grep **extended**: add obsolete-phone patterns `+92 315 5009620` / `+92315 5009620` / `+92 315 500-9620` | The published post #1 proves the old sweep (`+44`/`7577`/outcome-claims/Roadmap-fee) misses the exact violation that occurred (Growth v3.0 §3.1: obsolete format must never ship). |
| R4 | "apply to all 9" → **all 10**; Definition of success "All 9" → **All 10** | Post #10 (amended 20 Aug) was added without updating counts. |
| R5 | Post #4 title "…and the Honest Odds" — guard added: **verified public statistics only, no invented percentages, no odds/probability visuals** | v3.0 §4.2/§13.4 (no outcome-probability framing); Burslari stats are Class C — verify ≤30 days at build. |
| R6 | RU-cap flag: posts #9 **and** #10 are both Roman-Urdu — **2 RU posts in one cluster vs the "one RU version per cluster rule"** | #10 is management-ordered (change-log 20 Aug — stands). #9 is the rule's original RU version. Flag to management: confirm the cap is now "one per topic" or "two per cluster" and record in the master persona change-log. Until then, both proceed (management instruction = precedence rank 1, v3.0 §2). |
| R7 | Status check added for post #2 (due Sat 22 Aug — date has passed) | Confirm live/stage status at next ops meeting; if missed, re-slot to next Wed (2 Sep) and shift nothing else (cadence holds). |

---

## Calendar (P1 = launch-critical · P2 = amplifier)

| # | Date | Title (working) | Slug `/blog/…` | Primary keyword | Pri |
|---|---|---|---|---|---|
| 1 | **Wed 19 Aug** | Turkey Student Visa: A Document Checklist for Pakistani Applicants (2026) | `turkey-student-visa-documents-pakistan` | turkey student visa pakistan documents | **P1 — LIVE (19 Aug, deck A1)** ⚠️ live contact-format fix (Webdev Brief P1) |
| 2 | **Sat 22 Aug** | Turkey University Fees for Pakistani Students: Real 2026 Numbers in USD & PKR | `turkey-university-fees-pakistani-students-2026` | turkey university fees pakistani students | **P1** — confirm publish status (R7) |
| 3 | **Wed 26 Aug** | Study in Turkey Without IELTS: The Routes That Actually Exist (2026) | `study-in-turkey-without-ielts-2026` | study in turkey without ielts | **P1** |
| 4 | **Sat 29 Aug** *(was 30 Aug — R1)* | Türkiye Burslari 2027: Full-Scholarship Guide — and the Honest Odds | `turkiye-burslari-2027-guide-pakistani-students` | turkiye burslari 2027 pakistan | **P1** — verified-stats-only guard (R5) |
| 5 | **Wed 2 Sep** *(was 3 Sep — R1)* | Turkey Student Visa Processing Time & Fees from Pakistan (2026): The Real Calendar | `turkey-student-visa-processing-time-fees-pakistan` | turkey student visa processing time pakistan | P2 |
| 6 | **Sat 5 Sep** *(was 6 Sep — R1)* | İkamet After You Land: The 30-Day Residence Permit Clock Every Student Misses | `ikamet-student-residence-permit-turkey-guide` | ikamet for students turkey | P2 |
| 7 | **Wed 9 Sep** *(was 10 Sep — R1)* | Denklik & Attestation: How Pakistani Certificates Become Valid in Turkey (Board → IBCC → HEC → MOFA → Mission) | `denklik-attestation-documents-turkey-pakistani-students` | denklik pakistani students turkey | P2 |
| 8 | **Sat 12 Sep** *(was 13 Sep — R1)* | Istanbul vs Ankara vs Izmir: Which Turkish City Fits a Pakistani Student's Budget? | `best-cities-turkey-pakistani-students` | best city in turkey for international students | P2 |
| 9 | **Wed 16 Sep** *(was 17 Sep — R1, bonus)* | Turkey University Fees 2026 — Roman-Urdu edition (complete rewrite, code-switched) | `turkey-university-fees-pakistani-students-2026-roman-urdu` | turkey mein parhai ka kharcha | P2 — cluster's designated RU version (R6 flag) |
| 10 | **Sat 19 Sep** *(was 20 Sep — R1; amended 20 Aug)* | Bina IELTS Turkey Mein Parhai — Roman-Urdu twin of post #3 | `study-in-turkey-without-ielts-2026-roman-urdu` | bina ielts turkey mein parhai | P2 — management-ordered dual-language twin (change-log 20 Aug; R6 flag) |

**Next after sprint (already scheduled in master calendar):** Oct — *Turkey admission timeline* · Nov — *gap-year policy explainer* (Turkey section) · Dec — *Jan-intake checklist* · Jan 2027 — Burslari application-window reminder post.

---

## Per-post spec card (apply to all 10)

| Field | Standard |
|---|---|
| Template | Blog Brief §6 — 12 sections exact, TOC if >4 H2s, key-facts box + "what can change" caveat box (mandatory) |
| Category chip | **Turkey** (crimson `--tr` #9B1C31 → navy gradient) — #2/#9 also tagged Money & Scholarships |
| Schema | BlogPosting + BreadcrumbList (+ FAQPage when post ends with FAQs — schema text == visible text) |
| Dates | Real publish date only (`updated:`), never placeholders |
| Internal links | every post → `/study-in-turkey.html` + `/initial-profile-review.html`; cross-link siblings in cluster (#6↔#1, #5↔#1, #7↔#1) |
| CTA | Free Profile Check + WhatsApp — **displayed contact exactly `92315-500-9620`**; technical link `wa.me/923155009620?text=…studying%20in%20Turkey.` (digits only in URL — mid + end placements) |
| Sources (verify ≤30 days) | islamabad.emb.mfa.gov.tr · mfa.gov.tr · e-ikamet.goc.gov.tr · turkiyeburslari.gov.tr · university fee pages · HEC |
| Key figure sets (indicative labels) | visa ≈ PKR 12–24k all-in · 2–6 weeks processing · private UG $2,500–8,000/yr · living Istanbul $350–550/mo · İkamet ≈ $80–100 · ≈PKR 280/$ |
| Compliance sweep | grep before merge: `+44` · `7577` · **`+92 315 5009620` / `+92315 5009620` / `+92 315 500-9620` (R3)** · outcome-claims · Roadmap-fee · channel statement verbatim if channels mentioned |
| RU editions (#9/#10) | Separate slugs (`-roman-urdu` suffix), same 12-section template and all guardrails; edition = content language, not a locale (no hreflang); RU-cap status per R6 |

## Ops rhythm
1. **T-2 days:** Pathfinder delivers copy deck (§9 front-matter format) → management review.
2. **T-1 day:** PP-WEBDEV builds, runs QA (grep, schema validator, 360/768/1440, print) → stage.
3. **Publish day:** real date stamped → sitemap.xml `<url>` + `<lastmod>` added → Search Console URL-inspect → GBP post (short summary + link) → WhatsApp status card (office list).
4. **Sunday review:** indexation status of the week's posts; impressions logged; broken-link sweep on new internal links.

## Definition of success (30-day exit)
- All **10** posts live + indexed (GSC coverage clean); `/study-in-turkey.html` page built alongside post #1 so links resolve (dropdown 404 closed).
- Cluster begins appearing for ≥3 primary long-tails; ≥1 profile-check lead attributable to a Turkey post (UTM/GSC event).
- **Live-post compliance fix closed** (post #1 contact format, R2) — zero compliance findings in post-publish sweeps.
- Handoff to master calendar: October "Turkey admission timeline" scheduled with this cluster as its internal-link base.

---
*Amendments to this calendar = management instruction + change-log entry in the master persona. This rectification (24 Aug 2026) is logged above per that rule; R6 awaits management confirmation of the RU cap.*
