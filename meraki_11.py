
# a= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# sum1=0
# sum2=0
# i=0 
# while i<len(a):
#     if a[i]%2==0:
#         sum1=sum1+a[i]
#     else:
#         sum2=sum2+a[i]
#     i=i+1
# print("evennum",sum1)
# print("oddnum",sum2)            



# a= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 42,42,43]
# i=0
# b=[]
# while i<len(a):
#     c=a.count(a[i])
#     if c>=1:
#         if a[i] not in b:
#             b.append(a[i])
#     i=i+1
# print(b)        





# i=421
# while i<=460:
#     c=i-420
#     if c==35:
#         break   
#     else:
#         print(c) 
#     i=i+2   
   

a=int(input("enter the number:"))
if a%4==0:
    if a%100!=0:
        print("leap year")
    else:
        print("not ")
else:
    print("enter valid data")            