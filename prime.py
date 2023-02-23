# a=int(input("enter the number:"))
# i=1
# while i<a:
#     j=1
#     count=0
#     while j<=a:
#        if a%i==0 and a%1==0:
#           print("prime")
#        else:
#          print(" ")
#        j=j+1 
#     if count!=2:
#         print(i)
#     i=i+1        

a=int(input("enter:"))
count=0
i=1
while i<=a:
    if a%1 ==0 and a%i==0:
        count=count+1
    i=i+1
if count!=2:
    print("composite")
else:
    print("prime")            

