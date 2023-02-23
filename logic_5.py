


a=int(input("enter the number:"))
while a>=10:
    sum=0
    while a>0:
      b=a%10
      sum=sum+b
      a=a//10
    a=sum
if   a%2==0:
    print("even:",sum)
else:
    print("odd:",sum)  
# else:
#     print("its not 1 digit number:",sum)            