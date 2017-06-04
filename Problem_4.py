# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 15:33:22 2017

@author: bacro
"""
import itertools

n = [[x*y for x in range(100,1000)] for y in range(100,1000)]

onelist = list(itertools.chain.from_iterable(n))

def reverseString(nstring):
    revStr = nstring[::-1]
    return revStr

def checkIsPalindrome(nvar):
    nstr = str(nvar)
    nlen = len(nstr)
    if nlen%2==0:
        firstHalfStr = nstr[0:nlen/2]
        secondHalfStr = nstr[nlen/2:]
        secondHalfStrRev = reverseString(secondHalfStr)
        if firstHalfStr == secondHalfStrRev:
            return True
        else:
            return False
    else:
        firstHalfStr = nstr[0:nlen/2]
        secondHalfStr = nstr[nlen/2+1:]
        secondHalfStrRev = reverseString(secondHalfStr)
        if firstHalfStr == secondHalfStrRev:
            return True
        else:
            return False        
            
maxpalin = 0
for each in onelist:
    nstr = str(each)
    if checkIsPalindrome(nstr) == True:
        if each>maxpalin:
            maxpalin = each

print(maxpalin)