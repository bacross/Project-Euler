# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 17:06:33 2016

@author: bacro
"""

a= '75'
b= '95 64'
c= '17 47 82'
d= '18 35 87 10'
e= '20 04 82 47 65'
f= '19 01 23 75 03 34'
g= '88 02 77 73 07 63 67'
h= '99 65 04 28 06 16 70 92'
j= '41 41 26 56 83 40 80 70 33'
k= '41 48 72 33 47 32 37 16 94 29'
l= '53 71 44 65 25 43 91 52 97 51 14'
m= '70 11 33 28 77 73 17 78 39 68 17 57'
n= '91 71 52 38 17 14 91 43 58 50 27 29 48'
o= '63 66 04 68 89 53 67 30 73 16 69 87 40 31'
p= '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'
all = [a,b,c,d,e,f,g,h,j,k,l,m,n,o,p]

all_list=[]
for each in all:
    all_list.append(each.split())
    
# so i think the method is to reduce each num in each line to it's max sum of it's two choices
    
#need to turn to numbers first, otherwise int's will be pain in ass
new_list=[]
for each in all_list:
    tmp=[]
    for i in range(0,len(each)):
        tmp.append(int(each[i]))
    
    new_list.append(tmp)

line_below=new_list[len(new_list)-1]
for x in range(len(new_list)-2,0,-1):
    new_line=[]
    for y in range(len(new_list[x])):
        tmp = new_list[x][y]+max(line_below[y],line_below[y+1])
        new_line.append(tmp)
    line_below=new_line
    
        