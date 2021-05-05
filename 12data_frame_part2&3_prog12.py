# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:45:40 2020

@author: Gouri
"""
#there are 
#1.Numeric datatype
#2.Character datatype
#Character types in pandas
#1.Categorical:A string which has a few different value is called 'Categorical' data type
#2.Object type:A string which has mixed types such as numerical and strings is assigned as Object data type.
#'nan' i.e blank values are converted to Object data types
#Memory allocated to categorical type is fixed and limited. Hence it saves memory
#Memory for object type is not fixed
#dtypes return a series of data types of each column
#Syntax:dataframe.dtypes:    
import os
import pandas as pd
import numpy as np
os.chdir(r'C:\Users\Gouri\Anaconda3\Lib\site-packages\pandas')
cars_data=pd.read_csv(r'Programming-Knowledge--master\Toyota.csv',index_col=0)
print(cars_data)
cars_data1=cars_data.copy(deep=True)
#dataframe.dtypes return datatypes of each column
cars_data1.dtypes

#Count of uniqe datatypes
#get_dtype_counts() return counts of unique data types in dataframes
#yntax:datarame.get_dtype_counts()
cars_data1.get_dtype_counts()#means datatypes of each column 
#selecting data based on data types
#pandas.Dataframe.select_dtypes() returns subset of columns based on column dtypes
#syntax:Dataframe.select_dtypes(include None,exclude None):default values are none
cars_data1.select_dtypes(exclude=[object])
cars_data1.select_dtypes(include=['int64'])

#Concise summary of dataframe 
#syntax:dataframe.info()
cars_data1.info()
#KM,HP are read as object instead of integer
#np.unique(array):only single array has to passed.
print(np.unique(cars_data1['KM']))          #returns unique elements of column specified
#it has '??' special character hence all other values are converted to string and finally read as object
print(np.unique(cars_data1['MetColor']))
#though it has all of them as nan values except two values as floats ....it is converted to float64
print(np.unique(cars_data1['Automatic']))   #it should be category datatype bcz it has 0,1...but it is read as int64
#only unique values are returned hence..[0 1]

print(np.unique(cars_data1['Doors'])) #some of the values are of strings datatype and some are numerics...hence it is converted to object


#dataframes part 3:
#importing datarame
cars_data=pd.read_csv(r'C:\Users\Gouri\Anaconda3\Lib\site-packages\pandas\Programming-Knowledge--master\Toyota.csv',index_col=0,na_values=['????','??'])
cars_data.info()
#Converting variable's data types
#astype() is used to explicitly convert datatypes 
#Syntax:dataframe.astype(dtype):dtype is the type we want to change
cars_data['MetColor']=cars_data['MetColor'].astype('object')
cars_data['Automatic']=cars_data['Automatic'].astype('object')
cars_data.info()
cars_data['Automatic'].astype('float64')    #in this case it is converted temporarily ...if its to be converted permanently then convert it as above by assigning into dataframe
cars_data.info()

#impact of variables being category and object data type
#Syntax:ndarray.nbytes: Provides total number of bytes used by particular column
#If 'FuelType' is of 'object' datatype
cars_data['FuelType'].nbytes
#If 'FuelType' is of 'category' datatype
cars_data['FuelType'].astype('category').nbytes

#cleaning column 'Doors':
#checking unique values of variable 'Doors':
print(np.unique(cars_data['Doors']))
#using replace() to replace the existing value with the desired value
#syntax:dataframe.replace([to_place,value,...])
cars_data['Doors'].replace('three',3,inplace=True) #inplace=True will reflect the changes back to dataframe
cars_data['Doors'].replace('four',4,inplace=True)   
cars_data['Doors'].replace('five',5,inplace=True)
#this replacement can also be done using numpy.where() or pandas.where() 
#Python cannot differentiate newly added value with existing value to match them as object.It coniders it as a 'category' 
#now converting 'Doors' to int64
cars_data['Doors']=cars_data['Doors'].astype('int64')
cars_data.info()
print(np.unique(cars_data['Doors']))

#to detect missing values
#syntax:dataframe.isnull().sum() gives count of missing values in each column
cars_data.isnull().sum()
