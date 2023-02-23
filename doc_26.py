''''
Our task is to print the element which occurs 3 consecutive times in a Python list.
Example:
Input: [4, 5, 5, 5, 3, 8]
Output: 5
Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
Output: 1, 22
'''





a=[4, 5, 5, 5, 3, 8]
i=0
b=[]
c=[]
while i<len(a):
    d=a.count(a[i])
    if d>=3:
      b.append(d)
      if a[i] not in c:
        c.append(a[i])
    i=i+1
print(c)        