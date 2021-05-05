# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:25:27 2020

@author: Gouri
"""
#numpy stands for numerical python.
#It is a fundamental package for numerical compuations in python.
#Using numpy, we can perform: 
#Matematical and logical operations on arrays
#Fourier transforms
#Linear algebra operations
#Random number generation

#Creating array:
#Array is an ordered collection of basic data types of given length.
#Syntax:numpy.array(object)
import numpy as np
x=np.array([2,3,4,5])
print(x)
print(type(x))

#numpy can handle different categorical entities:
x=np.array([2,3,'n',5])
print(x)            #Each value is converted to string data type

#Generating arrays using linspace():to generate array randomly with step value within interval. 
#numpy.linspace()-returns equally spaced numbers within given range based on sample number.
#Syntax:numpy.linspace(start,stop,num,dtype,retstep)
#start-start of the interval
#stop-end of the interval
#num-no. of samples to be generated
#dtype-type of an output array
#retstep-return samples and step value

#Generating an array b with start=1 and stop=5
b=np.linspace(start=1,stop=5,num=10,endpoint=True,retstep=False)
#endpoint=True indicates last value to be included
#retstep=False indicates it returns only samples not step value
print(b)
c=np.linspace(start=1,stop=5,num=10,endpoint=False,retstep=True)
print(c) 


#Generating array using arange():
#numpy.arange()-returns equally spaced numbers within given range based on step value.
#Syntax:numpy.arange(start,stop,stop)
#start-start of interval
#stop-end of interval
#step-increament 
d=np.arange(start=1,stop=10,step=2)
print(d)

#Generating arrays filled with ones
#numpy.ones()-returns an array of given shape and type filled with ones.
#Syntax: numpy.ones(shape,dtype)
#shape-integer or sequence of integer specifying rows and columns
#dtype-data type(default:float)
np.ones((3,4))
np.ones((3,4),int)

#Generating arrays filled with zeros:
#syntax:numpy.zeros(shape,dtype)
#shape-rows and columns 
#dtype:data type
np.zeros((3,4))  
np.zeros((3,4),int)

#Generating array using random.rand():returs an array of given shape filled with random values
np.random.rand(3,4) 
np.random.rand(5) 

#Generate arrays using logspace():
#numpy.logspace():returns equally spaced numbers based on log scale.
#syntax:numpy.logspace(start,stop,num,endpoint,base,dtype)
#start:start value of interval
#stop:stop value of interval
#num:no. of samples to be generated
#endpoint:if true, stop is last sample
#base:base of the log space(default)
#dtype:type of array

#Generating array with 5 samples with base 10.0
np.logspace(1,10,num=5,endpoint=True,base=10.0) 

#Advantages of numpy:
#numpy supports vctorized operations.
#array operations are carried out in C and hence Universal functions in numpy are faster than operations 
#carried out on python lists:

#Advantages of numpy in terms of speed:
#timeit is module ich can be used to measure execution time for snippets of code.
#Comparing processing speed of a list and an array using an addition operation:
#creating a list:
x=range(1000)   
#timeit sum(x)
#18.4 µs ± 283 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
#creating a numpy array:
y=np.array(x)
#timeit np.sum(y)
#6.69 µs ± 132 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
#Here numpy array works faster than list.


#Advantages of numpy in terms of storage space:
#Comparing list x and array y from previous example to find memory used at run time.
#getsizeof()-returns size of object in bytes
#syntax:sys.getsizeof(object)
#itemsize-returns size of one element of a numpy array
#syntax:numpy.ndarray.itemsize

#Size of list can be found by multiplying size of an individual element with total number of elements in a list
import sys
sys.getsizeof(1)*len(x)  

#Size of an array can be found by multiplying size of an individual element with number of elements in te array:
y.itemsize*y.size
 