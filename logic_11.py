a=["hello","take"]
b=["dear","sir"]
i=0
d=[]
j=0
while i<len(a):
    j=0
    while j<len(a):
         c=a[i]+b[j]
         d.append(c)
         j=j+1
    i=i+1  
print(d)    