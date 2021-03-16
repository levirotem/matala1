# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:40:23 2021

@author: levir
"""


num = input("enter number: ")
num= float(num)


from equations import calculate

a=calculate(num)
print(a)