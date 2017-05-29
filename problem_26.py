# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 16:46:44 2016

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

L = 1000

'''This is a useful application of Fermat’s little thm
that says: 1/d has a cycle of n digits if 
10^n − 1 mod d = 0 for prime d. 
It also follows that a prime number in the denominator,
d, can yield up to d − 1 repeating decimal digits. 
We need to find the largest prime under 1000 
that has d − 1 digits. This is called a full 
reptend prime.'''

for d in primes_sieve1(L)[::-1]:
    period = 1
    while pow(10, period, d) != 1:
        period += 1
    if d-1 == period: 
        break
        

print("longest recurring cycle for 1/d, d =", d)

