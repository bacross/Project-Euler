# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:45:32 2015

@author: bacro
"""

# find all pythagorean triples between 1 and 1000

# generate list of primes

def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

tmp = primes_sieve1(1000)


# iterate over list of primes using Euclid's formula to find triples
# Fibonacci method for finding triples

#generate sequence of odd numbers
odds=[]
for i in range(1000):
    if i % 2 > 0:
        odds.append(i)

#find non-prime odds
non_prime_odds=[]
for each in odds:
    if each not in tmp:
        non_prime_odds.append(each)
        
#find non-prime odds that are squares
def is_square(sq):
  x = sq // 2 # divide by two and then take the low integer
  seen = set([x]) # create a set to check of this new integer
  while x * x != sq:  
    x = (x + (sq // x)) // 2  
    if x in seen: return False
    seen.add(x)
  return True

squares=[]
for each in non_prime_odds:
    if each != 1:
        if is_square(each):
            squares.append(each)
 
#iterate thru odds and check if a square, then implement fibonacci formula
import math
py_tri=[]
py_tri_root=[]
for i in range(0,len(odds)):
    if odds[i] in squares:
            a = int(math.sqrt(odds[i]))
            b = int(math.sqrt(sum(odds[0:i])))
            c = int(math.sqrt(sum(odds[0:i+1])))
            py_tri.append([a*a,b*b,c*c])
            py_tri_root.append([a,b,c])
            
print(py_tri_root[0:10])
          
star_tri=[]
for each in py_tri_root:
    if each[0]+each[1]+each[2]==1000:
            star_tri.append(each)
        
print(star_tri)   
        
allnums =[]
for i in range(3,1001):
    allnums.append(i)

py_tri_root=[]
for i in range(0,len(allnums)):
    if allnums[i] in squares:
            a = int(math.sqrt(allnums[i]))
            b = int(math.sqrt(sum(allnums[0:i])))
            c = int(math.sqrt(sum(allnums[0:i+1])))
            #py_tri.append([a*a,b*b,c*c])
           
           py_tri_root.append([a,b,c])           