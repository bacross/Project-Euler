# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 09:36:38 2016

@author: bacro
"""

def cltz_next(n): #returns the next number in the collatz sequence
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        return n

def cltz_len(n):
    lencltz=0
    while n>1:
        n=cltz_next(n)
        lencltz+=1
        yield lencltz

def cltz_convert(cltz):
    tmp = list(cltz)
    target = tmp[len(tmp)-1] + 1
    return target

def cltz(n):
    return cltz_convert(cltz_len(n))

def find_max(n):
    if n>=2:
        max_i=0
        max_len=0
        for i in range(2,n):
            tmp1 = cltz(i)
            if tmp1>max_len:
                max_len=tmp1
                max_i = i
                
        return [max_len,max_i]

print(find_max(1000000))



