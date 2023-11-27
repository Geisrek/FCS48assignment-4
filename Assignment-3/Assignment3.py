# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:48:08 2023

@author: USER
"""
import time
#Q1 it have O(n)
def matrecies(num_column):
    List1=[int(input('Enter element of the first row :')) for _ in range(num_column)]
    List2=[int(input('Enter element of the second row :')) for _ in range(num_column)]
    return [List1,List2,[List1[col]+List2[col] for col in range(num_column)]]
#This solution have O(n^2)
def matrex(row,column):
    rows=[[int(input(f'Enter element for row{r}:')) for _ in range(column)] for r in range((row))]
    ############
    def sum_List(index):
        Matrix_for_index=[row[index] for row in rows]
        return sum(Matrix_for_index,start=0)
    ##############
    sumation_list=[sum_List( index) for index in range(column)]
    rows.append(sumation_list)
    return rows
#print(matrex(2,3))
#Q2 O(n^3) because the max methode have O(n)
def rotateList(rows,columns):
    rotated_list=[[row[index] for row in rows ] for index in range(columns)]
    return rotated_list

#Q3 O(n)
def invertToDict(rows):
    return {f'Class{x}': rows[x] for x in range(len(rows))}
#print(invertToDict(rows))
#Q4 O(n^2)
def MatrixToDict():
    task=['firstname','lastname','ID','jobtitle','company']
    employees=[[input(f'{task[i]}{x+1}')if i!=2 else f'{task[i]}{x}' for i in range(len(task))]for x in range(int(input('Enter the rows number:')))]
    return {employee[2]:[employee[x] for x in range(len(employee)) if x !=2] for employee in employees}
#print(MatrixToDict())
def palendrom(s):
    if len(s)==0:
     return True
    if s[0]==s[len(s)-1]:
        return palendrom(s[1:len(s)-1])
    return False
#print(palendrom('racecar'))
def merge(Array,left,right):
    left_size=len(left)
    right_size=len(right)
    i,l,r=0,0,0
    while r<right_size and l<left_size:
        if left[l]<right[r]:
            Array[i]=left[l]
            l+=1 
        else:
            Array[i]=right[r]
            r+=1
        i+=1
    while l<left_size:
        Array[i]=left[l]
        l+=1 
        i+=1
    while r<right_size:
        Array[i]=right[r]
        r+=1
        i+=1
def mergeSort(Array):
    size=len(Array)
    if size<=1:
        return 
    left=Array[:size//2]
    right=Array[len(left):]
    mergeSort(left)
    mergeSort(right)
    merge(Array, left, right)
"""def binarySearch(Array,item,index=0):
    size=len(Array)
    print(Array,index)
    if size==1 and Array[0]!=item:
        return -1
    middle=Array[size//2]
    print(middle,middle==item,index)
    if middle<item:
        index+=len(Array[:size//2])
        binarySearch(Array[size//2:], item,index)
    elif middle>item:
        index+=len(Array[size//2:])
        binarySearch(Array[:size//2], item,index)
    else:
       index+=len(Array[:size//2])
       return index
    """
def binarySearch(lst,k):
    low=0
    high=len(lst)-1
    while low<= high:
        mid=(low+high)//2
        if k==lst[mid]:
            return mid
        elif k>lst[mid]:
            low=mid+1 
        else:
            high=mid-1 
    return -1
    
#Array=[3,5,7,8,1,2,3]
#mergeSort(Array)
#print(binarySearch(Array,8))
#print(Array)
def Print(s):
    print('-Reseption:',end='')
    for x in s:
        print(x,end='')
        time.sleep(0.20)
def main():
   tasks='1. Add Matrices\n2. Check Rotation\n3. Invert Dictionary\n4. Convert Matrix to Dictionary\n5. Check Palindrome\n6. Search for an Element & Merge Sort\n7. Exit'
   task=int(input(f'{tasks}\n:'))
   if task ==1:
       rows_number=int(input('Enter the rows number:'))
       columns_number=int(input('Enter the colimns number:'))
       print(matrex(rows_number, columns_number))
       main()
   elif task==2:
       rows_number=int(input('Enter the rows number:'))
       columns_number=int(input('Enter the columns number:'))
       rows=[[int(input(':')) for _ in range(columns_number)] for _ in range(rows_number)]
       print(rotateList(rows,columns_number),rows)
       main()
   elif task==3:
      rows_number=int(input('Enter the rows number:'))
      columns_number=int(input('Enter the columns number:'))
      rows=[[int(input(':')) for x in range(columns_number)] for _ in range(rows_number)]
      print(invertToDict(rows))
      main()
   elif task==4:
       print(MatrixToDict())
       main()
   elif task==5:
       print(palendrom(input('Enter the word you want to check:')))
       main()
   elif task==6:
       print('fill the Array by numbers')
       Array=[int(input(':')) for _ in range(8)]
       mergeSort(Array)
       print(Array)
       print(binarySearch(Array, int(input('wich item you want to search:'))))
       main()
   elif task==7:
       return
   else:
       print('Wrong choise ')
       main()
def reseption() :  
 Print('Khello comrad what your name')
 name=input('\n-You:')
 if len(name)<=2 or not name.isalpha():
     Print('\nPlease enter a valid name\n')
     reseption()
 Print(f'Nise to meet you comrad {name} ,please choose your task:')  
 main()
 Print('See you comrad C\\*')
reseption()
    