import pandas as pd
import random

random.seed(42)

# Define data parameters
regions = ['North', 'South', 'East', 'West']
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books']
salespersons = ['Alice', 'Bob', 'Carol', 'David', 'Emma', 'Frank']

# Generate 200 sales transactions
data = {
    'transaction_id': range(1001, 1201),
    'region': [random.choice(regions) for _ in range(200)],
    'category': [random.choice(categories) for _ in range(200)],
    'salesperson': [random.choice(salespersons) for _ in range(200)],
    'sales_amount': [round(random.uniform(50, 5000), 2) for _ in range(200)],
    'customer_id': [random.randint(5000, 5100) for _ in range(200)]
}

df = pd.DataFrame(data)
print(df.head(10))
print(f"\nDataset shape: {df.shape}")
print("=========================Task-1===========================================")

region_sales=df.groupby("region")["sales_amount"].sum().reset_index()
# print(f"1)total region by sales:\n{total_sales_amount}")
transation_count=df.groupby("category")["transaction_id"].count().reset_index()
# print(f"2)number of transaction:\n{number_transaction}")
average_sales=df.groupby("salesperson")["sales_amount"].mean().round(0).reset_index()
# print(f"3)average sales amount\n{average_sales}") 
basic_df=pd.concat([region_sales,transation_count,average_sales],axis=1)
basic_df=basic_df.sort_index(ascending=False)

print(basic_df)
print("================================Task-2=====================================")
group=df.groupby(['region', 'category'])['sales_amount'].sum().reset_index().max()
print(group)

seles=df.groupby('salesperson')['sales_amount'].agg(['sum', 'mean', 'count']).reset_index()
selsman=seles.sort_index(ascending=False)
print(selsman)
print("===============================taks-3=======================================")


def sales_range(x):
    return x.max() - x.min()


report=df.groupby('region')['sales_amount'].agg(['sum', 'mean', 'min', 'max', sales_range]).reset_index()
print(report)
final_report=df.groupby('region').agg({
    'sales_amount': ['sum', 'mean'],
    'customer_id': 'count'
}).reset_index()
print(final_report)