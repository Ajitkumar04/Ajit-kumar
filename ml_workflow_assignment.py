import pandas as pd
import numpy as np
df=pd.read_csv("c:\\Users\\a\\Downloads\\synthetic_repeat_purchase_data (1).csv")

print(df.corr())


y=df["repeat_purchase_flag"]
print("=============================================================Task 01====================================================================")

"""
Feacher:- discount_used_on_repeat_orde highly  corrration bewtwin repeat_purchase_flag traget
 raltion accoundtion disocunt_used_on_repeat_order high chance data leake:
"""
X=df.drop(["customer_id","repeat_purchase_flag"],axis=1)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.25,random_state=42)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train_scaled,y_train)
y_test_pred=model.predict(X_test_scaled)

from sklearn.metrics import r2_score,accuracy_score
r2=r2_score(y_test_pred,y_test)
print(r2)


train_acc=model.score(x_train_scaled,y_train)
test_acc=model.score(X_test_scaled,y_test)
print("train:",{train_acc})
print("test:",{test_acc})

print("=========================================Task 02================================================")
"Befor using complex models we must complete data cleaning EAD proper "
"train-testsplit,and leakage check to ensure reliable and unbiased model performance"