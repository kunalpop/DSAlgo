# -*- coding: utf-8 -*-
"""
Created on Sun May 29 15:49:34 2022
@author: Kunal Soni
@Description: singly linked list
"""

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headNode = None
        
       
    def create_ll(self,arr):
        self.headNode = Node()
        prev = self.headNode
                
        for i in range(0,len(arr)):
            
            node = Node(arr[i])
            prev.next = node
            prev = node
            
        return(self.headNode)
    
    def print_ll(self):
        
        node = self.headNode.next
        
        ll = []
        
        while(node != None):
            ll.append(node.value)
            node = node.next
        
        print(ll)
        
    def insert_ll(self,position,value):
        
        node = self.headNode
        
        i=0
        while(i<position):
            i += 1
            prev = node
            node = node.next
            
            if(i==position):
                newNode = Node(value)
                prev.next = newNode
                newNode.next = node
                break
                
    def delete_ll(self,position):
        
        node = self.headNode
        
        i=0
        while(i<position):
            i += 1
            prev = node
            node = node.next
            
            if(i==position):
                prev.next = node.next
                node = None
                break
                         
    def insert_ll(self,position,value):
        
        node = self.headNode
        
        i=0
        while(i<position):
            i += 1
            prev = node
            node = node.next
            
            if(i==position):
                newNode = Node(value)
                prev.next = newNode
                newNode.next = node
                
    def update_ll(self,position,value):
        
        node = self.headNode
        
        i=0
        while(i<position):
            i += 1
            prev = node
            node = node.next
            
            if(i==position):
                node.value = value
                break
                
    def reverse_ll(self):
        
        node = self.headNode.next
        prev = None
        while(node != None):

            suc = node.next
            node.next = prev
                        
            prev = node
            node = suc
        
        self.headNode.next = prev
        
        return()
        
def main():
    
    arr = [16,13,7]
    
    sll = SLinkedList()
    
    #Create singly linked list
    sll.create_ll(arr)
    
    #Print singly linked list
    print("Print a singly linked list:")
    sll.print_ll()
    
    #Insert singly linkedin list
    sll.insert_ll(2,1)
    print("\nInsert into and print singly linked list")
    sll.print_ll()
    
    #Delete singly linked list
    sll.delete_ll(2)
    print("\nDelete from and print singly linked list")
    sll.print_ll()
    
    #Update singly linked list
    sll.update_ll(3,17)
    print("\nUpdate and print singly linked list")
    sll.print_ll()
    
    #Reverse a singly linked list   
    sll.reverse_ll()
    print("\nReverse singly linked list")
    sll.print_ll()
    
if __name__ == "__main__":
    main()
    
    



