'''''
Given a List, extract all elements whose frequency is greater than K.
Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
Output: [4, 3]
Explanation: Both elements occur 4 times.
Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
Output: [4, 3, 6]
Explanation: Occur 4, 3, and 3 times respectively.
'''




a = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
i=0
b=[]
c=[]
while i<len(a):
    d=a.count(a[i])
    if d>=3:
        c.append(d)
        if a[i] not in b:
            b.append(a[i])
    i=i+1
print(b)