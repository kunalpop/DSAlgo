# -*- coding: utf-8 -*-
"""
Created on Mon May 30 22:43:18 2022
@author: Asus
@Description: Binary Search Tree
"""

class Node:
    def __init__(self,val=None):
        self.value = val
        self.left = None
        self.right = None

class BST:
    def __init__(self,arr):
        self.n_nodes = None
        
        self.root = None
        for val in arr:
            self.root = self.insert(self.root,val)
        
    
    def insert(self,root,val):
        if root is None:
            return Node(val)
        else:
            if root.value == val:
                return root
            elif root.value < val:
                root.right = self.insert(root.right, val)
            else:
                root.left = self.insert(root.left, val)
        return root
    
    def sort(self,root,arr):
        if root:
            self.sort(root.left,arr)
            arr.append(root.value)
            self.sort(root.right,arr)
            
            
    def minValueNode(self,node):
        current = node
     
        while(current.left is not None):
            current = current.left
     
        return(current)
            
    def delete(self,root,val):
 
        if root is None:
            return root
        
        if val < root.value:
            root.left = self.delete(root.left,val)
        elif(val > root.value):
            root.right = self.delete(root.right, val)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
     
            temp = self.minValueNode(root.right)
     
            root.value = temp.value
     
            root.right = self.delete(root.right, temp.value)
 
        return(root)
 
                

def main():
    
    arr = [30,50,15,20,10,40,60]
    arr = [8,3,10,1,6,14,4,7,13]
    
    bst = BST(arr)

    print("Root node:",bst.root)
    print("Root Value:",bst.root.value)    

    sarr = []
    bst.sort(bst.root,sarr)
    print("\nThe sorted array is as follows:")
    print(sarr)
    
    sarr=[]
    print("\nDelete node from BST:")
    bst.delete(bst.root,8)
    bst.sort(bst.root,sarr)
    print(sarr)

               
if __name__ == "__main__":
    main()
    

            
                   

        
        
        