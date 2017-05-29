# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:59:08 2015

@author: Bryan
"""

#find the smallest positive number that is evenly divisible by all numbers 1 thru 20
# i think there is a trick here where you don't have to cycle thru all the numbers
#start with multiples of 20
from collections import Counter

primes_below_20 = [2, 3, 5, 7, 11, 13, 17, 19]

def prime_factors(n):
    # Assume n <= 20 
    if n == 1:
        return []
    for prime in primes_below_20:
        if n % prime == 0:
            return [prime] + prime_factors(n / prime)

primes_needed = Counter()
 
for n in range(2, 21):
    primes = Counter(prime_factors(n))
    primes_needed = primes_needed | primes  # | gives the max of existing values

total = 1
for prime, amount in primes_needed.items():
    total *= prime ** amount

print(total)

