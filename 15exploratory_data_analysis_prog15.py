# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:14:30 2020

@author: Gouri
"""

import os
import pandas as pd

os.chdir(r'C:\Users\Gouri\Anaconda3\Lib\site-packages\pandas')
cars_data=pd.read_csv(r'Programming-Knowledge--master\Toyota.csv',index_col=0,na_values=["??","????"])

#Creating a copy of oriinal dataframe
cars_data2=cars_data.copy()

#Frequency table: pandas.crosstab() is used to create frequency table 
pd.crosstab(index=cars_data2['FuelType'],columns='count',dropna=True) 

#Two way tables:To check the relation between categorical variables:
#pandas.crosstab() is also used for creating two tables.
#To look at the frequency distribution of gearbox types with respect to diffrent fuel types of the cars:
#0-manual,1-automatic
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],dropna=True)

#Converting table values in terms of proportions is done is Joint Probability.Two way table:
#Joint Probability is the likeliood of to independent events happening at the same time.
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],normalize=True,dropna=True) 
#normalize=True converts all the table values of crosstab into proportions 

#Two way table: Marginal probability:
#pandas.crosstab() is used to get it.
#Marginal Probabilty is the probability of occurence of single event
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],margins=True,dropna=True,normalize=True)
#here probability of cars having manual gear box when the fuel type are CNG or Diesel or Petrol are 0.95

#Conditional probability: Probability of an event A, given that another event B has already occured.
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],margins=True,dropna=True,normalize='index')   #to make row sum as 1 which meant conditional probability is calculated when index event is already happened.
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],margins=True,dropna=True,normalize='columns')   #to make column sum as 1 which meant conditional probability is calculated when column event has already happened.

#Correlation:Strength of association between two variables.
#dataframe.corr(self, method='pearson')
#self is used to compute pairwise correlation of columns excluding NA/null values
#pearson method is used to find the correlation between numerical variables
numerical_data=cars_data2.select_dtypes(exclude='object')  
numerical_data.shape   #2 columns have been excluded as they are of object data types 
#Correlation between numerical variables:
corr_matrix=numerical_data.corr() 
corr_matrix
