# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:30:41 2016

@author: bacro
"""

a = [x for x in range(2,101)]
b= [x for x in range(2,101)]
distinct=[]
for each in a:
    for item in b:
        tmp = each**item
        if tmp not in distinct:
            distinct.append(tmp)

print(len(distinct))