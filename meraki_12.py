
a= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
sum1=0
sum2=0
c1=0
c2=0
i=0 
while i<len(a):
    if a[i]%2==0:
        sum1=sum1+a[i]
        c1=c1+1

    else:
        sum2=sum2+a[i]
        c2=c2+1
    i=i+1
print("eveavg",sum1/c1)
print("oddavg",sum2/c2)  