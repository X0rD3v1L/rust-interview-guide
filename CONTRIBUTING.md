# Contributing to the Rust Interview Guide

Thank you for wanting to contribute! This guide is a community-driven collection of real Rust interview experiences, and every honest submission makes it more valuable for everyone preparing for Rust roles.

---

## What You Can Contribute

* **Interview experiences** — your own real interview experience at any company where Rust was part of the process
* **Corrections** — fix factual errors, broken links, or typos in existing entries
* **Q&A improvements** — add answers to unanswered questions in `README.md`, or improve existing ones with better examples

---

## Guidelines

**Do:**
* Share your own experience — don't fabricate or copy from elsewhere
* Be accurate — describe what was actually asked, even if imperfect
* Be constructive — tips and reflections should help future candidates
* Anonymize interviewers — don't name individual interviewers; company name is fine

**Don't:**
* Bash or defame companies — factual accounts are fine, personal attacks are not
* Include confidential or proprietary problem statements that you were told to keep private
* Share another person's experience without their explicit consent
* Include your own or anyone else's personal contact information

---

## How to Submit an Interview Experience

### 1. Fork the repository

Click **Fork** on the top-right of the repo page, then clone your fork locally:

```bash
git clone https://github.com/<your-username>/rust-interview-guide.git
cd rust-interview-guide
```

### 2. Create your experience file

Each company has its own folder inside `interview-experiences/`. Multiple people can contribute experiences for the same company — they just live as separate files in the same folder.

```bash
# If the company folder already exists:
cp interview-experiences/TEMPLATE.md interview-experiences/<company-slug>/<filename>.md

# If this is the first experience for this company:
mkdir interview-experiences/<company-slug>
cp interview-experiences/TEMPLATE.md interview-experiences/<company-slug>/<filename>.md
```

**Folder name**: `{company-slug}` — all lowercase, words separated by hyphens.

**File name inside the folder**:

| You know... | Format | Example |
|---|---|---|
| Month + year | `{role-slug}-{yyyy}-{mm}.md` | `rust-developer-2025-01.md` |
| Year only | `{role-slug}-{yyyy}.md` | `rust-developer-2025.md` |
| Same role + same date exists | add `-{N}yoe` suffix | `rust-developer-2025-01-3yoe.md` |

Rules:
* All lowercase, words separated by hyphens
* Month is zero-padded (`01`–`12`)
* Use your years of Rust experience as the tiebreaker — two people at the same company, same role, same month will almost always have different YOE

```
interview-experiences/
  google/
    senior-rust-engineer-2025-03.md      ← Mar 2025 (first)
    senior-rust-engineer-2025-03-5yoe.md ← Mar 2025 (second, tiebroken by YOE)
  stripe/
    systems-engineer-2024-11.md
  infosys/
    rust-developer-2025.md               ← month unknown
    rust-developer-2025-01.md            ← Jan 2025, from someone else
```

### 3. Fill in the template

See [The Standard Format](#the-standard-format) below. Every section is required; use `N/A` if something genuinely doesn't apply.

### 4. Open a Pull Request

Push your branch and open a PR against `main`. Use this PR title format:

```
add: Interview experience for {Role} at {Company}
```

---

## The Standard Format

Below is the exact structure every experience file must follow. A blank copy is available at [`interview-experiences/TEMPLATE.md`](interview-experiences/TEMPLATE.md).

---

```markdown
# {Company Name} – {Role Title} – {X} Years Experience

## Overview

* **Company**: {Company Name}
* **Role**: {Role Title}
* **Location**: {City, Country} · {Remote / Hybrid / On-site}
* **Interview Date**: {Month, Year}
* **Experience Level**: {e.g., "2 years in Rust" or "3–5 years overall"}
* **Application Source**: {LinkedIn / Referral / HR Outreach / Naukri / Job Board / etc.}

---

## Interview Process

### Round 1 – {Round Type}

* **Duration**: ~{X} minutes
* **Format**: {Discussion / Live Coding / Take-Home Assignment / MCQ / HR Screening}

**Questions & Topics Discussed**

* ...

**Coding Problems** *(omit section if none)*

* [Problem Title](link) – brief note on what was asked or what made it tricky

---

### Round 2 – {Round Type}

*(repeat the round block for each round)*

---

## Key Topics Covered

*(bullet list of Rust/tech areas that came up across all rounds)*

* ...

---

## Outcome

* **Result**: {Selected / Offer Extended / Rejected / Ghosted / Neutral / Not Communicated}
* **Feedback Received**: {Yes / No / Informal}
* **Reflections**: {1–3 honest sentences about how it went, what surprised you, or what you'd do differently}

---

## Tips for Future Candidates

* ...
```

---

## Accepted Round Types

Use one of these labels for round headings (or a clear variant if none fits):

| Label | When to use |
|---|---|
| `HR Screening` | Initial call to verify profile, CTC, notice period |
| `Technical Interview` | Conceptual discussion, no live code editor |
| `Live Coding` | Coding in a shared editor or HackerRank |
| `Take-Home Assignment` | Offline task submitted before next round |
| `MCQ Test` | Multiple-choice questionnaire |
| `System Design` | Architecture / design discussion |
| `Managerial Round` | Culture, team fit, expectations |
| `HR Round` | Offer, compensation, logistics |

---

## Accepted Result Values

Use exactly one of these for `**Result**`:

* `Selected` — you received and accepted an offer
* `Offer Extended` — offer was made (outcome may be pending)
* `Rejected` — explicitly rejected by the company
* `Ghosted` — no response after the last round or follow-ups
* `Neutral` — feedback was neutral / inconclusive
* `Not Communicated` — no result was shared

---

## PR Checklist

Before submitting your PR, confirm:

* [ ] File is inside a company subfolder with correct naming: `interview-experiences/{company-slug}/{role-slug}-{yyyy}-{mm}.md` (or `{yyyy}` if month unknown)
* [ ] All sections from the template are present (use `N/A` for truly inapplicable ones)
* [ ] Bullet style is `*` throughout (not `-` or `1.`)
* [ ] Round headings use `### Round N – {Type}` format
* [ ] No personal information about interviewers is included
* [ ] Coding problem links are working (LeetCode, HackerRank, etc.)
* [ ] Outcome uses one of the accepted result values

---

## Questions?

Open an issue and label it `question`. We're happy to help.
