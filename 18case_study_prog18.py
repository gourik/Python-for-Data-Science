# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:34:02 2020

@author: Gouri
"""
#Classifying Personal Income:  

#Subsidy Inc. delivers subsidies to individuals based on their income.It has obtained a large data set athenticated 
#data on individual income, demograpic parameters and a few financial parameters.It wishes us to develop an income classifier system for individuals.

#Objective:Simplify te data system by reducing no. of variables to be studied without satisfying too much of accuracy.Such a system helps Subsidy Inc.
#in planning subsidy outlay,monitoring and preventing misuse.

import pandas as pd         #to work with dataframes
import numpy as np          #to work with numerical operations
import seaborn as sns       #to visualize data
from sklearn.model_selection import train_test_split    #to partition data
from sklearn.linear_model import LogisticRegression     #Importing library for logistic reression
from sklearn.metrics import accuracy_score,confusion_matrix  #Importing performance matrics-accuracy score and confusion matrix

#Importing data
data_income=pd.read_csv(r'E:\anaconda\income.csv')

#creating a copy of original data
data=data_income.copy()

#Exploratory data analysis:
#1.Getting to know the data
#2.Data preprocessing(Missing values)
#3.Cross tables and data visualization

#1. Getting to know the data :
#Checking variable's data types:
print(data.info())

#2. Check for missing values:
data.isnull()                      #It provides datarame o boolean values which is difficult to analyse
data.isnull().sum()                 # to sum the counts of missing values in a variable
#there are no missing values in a data

#Undertanding a data:Summary of numerical variables:
data.describe()                 #It provides statistical description of numerical variables:

#summary of categorical variables:
data.describe(include="O")

#frequncy of each category:
data['JobType'].value_counts()      #missing values exist
data['EdType'].value_counts()       #no missing values
data['maritalstatus'].value_counts()    #no missing values
data['occupation'].value_counts()       #missing values exist
data['relationship'].value_counts()     #missing values exist
data['race'].value_counts()             #no missing values
data['gender'].value_counts()           #no missing values
data['nativecountry'].value_counts()    #no missing values
data['SalStat'].value_counts()          #no missing values 

#Checking for unique classes:
np.unique(data['JobType'])
np.unique(data['occupation'])
#there exists ? instead of nan

#read the file by including na_values=[?]
data=pd.read_csv(r'E:\anaconda\income.csv',na_values=[' ?']) 
print(data)

#data preprocessing:
data.isnull().sum()

missing=data[data.isnull().any(axis=1)] #axis=1 is to consider atleast one column value is missing
print(missing)
#we cannot fill missing values by any of the methods.So we have to drop them.
 
data2=data.dropna(axis=0)

#Relationship between indepenent numerical variables:
corelation=data2.corr() #There is no corelation between numerical variables

#Relation between categorical variables:
#Cross tables and data visualization:
data2.columns 

#Gender proportion table:
gender=pd.crosstab(index=data2['gender'],columns='count',normalize=True)   
print(gender)

#Gender vs SalStat
gender_salstat=pd.crosstab(index=data2["gender"],columns=data2["SalStat"],margins=True,normalize="index")
print(gender_salstat)

#Frequency distribution of salary status:
SalStat=sns.countplot(data2['SalStat'])

#Histogram of Age:
sns.distplot(data2['age'],bins=10,kde=False)

#Box plot of Age and Salary status:
sns.boxplot('SalStat','age',data=data2)
data2.groupby('SalStat')['age'].median()

#Exploratory data analysis:
sns.countplot(y=data2['JobType'],hue=data2['SalStat'])
sns.countplot(y=data2['EdType'],hue=data2['SalStat'])
sns.countplot(y=data2['occupation'],hue=data2['SalStat'])
sns.distplot(data2['capitalgain'],bins=10,kde=False)
sns.boxplot(x=data2['SalStat'],y=data2['hoursperweek'])