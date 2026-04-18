import pandas as pd
import numpy as np 

data = {
    "feature_1": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    "feature_2": [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0],
    "target":    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)
print("=========================================task 02==============================================================")
y=df["target"]
X=df.drop("target",axis=1)
print(X,y)
print("=========================================Task 03===============================================================")
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_tes=train_test_split(X,y,test_size=0.20,random_state=42)
print("=========================================Task 04==========================================================================")
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
print("=========================================Task 05==================================================================")
print(X_train_scaled,X_test_scaled)
print("=========================================Task 06=====================================================================")
"first X,y vareables store  feuture  and target"
"than data spliting data create train data and test data"
"use stander scaler to normalazed data"
