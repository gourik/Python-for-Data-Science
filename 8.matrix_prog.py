# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:54:09 2020

@author: Gouri
"""

#Matrices are two dimensional data structures containing rows and columns.
#Creating matrix:
#matrix():returns matrix from an array object or string of data.
#Syntax:numpy.matrix(data)
import numpy as np
a=np.matrix("1,2,3,4;5,6,7,8;9,10,11,12")
print(a)

#Matrix Properties:
#shape():this returns number of rows and columns of a matrix
a.shape
#shape[0]:Returns no. of rows of a matrix
a.shape[0]
a.shape[1]  #no. of columns
#size():returns no. of elements in matrix
a.size

#Modifying matrix using insert():
#insert() adds element at specified position and axis in a matrix
#Syntax:numpy.insert(matrix,obj,values,axis)
#matrix:input matrix
#obj:index position
#values:matrix of values to be inserted
#axis:axis along which values should be inserted

#Adding 'col_new' as new column to matrix a:
#Create a matrix:
col_new=np.matrix("2,3,4")
print(col_new)

a=np.insert(a,0,col_new,axis=1)    
print(a)

#Adding a 'row_new' as new row to a:
row_new=np.matrix("4,5,6,7,8")
print(row_new)
a=np.insert(a,3,row_new,axis=0)
print(a)

#Modifying matrix using index number:
#Elements of matrix can be modified using index number.
print(a)
#if we want to change 1 with -3 in matrix a:
a[0,1]=-3
print(a)

#Accessing matrix using index number:
print(a)
#extract elements from second row of matrix a:
print(a[1,:])

#Extract third column of matrix a:
print(a[:,2])

#Extract element at index (1,2):
print(a[1,2])

#Matrix addition:
#numpy.add():performs elementwise addition between two matrices
#syntax:numpy.add(matrix_A,matrix_B)
A=np.matrix(np.arange(0,20)).reshape(5,4)
B=np.matrix(np.arange(20,40)).reshape(5,4)
print(A)
print(B)
c=np.add(A,B)
print(c)

#matrix subtraction:
#numpy.subtract(matrix1,matrix2)
#Consider same matrix A and B
D=np.subtract(A,B)
print(D)    

#Matrix multiplication:numpy.dot(matrix_A,matrix_B)
E=np.dot(A,B)   #this throws error 
E=np.dot(A,np.transpose(B))
print(E)

#Matrix division:
#numpy.divide():performs elementwise division between two matrices:
#Syntax:numpy.divide(matrix_A,matrix_B)
print(np.divide(A,B))
