# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 03:52:59 2019

@author: DELL
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the dataset

dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values

# encoding categorial data
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencode_x = LabelEncoder()
x[:,3] =  labelencode_x.fit_transform(x[:,3])
onehotencoder = OneHotEncoder(categorical_features=[3])
x = onehotencoder.fit_transform(x).toarray()

#avoiding the Dummy variable trap
x = x[:,1:]

# splitting training and test set
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.2,random_state = 0)


# fitting multiple regresiion to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

#predecting the test set result
y_pred = regressor.predict(x_test)



# building the optimal model using backward elimination
import statsmodels.formula.api as sm
x = np.append(arr = np.ones((50,1)).astype(int),values=x,axis=1)
x_opt = x[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y,exog = x_opt).fit()
regressor_OLS.summary()

# probability of x2 was greter
x_opt = x[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y,exog = x_opt).fit()
regressor_OLS.summary()


x_opt = x[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog = y,exog = x_opt).fit()
regressor_OLS.summary()

x_opt = x[:,[0,3,5]]
regressor_OLS = sm.OLS(endog = y,exog = x_opt).fit()
regressor_OLS.summary()

x_opt = x[:,[0,3]]
regressor_OLS = sm.OLS(endog = y,exog = x_opt).fit()
regressor_OLS.summary()

# again doing after idetification
dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[:,0:1].values
y = dataset.iloc[:,-1].values



# splitting training and test set
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.2,random_state = 0)



# fitting multiple regresiion to training set
from sklearn.linear_model import LinearRegression
final_regressor = LinearRegression()
final_regressor.fit(x_train,y_train)

y_pred = final_regressor.predict(x_test)

plt.scatter(x_train,y_train,color='red' )
plt.plot(x_train, final_regressor.predict(x_train),color='blue')

plt.xlabel("r&d")
plt.ylabel("profit")

plt.title("r&d and profit")

