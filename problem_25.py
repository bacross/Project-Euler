# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:51:22 2016

@author: bacro
"""

fib_list=[1,1,2]

i=3
while len(str(fib_list[2]))<1000:
    tmp2=fib_list[1]
    tmp3=fib_list[2]
    fib_list[0]=tmp2
    fib_list[1]=tmp3
    fib_list[2]=tmp2+tmp3
    i=i+1
    
print(i)