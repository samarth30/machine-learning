# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 02:35:57 2019

@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# importing the dataset

dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values


#fitting the Random Forest regression in the model
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=300,random_state=0)
regressor.fit(x,y)

#predict the sallary
y_pred = regressor.predict(6.5)

# graph of Random forest regression
x_grid = np.arange(min(x),max(x),0.01)
x_grid = x_grid.reshape(len(x_grid),1)
plt.scatter(x,y,color="red")
plt.plot(x_grid,regressor.predict(x_grid),color="blue")
plt.title("truth or bluff (Random Forest regression)")
plt.xlabel("position level")
plt.ylabel("sallary")
plt.show()


