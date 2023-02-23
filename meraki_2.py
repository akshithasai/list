 a=[23,45,67,32,41,40,33,33]
count=0
i=0
while i<len(a):
    if a[i]>=20 and a[i]<=40:
        count=count+1
    i=i+1
print(count)        