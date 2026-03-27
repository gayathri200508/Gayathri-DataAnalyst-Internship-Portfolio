import pandas as pd
import numpy as np

print("=" * 55)
print("   TASK 1 - DATA IMMERSION & WRANGLING")
print("   ApexPlanet Internship - Gayathri")
print("=" * 55)

df = pd.read_csv('raw_sales_data.csv')
print(f"Total Rows    : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")

missing = df.isnull().sum()
for col, val in missing[missing > 0].items():
    print(f"   {col}: {val} missing values")

print(f"Duplicate Rows: {df.duplicated().sum()}")

df_clean = df.copy()
df_clean = df_clean.drop_duplicates()
df_clean['Gender'] = df_clean['Gender'].str.strip().str.title()
df_clean['Order_Status'] = df_clean['Order_Status'].str.strip().str.title()
df_clean['City'] = df_clean['City'].str.strip().str.title()
df_clean['Payment_Method'] = df_clean['Payment_Method'].str.strip()

def fix_date(val):
    for fmt in ('%Y-%m-%d', '%d/%m/%Y'):
        try:
            return pd.to_datetime(val, format=fmt)
        except:
            pass
    return pd.NaT

df_clean['Order_Date'] = df_clean['Order_Date'].apply(fix_date)
df_clean['Date_of_Birth'] = pd.to_datetime(df_clean['Date_of_Birth'], errors='coerce')

median_price = df_clean.loc[df_clean['Unit_Price'] > 0, 'Unit_Price'].median()
bad_price = (df_clean['Unit_Price'] <= 0) | (df_clean['Unit_Price'] > 10000)
df_clean.loc[bad_price, 'Unit_Price'] = median_price

df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].median()).astype(int)
df_clean['City'] = df_clean['City'].fillna(df_clean['City'].mode()[0])
df_clean['Payment_Method'] = df_clean['Payment_Method'].fillna(df_clean['Payment_Method'].mode()[0])
df_clean['Customer_Rating'] = df_clean['Customer_Rating'].fillna(df_clean['Customer_Rating'].median())

def age_group(age):
    if age < 25: return 'Young (18-24)'
    elif age < 35: return 'Adult (25-34)'
    elif age < 50: return 'Middle-Aged (35-49)'
    else: return 'Senior (50+)'

df_clean['Age_Group'] = df_clean['Age'].apply(age_group)
df_clean['Total_Amount'] = np.round(df_clean['Quantity'] * df_clean['Unit_Price'] * (1 - df_clean['Discount']), 2)
df_clean['Revenue_Tier'] = pd.cut(df_clean['Total_Amount'],
    bins=[0, 500, 2000, 5000, float('inf')],
    labels=['Low (<500)', 'Medium (500-2K)', 'High (2K-5K)', 'Premium (5K+)'])
df_clean['Order_Month'] = df_clean['Order_Date'].dt.month_name