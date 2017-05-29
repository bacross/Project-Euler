# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:36:55 2016

@author: bacro
"""
import math


def get_factors(n):
    return sum(2 for i in range(1, round(math.sqrt(n)+1)) if not n % i)


def generate_triangles(limit):
    l=1
    while l<=limit:
        yield sum(range(l + 1))
        l += 1

def test_triangles():
    triangles = generate_triangles(100000)
    for i in triangles:
        if get_factors(i) > 499:
            return i
            
print(test_triangles())