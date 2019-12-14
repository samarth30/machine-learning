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
y = dataset.iloc[:,2:3].values


# feature scalling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)


#fitting the svr in the model
from sklearn.svm import SVR
regressor = SVR(kernel="rbf")
regressor.fit(x,y)

y_pred = sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([[6.5]]))))

# graph linear regression
plt.scatter(x,y,color="red")
plt.plot(x,regressor.predict(x),color="blue")
plt.title("truth or bluff (Linear regression)")
plt.xlabel("position level")
plt.ylabel("sallary")
plt.show()


