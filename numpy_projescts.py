import numpy as np

data = np.array([[22.5, 19.0, 31.2, 28.7, 25.1],
                 [17.3, 22.8, 30.5, 26.4, 21.9],
                 [33.1, 29.6, 18.4, 24.0, 27.8],
                 [20.2, 23.5, 31.9, 28.1, 22.6]])
''' ======================================================================='''
'''Task 1.'''
print("=============================================")
shap=np.shape(data)
print("shap=",shap)
tem=np.mean(data,axis=1)
print(tem)

print("===============================================")
''' task-2'''
boolen_id=data[data>28.0]
print(boolen_id)
print("===============================================")

''' task-3'''
normalized=(data - data.min())/(data.max() - data.min())

print(np.round(normalized,2))
 