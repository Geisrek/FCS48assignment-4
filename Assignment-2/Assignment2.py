def mediant(nums1,nums2):
  N_lst=nums1+nums2
  N_lst.sort()
  size=len(N_lst)
  if size%2==1:
     return float(N_lst[size//2])
  else:
    mid1=N_lst[size//2-1]
    mid2=N_lst[size//2]
    return (float(mid1)+float(mid2))/2.0
print(mediant([1,2],[3,4]))
#Q1
def RepepeateString(s,n):
  return s[::-1]*n
s=input('Enter a input:')
n=int(input('Enter a integer:'))
print(RepepeateString(s,n))
#Q2
def Rearenge(s):
  Array= [x for x in s if x.isupper()]+[x for x in s if not x.isupper() and x!=' ']
  st=''
  for x in Array:
    st+=x
  return st
print(Rearenge(input('Enter string:')))
#Q3
def compareStrings(s1,s2):
    set_1={x for x in s1}
    set_2={x for x in s2}
    return set_1==set_2
print(compareStrings(input('Enter string 1:'),input('Enter string 2:')))

#Q4
def GetMax(lst):
  N_list=list(set(lst))
  return f'The max item is:{N_list[len(N_list)-1]},at the index:{lst.index(N_list[len(N_list)-1])}'
numbers=[1,2,3,4,5]
print(GetMax(numbers))
def GetMin(lst):
  N_list=list(set(lst))
  return f'The min item is:{N_list[0]},at the index:{lst.index(N_list[0])}'
print(GetMin(numbers))
#Q5 
def sumDigits(num):
   if num//10==0:
      return num
   N_num=num-((num//10)*10)
   num//=10
   return N_num+sumDigits(num)
print(sumDigits(348))
#Q6
def DeleteRepeated(s,i=1,j=0):
    if i+1<=len(s):
       if s[j]==s[i] :
          j=i
          i+=1
          s=s[:j]+s[i:]
          return DeleteRepeated(s)
       else:
          j=i
          i+=1
          return DeleteRepeated(s,i,j)
    return s
print(DeleteRepeated(input('Q6 Enter string:')))
def removeRep(s):
  if len(s)<2:
     return s
  if s[0]==s[1]:
    return removeRep(s[1:])
  else:
    return s[0]+removeRep(s[1:])  
print("->",removeRep("Heeelllo Wooooorlld"))
#Q7
def ReversNumber(num,p=0):
  p=len(str(num))-1
  if num//10==0:
      return num
  return ((num%10)*(10**p))+ReversNumber(num//10,p-1)
print(ReversNumber(12345))
#or simply
print(int(str(12345)[::-1]))
       
