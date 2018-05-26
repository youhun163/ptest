#!/bin/env/python

# first test to formatted output

name = input("Name:")
age  = int(input("Age:"))
job  = input("Job:")
home = input("Home:")

#formatted
info = '''
--------------info of %s --------------
Name:       %s
Age:        %d
Job:        %s
Home:       %s
--------------end, %s------------------
''' %(name,name,age,job,home,name)

print(info)