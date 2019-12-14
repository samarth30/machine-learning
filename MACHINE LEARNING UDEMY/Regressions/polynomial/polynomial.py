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

# fitting linear regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x,y)


# fitting polynomial regression into linease regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
x_poly = poly_reg.fit_transform(x)

lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)

# graph linear regression
plt.scatter(x,y,color="red")
plt.plot(x,lin_reg.predict(x),color="blue")
plt.title("truth or bluff (Linear regression)")
plt.xlabel("position level")
plt.ylabel("sallary")
plt.show()

# graph of plynomial regression
x_grid = np.arange(min(x),max(x),0.1)
x_grid = x_grid.reshape(len(x_grid),1)
plt.scatter(x,y,color="red")
plt.plot(x_grid,lin_reg2.predict( poly_reg.fit_transform(x_grid)),color="blue")
plt.title("truth or bluff (Linear regression)")
plt.xlabel("position level")
plt.ylabel("sallary")
plt.show()

#predicitng a new test case
lin_reg.predict(6.5)

#predicting by polynomial
lin_reg2.predict(poly_reg.fit_transform(6.5))
