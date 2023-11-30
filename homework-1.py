# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:06:01 2023

@author: USER
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def addNode(self,val):
        return Node(val)
    def isEmpty(self):
        return self.root==None
    def insert(self,root,val):
        if root==None:
            root= self.addNode(val)
        elif val>root.data:
            root.right= self.insert(root.right,val)
        elif val<root.data:
            root.left= self.insert(root.left, val)
        return root
    def displayTree(self,root):
        if root!=None:
            self.displayTree(root.left)
            print(root.data)
            self.displayTree(root.right)
        
    def deleteNode(self,root,val):
        current=root
        prev=None
        node=None
        left=None
        right=None
        while current!=None and current.data!=val :
           if val>current.data:
               prev=current
               current=current.right
           elif val<current.data:
               prev=current
               current=current.left
                #current=None
        if current==None:
            print("Node not exist")
            return
        node=current
        left=current.left
        right=current.right
        vals=vars(node)
        if vals['left']==None and vals['right']==None:
            if val<prev.data:
                prev.left=None
            elif val>prev.data:
                prev.right=None
        elif val>root.data:
            if left==None:
                node=node.right
                prev.right=node
            else:
                leef=left
                prenode=node
                
                while leef.left!=None:
                    
                    prenode=leef
                    leef=leef.left
                new_vertex=Node(leef.data)
                prenode.left=None
                new_vertex.left=prenode.left
                new_vertex.right=right
                prev.right=new_vertex
        elif val<root.data :
            if right==None:
                node=node.left
                prev.left=node
            else:
                leef=right
                prenode=node
                while leef.right!=None:
                    prenode=leef
                    leef=leef.right
                new_vertex=Node(leef.data)
                prenode.right=None
                new_vertex.left=left
                new_vertex.right=prenode.right
                prev.right=new_vertex
        
        
        
            
tree=Tree()
root=tree.addNode(5)
tree.insert( root,2)
tree.insert( root,7)
tree.insert( root,3)
tree.insert( root,1)
tree.insert( root,4)
tree.insert( root,6)
tree.insert( root,8)
tree.insert( root,0)
tree.insert( root,9)
tree.insert( root,-1)
tree.displayTree(root)
tree.deleteNode(root, 8)
print("################################")
tree.displayTree(root)