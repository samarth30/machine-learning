


import numpy as np
import matplotlib as plt
import pandas as pd

# importing the dataset

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# taking care of missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN' , strategy='mean',axis=0)
imputer.fit(x[:,1:3])

x[:,1:3] = imputer.transform(x[:,1:3])

# encoding categorial data
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencode_x = LabelEncoder()
x[:,0] =  labelencode_x.fit_transform(x[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
onehotencoder.fit_transform(x).toarray()

labelencode_y = LabelEncoder()
y =  labelencode_y.fit_transform(y)

# splitting training and test set
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.2,random_state = 0)

# feature scalling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)










