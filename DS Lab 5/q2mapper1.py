import fileinput

import pandas as pd
from pandas.core import frame

Cov = pd.read_csv("heart_disease_data.csv")
Frame=pd.DataFrame(Cov.values, columns = ["age", "sex", "cp", "trestbps", "chol", "fbs","restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"])

Frame.style.hide_index()

arr=Frame['trestbps'].to_string(index=False).split('\n')

print(arr)

arr1=[]
for ele in arr:
    arr1.append(ele.strip())

arr1.sort()

for ele in arr1:
    print(ele,1)
