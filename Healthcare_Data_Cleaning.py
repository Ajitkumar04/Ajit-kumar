import pandas as pd
import numpy as np

data = {
    'patient_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 101, 107, 118, 119, 120],
    'age': ['25', '34', None, '45', '29', None, '38', '52', '27', '41',
            '33', 'unknown', '48', '26', '35', '25', '38', '31', None, '44'],
    'weight': ['70', '65', '80', None, '75', None, '68', '90', '72', '85',
               '78', None, '82', '69', 'N/A', '70', '68', '74', None, '88'],
    'blood_pressure': [120, 130, None, 140, 125, None, 135, None, 118, 145,
                      128, None, 138, 122, None, 120, 135, 126, None, 142],
    'medication': ['Aspirin', 'Metformin', 'Lisinopril', None, 'Aspirin',
                   'Metformin', 'Lisinopril', 'Aspirin', None, 'Metformin',
                   'Lisinopril', 'Aspirin', None, 'Metformin', 'Aspirin',
                   'Aspirin', 'Lisinopril', 'Metformin', 'Aspirin', None],
    'insurance_provider': ['Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None,
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', 'Blue Cross',
                          'Aetna', None, 'UnitedHealth', 'Blue Cross', 'Aetna',
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None]
}

df = pd.DataFrame(data)
print("=====================Task 1:==============================")
info=(df.info())
print((df.isnull().sum()))
print(df.isnull().sum()/len(df)*100)
print(df.duplicated().sum())
print("========================Task 2:============================")
df['age']=pd.to_numeric(df['age'],errors='coerce')
df['weight']=pd.to_numeric(df['weight'],errors='coerce')
print((df.isnull().sum()))
df['insurance_provider']=df['insurance_provider'].astype("category")
print(df.dtypes)

print('=======================Task 3:===========================')
df['age']=df['age'].fillna(df['age'].median())
df['weight']=df['weight'].fillna(df['weight'].median())
df['blood_pressure']=df['blood_pressure'].fillna(df['blood_pressure'].median())
df['medication']=df['medication'].fillna(df['medication'].mode()[0])
df["insurance_provider"]=df["insurance_provider"].cat.add_categories('unknown')
df['insurance_provider']=df['insurance_provider'].fillna("unknown")
print(df.isnull().sum())

print("=========================Task 4:=========================")
(df[df.duplicated(keep=False)])
print(df.duplicated(subset=['patient_id']))
print(df.shape)
print(df.drop_duplicates(subset=['patient_id'],keep='first'))
print(df.shape)
print("===========================Task 5:===========================")
df=pd.DataFrame(data)
df_clean=df.copy()
print("*************************BEFORE CLEANING***********************")
report = {}
report['shape_before'] = df_clean.shape
report['missing_before'] = df_clean.isnull().sum()
report['duplicates_before'] = df_clean.duplicated(subset=['patient_id']).sum()
report['dtypes_before'] = df_clean.dtypes
print(report)
print('************************Cleaning**************************')
df_clean['age'] = pd.to_numeric(df_clean['age'], errors='coerce')
df_clean['weight'] = pd.to_numeric(df_clean['weight'], errors='coerce')
df_clean['insurance_provider'] = df_clean['insurance_provider'].astype('category')

df_clean['age'] = df_clean['age'].fillna(df_clean['age'].median())
df_clean['weight'] = df_clean['weight'].fillna(df_clean['weight'].median())
df_clean['blood_pressure'] = df_clean['blood_pressure'].fillna(df_clean['blood_pressure'].median())
df_clean['medication'] = df_clean['medication'].fillna(df_clean['medication'].mode()[0])
df_clean["insurance_provider"]=df_clean["insurance_provider"].cat.add_categories('unknown')
df_clean['insurance_provider'] = df_clean['insurance_provider'].fillna('unknown')
df_clean = df_clean.drop_duplicates(subset=['patient_id'], keep='first')
print(df_clean)
print("****************************verification report***************************")
print(f"Before....{df.shape}=After....{df_clean.shape}")
print(f"\nBefor  =....{df.isnull().sum()}\nAfter =....{df_clean.isnull().sum()}")
print(f"\nBefor=....{df.duplicated(subset=["patient_id"]).sum()}\nAfter=....{df_clean.duplicated(subset=['patient_id']).sum()}")
print(f"Before=....\n{df.dtypes}\nAfter=....\n{df_clean.dtypes}")
print(f"Before=....\n{pd.to_numeric(df['age'], errors='coerce')}\nAfter=....\n{pd.to_numeric(df_clean['age'],errors='coerce')}")
print(f"Before=....\n{pd.to_numeric(df['weight'], errors='coerce')}\nAfter=....\n{pd.to_numeric(df_clean['weight'],errors='coerce')}")
print(f"Before=....\n{pd.to_numeric(df['insurance_provider'], errors='coerce')}\nAfter=....\n{pd.to_numeric(df_clean['insurance_provider'],errors='coerce')}")
print(f"Befor=....{df['age'].fillna(df['age'].median)} \n After=....{df_clean['age'].fillna(df_clean['age'].median())}")
print(f"Befor=....{df['age'].fillna(df['age'].median)}\nAfter=....{df_clean['weight'].fillna(df_clean['weight'].median())}")
print(f"Befor=....{df['blood_pressure'].fillna(df['blood_pressure'].median)}\n After=....{df_clean['blood_pressure'].fillna(df_clean['blood_pressure'].median())}")
print(f"Befor=....{df['medication'].fillna(df['medication'].mode()[0])}\n after=...{df_clean['medication'].fillna(df_clean['medication'].mode()[0])}")
