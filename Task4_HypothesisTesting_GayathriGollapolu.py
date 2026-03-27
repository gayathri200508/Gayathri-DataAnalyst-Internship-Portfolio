import pandas as pd
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("cleaned_sales_data.csv")

print("TASK 4 — HYPOTHESIS TESTING")

total_revenue = df["Total_Amount"].sum()
avg_order = df["Total_Amount"].mean()
avg_rating = df["Customer_Rating"].mean()
top_category = df.groupby("Category")["Total_Amount"].sum().idxmax()
top_city = df["City"].value_counts().idxmax()
top_payment = df["Payment_Method"].value_counts().idxmax()
return_rate = (df["Order_Status"] == "Returned").sum() / len(df) * 100

print("Total Revenue:", total_revenue)
print("Avg Order Value:", avg_order)
print("Avg Rating:", avg_rating)
print("Top Category:", top_category)
print("Top City:", top_city)
print("Top Payment:", top_payment)
print("Return Rate:", return_rate)

print("\nHypothesis:")
print("Accessories revenue per order > Other categories")

accessories = df[df["Category"] == "Accessories"]["Total_Amount"].dropna()
others = df[df["Category"] != "Accessories"]["Total_Amount"].dropna()

print("\nStats:")
print("Accessories Mean:", accessories.mean())
print("Others Mean:", others.mean())

lev_stat, lev_p = stats.levene(accessories, others)
equal_var = lev_p > 0.05

t_stat, p_two = stats.ttest_ind(accessories, others, equal_var=equal_var)
p_one = p_two / 2

diff_mean = accessories.mean() - others.mean()
se = np.sqrt(accessories.var()/len(accessories) + others.var()/len(others))
df_dof = len(accessories) + len(others) - 2
t_crit = stats.t.ppf(0.975, df=df_dof)

ci_low = diff_mean - t_crit * se
ci_high = diff_mean + t_crit * se

pooled_std = np.sqrt(((len(accessories)-1)*accessories.std()**2 +
                      (len(others)-1)*others.std()**2) / df_dof)

cohens_d = diff_mean / pooled_std

print("\nResults:")
print("T value:", t_stat)
print("P value:", p_one)
print("CI:", ci_low, ci_high)
print("Effect size:", cohens_d)

if p_one < 0.05 and t_stat > 0:
    print("\nDecision: Reject H0")
    print("Accessories give higher revenue")
else:
    print("\nDecision: Cannot reject H0")
    print("No strong difference")

cat_rev = df.groupby("Category")["Total_Amount"].agg(["sum","mean","count"])
cat_rev.columns = ["Total","Avg","Orders"]
cat_rev["Share"] = (cat_rev["Total"] / cat_rev["Total"].sum() * 100).round(1)
cat_rev = cat_rev.sort_values("Total", ascending=False)

print("\nCategory Revenue:")
print(cat_rev)

city_rev = df.groupby("City")["Total_Amount"].sum().sort_values(ascending=False).head(5)

print("\nTop Cities:")
for city, rev in city_rev.items():
    print(city, rev)

pay_dist = df["Payment_Method"].value_counts()

print("\nPayment Methods:")
for pm, cnt in pay_dist.items():
    print(pm, cnt)

status_dist = df["Order_Status"].value_counts()

print("\nOrder Status:")
for st, cnt in status_dist.items():
    print(st, cnt)

print("\nTask 4 completed")