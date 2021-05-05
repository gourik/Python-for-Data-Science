# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:48:36 2020

@author: Gouri
"""
import numpy as np
#Determinant of matrix:Determinant of matrix is calculated for square matrices
#numpy.linalg.det():returns determinant of matrix
#Syntax:numpy.linalg.det(matrix)
x=np.matrix("4,5,16,7;2,-3,2,3;3,4,5,6;4,7,8,9")
print(x)
det_matrix=np.linalg.det(x)
print(det_matrix)

#Rank of matrix:
#numpy.linalg.matrix_rank(matrix):returns rank of matrix
rank=np.linalg.matrix_rank(x)
print(rank)

#Inverse of matrix:
#numpy.linalg.inv(matrix):returns multiplicative invesrse of matrix
#consider matrix mat:
mat1=np.matrix("3,1,2;3,2,5;6,7,8")
inv_mat=np.linalg.inv(mat1)
mat2=np.matrix("2,1,2;1,0,1;3,1,3")
inv_mat2=np.linalg.inv(mat2)        #throws error as it has its determinant as 0.
np.linalg.det(mat2)
print(inv_mat)


#System of linear equations:
#Consider a system of linaer equations:
#3x+y+2z=2
#3x+2y+5z=-1
#6x+7y+8z=3
#writing them in the form of Ax=b
#3 1 2  x   2
#3 2 5  y = -1
#6 7 8  z    3

#numpy.linalg.solve(matrix_A,matrix_b)-return solution to system Ax=b
#Create matrix A and b
A=np.matrix("3,1,2;3,2,5;6,7,8")
print(A)
b=np.matrix("2,-1,3").transpose()       #X=inv(A).b
print(b)
sol=np.linalg.solve(A,b)
print(sol)


#Linear algebra part 2:
#Creating matrix:
A2=np.matrix("0.24,0.15,0.18,0.07;0.65,0.10,0.24,0.04;0.10,0.54,0.42,0.54;0.01,0.21,0.18,0.35")
print(A2)
b2=np.matrix("75,125,200,100").transpose()
print(b2)
sol2=np.linalg.solve(A2,b2)
print(sol2)
