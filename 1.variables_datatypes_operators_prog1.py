# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:19:19 2020

@author: Gouri
"""

#naming variables:Variables can be named alphanumerically:
age=55
Age=55
age2=55
Age2=55
#Other special character:
#Underscore_:
employee_id=501
#underscore should not be at first or last position
#other special characters are not allowed
#Naming conventions:
#1.Camel case:
ageEmp=45#lowe camelcase
AgeEmp=43#upper camel case
#2.Snake:
ag_emp=3
Age_emp=2
#3.Pascal:
EmpAge=30

#assigning values to multiple variables:
physics,chemistry,mathematics=89,90,75

#Basic data types:
#boolan: 
#represent two values of logic and associated with conditional statements.
#Values:True an False
#Representation:bool

#integer:represents +ve and -ve whole numbers.Z set of all integers.
#representation:int

#Complex:represents real and imaginary part.(a+ib)
#reprsentation:complex

#Float:represents real numbers:
#representation:float

#String:
#all characters enclosed between single or double characters:
#representation:str
#Statistical typed languages:
#data types have to be declared and as they are compiled their data types are known 
#Dynamically typed languaes:
#types of data is known at run time and their data type need not be specified

#Identiying object's data type:
#syntax:type of object:
Employee_name="Ram"
age=44
height=150.6
emp_id='1'
type(Employee_name)
type(age)
type(height) 

#verifying object data type:
type(height) is str

#Coercing object to new data type:
#Syntax:datatype(object)
ht=int(height)
type(ht)
empid=int(emp_id)
type(empid)
emp=int(Employee_name)      #tis kind of coersions are not allowed

#operator and operand:
2+3  #2,3 are operands and + is operator
#Arithmetic operators:
a=10, b=5
#'+'  addition :a+b=15
#'-' subtraction: a-b=5
#'*' multiplication: a*b=50
#'/' division:a/b =2.0
#'%' remainder:a%b=0
#'**' exponent:a**b =100000

#heierarcy of operators:
#parenthesis ()
#Exponent **
#Division /
#Multiplication *
#addition and subtraction: +,-

#assignment operators:
#'=': Assign values from right side operands to left side operand:
a=5
b=10
#'+=':Adds right operand to left operand and stores result on left side operand:
a+=b  #a=15
#'-=':Subtracts right operand to left operand and stores result on left side operand:
a-=b  #a=5
#'*=':Multiplies right operand to left operand and stores it on left side operand:
a*=b #a=50
#'/=':Divides right operand from left operand and store it on left side operand:
a/=b #5

#Relational or Comparision operators:
#Tests numerical equalities and inequalities between two operands and returns a boolean value.
#All relational operator have ssam precedence(priority)
x=5
y=7
# < --> Strictly less than 
print(x<y) 
# <= --> Less than equal to
print(x<=y)
#> greater than
print(x>y) 
#>= greater than equal to
print(x>=y)
#== is equal to
print(x==y)
#!= Not equal to
print(x!=0)

#Logical operators:
#These are used when operands are conditional statements and returns boolean value.
#In python, logical operators are designed to work on scalar values or boolean values.
#or :Logical OR
print((x>y) or (x<y))
#and :Logical AND
print((x>y) and(x<0))
#not: Logical NOT
print(not(x==y))

#Bitwise operators:
#Used when operands are intgers.
#Integers are treated as a string of binary digits.
#Operates bit by bit.
#Can also operate on conditional statements which compare scalar values or arrays.
#Bitwise OR(|), Bitwise AND(&)
#Binar code for x=5 is 0000 0101 and for y=7 is 0000 0111
#In bitwise OR(|), operator copies a bit to te result if it exists in either of operands.
#In bitwise AND(&), operator copies a bit to the result if it exists in both operands.
x|y  #7
print((x<y)|(x==y)) #True

#Precedence of operators:
#Paranthesis -  ()
#Exponent   -   **
#Division   - /
#Multiplication- *
#Addition,Subtraction- +,-
#Bitwise AND- &
#Bitwise OR- |
#Relational operators- <,<=,>,>=,==,!=
#Logical Not: not
#Logical AND: and
#Logical OR:or   