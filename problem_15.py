# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:41:18 2016

@author: bacro
"""
import random

nrows=4
ncols=4

mat = [[0 for x in range(nrows)] for y in range(ncols)] #inner lists are elements of a row, outer list is rows




#print(mat)

def num_paths(n):
    nrows=n
    ncols=n
    tries=0
    paths=[]
    while tries<10000:
        mat = [[0 for x in range(nrows)] for y in range(ncols)] #inner lists are elements of a row, outer list is rows
        mat[0][0]=1 #first coordinate is rows, second columns
        row_coord = 0
        col_coord = 0
        while mat[nrows-1][ncols-1] == 0:
            if row_coord == nrows-1:
                #can only move right
                coinflip = 1
            else:
                if col_coord == ncols-1:
                    #can only move down
                    coinflip = 0
                else:
                    #move randomly                
                    coinflip = random.randint(0,1)
            
            if coinflip ==1: #turn on the slot to the right
                mat[row_coord][col_coord+1] = 1
                row_coord = row_coord
                col_coord = col_coord+1
            else: # turn on the slot down and reposition down
                mat[row_coord+1][col_coord] = 1
                row_coord = row_coord+1
                col_coord = col_coord
                
        if mat not in paths:
            paths.append(mat)
        
        tries +=1
    
    return len(paths)




            
