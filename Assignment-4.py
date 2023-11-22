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
        self.size=0
    def isEmpty(self):
        return len(self.queue)==0
    def enqueue(self,val):
        self.size+=1
        self.queue.append(val)
    def dequeue(self):
        if not self.isEmpty():
         self.size-=1
         return self.queue.pop(0)
        return
    def peekFirst(self):
        return self.queue[0]
    def peekLast(self):
        return self.queue[len(self.queue)-1]
class Stack:
    def __init__(self):
        self.Stack=[]
        self.size=0
    def isEmpty(self):
        return len(self.Stack)==0
    def add(self,val):
        self.Stack.append(val)
        self.size+=1
    def POP(self):
        if not self.isEmpty():
            self.size-=1
            return self.Stack.pop()
        return
    def peekFirst(self):
        return self.Stack[0]
    def peekLast(self):
        return self.Stack[len(self.Stack)-1]
"""queue=Queue()
queue.enqueue('b')
queue.enqueue('n')
queue.enqueue('a')
queue.enqueue('n')
while not queue.isEmpty():
    print(queue.dequeue())
print(queue.isEmpty())
stack=Stack()
stack.add('n')
stack.add('a')
stack.add('n')
stack.add('b')
while not stack.isEmpty():
    print(stack.POP())"""
#3
class Student:
    def __init__(self,name,final,midterm,personalety):
        self.name=name
        self.final=final
        self.midterm=midterm
        self.personalety=personalety
        self.next=None
class PriorestyQueue:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    #O(n)
    def enQueue(self,student):
        if self.isEmpty():
            self.head=student
        else:
            current=self.head
            preve=None
            while preve==None and current!=None:
                if student.personalety:
                    print(4)
                    if student.final>current.final:
                        preve=current
                        current=student
                        current.next=preve
                        
                    elif student.final==current.final:
                        print(3)
                        if student.midterm>=current.midterm :
                            preve=current
                            current=student
                            current.next=preve
                        else:
                            if current.next!=None and not current.next.personalety:
                                preve=current.next
                                student.next=preve
                                current.next=student
                            elif current.next==None:
                                prive=student
                                current.next=student
                                current=None
                    else:
                        if current.next!=None and not current.next.personalety:
                            preve=current.next
                            student.next=preve
                            current.next=student
                        elif current.next==None:
                            prive=student
                            current.next=student
                            current=None
                else:
                    if current.next==None:
                        prive=student
                        current.next=student
                        current=None
                if current!=None:
                   current=current.next
            
    def deQueue(self):
        if not self.isEmpty():
            preve=self.head
            self.head=self.head.next
            return f"{preve.name},{preve.final},{preve.midterm},{preve.personalety}"
        return
            
"""PQueue=PriorestyQueue()

PQueue.enQueue(Student('Rafik',90,90,True))             
PQueue.enQueue(Student('Rawan',90,60,True))  
PQueue.enQueue(Student('Radwan',100,100,False)) 
PQueue.enQueue(Student('Fred',80,90,True)) 
PQueue.enQueue(Student('Karim',90,100,True)) 
PQueue.enQueue(Student('Ali',90,30,True))
PQueue.enQueue(Student('Walid',40,40,True))
while not PQueue.isEmpty():
     print(PQueue.deQueue())     """ 
     
                            
#4
def Calculate(n1,op,n2):
    if not (n1+n2).isalnum():
        return
    if op=="*":
        return eval(n1)*eval(n2)
    elif op=="/":
        return eval(n1)/eval(n2)
    elif op=="+":
        return eval(n1)+eval(n2)
    elif op=="-":
        return eval(n1)-eval(n2)
    else:
        print("This operation is not exist")
        return -1
print(Calculate('7', "+", '2'))
infix="1+(3*(4/2))+1+(2*7)*(10/(2-2))"

bracket="(1+(2*2)/(1+1)*1)"
operations=bracket.split(")")

print(operations)
def getLastOne(s):
    if s.find('(')==-1 and s.find(')'):
        return s
    return getLastOne(s[1:-1])
print(getLastOne(bracket))
def splitop(infix):
    i=0
    count=0
    st=''
    l=[]
    while i<len(infix):
        if infix[i]=='(':
            count+=1
        elif infix[i]==')':
            count-=1
        if count>=1:
            st+=infix[i]
        elif count==0 :
            st+=infix[i]
            l.append(st)
            st=''
        i+=1
    return l
l=splitop(infix)
print(l)
for x in l:
    if x[0]=='(':
        print(splitop(x[1:-1]))
    else:
        print(splitop(x))
     
    
