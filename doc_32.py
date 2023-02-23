''''Given start and end of a range, write a Python program to print all positive numbers in given range.
Example:
Input: start = -4, end = 5
Output: 0, 1, 2, 3, 4, 5 

Input: start = -3, end = 4
Output: 0, 1, 2, 3, 4
'''





a=int(input("enter the number:"))
b=int(input("entr the number2:"))
c=[]
while a<=b:
    if a>=0:
        c.append(a)
    a=a+1
print(c) 
