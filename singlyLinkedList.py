# -*- coding: utf-8 -*-
"""
Created on Sun May 29 15:49:34 2022
@author: Kunal Soni
@Description: singly linked list
"""

class Node:
    def __init__(self,value=None):
        self.value = value
        self.prev = None
        self.next = None

class DLinkedList():
    def __init__(self):
        self.head = None
        self.tail= None
        
    def create_ll(self,arr):
        self.head = Node(arr[0])
        
        prev = self.head
                
        for i in range(1,len(arr)): 
            
            node = Node(arr[i])
            prev.next = node
            node.prev = prev
            
            prev = node
            
        self.tail = prev
            
            
    def print_ll(self):
        
        node = self.head
        
        ll = []
        
        while(node != None):
            ll.append(node.value)
            node = node.next
            
        print(ll)

    def print_reverse_ll(self):
        
        node = self.tail
            
        ll = []
        
        while(node != None):
            ll.append(node.value)
            node = node.prev
        
        print(ll)
        
        
    def insert_ll(self,position,value):
        
        node = self.head
        
        i=1
        while(i<=position):
            
            if(i==position):
                newNode = Node(value)
                prev.next = newNode
                newNode.next = node
                node.prev = newNode
                newNode.prev = prev
                i += 1
            else:
                i += 1
                prev = node
                node = node.next

    def delete_ll(self,position):
        
        node = self.head
        
        i=1
        while(i<=position):
            if(i==position):
                prev.next = node.next
                node = None
                i += 1
            else:
                i += 1
                prev = node
                node = node.next 
                
    def update_ll(self,position,value):
        
        node = self.head
        
        i=1
        while(i<=position):
            if(i==position):
                node.value = value
                i += 1
            else:
                i += 1
                prev = node
                node = node.next
            
    def reverse_ll(self):
        
        node = self.head
        prev = None
        
        while(node != None):
            succ = node.next
            
            node.next = prev
            node.prev = succ
            
            prev = node
            node = succ
        
        self.tail = self.head
        self.head = prev
        return()
        

def main():
    
    arr = [16,13,7]
    
    dll = DLinkedList()
    
    dll.create_ll(arr)
    print("Print a doubly linked list:")
    dll.print_ll()
    
    dll.insert_ll(2,1)
    print("\nInsert into and print doubly linked list")
    dll.print_ll()
    
    dll.delete_ll(2)
    print("\nDelete from and print doubly linked list")
    dll.print_ll()
    
    dll.update_ll(3,17)
    print("\nUpdate and print doubly linked list")
    dll.print_ll()
    
    dll.reverse_ll()
    print("\nReverse doubly linked list")
    dll.print_ll()
    
    
if __name__ == "__main__":
    main()
    


    



