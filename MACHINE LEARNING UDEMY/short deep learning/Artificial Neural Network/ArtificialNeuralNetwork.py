# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:56:44 2019

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the dataset

dataset = pd.read_csv('churn_Modelling.csv')
x = dataset.iloc[:,3:13].values
y = dataset.iloc[:,13].values


# encoding categoriial data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
lableencoder_x_1 = LabelEncoder()
x[:,1] = lableencoder_x_1.fit_transform(x[:,1])
lableencoder_x_2 = LabelEncoder()
x[:,2]= lableencoder_x_2.fit_transform(x[:,2])
onehotencoder = OneHotEncoder()
x = onehotencoder.fit_transform(x).toarray()
x = x[:,1:]



import keras








