import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt
%matplotlib inline
flower_dimensions = []
k = int(input("Enter the value of K: "))
location = "C:\\Users\\imraj\\Desktop\\Simpli Learn\\Data Science with Python\\Data Sets\\iris.csv"
flower_data = pd.read_csv(location)
print(flower_data.head())
flower_dimensions.append(float(input("sepal_length: ")))
flower_dimensions.append(float(input("sepal_width: ")))
flower_dimensions.append(float(input("petal_length: ")))
flower_dimensions.append(float(input("petal_width: ")))
flower_data['distance'] = 0
for index, row in flower_data.iterrows():
    flower_data.loc[index, 'distance'] = sqrt((flower_dimensions[0] - row['sepal_length'])**2
                                             +(flower_dimensions[1] - row['sepal_width'])**2
                                             +(flower_dimensions[2] - row['petal_length'])**2
                                             +(flower_dimensions[3] - row['petal_width'])**2)
flower_data.sort_values('distance', inplace=True)
flower_data_k = flower_data.iloc[:k, :].copy()
flower_data_k['class'].value_counts()
sns.swarmplot(x='class', y='sepal_length', data=flower_data)
sns.swarmplot(x='class', y='sepal_width', data=flower_data)
sns.swarmplot(x='class', y='petal_length', data=flower_data)
sns.swarmplot(x='class', y='sepal_width', data=flower_data)
