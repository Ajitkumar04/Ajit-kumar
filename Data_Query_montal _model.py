import pandas as pd
students_data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Alice', 'Bob', None, 'David', 'Emma', 'Frank', 'Grace'],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', None, 'emma@email.com', 'frank@email.com', 'grace@email.com'],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', None, 'Chennai', 'Delhi']
}

enrollments_data = {
    'student_id': [101, 102, 103, 105, 108, 109],
    'course_name': ['Python', 'Data Science', 'Python', 'Machine Learning', 'AI', 'Python'],
    'enrollment_date': ['2024-01-15', '2024-01-20', '2024-02-01', '2024-02-10', '2024-02-15', '2024-03-01']
}

scores_data = {
    'student_id': [101, 102, 104, 105, 106],
    'exam_score': [85, 92, 78, 88, 95]
}

print("=====================Task:1=================================")
df=pd.DataFrame(students_data)
dp=pd.DataFrame(enrollments_data)
ds=pd.DataFrame(scores_data)
#for the students dataFreme:

data=(df.isnull().sum()/df.shape[0]*100,)
print(data)
df['city']=df['city'].fillna('Unknown')
df.dropna(subset=['name'],inplace=True)
print(df)
print('============================Task-2====================================================')
join_merge=pd.merge(df,dp,on='student_id',how='inner')
print(join_merge)
print('        3 student apper in the result')
print('dfstudent_id == dp student_id match and =101,102,105inner only use  mach id')
print("************************************************")
Left_merge=pd.merge(df,dp,on="student_id",how='left')
print(Left_merge)
print("        6 rows in the result")
print("        3 student are NaN value")
print("*************************************************")
right_join=pd.merge(df,dp,on="student_id",how="right")
print(right_join)
print("         6 rows in the result")
print("           3 student NaN name")
print('**************************************************')
full_join=pd.merge(df,dp,on="student_id",how="outer",indicator=True)
print(full_join)
print('      9 rows in result')
print("  not only one student ")
print("***************************************")
print("=========================Task-3=======================================")
lookup=dict(zip(ds['student_id'],ds['exam_score']))
df['exam_score']=df['student_id'].map(lookup)
print(df)
print("---------------------------------------")
# print("  performance comparison")
# map( is more effcinent than merge when adding a singal colums beacause 
# it performs a direct key value lookup instead of joining enter datafreme.)
print('simple outmation======================')
def snart_merge(left,right,key,join_type="left"):
  result=pd.merge(left,right,on=key,how=join_type )
  print(f"===MERGE REPORT({join_type.upper()}JOIN on '{key}')===")
  print(f"Left total Rows:{len(left)}")
  print(f"RIGHT table rows:{len(right)}")
  print(f"Result rows:{len(result)}")
  nulls=result.isnull().sum().sum()
  if nulls>0:
    print(f'NaN values added:{nulls}(unmatch rows)')
  else:
    print(f"NaN values added:0 (all rows match)")
  print()
  return result

inner_result=snart_merge(df,dp,key="student_id",join_type="left")
print(inner_result)