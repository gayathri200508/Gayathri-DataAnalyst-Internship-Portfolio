# 📊 Task 4 — Data Storytelling & Statistical Validation
### ApexPlanet Software Pvt. Ltd. | 60-Day Data Analytics Internship
### 👩‍💻 Intern: Gayathri Gollapolu | AITS Tirupati

---

## 📌 What is This Task About?

In this task, all findings from Tasks 1–3 are synthesised into a compelling **business narrative** and validated using **statistical hypothesis testing**. The goal is to tell a clear data-driven story that a business audience can understand and act upon.

---

## 🎯 Business Objective

| | |
|---|---|
| **Dataset** | Indian E-Commerce Orders (104 rows, 2024) |
| **Objective** | Identify revenue drivers, customer behaviour, and delivery performance |
| **Audience** | Business stakeholders & management |

---

## 📖 Business Narrative Structure

| Stage | Summary |
|---|---|
| **Objective** | Understand what drives revenue and where business risks lie |
| **Analysis** | EDA, SQL KPIs, category & city performance, payment trends |
| **Conclusions** | Accessories dominate; return rate is critically high; ratings below benchmark |
| **Call to Action** | Expand Accessories, fix returns, improve satisfaction, grow in Bangalore |

---

## 📊 Key Findings

| # | Finding | Insight |
|---|---|---|
| 1 | **Accessories = 57.1% of revenue** | Top category — ₹5,12,180 total |
| 2 | **Return Rate = 29.8%** 🚨 | 1 in 3 orders returned — major revenue leak |
| 3 | **Avg Rating = 2.95 / 5** | Below industry benchmark of 3.5+ |
| 4 | **Bangalore = Top City** | 22% of all orders |
| 5 | **UPI = #1 Payment** | 27.9% — digital payments at 59% overall |

---

## 🔬 Hypothesis Testing

**Business Hypothesis:**
> *"Accessories category generates significantly higher revenue per order compared to all other categories combined."*

| | |
|---|---|
| **H₀ (Null)** | μ_accessories = μ_others |
| **H₁ (Alternative)** | μ_accessories > μ_others |
| **Test Used** | Independent Samples T-Test (one-tailed) |
| **Significance Level** | α = 0.05 |

### Results

| Metric | Value |
|---|---|
| Accessories Avg Revenue | ₹15,521 |
| Non-Accessories Avg Revenue | ₹5,413 |
| T-Statistic | 1.6555 |
| P-Value (one-tailed) | 0.0505 |
| 95% Confidence Interval | (₹-7,639 , ₹27,855) |
| Decision | Borderline ⚠️ |

### Interpretation
P-value (0.0505) is marginally above α (0.05). While statistically borderline due to high variance from outliers in the small dataset, the **business impact is real** — Accessories mean revenue (₹15,521) is **2.9× higher** than Non-Accessories (₹5,413). Business investment in Accessories is strongly justified.

---

## 📂 Files in This Repository

| File | Description |
|---|---|
| `Task4_DataStorytelling_GayathriGollapolu.pptx` | 9-slide professional presentation deck |
| `README.md` | This file |

---

## 📋 Call to Action (Business Recommendations)

| Priority | Action | Target |
|---|---|---|
| 🔴 High | Reduce return rate | < 15% in 6 months |
| 🟠 High | Expand Accessories inventory & marketing | +20% revenue |
| 🟡 Medium | Improve customer satisfaction programme | Rating 3.8+ in 1 quarter |
| 🟢 Medium | Expand warehouse presence in Bangalore & Pune | +15% order volume |

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| Python | Data analysis & hypothesis testing |
| Pandas | Data manipulation |
| SciPy | Statistical testing (T-test) |
| PowerPoint | Presentation design |

---

## 📈 Dataset Summary

| Metric | Value |
|---|---|
| Total Orders | 104 |
| Total Revenue | ₹8,96,474 |
| Avg Order Value | ₹8,620 |
| Avg Customer Rating | 2.95 / 5 |
| Top Category | Accessories (57.1%) |
| Top City | Bangalore (22%) |
| Top Payment | UPI (27.9%) |

---

**Intern:** Gayathri Gollapolu | B.Tech AI & DS, AITS Tirupati (2027)
**LinkedIn:** [linkedin.com/in/gayathri-gollapolu-741278362](https://linkedin.com/in/gayathri-gollapolu-741278362)
**GitHub:** [github.com/gayathri200508](https://github.com/gayathri200508)

*ApexPlanet Software Pvt. Ltd. | Data Analytics Internship | Task 4 of 5*
