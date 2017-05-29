# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:43:03 2016

@author: bacro
"""

def fifthpow(x):
    tmp=str(x)
    tmpsum=0
    for each in tmp:
        tmpsum += int(each)**5
        
    return tmpsum

            
tmptmp=0
for each in range(2,10000000):
    if each == fifthpow(each):
        tmptmp += each
        
print(tmptmp)