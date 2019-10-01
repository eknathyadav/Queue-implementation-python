#Queue implementation using linked list
"""
Created on Tue Oct  1 21:33:23 2019

@author: Eknath
"""
import gc
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.head  = None
    def enqueue(self,new_node):
        if self.front==None and self.head==None:
            self.front = new_node
            self.head = new_node
        else:
            self.head.next = new_node
            self.head = new_node
            """
            while True:
                if last_node.next ==None:
                    break
                last_node = last_node.next
            last_node.next = new_node
            self.head = new_node
            """
    def dequeue(self,d):
        cur = self.front
        while cur.data!=d:
            cur = cur.next
        if cur==self.head:
            self.front =None
            self.head = None
        else:
            self.front = cur.next
    def printqueue(self):
        curr = self.front
        while curr!=None:
            print(curr.data)
            curr = curr.next
first = node(1)      
first1 = node(2)  
first2 = node(3)   
queue = Queue()
print("--------------After enqueue---------------")
queue.enqueue(first)
queue.enqueue(first1)
queue.enqueue(first2)
queue.printqueue()
print("--------------After dequeue---------------")
queue.dequeue(1)
queue.printqueue()


