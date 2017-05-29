# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:04:55 2016

@author: bacro
"""

import time
def sum_div(n):
    '''n_series = pd.Series(range(1,n))
    f=lambda x: n%x
    ami = n_series[n_series.apply(f)==0].sum()
    return ami'''
    s=0
    for i in range(1,n):
        if n%i==0: 
            s+=i
    
    return s

def ami_pair(low,high):
    L = [sum_div(x) for x in range(low,high+1)]
    pairs=[]
    for i in range(high - low + 1):
        ind = L[i]
        if i + low < ind and low <= ind and ind <= high and L[ind - low] == i + low:
            pairs.append([i+low,ind])
    return pairs
            

def sum_list(nlist):
    return sum([sum(pair) for pair in nlist])
    
start = time.time()
 
ans = sum_list(ami_pair(1,10000))
 
elapsed = time.time() - start
 
print(ans,elapsed)
