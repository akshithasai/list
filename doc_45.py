'''
 Write a Python program to remove the last N number of elements from a given list. 
Original lists:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
Remove the last 3 elements from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
Remove the last 5 elements from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
Remove the last 1 element from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]
'''

# a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# i=0
# b=[]
# while i<=len(a):
#     if i==13:
#         break
#     else:
#          b.append(a[i])
#     i=i+1
   
# print(b)    



a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
k=int(input("enter the number:"))
s=len(a)-k
h=0
i=[]
while h<s:
    i.append(a[h])
    h=h+1
print(i)    