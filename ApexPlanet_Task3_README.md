# 🛒 Task 3 — Deep-Dive Analysis & Interactive Dashboard
### ApexPlanet Software Pvt. Ltd. · Gayathri Gollapolu

---

## 📌 Overview
Deep-dive business analysis on the E-Commerce Orders dataset, with a fully interactive BI Dashboard built using Python (Streamlit + Plotly).

---

## 🎯 5 Core KPIs

| # | KPI | Formula | Business Rationale |
|---|-----|---------|-------------------|
| 1 | **Total Revenue** | `Σ(revenue)` | Overall business health indicator |
| 2 | **Average Order Value (AOV)** | `Mean(revenue)` | Benchmarks customer spend per order; guides pricing strategy |
| 3 | **High-Value Conversion Rate** | `(Orders > AOV) / Total Orders × 100` | Measures % of orders exceeding average — high-value customer segment |
| 4 | **UPI Adoption Rate** | `(UPI Orders / Total Orders) × 100` | Tracks digital payment penetration — key for fintech strategy |
| 5 | **Category Revenue Share** | `Category Revenue / Total Revenue × 100` | Identifies top-performing product categories for inventory focus |

---

## 🔍 Deep-Dive: Category Performance Analysis

Key questions answered:
- Which category generates the most revenue?
- Which category has the highest Average Order Value?
- How does unit price correlate with order revenue?
- Which region × category combination performs best?

---

## 📊 Dashboard Features

- ✅ Sidebar filters: Category, Region, Payment Method, Price Range
- ✅ 5 live KPI cards
- ✅ 4 analysis tabs with 12+ interactive charts
- ✅ Region × Category heatmap
- ✅ Auto-generated business insights

---

## 🚀 How to Run

```bash
pip install streamlit plotly pandas numpy
streamlit run apexplanet_dashboard.py
```

> Place `ecommerce_data.csv` in the same folder before running.

---

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data wrangling |
| Plotly | Interactive charts |
| Streamlit | Dashboard UI |

---

## 📈 Key Findings

1. **Electronics** generates the highest total revenue
2. **High-Value Conversion Rate** indicates a strong premium customer segment
3. **Digital payments** dominate — UPI + Cards combined exceed 70%+
4. Region × Category heatmap reveals targeted investment opportunities
5. AOV varies significantly across payment methods — credit card users spend more

---

**Intern:** Gayathri Gollapolu | AITS Tirupati — B.Tech AI & DS  
**LinkedIn:** [linkedin.com/in/gayathri-gollapolu-741278362](https://linkedin.com/in/gayathri-gollapolu-741278362)  
**GitHub:** [github.com/gayathri200508](https://github.com/gayathri200508)
