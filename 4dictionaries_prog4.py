# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:38:14 2020

@author: Gouri
"""

#Dictionaries:
#Dictionary is a hash table data structure.
#It works on key-value pairs.It maps keys to values.
#It is enclosed between {}

#Creating a dictionary with different fuel types:
fuel_type={"petrol":1,"Diesel":2,"CNG":3}
print(fuel_type)

#Accessing components of dictionary:
#To know value of te key petrol from fuel_type:
print(fuel_type['petrol'])

#To access keys from dictionary:
#Syntax:dictionary_name.keys():
fuel_type.keys()

#To access values from dictionary fuel_type:
#Syntax:dictionary_name.values()
fuel_type.values()

#To access both keys and values of dictionary:
#Syntax:dictionary_name.items()
fuel_type.items()

#Modifying dictionary:
#Adding new key-value pair to existing dictionary fuel_type using keys:
#Syntax:dictionary_name[key]=value
fuel_type['electric']=4
print(fuel_type)

#Modifying using builtin command:update():
#dictionary_name.update({key:value})
fuel_type.update({'electric':4})

#Modifying dictionary:
#Modify existing key of dictionary
#Assign value to be changed to corresponding key of dictionary
#value 3 needs to updated to 5:
fuel_type['CNG']=5  
print(fuel_type)

#Modifying dictionary using del:
#del() removes key-value pairs:
#syntax:del dictionary_name[key]
del fuel_type['CNG']
print(fuel_type)

#modifying using clear()
#It removes all the key value pairs from dictionary:
#Syntax:dictionary_name.clear()
fuel_type.clear()
print(fuel_type)
