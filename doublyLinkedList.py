# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:52:56 2022
@author: Kunal
@Description: doubly linked list
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
        self.head = Node()
        self.tail = Node()
        
        prev = self.head
        succ = self.tail
        
        i = 0
        
        for v in arr: 
            if(i==0):
                node = Node(v)
                prev.next = node
                node.prev = None
                prev = node
            elif(i==len(arr)-1):
                node = Node(v)
                prev.next = node
                node.prev = prev
                self.tail.prev = node
            else:
                node = Node(v)
                prev.next = node
                node.prev = prev
                prev = node
            i += 1
            
    def print_ll(self):
        
        node = self.head.next
        
        ll = []
        
        while(node != None):
            ll.append(node.value)
            node = node.next
            
        print(ll)

        #node = self.tail.prev
            
        #ll = []
        
        #while(node != None):
        #    ll.append(node.value)
        #    node = node.prev
        
        #print(ll)
        
        
    def insert_ll(self,position,value):
        
        node = self.head
        
        i=0
        while(i<position):
            i += 1
            prev = node
            node = node.next
            
            if(i==position):
                newNode = Node(value)
                prev.next = newNode
                newNode.next = node
                node.prev = newNode
                newNode.prev = prev
                break

    def delete_ll(self,position):
        
        node = self.head
        
        i=0
        while(i<position):
            i += 1
            prev = node
            node = node.next
            
            if(i==position):
                prev.next = node.next
                node = None
                break
                
    def update_ll(self,position,value):
        
        node = self.head
        
        i=0
        while(i<position):
            i += 1
            prev = node
            node = node.next
            
            if(i==position):
                node.value = value
                break
            
    def reverse_ll(self):
        
        node = self.head.next
        prev = None
        self.tail.prev = node
        
        while(node != None):
            succ = node.next
            
            node.next = prev
            node.prev = succ
                        
            prev = node
            node = succ
        
        self.head.next = prev
        
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
