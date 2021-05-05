# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:55:30 2020

@author: Gouri
"""

#Reshaping a array:
#reshape(): Recasts an array to new shape without changing its data.
import numpy as np
grid=np.arange(start=1,stop=10).reshape(3,3)   
print(grid)

#Array dimesions:
#Create an array a in another method:
a=np.array([[1,2,3],[4,5,6],[7,8,9]])

#shape()-returns dimensions of an array:
#syntax:array_name.shape
a.shape

#Numpy addition:
#numpy.add():Performs elementwise addition between two arrays:
#syntax:numpy.add(array_1,array_2)
b=np.arange(start=11,stop=20).reshape(3,3)
print(b)
np.add(a,b)

#numpy multiplication:
#numpy.multiply()-performs elementwise multiplication between two arrays
#syntax:numpy.multiply(array_1,array_2)
np.multiply(a,b)

#other numpy functions:
#numpy.subtract():performs elementwise subtraction between two arrays.
#numpy.divide():returns elementwise division of elements.
#numpy.reminder():return elementwise remainder of division.

#Accessing components of an array:
#Components of an array can be accessed using index number:
print(a)
#access element 2 with index (0,1) from a.
a[0,1]

#Extract elements from second and third row of array a.
a[1:3]

#Extract elements from first column of array a.
a[:,0]

#Extract elements from first row of an array a.
a[0,:] 

#Subset of array:
#Consider array a
print(a)
#Subset 2x2 array from original array a:
#Consider first two rows and first two columns from a:
a_sub=a[:2,:2]
print(a_sub) 
#here value 1 should be updated to 12:
a_sub[0,0]=12
print(a_sub)
#Modifying this subset will automatically changes contents of an array:
print(a)  

#Modifying array using transpose():
#numpy.transpose():permute te dimensions of array
#Syntax:numpy.transpose(array)
np.transpose(a)    

#Modifying array using append():
#append()-adds values at the end of array
#syntax:numpy.append(array,axis)
a_row=np.append(a,[[10,11,14]],axis=0) 
print(a_row)
#Create an array and reshape to column array:
col=np.array([21,22,23]).reshape(3,1)
np.append(a,col,axis=1)

#Modifying using insert():
#insert()-adds values at a given position and axis in an array:
#Syntax:numpy.insert(array,obj,values,axis)
#array-input array
#obj-index position
#values-array of values to be inserted
#axis-axis along which values should be inserted
#Consider array a:
print(a) 
#Inserting new array along row and at 1st position:
a_ins=np.insert(a,1,[13,15,16],axis=0) 
print(a_ins)

#modifying array using delete():
#delete()-removes values at a given position and axis in an array.
#Syntax:numpy.delete(array,obj,axis)
#array-input array
#obj-index
#axis-axis along which array should be removed
#Delete third row from existing array a_ins:
a_del=np.delete(a_ins,2,axis=0)
print(a_del)
