'''
Write a Python program to create a list reflecting the modified run-length encoding from 
a given list of integers or a given list of characters. 
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
List reflecting the modified run-length encoding from the said list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Original String:
aabcddddadnss
List reflecting the modified run-length encoding from the said string:
[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]
'''






a=[1, 1, 2, 3, 4, 4, 5, 1]
b=[]
i=0
while i<len(a):
    c=[]
    c.append(a[i])
    c.append(a.count(a[i]))
    if (c not in b):
          b.append(c)
    i=i+1
print(b)          



# n=int(input("enter no:"))
# a=n
# for i in range(0,n):
#     h=n%10000
#     b=n%1000
#     c=n%100
#     d=n%10
#     i=i+1
# print(n-h,"+",h-b,"+",b-c,"+",c-d,"+",d)