# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:51:50 2016

@author: bacro
"""
def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

tmp_pr = primes_sieve1(1000)


def qf(a,b,x):
    return (x*x + a*x +b)
    
def count_primes(a,b,prime_list):
    pr_ct = 0    
    for n in range(0,1000):
        if qf(a,b,n) in prime_list:
            pr_ct += 1
    
    return pr_ct
    
prime_counts=[]
index_counts=[]

for a in range(0,42,1):
    for b in range(0,42,1):
        tmp = count_primes(a,b,tmp_pr)
        prime_counts.append(tmp)
        index_counts.append([a,b])
        
        