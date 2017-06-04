# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 10:58:01 2017

@author: bacro
"""

fibs = [1,2]

x=1
while x<4000000:
    n = len(fibs) - 1
    x = fibs[n]+fibs[n-1]
    if x <4000000:
        fibs.append(x)
    
nsumb = sum(each for each in fibs if each%2==0)  


    