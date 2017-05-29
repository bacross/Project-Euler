# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 13:07:11 2016

@author: bacro
"""

node_values = [2,1,0.5,0.2,0.1,0.05,0.02,0.01]
new_list=[]
for q in range(len(node_values)-1,-1,-1):
    new_list.append(node_values[q])
    
node_values=new_list
target = 2
two_count = 0
node_range = [x for x in range(0,target)]
cum_sum = [y*node_values[0] for y in node_range] # what is the sum for each node in this coin step
two_count+=cum_sum.count(2) #how many twos in this coin_step              

for i in range(0,len(node_values)): # step across coins
    
    #now need to determine the nodes for the next coin step
    if i < len(node_values)-1:
        node_range=[]
        tmp_tmp_sum=[]
        for item in cum_sum:
            if item <> 2: #only create next nodes for non-two values, which limits the tree space
                tmp = [z for z in range(0,int((target-item)/node_values[i+1] + 1))]
                tmp_sum = [z*node_values[i+1] + int(item) for z in range(0,int((target-item)/node_values[i+1] + 1))]
                for ntmp in tmp:
                    node_range.append(ntmp)
                for nsum in tmp_sum:
                    tmp_tmp_sum.append(nsum)
        
        cum_sum = tmp_tmp_sum
        two_count += cum_sum.count(2)
    #iterate to the next coin step
        
print(two_count)
                