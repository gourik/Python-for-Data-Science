# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#List is a data structure consists of ordered collectoin of objects.
#Objects witin a list are known as elements or components.
#Elements need not be of same data type...tey can be of different data type.
#It can contain a numeric array,a logical value,matrix,complex vector, a character array,function
#Elements within list are enclosed between []
#Creating list: employee id, emploee_name and variable containing no. of employees:
id=[1,2,3,4]
employee_name=["Ram","Preeti","Satish","John"]
num_emp=4
employee_list=[id,employee_name,num_emp]
#To view a list:
print(employee_list)
#slicing:To access more than one element from list ranging from [x:y].x-inclusive, y-exclusive
print(employee_list[0][0:2])
#Indexing of lists:
#1.Positive indexing:left to right:Starts with 0 and ends at n-1
#2.Negative indexing:right to left:starts with -1 and ends at -n
#employee_name=    ["Ram","Preeti","Satish","John"]....
#Positive indexing:   0     1         2       3
#Negative indexing:   -4      -3          -2        -1 

#Accessing components of a list:
#There are two components in a list:Top level and sublevel components:
#To access top level components, use single slicing operator [].
#To access sub level components, use double slicing operator[][].
#Top level components are:id,empolyee_name,num_emp
#Sub level components are:[1,2,3,4],["Ram","preeti","Satish","John"],4
#To extract id from employee_list:
print(employee_list[0])
#To extract "Preeti" from employee_list:
print(employee_list[1][1])
#To extract second id from level id of employee_list:
print(employee_list[0][1])

#Part2:
#Modifying components of a list using two methods:
#1.Assigning elements directly to index position that has to be updated
#2.Using inbuilt function:element to be updated is givn as input to function along with its index.
#1. 
#Assign values to be changed to corresponding index of list:
#Changing value in top level components of list:
#Change number of employees to 5:
employee_list[2]=5   
print(employee_list)
#Change the value in sub level component of a list:
#Change 'John' to 'Karan'
employee_list[1][3]="Karan"
print(employee_list)

#2.
#Modifying components using append():
#append():adds an object at the end of list.
#Syntax:list[index].append(object):if index is not specified then object is added at new level of the list
#There are two way to add elemnts to a list:
#a. Add an elment to a list:
#b. Add list to a list:
#a. Adding an element to a list:
employee_list[0].append(5)
employee_list[1].append('Nirmal')
print(employee_list)
#b Adding a list to a list:
#Adding a new list age to the list employee_list:
age=[23,25,36,43,52]
employee_list.append(age) 
print(employee_list)

#Modifying using insert():
#It adds an object at the given position in the list.
#Syntax:list[index].insert(position,object):
#Adding number 6 at 1st position to level id from employee_list:
employee_list[0].insert(0,6) 
print(employee_list)

#Modifying using del:
#del-Removs element from a list at specified index:
#syntax:del list_name[index1][index2]:
#index1:index of top level components of list.
#index2:index of sub level components of list.
#Drop age from employee_list:
del employee_list[3] 
print(employee_list)

#Modifying using remove:
#remove(): removes first matching element from the list
#Syntax:list[index].remove(object):
#Remove 'Ram' from employee_name of employee_list:
employee_list[1].remove('Ram')  
print(employee_list)
#Consider another list:
salary=["high","Low","medium","Low"]
#removing first occurence of 'Low':
salary.remove('Low')
print(salary)

#Modifying components using pop():
#pop() displays the object that is being removed from list specified by its index number.
#Syntax:listname[index1].pop(index2):
employee_list[0].pop(0)  
