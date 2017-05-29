# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:49:16 2016

@author: bacro
"""

def find_sum_facts(n):
    s=0
    for i in range(1,n):
        if n%i==0: 
            s+=i
    return s
       

L=28123
s=0
abn=set()

for n in range(1,L):
    if find_sum_facts(n)>n:
        abn.add(n)
    if not any((n-a in abn) for a in abn):
        s+=n
        
print(s)

    
    
