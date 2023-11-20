#Ex1
#Step-1 count how mny operations you have
#step-2 define the priorety for each operations
#step-3 solve

function=input("")
output=0
Multiply=function.count('*')
Integer_devide=function.count('//')
devide=function.count('/')
combine=function.count('+')
subtract=function.count('-')
mojulos=function.count('%')
operations=Multiply+Integer_devide+(max(Integer_devide*2,devide)-min(Integer_devide*2,devide))+subtract+combine+mojulos

while operations>0:
  current_operation=function
  old_operation=''
  #check the operation that have priorety with prantesis
  while current_operation.find('(')!=-1:
    current_operation=current_operation[function.find('(')+1:function.find(')')]
    print(current_operation) 
  old_operation=current_operation
  current=0
  #define the operation by it priorety and assign it index to current variable
  if current_operation.find('*')!=-1:
     current=current_operation.find('*')
  if current_operation.find('//')!=-1 and current_operation.find('*')==-1:
     current=current_operation.find('//')
  if current_operation.find('/')!=-1 and current_operation.find('*')==-1 and current_operation.find('//')==-1:
     current=current_operation.find('/')
  if current_operation.find('+')!=-1 and current_operation.find('/')==-1 and current_operation.find('*')==-1 and current_operation.find('//')==-1:
     current=current_operation.find('+')
  if  current_operation.find('-')!=-1 and current_operation.find('+')==-1 and current_operation.find('/')==-1 and current_operation.find('*')==-1 and current_operation.find('//')==-1:
    current= current_operation.find('-')
  if current_operation.find('%')!=-1 and current_operation.find('-')==-1 and current_operation.find('+')==-1 and current_operation.find('/')==-1 and current_operation.find('*')==-1 and current_operation.find('//')==-1:
    current=current_operation.find('%')
   left_side=''
   Right_side=''
   x=0
   start=0
   end=0 
   #take the operation wewant as a slice and split it to left side and right side 
   # and also take the number only
   while x < len(current_operation):
     if x < current :
        if current_operation[x].isnumeric() or current_operation[x]=='.':
           left_side+=current_operation[x]
           start=x
        else:
           left_side=''
     elif x>current:
        if current_operation[x].isnumeric() or current_operation[x]=='.':
           Right_side+=current_operation[x]
        elif current_operation[x]=='/' and current_operation[x-1]=='/':
           Right_side+=''
        else:
           end=x
           x=len(current_operation)
     x+=1
   #execute the operation
   if current_operation[current]=='*':
         result=eval(left_side)*eval(Right_side)
   elif current_operation[current:current+2]=='//':
         result=eval(left_side)//eval(Right_side)
   elif current_operation[current]=='/':
         result=eval(left_side)/eval(Right_side)
   elif current_operation[current]=='+':
         result=eval(left_side)+eval(Right_side)
   elif current_operation[current]=='-':
         result=eval(left_side)-eval(Right_side)
   elif current_operation[current]=='%':
         result=eval(left_side)%eval(Right_side)
   #replace the operation with the result in the main string   
   if function.find(old_operation)==0 and len(function)>3 and current_operation[current:current+2]!='//':
         function=f'{result}'+function[function.find(old_operation)+len(old_operation)-2:]
         print('a',function)
   elif function.find(old_operation)==0 and len(function)==3:
         function=f'{result}'
   elif end==len(function)-1:
         function=function[:function.find(old_operation)]+f'{result}'
         print('b')
   else:
         print('c',function[current:current+1],end,start,current)
         if current_operation[current:current+2]=='//' and len(current_operation)>4:
            function=function[:function.find(old_operation)-1]+f'{result}'+function[function.find(old_operation)+len(old_operation)+2:]
         elif current_operation[current:current+2]=='//' and len(current_operation)==4:
            function=f'{result}'
         else:
            function=function[:function.find(old_operation)-1]+f'{result}'+function[function.find(old_operation)+len(old_operation)+1:]
      
print(function)
#Ex2
ID,name,addres=f"{0}{input('Enter the ID:' ).strip()}",input('inter your name:').upper().strip(),input('input the addres:').lower().strip()
date=''
day,Month,year=input('input the day \{DD\}:').strip(),input('input the Month\{MM\}:').strip(),input('input the year \{YYYY\}').strip()
if len(day)<2 and len(day)>0:
    date+=f"0{day}"
elif len(day)==2:
    date+=day
else:
    print("invalid date")

if len(Month)<2 and len(Month)>0:
    date+=f"/0{Month}"
elif len(Month)==2:
    date+=f"/{Month}"
else:
    print("invalid date")
if len(year)==4:
   date+=f'/{year}'
else:
     print('invalid date')
     
print(ID,name,date,addres)
#Ex3
num=input('input a number:')
if num.isnumeric():
   print(f'{len(num)}')
else:
   print('you input invalid character')
#Ex4
Grade=input('input your grade:')
if Grade.isnumeric():
  Grade=int(Grade)
  if Grade<60:
     print('F')
  elif Grade>=60 and Grade<63:
     print('D-')
  elif Grade>=63 and Grade<67:
     print('D')
  elif Grade>=67 and Grade<70:
     print('D+')
  elif Grade>=70 and Grade<73:
     print('C-')
  elif Grade>=73 and Grade<77:
     print('C')
  elif Grade>=77 and Grade<80:
     print('C+')
  elif Grade>=80 and Grade<83:
     print('B-')
  elif Grade>=83 and Grade<87:
     print('B')
  elif Grade>=87 and Grade<90:
     print('B+')
  elif Grade>=90 and Grade<93:
     print('A-')
  elif Grade>=93 and Grade<97:
     print('A')
  elif Grade>=97:
     print('A+')
#Ex5
n=(int(input("Enter the patern height:"))*2)
i=0
for x in range(1,n):
    print()
    if x<n//2:
        while i<x:
          print('*',end='')
          i+=1
        i=0
    else:
        i=x-(n//2)
        j=x-i
        while j>i:
          print('*',end='')
          j-=1
    
#EX6
print()
num_1=int(input('input the first number:'))
num_2=int(input('input the second number:'))
if num_1<num_2:
    for x in range(num_1,num_2+2):
        if x%2==0:
           print(x)
else:
    print('invalid operation')

 

     
  
   
