# Path Plaza Blog — Developer Build Brief
**For: PP-WEBDEV · Prepared by: Pathfinder v4.0 · 18 August 2026 · Status: approved scope, ready to build**
Governing documents: **Brand Identity Kit v1.0** (`Path_Plaza_Brand_Assets/Path_Plaza_Brand_Identity_Kit_v1.md`) · **SEO Guide Part 6** (`Path_Plaza_SEO_Guide_2026.md`) · Pathfinder v4.0 (§26, §31, §36) · existing `blog.html` v2

---

## 1. Objective
Turn the blog from a v2 placeholder index into the site's **tier-3 SEO engine and trust layer**: long-tail keyword capture (incl. Roman-Urdu), E-E-A-T trust for YMYL-adjacent visa content, and a conversion path feeding the Free Initial Profile Review from every article.

**Success measures (90 days):** blog impressions in Search Console from zero → indexed; 3+ posts ranking page-1 for their primary long-tail; profile-check CTR from article CTA ≥ 4%.

## 2. Current state → target state

| Item | v2 today | Target |
|---|---|---|
| Index | `blog.html`, v2 `.site-shell` chrome, 11 cards as H2s, all marked "Publishing with site launch", Blog JSON-LD, vanilla-JS category filter | Same file **re-skinned to the v4.0 shell** (navy strip + sticky header + Destinations dropdown + 5-col legal footer), cards upgraded with category chips + real-date support + featured slot |
| Articles | 0 (titles exist as cards only) | Per-post files `/blog/<slug>.html`, one URL per post, Article schema each |
| Content | 11 launch titles carried verbatim from Content v2 | Phase A: 3 pilot articles written & shipped (§8) · Phase B: calendar cadence 3–4/month |
| Tracking | none detailed | GA4-ready hooks + conversion event spec (§10.4) |

**Keep from v2 (do not regress):** the honest status model (no fake dates), self-contained single-file philosophy, keyword-qualified titles verbatim.

## 3. Architecture & URL plan (static site — no CMS)
- Index stays at **`/blog.html`** (already footer-referenced; sitemap entry exists).
- Articles live in **`/blog/<slug>.html`** — one file per post, each self-contained (inline CSS/JS, base64 logo), following the destination-page build contract.
- Slugs: lowercase, hyphenated, keyword-first, ≤60 chars (`turkey-student-visa-documents-pakistan`).
- **Sitemap.xml** gains one `<url>` per article on publish; `robots.txt` unchanged (clean).
- Canonical on every article; RSS/feed: **out of scope** (static, low cadence).
- No comments, no newsletter capture, no login — surface area deliberately minimal (§26 data discipline).

## 4. Design system (binding)
Everything per **Brand Kit v1.0 §3–§7**; deltas/callouts for the blog specifically:
- Blog index hero: navy band, H1 "The Path Plaza Blog", one-line Roman-Urdu accent: *"Saaf answers, sahi maloomat — har article verified."*
- Article type comfort: body 17px/1.7, measure ~70ch, Georgia pull-quote style for the honesty lines.
- Article **header micro-band**: category chip (destination accent colour) · reading time · `Updated [Month Year]` — real dates only; the "Publishing with site launch" pill pattern from v2 dies on first publish and must not be reused with invented dates.
- There is **no `.site-shell`** anymore: all chrome = brand-kit header/footer components per §6 of the kit (shared snippets the developer copies across files).
- Category colour mapping = destination accent tokens (`--uk`, `--ie`, `--my`, `--tr`); non-destination categories: **Process & Visa Files** → blue · **Parents & Family** → teal · **Money & Scholarships** → gold.
- Motion: `.rv` reveals on cards/timeline graphics only; static prose; reduced-motion + no-JS + print rules all apply.

## 5. Blog index page (upgrade spec — `blog.html`)
1. Head: title `Study Abroad Blog — UK, Turkey, Ireland, Malaysia | Path Plaza` (keep), meta description (keep), canonical, OG/Twitter, `Blog` JSON-LD (update `url` to `https://pathplaza.com/blog.html`, add `sameAs`).
2. Hero + **featured article slot** (first live post, later editorial pick).
3. **Filter bar:** All · UK · Ireland · Malaysia · Turkey · Process & Visa Files · Money & Scholarships · Parents & Family — vanilla JS filter, chips show post counts, all cards visible if JS off (v2 behaviour preserved).
4. **Card anatomy:** category chip (accent) · H2 title (links to article) · 2-line excerpt · date + reading time · destination flag emoji (index only — emoji allowed on web, never in PDFs/docs) · "Read →".
5. Never > 2 cards without dates once publishing starts; placeholders simply removed until written (no ghost inventory).
6. Mid-index CTA band after row 2: "Confused where you stand? Free profile check →".
7. Pagination: not needed until 18+ posts; then vanilla JS "load more" (progressive).

## 6. Article page template (binding — one canonical file every post clones)
Sections in order:
1. **Head:** title pattern `<Primary keyword phrase> | Path Plaza Blog`; meta ≤155 chars; canonical; OG `type=article` (+ published/modified times); **BlogPosting JSON-LD**: headline, dates, `author` + `reviewedBy` (see byline), `publisher` Organization w/ logo, `mainEntityOfPage`, `about`, optional FAQPage block when the post ends with FAQs.
2. **Breadcrumb** (visible + schema): Home › Blog › <Category> › <Post>.
3. **Article hero:** category chip · H1 · 2-line honest summary (from SEO guide §6.3) · byline + Updated badge.
4. **Key-facts box** (bordered gold, icon): 3–6 bullets of the dated figures, each with *(indicative / verified-Aug-2026)* labels.
5. **Body H2s** with a table wherever numbers appear; TOC (anchor list) when >4 H2s.
6. **"What can change" caveat box** (teal) — mandatory: fee bands, deadlines and rules shown can shift; verified at counselling within 30 days.
7. **Mid-article CTA card** (once, after ~60% scroll content): WhatsApp prefill matching the post's destination.
8. **Sources block** (bulleted, `rel="noopener"`): minimum **2 official authority links** (gov.uk, irishimmigration.ie, educationinireland.com, educationmalaysia.gov.my, turkiyeburslari.gov.tr, HEC, university pages).
9. **Byline block (verbatim):** *"Path Plaza Counselling Team · Reviewed by Aneela Usman, Path Plaza (SMC) Pvt Ltd, Lahore."* + office address line (E-E-A-T per SEO §6.4).
10. **End CTA card:** "Find out where you stand — free" → `/initial-profile-review.html` + WhatsApp deep link + email plain.
11. **Related posts** (3 cards, same category first) + prev/next links.
12. Standard 5-column legal footer. No sidebar. No ad slots. No pop-ups.

## 7. Compliance & editorial guardrails (hard — apply to every post)
- No outcome/probability claims; never "approval chances" — write "factors that strengthen a file".
- Every figure dated + labelled; official-source verified or flagged *(indicative — re-verify ≤30 days)*.
- **Never publish the Roadmap fee** or any service price. Free profile check is the only monetised-path mention, plus "fixed written fee quoted in consultation" phrasing.
- Contacts per §36.7: PK WhatsApp +92 315 5009620 + info@pathplaza.com only. Sweep for `+44` before deploy.
- No "partner university" phrasing anywhere; if channels are referenced, use the approved channel statement **verbatim** (Brand Kit §5).
- Roman-Urdu versions: one per cluster's top post; they are **separate slugs** (`<slug>-roman-urdu`), cross-linked both ways, same compliance bar, natural code-switched prose (not translation-bot output).
- Workflow: Pathfinder drafts (copy deck, §9) → management review (Aneela Usman) → PP-WEBDEV ships → real date set → sitemap updated → compliance grep logged.
- Corrections policy: update in place + bump the `Updated` date; never silently edit figures.

## 8. Launch content plan

### Phase A — this sprint (index upgrade + 3 pilot posts)
Chosen for synergy with the new destination pages + the Jan–Feb Türkiye Burslari window:

| # | Slug | Title (working) | Primary keyword | Cluster | Notes |
|---|---|---|---|---|---|
| A1 | `/blog/turkey-student-visa-documents-pakistan.html` | Turkey Student Visa: A Document Checklist for Pakistani Applicants (2026) | turkey student visa pakistan documents | Turkey | v2 card already exists — assign real date; links study-in-turkey.html; sources: Turkish mission guidance, DGMM e-İkamet |
| A2 | `/blog/malaysia-university-fees-pakistani-students-2026.html` | Malaysia University Fees Explained: What Your Family Will Actually Pay in 2026 | malaysia university fees pakistani students | Malaysia/Money | table-led; RM+PKR, indicative labels; links study-in-malaysia.html |
| A3 | `/blog/pte-vs-ielts-2026-which-test.html` | PTE vs IELTS in 2026: Which Test for UK, Ireland, Malaysia & Turkey? | pte vs ielts 2026 | Process | comparison table; date-verified acceptance notes per destination |

### Phase B — editorial calendar (SEO Guide §6.2, verbatim governing)
| Month | Publish |
|---|---|
| Sep 2026 | UK January-intake deadline guide · PTE vs IELTS (A3 covers) · Malaysia fee explainer (A2 covers) |
| Oct 2026 | How CAS works · Ireland visa file checklist · Turkey admission timeline · GBP review push |
| Nov 2026 | **Visa-file honesty (flagship trust post)** · scholarship types explained · gap-year policy explainer |
| Dec 2026 | Holiday deadlines · pre-departure money/banking · Jan-intake checklist |
| Jan 2027 | Sept-2027 season opener · "UK vs Malaysia honest math" · parent-guide post |

Cadence 3–4 posts/month minimum; remaining 9 v2 cards absorb into this calendar or are retired on management call.

## 9. Copy-deck format (what PP-WEBDEV receives per article)
Pathfinder delivers a single `.md` per post with this front matter, then body in markdown:
```
---
slug: turkey-student-visa-documents-pakistan
title: <H1 + meta title variant>
description: <≤155 chars>
category: Turkey            # one of the 7 chips
primary_keyword: ...
updated: 2026-08-…          # set at publish
reading_time: …             # computed at build
dest_prefill: Turkey        # WhatsApp prefill key
sources: [url, url, …]
related: [slug, slug, slug]
---
```
Build rule: body → the §6 template verbatim; no editorial improvisation at build time.

## 10. Technical & ops requirements
1. **Performance:** each article ≤350KB all-in, LCP <2.5s (360px, 3G throttle); inline SVG/data-URI images only.
2. **Responsive:** kit §6 matrix; TOC collapses into a `<details>` under the hero ≤768px.
3. **Accessibility:** AA contrast, keyboard-visible focus, skip-link, article wrapped in `<article>` with proper heading order.
4. **Analytics hooks (fills the 16-Aug audit gap):** shared inline GA4 snippet pattern with `dataLayer` events — `article_view` (slug, category), `cta_profile_click`, `cta_whatsapp_click` (location: article_mid | article_end). If GA4 ID not yet supplied, ship with a single clearly-commented placeholder block, events firing only when configured.
5. **Sitemap:** each article added at publish with real `<lastmod>`; resubmit in Search Console at Phase A completion.
6. **QA per deploy:** `+44`/`7577`/banned-phrase grep; schema validator pass (BlogPosting + BreadcrumbList); 360/768/1440 device pass; print pass; link check (all internal targets resolve; sources are 200s on publish day).

## 11. Acceptance checklist
- [ ] `blog.html` re-skinned to v4.0 shell; v2 honest-status model preserved (no fake dates); filter works JS-on and degrades JS-off
- [ ] 3 Phase-A articles built from copy decks, template §6 exact, all guardrails §7 pass
- [ ] Index cards A1–A3 carry real dates + hrefs; remaining v2 cards repositioned per §8/Phase B
- [ ] Every article: 2+ official sources, key-facts + caveat boxes, both CTAs, byline verbatim
- [ ] Schema/sitemap/canonical QA per §10.6; compliance grep logged clean
- [ ] Change-log entry appended to master persona on merge (management instruction = this brief)

---
*Authority note: this brief operationalises SEO Guide Part 6 and Brand Kit v1.0; where anything here conflicts with Pathfinder v4.0, the persona's newest section prevails.*
