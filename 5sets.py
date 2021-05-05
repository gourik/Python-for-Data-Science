# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:13:48 2020

@author: Gouri
"""
#Set:
#Set is collection o ditinct objects
#It does not hold duplicate items
#Sets do not store elements in particular order.
#Created using {}.

#Creating a set:
age={56,52,41,63,41}    #do not throw an error.... 
print(age)              #but it removes duplicate elements

#Creating another set employee_name:
employee_name={'ram','preeti','satish','john','nirmal'} 
print(employee_name)

#Modify using add():
#add():adds element(s) at any position of set
#Adding name Ganesh to employee_name:
#Syntax:set_name.add(object)
employee_name.add('Ganesh')  
print(employee_name)

#Modifying using discard():
#removes matching object from set:
#Syntax:set_name.discard(object):
employee_name.discard('john')
print(employee_name)

#to remove all the elements from existing set using clear()
#syntax:set_name.clear()
employee_name.clear()
print(employee_name)

#Set operations:
junior_datascientist={'R','Python','Tableau'}
data_scientist={'R','Python','Scala','Java','Tableau'}
print(junior_datascientist)
print(data_scientist)

#Set Union:
#Union():returns all elements belonging to both set A and B
#Syntax:Set_A.union(Set_B)
union=junior_datascientist.union(data_scientist)
print(union)

#Set intersection:
#intersection(): returns elements common to both A and B
#Syntax:Set_A.intersection(Set_B)
intersection=junior_datascientist.intersection(data_scientist)
print(intersection)

#Set difference:
#difference()-returns elements beloning to A but not B
difference=junior_datascientist.difference(data_scientist)
print(difference)

diff=data_scientist.difference(junior_datascientist)
print(diff)

#Symmetric difference:
#It returns elements not common to both sets:1-(A intersection B)
symmetric_difference=junior_datascientist.symmetric_difference(data_scientist)
print(symmetric_difference)
