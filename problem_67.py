# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 17:33:20 2016

@author: bacro
"""
text_file = 'C:/Users/bacro/OneDrive/Python Scripts/Project Euler/p067_triangle.txt'
tri=open(text_file,'r')
tmp_tri = tri.read()
tmp_tri = tmp_tri.splitlines()

all_list=[]
for each in tmp_tri:
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