# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 03:23:05 2019

@author: akash
"""
import pandas as pd
import numpy as np
import sklearn as sk
train = pd.read_csv("Train.csv")
test = pd.read_csv("file:///D:/Hackathon/HDFC/DataSet/Test.csv") 
labels = train["Col2"]
train = train.drop("Col1", axis = 1)

all_data = pd.concat([train, test], axis = 0)

null_val = train.isnull().sum()

remov_na = np.where( null_val >


#df = pd.DataFrame(data)
#data.dtypes()
print(data.describe())






data33 = data.interpolate(method ='linear', limit_direction ='forward', ) 


data33["Col19"].fillna(data33['Col19'].mean(),inplace= True)
data33["Col20"].fillna(data33['Col20'].mean(),inplace= True)
data33.fillna(data33.mean())
#dff.fillna(dff.mean())

#df['numeric column name'].fillna(df['numeric column name'].mean(), inplace = True)

yy =data33.isnull().sum()