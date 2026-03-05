# Mapping Grades Across Universities

## Why Is Grade Conversion Hard?

## Why Grade Conversion Is Hard

Universities use **different grading scales**

- 🇮🇹 **Italy** → 18–30 (+ *lode*)
- 🇦🇺 **Australia** → 0–100 with class bands (*Credit, Distinction, High Distinction*)
- 🇺🇸 **USA** → Letters (A–F) and GPA
- 🇪🇺 **Europe** → ECTS grades (A–F, percentile-based)

## Why Grade Conversion Is Hard

Numeric values do **not carry the same meaning**

- 🇩🇪 **Germany**  
  - **1.0 = Excellent (best possible grade)**  
  - 5.0 = Fail

- 🇫🇷 / 🇺🇸 / 🇦🇺
  - **1 or 0 = Lowest grade**,
  - higher numbers = better performance

## Why Grade Conversion Is Hard

What matters is **relative performance**, not raw score

The academic meaning of a grade depends on **how a student performs relative to peers**, not on the absolute number.

Example:
- Student A: **75/100**, top **10%** of cohort → *excellent performance*
- Student B: **85/100**, median of cohort → *average performance*

👉 Even though **85 > 75**, **75 represents stronger academic achievement** in context

## The Core Question

> **How do we compare grades fairly across systems with different distributions?**

Answer:

* by comparing **where a student ranks**
* not just **what number they scored**

## Numeric Grades vs Percentiles

* A numeric grade is **absolute**
* A percentile is **relative**
* Two identical numbers can correspond to **very different percentiles**

Example:

* 75/100 may be:

  * top 10% in one system
  * average in another

## What ECTS Is Based On

The ECTS grading scale is explicitly **percentile-based**.

It compares students **within the same cohort**, not across institutions.

## Official ECTS Percentile Definition

| ECTS Grade | Percentile Rank          |
| ---------- | ------------------------ |
| **A**      | Top **10%**              |
| **B**      | Next **25%**             |
| **C**      | Next **30%**             |
| **D**      | Next **25%**             |
| **E**      | Bottom **10%** (passing) |
| **F**      | Fail                     |

📘 European Commission User’s Guide

## Why Percentiles Matter

* Remove bias from:

  * grade inflation
  * grade deflation
* Normalize across:

  * cultures
  * assessment styles
  * difficulty levels

✔ Fair
✔ Transparent
✔ Reproducible

## Mapping Foreign Grades → Percentiles

Step 1:

* Identify **official grade bands** or classifications

Step 2:

* Associate each band with an **approximate percentile range**

Step 3:

* Assign corresponding **ECTS letter**

## Example: Australia → Percentiles → ECTS

| Australia | Classification   | Approx. Percentile | ECTS  |
| --------- | ---------------- | ------------------ | ----- |
| 85–100    | High Distinction | Top ~10%           | A     |
| 75–84     | Distinction      | 75–90%             | B     |
| 65–74     | Credit           | 45–75%             | C     |
| 50–64     | Pass             | 10–45%             | D / E |
| <50       | Fail             | <10%               | F     |

📌 Percentiles derived from national academic practice

## Why This Mapping Is Reasonable

* Australian universities:

  * rarely award >85
  * strongly concentrate grades in middle bands
* Numeric ranges reflect **performance tiers**, not equal intervals

## ECTS → Italian Grades (UNIBO Example)

| ECTS | Percentile | Italian Grade |
| ---- | ---------- | ------------- |
| A    | ≥ 90th     | 30–30L        |
| B    | 65–90th    | 29–30         |
| C    | 35–65th    | 26–28         |
| D    | 10–35th    | 21–25         |
| E    | < 10th     | 18–20         |

## Two-Step Conversion Model

1️⃣ Foreign grade → **Percentile band**
2️⃣ Percentile band → **ECTS letter**
3️⃣ ECTS letter → **Italian grade**

✔ Preserves ranking
✔ Preserves meaning
✔ Avoids distortions

## Optional: Within-Band Interpolation

If numeric data exists:

* interpolate **within the same percentile band**
* never cross ECTS thresholds

⚠️ Refinement, not replacement

## Why Linear Scaling Fails

Linear scaling assumes:

* uniform distributions
* equal difficulty
* equal grading culture

All false in international contexts ❌

## Transparency & Documentation

Every conversion should document:

* grading system used
* percentile assumptions
* ECTS reference
* Italian mapping table

## Key Takeaways

* 🎯 Percentiles define equivalence
* 🎓 ECTS is a percentile system
* 🇪🇺 Italian conversion relies on ECTS
* ❌ Raw numbers are misleading

## Final Thought

> **Grades measure rank, not points.
> Percentiles preserve rank.**

If you want, I can:

* add **formal citations (EU Guide, UNIBO docs)**
* compress this into **10 slides**
* tailor percentiles for **USA / Korea / UK**
* add a **flowchart slide**

Just tell me.
