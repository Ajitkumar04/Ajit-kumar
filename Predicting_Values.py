import pandas as pd
import numpy as np

data = {
    "feature_1": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    "feature_2": [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0],
    "scores":    [40, 45, 55, 75, 105, 120, 125, 145, 175, 205]
}
df = pd.DataFrame(data)
y=df["scores"]
X=df.drop("scores",axis=1)
print(X,y)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_tes=train_test_split(X,y,test_size=0.20,random_state=42)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train_scaled,y_train)
y_train_pried=model.predict(X_test_scaled)
from sklearn.