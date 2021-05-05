# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:10:29 2020

@author: Gouri
"""

#Data visualization using seaborn library:
#creating basic scatter plot:
#importing necessary libraries
import pandas as pd      
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#importing data into spyder:
cars_data=pd.read_csv(r'C:\Users\Gouri\Anaconda3\Lib\site-packages\pandas\Programming-Knowledge--master\Toyota.csv',index_col=0,na_values=['??','????'])
cars_data.dropna(axis=0,inplace=True)
#Scatter plot of Price vs Age with default arguments:
sns.set(style="darkgrid")
sns.regplot(x=cars_data['Age'], y=cars_data['Price']) #there is a regression line rawn in t scatter plot i.e because by default fit_reg=True for regplot()
#this attribute when set to true ...estimates and plots regression model relating x and Y variables

#Scatter plot of Price vs Age without te regression fit line:
sns.regplot(x=cars_data['Age'],y=cars_data['Price'],fit_reg=False)
#xticks:ticks on x-axis, yticks:ticks on y-axis, boxes:grids, points:markers

#Scatter plot of Price vs Age by customizing the appearance of markers:
sns.regplot(x=cars_data['Age'],y=cars_data['Price'],marker="*",fit_reg=False,)

#Scatter plot of Price vs Age by FuelType:Examining how Price values are affecting on Age values for different FelTypes.
#'hue' parameter is used to include another variable to show fuel types categories with different colors:
sns.lmplot(x="Age", y="Price", data=cars_data, fit_reg=False, hue="FuelType",legend=True, palette="Set1")
#legend is used to differenciate FuelType data points with other two variables, palette="set1" is used to set data points of FuelType to color palette "Set1".
#We can custom this appearance of the markers using transparency,shape,size paramters.

#Histogram:With default kernel density estimate:means kernel density distribution used to estimate histogram
sns.distplot(cars_data['Age'], kde=True)    #a curve is drwan for y-axis to represent kernel density
#it has too many intervals which is difficult to interpret 

sns.distplot(cars_data['Age'], kde=False, bins=5) 

#Bar plot is used to check freqency distribution of categorical variable.'FuelType' is a categorical variable in our example:
#frequency distribution of FuelType of cars:
sns.countplot(x="FuelType",data=cars_data)

#Grouped bar plot: of FuelType and Automatic
sns.countplot(x='FuelType',data=cars_data,hue="Automatic") 
pd.crosstab(index=cars_data["Automatic"],columns=cars_data["FuelType"],dropna=True)

#Box and whiskers plot for numerical variable:
#Box and whiskers plot of Price to visually interpret five number summary of price distribution:
sns.boxplot(y=cars_data["Price"]) 
#lower most line indicates min value, upper most line indictes max value, midline of box-meian value(50%), lower line of box- 25% of Price,upper line of box=75% of price, vertical line above max value-outliers(extreme values) exceeding max value

#Box and wiskers plot for numerical and cateorical variable:
#Price of cars for various fuel types:
sns.boxplot(x=cars_data["FuelType"],y=cars_data["Price"])

#Grouped box and whiskers plot:of price vs fueltype and automatic:
sns.boxplot(x=cars_data["FuelType"],y=cars_data["Price"],hue=cars_data["Automatic"])

#Box wiskers plot and Histogram:
#Plotting Box whikers plot and Histogram on same window:
#Split plotting window into parts:
f,(ax_box,ax_hist)=plt.subplots(2, gridspec_kw={"height_ratios":(0.15,.85)})
sns.boxplot(cars_data["Price"], ax=ax_box)
sns.distplot(cars_data["Price"], ax=ax_hist, kde=False) 

#Pairwise plots:
sns.pairplot(cars_data,kind="scatter",hue="FuelType")
plt.show()
#diagonal istribution are univariate distribution 
sns.pairplot(cars_data,kind="scatter")
plt.show()
