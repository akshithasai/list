'''''
Count unique values inside a list.
input_list = [1, 2, 2, 5, 8, 4, 4, 8]
Count = 5 #because [1,2,5,8,4] are unique values.
'''



a=[1,2,2,5,8,4,4,8]
i=0
b=[]
count=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        count=count+1
    i=i+1
print(count)        
print(b)