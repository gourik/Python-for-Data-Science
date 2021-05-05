# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:30:43 2020

@author: Gouri
"""
#dataframe is a 2 dimenional data structure with rows(samples or records) 0 to n-1 and columns(variables)
#importing data into spyder
import os         #library for changing the working directory
import pandas as pd #to work with dataframes
import numpy as np

os.chdir(r"C:\Users\Gouri\Anaconda3\Lib\site-packages\pandas")

#importing csv file into spyder
cars_data=pd.read_csv(r'Programming-Knowledge--master\Toyota.csv',index_col=0)
print(cars_data)

#creating copies of original datas
#In python there are 2 ways of creating copies.
#1.shallow copy
#2.deep copy 

#1.shallow copy:when copying, a new variable is created which shares addressof an object but a new object is not created, so changes will be reflected into original file
sample=cars_data.copy(deep=False) #default for deep is true
#or shallow copy can also be creatd as
#samp=cars_data

#2.Deep copy: a copy of object is copied into another object without refering to the original. Hence changes made to a copy of original object will not be reflected to original object
cars_data1=cars_data.copy(deep=True)

#attributes of dataframes
#1. DataFrame.index: which returns index(row labels) of the dataframe
cars_data1.index  #returns row labels of cars_data1
print(cars_data1)
#2.DataFrame.columns: To get column names of dataframe
print(cars_data1.columns)    
#3.DataFrame.size:
#To get total number of elements from dataframe
print(cars_data1.size)
#4.DataFrame.shape: provides dimension of dataframe
cars_data1.shape
#5.DataFrame.memory_usage([index,deep]):memory usage of each column in bytes
cars_data1.memory_usage()
#6.DataFrame.ndim
#The number of axes/array dimenions
cars_data1.ndim

#Indexing and selecting data
#DataFrame.head(n):head(n) returns the first n rows from dataframe  
cars_data1.head(6)  #by default, head() returns first 5 rows.
cars_data1.head()
#tail function retrn last n rows of DataFrame
cars_data1.tail(7)
cars_data1.tail() #by default it returns last 5 rows
#To access a scalar value(single value), the fastest way is to use at and iat methods
#at: it provides label based scalar lookups
cars_data1.at[4,'Age'] #rowlabel 4 and Age column
cars_data1.at[4,'FuelType']
#iat: It provide integer based lookups
cars_data1.iat[5,6] #instead of using lables as in above, rowindex and column index can be used.
 #count rows 5 and 6 from 0(row labelled 5 and column labelled 6 excluding index column)
cars_data1.iat[4,5]
cars_data1.iat[2,5]
cars_data1.iat[0,0]
cars_data1.iat[:,0]
#To access a group of rows and columns by label(s) .loc[] can be used.
cars_data1.loc[:,'FuelType'] 
cars_data1.loc[3,'MetColor'] #scalar value from row labelled 3 and column MetColor is extracted
#.loc[] is meant for selecting grouped values ...so : should be used for row index
cars_data1.loc[:,['Age','FuelType']] #using multiple columns to access 
