# 🛍️ Task 1 – Data Immersion & Wrangling
### ApexPlanet Software Pvt. Ltd. | 60-Day Data Analytics Internship
### 👩‍💻 Intern: Gayathri

## 📌 What is This Task About?
In this task I learned how to:
- Load a messy dataset
- Find data quality problems
- Fix all the problems
- Add new useful columns
- Save a clean dataset

## 📂 Files in This Repository

| File | Description |
|---|---|
| `raw_sales_data.csv` | Original messy dataset |
| `task1_data_cleaning.py` | Python script to clean data |
| `cleaned_sales_data.csv` | Final clean dataset |
| `data_dictionary.md` | Explanation of all columns |

## ❌ Problems Found in Raw Data

| # | Problem | Count |
|---|---|---|
| 1 | Missing Values | 23 |
| 2 | Duplicate Rows | 5 |
| 3 | Inconsistent Text | 15 |
| 4 | Mixed Date Formats | 10 |
| 5 | Invalid Prices | 3 |

## ✅ How I Fixed Them

| # | Fix |
|---|---|
| 1 | Filled missing values with median and mode |
| 2 | Removed duplicate rows |
| 3 | Standardized all text to Title Case |
| 4 | Unified all dates to YYYY-MM-DD format |
| 5 | Replaced bad prices with median price |

## 📊 Result

| | Before | After |
|---|---|---|
| Rows | 105 | 104 |
| Columns | 17 | 21 |
| Missing Values | 23 | 0 ✅ |
| Duplicates | 5 | 0 ✅ |

## 🛠️ Tools Used
- Python 3.14
- Pandas
- NumPy

*ApexPlanet Software Pvt. Ltd. | Data Analytics Internship | Task 1 of 5*