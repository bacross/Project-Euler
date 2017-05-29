# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:50:37 2016

@author: bacro
"""

import math
def sum_num(n):
    nfact=math.factorial(n)
    str_nfact=str(nfact)
    numsum=0
    for each in str_nfact:
        numsum += int(each)
        
    return numsum
    
print(sum_num(10))