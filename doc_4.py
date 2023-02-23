'''
List product excluding duplicates.
	List = [6,1,3,5,6,3,1]
	Output: 60
'''
a=[3,4,2,4,5,6,7,1,3,2]
i=0
b=[]
p=1
while i<len(a):
    c=a.count(a[i])
    if c>=1: 
        if a[i] not in b:
             b.append(a[i]) 
             p=p*a[i]
    i=i+1
print(p)    