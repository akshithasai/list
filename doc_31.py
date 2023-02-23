''''
Given the start and end of a range, write a Python program to print all negative numbers in a given range.
Example:
Input: start = -4, end = 5
Output: -4, -3, -2, -1
'''
a=int(input("enter the number:"))
b=int(input("entr the number2:"))
c=[]
while a<=b:
    c.append(a)
    if a==-1:
        break
    a=a+1
print(c) 