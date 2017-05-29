# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 10:29:00 2015

@author: bacro
"""

# simple Euclid algorithm for finding pythagorean triples
# a = m^2 -n^2
# b = 2mn
# c = m^2 + n^2

trips=[]
for m in range(1,500):
    for n in range(1,500):
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        trips.append([a,b,c])

trip_star=[]
for each in trips:
    trip_sum = each[0]+each[1]+each[2]
    if trip_sum == 1000:
        trip_star.append(each)
     
print(trip_star)