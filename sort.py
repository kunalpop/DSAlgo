# -*- coding: utf-8 -*-
"""
Created on Wed May 25 22:49:23 2022
@author: Kunal Soni
@Description: all sorting algorithms
"""


import math
import os
import sys

def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
        return(arr)
        
            
class Sort():
    
    def __init__(self,arr):
        self.arr = arr
        
    def bubbleSort(self):
        arr = self.arr
        n = len(arr)
        swaps = 1
        
        while(swaps>0):
            swaps = 0
            for j in range(n-1):
                if(arr[j]>arr[j+1]):
                    tmp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = tmp
                    swaps += 1 
        return(arr)
    
    def selectionSort(self):
        arr = self.arr
        n = len(arr)
        for i in range(n):
            mn = arr[i]
            ix = i
            for j in range(i+1,n):
                if(arr[j]<mn):
                    mn = arr[j]
                    ix = j
            tmp = arr[i]
            arr[i] = mn
            arr[ix] = tmp
            
        return(arr)
    
    def insertionSort(self):
        arr = self.arr
        n = len(arr)
        
        count = 0
        
        while(count>0):
            count = 0
            for i in range(n):
                tmp = arr[i]
                for j in range(i,-1,-1):
                    if(arr[j]>arr[i]):
                        arr[i] = arr[j]
                        arr[j] = tmp
                        count += 1
    
        return(arr)   
    
def main():
        
    arr = [10,5,6,7,3,1,2,4,9,8]
    #arr = ['C','a','D','F','p']
    
    sort = Sort(arr)
    
    print("Original array")
    print(arr)
    
    print("\nBubble sorted array")
    print(sort.bubbleSort())
    
    print("\nSelection sorted array")
    print(sort.selectionSort())
    
    print("\nInsertion sorted array")
    print(sort.insertionSort())
    
    print("\nMerge sorted array")
    print( mergeSort(arr) )
    
if __name__ == "__main__":
    main()