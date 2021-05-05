# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:20:23 2020

@author: Gouri
"""
#if else family of contructs
#if contruct: if expression:
#                statements
#if-else construct:if expression:
#                    statements
#                  else:
#                      statements
#if-elif-else
#construct:    if expression1
#                   stmts
#                elif expression2
#                    stmts
#                    else
#                        stmts

#foor loop:execute certain commands repeatedly and use logic to stop iteratation.
#command: for iter in sequence:
#                    stmts
#while loop:it is executed when a set of commands are to be excuted depending on a specific codition
#syntax:while(condition is satisfied):
#       statements
import os
import pandas as pd
import numpy as np
os.chdir(r'C:\Users\Gouri\Anaconda3\Lib\site-packages\pandas')
cars_data1=pd.read_csv(r'Programming-Knowledge--master\Toyota.csv',index_col=0)
cars_data1.insert(10,"Price_Class","")   #it creates a column with blank value
print(cars_data1)
#for i in range(0,len(cars_data1['Price']),1):
##    if(cars_data1['Price'][i]<=8450):
#        cars_data1['Price_Class'][i]='Low'
#    elif(cars_data1['Price'][i]>11950):
#            cars_data1['Price_Class'][i]='High'
#    else:
#            cars_data1['Price_Class'][i]='Medium'

#i=0
#print(i)
#while i<len(cars_data1['Price']):
#    if (cars_data1['Price'][i]<=8450):
#        cars_data1['Price_Class'][i]="Low"
#    elif((cars_data1['Price'][i]>11950)):
#        cars_data1['Price_Class'][i]="High"
#    else:
#        cars_data1['Price_Class'][i]="Medium"
#    i+=1
#Functions in Python:def function_name(parameters):
#                        statements
#Converting Age variable from months to years by defining a function. Converted values will be stored in 
# a new column called "Age_Converted".So, inserting a new column
cars_data1.insert(11,"Age_Converted",0)
cars_data1
def c_convert(val):
    val_converted=val/12
    return val_converted

cars_data1["Age_Converted"]=c_convert(cars_data1['Age'])
#when division occurs in python,....it provides the result in 5 to 6 decimal points.but, here we need is just one digit after the decimal point.
#So, to do that, round funcion is called by passing 1 as arguement
cars_data1["Age_Converted"]=round(cars_data1["Age_Converted"],1)
#Function with multiple inputs but single output:
#example:Converted values of kilometer will be stored in a new column 'km_per_month'. Hence, inserting a new column:
cars_data1.insert(12,"km_per_month",0)
cars_data1 
#example function for multiple inputs and outputs:But output is returned in the form of list
def c_convert(val1,val2):
    val_converted=val1/12
    ratio=val2/val1
    return[val_converted,ratio]
    
cars_data1["Age_Converted"],cars_data1["km_per_month"]=c_convert(cars_data1['Age'],cars_data1['KM'])
 