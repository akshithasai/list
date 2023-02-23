a=int(input("enter the number:"))
i=1
c=0
while i<=a:
    if a%i==0 and a%1==0:
        c=c+1
    i=i+1
if c==2:
    j=0
    while a>0:
        b=a%10
        j=j*10+b
        a=a//10
    c1=0
    k=1
    while k<=j:
        if j%k==0:
            c1=c1+1
        k=k+1
    if c1==2:
        print("twisted") 
    else:
        print("prime but not twisted")
else:
    print("not prime")                       


