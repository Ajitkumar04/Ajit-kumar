import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

np.random.seed(42)

n = 200

data = {
    "order_id": range(1001, 1001 + n),
    "city": np.random.choice(["Mumbai", "Delhi", "Bangalore", "Chennai"], size=n),
    "category": np.random.choice(["Electronics", "Clothing", "Groceries", "Furniture"], size=n),
    "order_value": np.random.randint(200, 5000, size=n).astype(float),
    "delivery_days": np.random.randint(1, 15, size=n).astype(float),
    "rating": np.random.choice([1, 2, 3, 4, 5, None], size=n)
}

missing_indices_order = np.random.choice(n, size=15, replace=False)
missing_indices_delivery = np.random.choice(n, size=10, replace=False)
data["order_value"][missing_indices_order] = np.nan
data["delivery_days"][missing_indices_delivery] = np.nan

data["order_value"][5] = 95000
data["order_value"][88] = 87000

df = pd.DataFrame(data)
print(df.shape)
df.head()
print("=============================================Taks 1- Inspect & Handle Missing values==================================")

print(df.shape)
print(df.info())
print(df.isnull().sum())
pr_null=df.isnull().sum()/len(df)*100
print(pr_null.round(2))

print("================================taks 2 -summaize & visualize===================")
discib=df.describe()
print(discib)
fig=sns.histplot(df,x="order_value")
plt.show()

box=sns.boxplot(df,x="delivery_days")
plt.show()

print("======================================Taks 3 correlation analsis===============")
cr=df.corr(numeric_only=True)
print(cr)
sns.heatmap(cr)
plt.show()

sns.heatmap(df[["order_value","delivery_days"]].corr(),annot=True)
plt.show()