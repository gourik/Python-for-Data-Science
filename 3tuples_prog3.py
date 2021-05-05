# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:17:54 2020

@author: Gouri
"""
#Tuple:
#It is an ordered collection of objects
#Some of the operations on tuples are similar to lists
#Tuples are enclosed between ().
#Immutable: Once created cannot be modified later.

#creating a tuple:
#creating a tuple with employee_id,name,age,salary_details
employee_details=('p001','John',35,40000)
print(employee_details)  

#Indexing:There are two types of indexing:
#Positive indexing:Starts from left most element and from 0 and ranges till (n-1)
#Negative indexing:Starts from right most element and from -1 and ranges till -n.
#Accessing components of tuple:
#Using single slicing operator []:
#Syntax:tuple_name[index]:
employee_details[3] 

#Slicing:
#Used to access a set of elements from a tuple by creating a range of index numbers [x:y],
#where x-index number where the slice begins(inclusive)
#y-index where slice ends (exclusive)
#Elements are extracted from x to y-1:
#To extract name and age from employee_details:
employee_details[1:3]
#To extract id,name,age from employee_details
employee_details[:3]
#Length of a tuple:
#len():returns length of a tuple.
#Syntax:len(tuple_name):
len(employee_details)

#Finding minimum and maximum from tuple:
#min()-returns the lowest value in the tuple
#max()-returns the highest value in the tuple
#Syntax:min(tuple_name)
#create a tuple of marks secured by students in English:
english=(56,85,96,75,12) 
min(english)
max(english)

#Combing tuples:Concatination of two tuples
#create a tuple with employee education and department details:
employee_details2=('M.Com','Accounts')
#Combining two tuples:
employee_details3=employee_details+employee_details2
print(employee_details3)
