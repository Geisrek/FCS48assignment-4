# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:48:08 2023

@author: USER
"""

#Q1 it have O(1)
def matrecies(num_column):
    List1=[int(input('Enter element of the first row:')) for _ in range(num_column)]
    List2=[int(input('Enter element of the second row:')) for _ in range(num_column)]
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
print(matrex(2,3))
#O(n^3) because the max methode have O(n)
def rotateList(rows):
    rotated_list=[[row[index] for row in rows if index<len(row)] for index in range(len(max(rows)))]
    return rotated_list
rows=[[x for x in range(i,i+3)] for i in range(0,12,3)]
print('->',rows,max(rows))
print('->>',rotateList(rows))