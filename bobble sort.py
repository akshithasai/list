a=[40,90,50,10,20,60]
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
        # print(a)
        j=j+1
    i=i+1
print(a)