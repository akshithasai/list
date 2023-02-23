
a=int(input("enter the number:"))
b=int(input("entr the number2:"))
c=[]
while a<=b:
    c.append(a)
    a=a+1
print(c) 
i=0
max=0
while i<len(c):
    if c[i]>max:
       max=c[i]
    i=i+1
print(max)          




