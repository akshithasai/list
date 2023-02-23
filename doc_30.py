''''
Given a list of numbers, write a Python program to count positive and negative numbers in a List.
Example:
list1 = [2, -7, 5, -64, -14]
Output: pos = 2, neg = 3

Iist2 = [-12, 14, 95, 3]
Output: pos = 3, neg = 1
'''





a = [2, -7, 5, -64, -14]
i=0
count1=0
count2=0
while i<len(a):
    if a[i]>0:
        count1=count1+1
    else:
        count2=count2+1
    i=i+1    
print("even",count1) 
print("odd",count2)           