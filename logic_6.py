


a=["akshitha","chakali"]
i=0
b=""
while i<len(a):
    j=0
    # b=" "
    while j<len(a)-1:
        c=a[i][j]
        b=b+"."+c.upper()
        j=j+1
    i=i+1
print(b[1:])        
