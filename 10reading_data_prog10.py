# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import pandas as pd
os.chdir(r"C:\Users\Gouri\Anaconda3\Lib\site-packages\pandas")

#importing csv files into spyder
data_csv=pd.read_csv(r"Programming-Knowledge--master\Iris_data_sample_new.csv")  #here data_csv is dataframe....data into spyder is called datarame and contains data in spreadsheet form i.e row as sample and column as variable.
print(data_csv)
#missing or blank values are read as 'nan'
#removing extra id columns by passing index_col=0
data_csv_changed=pd.read_csv(r'Programming-Knowledge--master\Iris_data_sample_new.csv',index_col=0)
print(data_csv_changed)

#Converting junk data such as '??'..'###' into nan values
data_csv_changed=pd.read_csv(r'Programming-Knowledge--master\Iris_data_sample_new.csv',index_col=0,na_values=["??"])     #this is not executed as mentioned 
print(data_csv_changed)

data_csv_changed=pd.read_csv(r'Programming-Knowledge--master\Iris_data_sample_new.csv',index_col=0,na_values=["??","###"])     #this is not executed as mentioned 
print(data_csv_changed)


#importing excel spreadsheets into spyder
data_xlsx=pd.read_excel(r'Programming-Knowledge--master\file_example_XLSX_10.xlsx',index_col=0) #if there are many tabs...then if we want to access by sheet name....then sheet_name=' ' should be passed 
print(data_xlsx)

data_xlsx_na=pd.read_excel(r'Programming-Knowledge--master\file_example_XLSX_10.xlsx',index_col=0,na_values=["??","###"])
print(data_xlsx_na)                                                                                                          


#importing text data
data_txt1=pd.read_table(r'Programming-Knowledge--master\sample.txt',sep="\t")  #this delimiter hasn't worked here
print(data_txt1)

data_txt2=pd.read_table(r'Programming-Knowledge--master\sample.txt',delimiter=",")  #this delimiter hasn't worked here
print(data_txt2)
data_txt3=pd.read_table(r'Programming-Knowledge--master\sample.txt',delimiter=" ")  #this delimiter hasn't worked here
print(data_txt3)
