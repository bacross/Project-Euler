# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#build a series of primes
#start with building a series of numbers

numbers=list(range(100))

def primes_sieve_erathos(limit):
    a=[True]*limit #Initialize the primality list
    a[0] = a[1] = False
    
    for (i,isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit): # Mark factors non-prime
                a[n]=False
    
    
temp = primes_sieve_erathos(100)
    
primes=[]
for element in temp:
    primes.append(element)



#count primes until you get to 10001st prime