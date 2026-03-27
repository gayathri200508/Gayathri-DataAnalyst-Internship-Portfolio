import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(10)
random.seed(10)
n = 100

products = ['Saree','Kurti','Jeans','T-Shirt','Lehenga','Shoes','Handbag','Jewellery']
categories = {'Saree':'Traditional Wear','Kurti':'Traditional Wear','Lehenga':'Traditional Wear','Jeans':'Western Wear','T-Shirt':'Western Wear','Shoes':'Footwear','Handbag':'Accessories','Jewellery':'Accessories'}
cities = ['Hyderabad','Chennai','Bangalore','Mumbai','Delhi','Pune','Kolkata','Jaipur']
payments = ['UPI','Credit Card','Debit Card','Cash','Net Banking']
statuses = ['Delivered','Returned','Pending','Cancelled']

order_ids = [f'ORD{str(i).zfill(3)}' for i in range(1,n+1)]
customer_ids = [f'CUST{str(i).zfill(3)}' for i in np.random.randint(1,51,n)]
product_list = [random.choice(products) for _ in range(n)]
ages = np.random.randint(18,55,n)
genders_list = [random.choice(['Female','Male']) for _ in range(n)]
cities_list = [random.choice(cities) for _ in range(n)]
quantities = np.random.randint(1,5,n)
prices = np.round(np.random.uniform(200,5000,n),2)
discounts = np.round(np.random.uniform(0,0.4,n),2)
pay_list = [random.choice(payments) for _ in range(n)]
status_list = [random.choice(statuses) for _ in range(n)]
ratings = np.random.randint(1,6,n)
start_date = datetime(2024,1,1)
dates = [(start_date+timedelta(days=int(x))).strftime('%Y-%m-%d') for x in np.random.randint(0,365,n)]
dobs = [(datetime(2024,1,1)-timedelta(days=int(a)*365)).strftime('%Y-%m-%d') for a in ages]

df = pd.DataFrame({
    'Order_ID':order_ids,'Customer_ID':customer_ids,
    'Customer_Name':[f'Customer_{i}' for i in range(1,n+1)],
    'Age':ages,'Gender':genders_list,'City':cities_list,
    'Product_Name':product_list,'Category':[categories[p] for p in product_list],
    'Quantity':quantities,'Unit_Price':prices,'Discount':discounts,
    'Order_Date':dates,'Payment_Method':pay_list,'Order_Status':status_list,
    'Customer_Rating':ratings,'Date_of_Birth':dobs})

df['Total_Amount'] = np.round(df['Quantity']*df['Unit_Price']*(1-df['Discount']),2)

for col,count in [('Age',6),('City',5),('Customer_Rating',8),('Payment_Method',4)]:
    idx = df.sample(count,random_state=1).index
    df.loc[idx,col] = np.nan

dupes = df.sample(5,random_state=2)
df = pd.concat([df,dupes],ignore_index=True)

idx3 = df.sample(10,random_state=3).index
df.loc[idx3,'Gender'] = df.loc[idx3,'Gender'].str.lower()
idx4 = df.sample(5,random_state=4).index
df.loc[idx4,'Order_Status'] = df.loc[idx4,'Order_Status'].str.upper()

idx5 = df.sample(3,random_state=5).index
df.loc[idx5,'Unit_Price'] = [-100,0,99999]

idx6 = df.sample(10,random_state=6).index
df.loc[idx6,'Order_Date'] = pd.to_datetime(df.loc[idx6,'Order_Date']).dt.strftime('%d/%m/%Y')

df.to_csv('raw_sales_data.csv',index=False)
print("✅ raw_sales_data.csv created!")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

