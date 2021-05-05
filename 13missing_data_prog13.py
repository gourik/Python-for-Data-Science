# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:12:11 2020

@author: Gouri
"""

import pandas as pd
import numpy as np
#importing missing data
cars_data=pd.read_csv(r'C:\Users\Gouri\Anaconda3\Lib\site-packages\pandas\Programming-Knowledge--master\Toyota.csv',index_col=0,na_values=['????','??'])

#creating a copies of data
cars_data2=cars_data.copy()     #default arguement of copy() function is true.So it will be deep copy
cars_data3=cars_data2.copy()
#Identifying missing data:
#In pandas dataframes all the missing values are read by Pyhton as NaN(Not a Number).isnull() and isna() are used to check the null values. 
#They return boolean values which are true for NaN values.
#to count number of missing values in each column..dataframe.isna().sum() or dataframe.isnull().sum()
cars_data2.isna().sum()
#when many columns have null values.....one of the approaches is to remove rows if they have null values across all the columns.
#to do that....e have to subset the rows that have one or more missing values
cars_data2.isnull()                         
cars_data2.isnull().any(axis=1)

missing=cars_data2[cars_data2.isnull().any(axis=1)]
print(missing)   

#two ways to approaches to fill the missing values:
#1.Filling missing values by mean or median in case of numerical values
#2.Fill missing values with the class which has maximum count,in case of Category variable
#Imputing missing values:
#*Look at the description to know whether nmerical variables should be immputed with mean or median
#use dataframe.describe():This generates decriptive statistics that summarize central tendency,dipersion and shape of a dataset's distribution, excluding NaN values
cars_data2.describe() 
#filling NaN values of Age column:
#Age has mean as 55.67... and median as 60.00 hence it can be replaced with any of the values as there is no much diff in their values. But, mean is lesser compared to median so it is used to fill nan value
#to fill NA/NAN values there is a function called dataframe.fillna().
cars_data2['Age'].fillna(cars_data['Age'].mean(),inplace=True) 
cars_data2['Age']
#Imputing missing values of KM:
cars_data2['KM'].fillna(cars_data2['KM'].median(),inplace=True)
cars_data2['KM']
#Imputing HP missing values
cars_data2['HP'].fillna(cars_data2['HP'].mean(),inplace=True)
cars_data2['HP']
cars_data2.isnull().sum()
cars_data2['FuelType']
#FuelType and MetColor are Category variables and hence they are filled with the most frequently occuring class of variable.
#to do that, series.value_counts()  should be used. This returns element which is most frequently occured by excluding NA values by default
cars_data2['FuelType'].value_counts()
#if we want just the most frequently occuring value....then
cars_data2['FuelType'].value_counts().index[0] 
#To fill NA/NAN values of 'FuelType':
cars_data2['FuelType'].fillna(cars_data2['FuelType'].value_counts().index[0],inplace=True)
cars_data2['FuelType']
cars_data2.isnull().sum()
cars_data2['MetColor'].value_counts()
#instead of using value_counts() .....dataframe.mode() can be used to fill category variable with mode values
cars_data2['MetColor'].mode()
cars_data2['MetColor'].fillna(cars_data2['MetColor'].mode()[0],inplace=True)
cars_data2['MetColor']
cars_data2.isnull().sum()

#Imputing missing values in both nmerical and category variables at one stretch:
#apply() is used to apply along row or column:but in this case it is used across column as fillna() functions along column.
cars_data3=cars_data3.apply(lambda x:x.fillna(x.mean()) if x.dtype=='float' else x.fillna(x.value_counts().index[0]))
cars_data3.isnull().sum()
