# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:51:53 2015

@author: Bryan
"""

# sum(i=1 to 10) i^2 = 385
#(sum(i=1 to 10) i)^2 = 3025
# x = (sum(i=1 to n) i)^2 = ((n+1)*(n/2))^2
# y = sum(i=1 to n) i^2
# so for each i we have ((i+1)*(i/2))^2 - (i^2) = ((i+1)*(i/2)+i)*((i+1)*(i/2)-i)

temp=0
i=100
sumsq=0
for j in range(1,i+1):
    sumsq = sumsq+ j*j

sqsum = ((i+1)*(i/2))*((i+1)*(i/2))
    
print(sqsum - sumsq)