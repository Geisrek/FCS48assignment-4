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
        if self.isEmpty():
            return
        elif self.head.Data==item:
            self.head=self.head.next
        else:
            current=self.head
            priv=current
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
def singlyLinkedList(lst):
    choise=input('a. Add Node\nb. Display Nodes\nc. Search for & Delete Node\nd. Return to main menu:')
    if choise=='a':
       node=int(input("input a numerical value:"))
       lst.add(node)
       singlyLinkedList(lst)
    elif choise=='b':
        lst.displayList()
        singlyLinkedList(lst)
    elif choise=='c':
        item=int(input("input a numerical value to search & delet:"))
        lst.delete(item)
        singlyLinkedList(lst)
    elif choise=='d':
        return
    else:
        print('Wrong paramiter')
        singlyLinkedList(lst)
Linked_List=LinkedList()
singlyLinkedList(Linked_List)
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
class PriorestyQueueStudents:
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
            
"""PQueue=PriorestyQueueStudents()

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
class NumNode:
    def __init__(self,Data,priority):
        self.Data=Data
        self.priority=priority
        self.next=None
class PriorityQueue:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def enQueue(self,item,priority):
        new_item=NumNode(item,priority)
        if self.isEmpty() or new_item.priority>self.head.priority:
            new_item.next=self.head
            self.head=new_item
        else:
            current=self.head
            while current.next and current.next.priority>=new_item.priority:
                current=current.next
            new_item.next=current.next
            current.next=new_item
    def deQueue(self):
        if not self.isEmpty():
            output=self.head.Data
            self.head=self.head.next
            return output
        return 
"""PQ=PriorityQueue()
PQ.enQueue(3,10)
PQ.enQueue(1,11)
PQ.enQueue(-3,1)
PQ.enQueue(10,9)
PQ.enQueue(0,5)
while not PQ.isEmpty():
    print(PQ.deQueue())"""
                
def Calculate(n1,op,n2):
    if not (n1+n2).isalnum():
        return''
    if op=="*":
        return eval(n1)*eval(n2)
    elif op=="/":
        return eval(n1)//eval(n2)
    elif op=="+":
        return eval(n1)+eval(n2)
    elif op=="-":
        return eval(n1)-eval(n2)
    else:
        print("This operation is not exist")
        return -1
#print(Calculate('7', "+", '2'))
#infix="((3+6)-7)*(4/2)"

#bracket="1+(2*2)/(1+1)*1"
#operations=bracket.split(")")

#print(operations)
def getLastOne(s):
    if s.find('(')==-1 and s.find(')'):
        return s
    return getLastOne(s[1:-1])
#print(getLastOne(bracket))
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
def opp(s,nque,oque):
    op_values={'(':6,')':-6,'*':5,'/':4,'+':3,'-':2}
    i=0
    state=1
    anyrhink=0
    priority=0
    prev_prio=0
    st=''
    while i<len(s):
        #print(s[i],priority,state,st)
        if s[i].isdigit():
            st+=s[i]
        else:
           if s[i] in op_values:
               if not s[i]=='('and not s[i]==')' :
                   state=op_values[s[i]]+ anyrhink
                   priority=state
                   #print(st)
                   
                   nque.enQueue(st,max(priority, prev_prio))
                   oque.enQueue(s[i],priority)
                   #print(s[i],op_values[s[i]]+prev_prio)
                   st=''
                   prev_prio=priority
               elif s[i]=='(':
                    anyrhink+=op_values[s[i]]
               elif s[i]==')':
                   if st!='':
                     nque.enQueue(st,max(priority, prev_prio))
                   st=''
                   anyrhink+=op_values[s[i]]
                   

        i+=1
#print(splitop(infix))
def executeOp(infix):
    ops=splitop(infix)
    S=''
    lst=[]
    for o in ops:
      lst.append(o)
      
      if not "(" in o:
            S+=o
            lst[len(lst)-1]=o
            
      elif "(" in o:
            nque=PriorityQueue()
            oque=PriorityQueue()
            opp(o,nque,oque)
            oper=''
            prev=''
            result=0
            while not nque.isEmpty()  :
                num=nque.deQueue()
                if not oque.isEmpty():
                  oper=num+oque.deQueue()
                  
                  
                else:
                    oper=num
                
                prev+=oper
                #print('-',prev)
                
                if len(prev)>=3:
                    n=''
                    n2=''
                    s=''
                    
                    j=0
                    #print(prev)
                    while j<len(prev) and prev[j].isnumeric():
                        #print(prev)
                        n+=prev[j]
                        j+=1
                        if not prev[j].isnumeric():
                            s=prev[j]
                    i=j+1
                    while i<len(prev) and prev[i].isnumeric():
                        n2+=prev[i]
                        i+=1
                    out=prev[:2]
                    #print('->',n,s,n2)
                    result=Calculate(n,s,n2)
                    #print(result)
                    prev=str(result)+prev[i:]
                    lst[len(lst)-1]=result
                S=prev
                #print(S,'<')
    return lst
                
                
    
def Calculator(infix):
    operat=executeOp(infix)
    #print(operat)
    st=operat[0]
    for x in range(0,len(operat),2):
        if x<len(operat)-1:
            #print(str(st), operat[x+1], str(operat[x+2]))
            st=Calculate(str(st), operat[x+1], str(operat[x+2]))
        
            #print(st)
    return st

#print(Calculator("((3+6)-7)*(4/2)"))
class Graph:
    def __init__(self):
        self.graph={}
    def isEmpty(self):
        return len(self.graph)==0
    def add(self,new_vertex):
        self.graph.update({new_vertex:LinkedList()})
    def connectNodes(self,node,node_connect):
        if node in self.graph and node_connect:
            self.graph[node].add(node_connect)
        else:
            error=node if not node in self.graph else node_connect
            raise Exception(f"This node '{error}' is not exist")
    def removeEdge(self,node,node2):
        if node in self.graph and node2 in self.graph:
            self.graph[node].delete(node2)
            self.graph[node2].delete(node)
        else:
            error=node if not node in self.graph else node2
            raise Exception(f"This node '{error}' is not exist")
    #O(n)
    def removeVertex(self,node):
        if node in self.graph:
            self.graph.pop(node)
            for x in self.graph:
                self.graph[x].delete(node)
                #O(n^2)
        else:
            raise Exception(f"This node '{node}' is not exist")
    def displayGraph(self,degree):
        if not degree in self.graph:
            raise Exception(f"This node '{degree}' is not exist")
        else:
            visited=list(self.graph.keys())
            
            Que=Queue()
            Que.enqueue(degree)
            while len(visited)>0:
                if Que.isEmpty():
                    Que.enqueue(visited.pop(0))
                else:
                    vertex=Que.dequeue()
                    
                    if vertex in self.graph:
                        
                        vertex_List=self.graph.pop(vertex)
                        if vertex in visited:
                         visited.remove(vertex)
                        current=vertex_List.head
                        while current!=None:
                                data=current.Data
                                Que.enqueue(data)
                                print(vertex,'->',data)
                                current=current.next
"""graph=Graph()
graph.add(1)
graph.add(2)
graph.add(3)
graph.add(4)
graph.add(5)
graph.add(6)
graph.connectNodes(1, 3)
graph.connectNodes(2, 3) 
graph.connectNodes(2, 4)    
graph.connectNodes(3, 1)  
graph.connectNodes(3, 2)
graph.connectNodes(4, 1)
graph.connectNodes(5, 6)
graph.displayGraph(3)
print("-------------------")
graph.add(1)
graph.add(2)
graph.add(3)
graph.add(4)
graph.add(5)
graph.add(6)
graph.connectNodes(1, 3)
graph.connectNodes(2, 3) 
graph.connectNodes(2, 4)    
graph.connectNodes(3, 1)  
graph.connectNodes(3, 2)
graph.connectNodes(4, 1)
graph.connectNodes(5, 6)       
graph.removeEdge(3,2)
graph.displayGraph(3)"""
    