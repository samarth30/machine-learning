# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 03:52:59 2019

@author: DELL
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the dataset

dataset = pd.read_csv('Social_Network_Ads.csv')
x = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,4].values


# splitting training and test set
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.25,random_state = 0)

# feature scalling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

# fiiting Logistic regression into test set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)


# predecting the test result
y_pred = regressor.predict(x_test)


# plotting the graph training set
plt.scatter(x_train,y_train,color='red' )
plt.plot(x_train, regressor.predict(x_train),color='blue')

plt.title('sallery vs experience(training set)')
plt.xlabel('experience')
plt.ylabel('salary')


# plotting the graph test set
plt.scatter(x_test,y_test,color='red' )
plt.plot(x_test, y_pred,color='blue')
plt.title('sallery vs experience(training set)')
plt.xlabel('experience')
plt.ylabel('salary')







