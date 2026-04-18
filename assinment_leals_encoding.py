import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'City': ['Mumbai', 'Delhi', 'Chennai', 'Mumbai', 'Delhi'],
    'Size': ['Small', 'Large', 'Medium', 'Large', 'Small'],
    'Age': [25, 45, 32, 60, 28],
    'Fare': [15, 300, 85, 450, 20]
}

df = pd.DataFrame(data)
df.columns=df.columns.str.lower()
print(df.columns)
df["gender"].replace({"Male":1,"Female":0},inplace=True)
df["size"].replace({"Large":2,"Medium":1,"Small":0},inplace=True)
df_dum=pd.get_dummies(df,drop_first=True,dtype=int)
print(df_dum)

plt.scatter(df_dum["age"],df_dum["fare"])
plt.show()