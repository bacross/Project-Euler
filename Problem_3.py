# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 11:51:52 2017

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

bignum = 600851475143

nprimes = primes_sieve1(1000000)

maxPrimeFactor = 1
for each in nprimes:
    if bignum % each == 0:
        if each>maxPrimeFactor:
            maxPrimeFactor = each
            
print(maxPrimeFactor)