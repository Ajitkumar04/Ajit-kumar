import pandas as pd 
data={'Student_ID':[101,102,103,104,105,106,107,108,109,110],
      'Name':['Alice','Bob','Charlie','Diana','Ethan','Fiona','Geroge','hannah','lvan','julia'],
      'Age':[20,21,19,22,20,21,23,19,22,20],
      'Marks':[88,75,92,65,78,85,70,95,60,80],
      'grade':["A",'B','A','C','B','A','B','A','C','B']

}
df=pd.DataFrame(data)
df.to_csv('student.csv',index=False)
print('==================================-')
dp=pd.read_csv('student.csv')
Head=dp.head(3)
print(Head)
print('====================================')
Dicscrip=dp.describe()
print(Dicscrip)
print('====================================') 
Shap=dp.shape
print(Shap)
print('=====================================')
Info=dp.info()
print(Info)
print('=====================================')