# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:46:32 2016

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

tmp = primes_sieve1(2000001)