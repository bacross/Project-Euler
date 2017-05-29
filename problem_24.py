# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:36:56 2016

@author: bacro
"""


# there are 10! total permutations of the list [x for x in range(10)]
# there are 362,880 that begin with 0
# there are 725,760 that being with 0,1
# list begins with 2

# there are 725,760 + 40,320 that begin with 2,0
# there are 725,760 + 2*40,320 that begin with 2,0 or 2,1 -> it begins 2,6
# before 2,6 there are 725,760 + 6*40,320 permutations
#7! is 5,040 -> (1000000 - 725,760 - 6*40320)/5040 -> i'm looking for the 
# 6th number in the set of unused numbers [0,1,3,4,5,7,8,9] or 7
# so it starts 2,1,7
# so prior to 2,1,7 there are 725760+6*40320+6*5040 permutations or 997920
# and there remain 2,080 to 1mm
# math.factorial(6) = 720 so looking for the second item in the set [0,3,4,5,8,9] or 1
# so the sequence is now 

from math import factorial as fact

target = 1000000
set_list=[x for x in range(10)]

tgt_list=[]
start_pt=0
while len(tgt_list)<len(set_list):
    tmp_list=[]
    for each in set_list:
        if each not in tgt_list:        
            tmp_list.append(each)
    
    resid_nums = len(set_list)-len(tgt_list)
    nsteps=1
    perm_size = fact(resid_nums-1)
    while (nsteps+1)*perm_size + start_pt < target:
        nsteps+=1
    start_pt += nsteps*perm_size
    tgt_list.append(tmp_list[nsteps])
    
nstr=""
for each in tgt_list:
    nstr += str(each)
    
print(nstr)