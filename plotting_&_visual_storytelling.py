import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [12000, 15000, 13500, 17000, 16000, 19000,
         18500, 21000, 20000, 22500, 24000, 26000]

subjects = ['Math', 'Science', 'English', 'History', 'Art']
scores   = [78, 85, 72, 90, 65]

study_hours = np.random.uniform(1, 10, 100)
exam_scores = study_hours * 8 + np.random.normal(0, 5, 100)

product_sales = np.random.normal(loc=50, scale=10, size=200)

print("=============================tasks 01===================================")

plt.plot(months,sales,color="orange",linewidth=2,marker="o")
plt.title('Monthly & Sales')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()
print("============================Tasks-02====================================")
from re import sub
plt.bar(subjects,scores,color="blue")
plt.title("subjects & scores")
plt.xlabel("subjects")
plt.ylabel("scores")
plt.show()
print("============================tasks-03======================================")
sns.scatterplot(x=study_hours,y=exam_scores,alpha=1)
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.show()
print("============================tasks-04========================================")
sns.boxplot(product_sales)
plt.title("Product Sales Distribution")
plt.xlabel("Sales")
plt.show()