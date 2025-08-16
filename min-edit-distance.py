#!/usr/bin/env python
# coding: utf-8

# # Min Edit Distance - Dynamic Programming

# ##### Author: Kunal Soni
# ##### Last Modified: 17 Aug 2025

source = "intention"
target = "execution"


class Cost:
    
    #Inset target character
    def insertion(tch):
        return 1
    
    #Delete source character
    def deletion(sch):
        return 1
    
    #Substitute source character with target character
    def substitute(sch,tch):
        return 0 if sch==tch else 2
    

def min_edit_distance(source,target):
    m = len(source)
    n = len(target)
    
    #Define edit distance table as matrix
    D = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    #Initialize first row and first column
    for i in range(1,m+1):
        D[i][0] = i
        
    for j in range(1,n+1):
        D[0][j] = j
        
    #Dynamic programming
    for i in range(1,m+1):
        for j in range(1,n+1):
            D[i][j] = min(D[i][j-1] + Cost.insertion(target[j-1]),D[i-1][j] + Cost.deletion(source[i-1]), D[i-1][j-1] + Cost.substitute(source[i-1],target[j-1]))
    
    return D[m][n]



print("Minimum Edit Distance:",min_edit_distance(source,target))





