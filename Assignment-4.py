# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 00:21:16 2023

@author: USER
"""

class Node:
    def __init__(self,val):
        self.Data=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def add(self,val):
        if self.isEmpty():
            self.head=Node(val)
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=Node(val)
    def delete(self,item):
        current=self.head
        priv=None
        while current!=None :
            if current.Data==item:
                priv.next=current.next
            priv=current
            current=current.next
    def displayList(self):
        current=self.head
        while current!=None:
            print(current.Data)
            current=current.next
"""link=LinkedList()
link.add(1)
link.add(2)
link.add(3)
link.add(4)
link.displayList()
link.delete(4)
link.displayList()"""
class Queue:
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        return len(self.queue)==0
    def enqueue(self,val):
        self.queue.append(val)
    def dequeue(self):
        if not self.isEmpty():
         return self.queue.pop(0)
        return
    def peekFirst(self):
        return self.queue[0]
    def peekLast(self):
        return self.queue[len(self.queue)-1]
queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
while not queue.isEmpty():
    print(queue.dequeue())
print(queue.isEmpty())