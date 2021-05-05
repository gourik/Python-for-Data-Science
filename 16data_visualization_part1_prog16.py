# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:40:36 2020

@author: Gouri
"""

#Data Visualization allows us to quickly interpret data an adjust different variables to see their effect
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

cars_data=pd.read_csv(r'C:\Users\Gouri\Anaconda3\Lib\site-packages\pandas\Programming-Knowledge--master\Toyota.csv',index_col=0,na_values=['??','????'])

#removing missing values from dataframe:
cars_data.dropna(axis=0, inplace=True)
plt.scatter(cars_data['Age'],cars_data['Price'],c='red') #scatter plot representing relation between two variables
plt.title('Scatter plot of Price vs Age of Cars')
plt.xlabel('Age(months)')
plt.ylabel('Price(Euros)')
plt.show()

#Histogram:It is a graphical representation of data using bars of different heigts
plt.hist(cars_data['KM'])   #there is no yaxis specified..in suc cases it calculates frequency of each unique values of KM variable 
#this doesn't seperate each bin properly
plt.hist(cars_data['KM'],color='green',edgecolor='white',bins=5) 
plt.title("Histogram of kilometer")
plt.xlabel('Kilometer')
plt.ylabel('Frequency')
plt.show()

#bar plot:represents categorical data with rectanglar bars with lenghts proportional to counts that they represent
counts=[979,120,12]
fuelType=('Petrol','CNG','Diesel')
index=np.arange(len(fuelType))
plt.bar(index,counts,color=['red','blue','cyan'])
plt.title("Bar plot of fuel types")
plt.xlabel('FuelTypes')
plt.xticks(index,fuelType,rotation=0)
plt.ylabel('Frequency')
plt.show()
