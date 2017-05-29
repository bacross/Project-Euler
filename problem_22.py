# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:20:21 2016

@author: bacro
"""
import pandas as pd

def name_value(nstr):
    letter_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    value_list=[x for x in range(1,27)]
    letter_dict=dict(zip(letter_list,value_list))
    name_sum=0
    nstr=nstr.lower()
    for each in nstr:
        if each in letter_list:        
            name_sum += letter_dict[each]
        
    return name_sum

name_file = 'C:/Users/bacro/OneDrive/Python Scripts/Project Euler/p022_names.txt'

tmp = open(name_file)

tmp2 = tmp.read()

tmp2_list=tmp2.split(',')

for i in range(len(tmp2_list)):
    tmp2_list[i] = tmp2_list[i].strip('"')
    
namesdf = pd.DataFrame(tmp2_list)
namesdf = namesdf.sort(0)
namesdf['rank']=range(1,len(namesdf[0])+1)
namesdf['namesum']=namesdf[0].apply(name_value)
namesdf['namerankprod']=namesdf['rank']*namesdf['namesum']
targetsum = namesdf['namerankprod'].sum()
print(targetsum)