# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 18:55:16 2016

@author: bacro
"""
import pandas as pd
from pandas import DataFrame

def is_sunday(n):
    if n==0:
        var=False
    else:        
        if n%7==0:
            var=True
        else:
            var=False
    return var
    
years=[x for x in range(1900,2011)]

days_per_year=[]
for each in years:
    if each%100==0:
        if each%400==0:
            days_per_year.append(366)
        else:
            days_per_year.append(365)
    else:
        if each%4==0:
            days_per_year.append(366)
        else:
            days_per_year.append(365)

def days_for_year(n):
    if n==365:
        jan=[i for i in range(1,32)]
        feb=[i for i in range(1,29)]
        mar=[i for i in range(1,32)]
        apr=[i for i in range(1,31)]
        may=[i for i in range(1,32)]
        jun=[i for i in range(1,31)]
        jul=[i for i in range(1,32)]
        aug=[i for i in range(1,32)]
        sep=[i for i in range(1,31)]
        octo=[i for i in range(1,32)]
        nov=[i for i in range(1,31)]
        dec=[i for i in range(1,32)]
    else:
        jan=[i for i in range(1,32)]
        feb=[i for i in range(1,30)]
        mar=[i for i in range(1,32)]
        apr=[i for i in range(1,31)]
        may=[i for i in range(1,32)]
        jun=[i for i in range(1,31)]
        jul=[i for i in range(1,32)]
        aug=[i for i in range(1,32)]
        sep=[i for i in range(1,31)]
        octo=[i for i in range(1,32)]
        nov=[i for i in range(1,31)]
        dec=[i for i in range(1,32)]
        
    tmp_year=[jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]
    
    year_days=[]    
    for each in tmp_year:
        for day in each:        
            year_days.append(day)
            
    return year_days
    
df = DataFrame(days_per_year,index=years)

last_year_end='sun'
week=['sun','mon','tues','wed','thurs','fri','sat']
counter =0
for i in range(1901,2001):
    
    temp_days_list = days_for_year(int(df[df.index==i][0]))
    days_of_week=[]
    start_day = (week.index(last_year_end)+1)%7
    for each in temp_days_list:
        days_of_week.append(week[start_day])
        start_day += 1
        start_day = start_day%7
        
    for j in range(len(temp_days_list)):
        if days_of_week[j]=='sun' and temp_days_list[j]==1:
            counter+=1
    
    last_year_end = days_of_week[-1]


print(counter)
        