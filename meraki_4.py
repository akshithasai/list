# a=[367,4,2,13,56,13,333]
# max1=0
# max2=0
# i=0
# while i<len(a):
#     if a[i]>max1:
#         max1=a[i]
#     i=i+1
# j=0   
# while j<len(a):
#    if a[j]>max2 and a[j]!=max1:
#       max2=a[j]
#    j=j+1
# print(max2)

a=int(input("enter the number:"))
if a<=70:
    print("ok")
elif a>=70 and a<=150:
    b=(a-70)//5
    print("points:",b)
    if b>=12:
        print("licence suspended") 
    else:
        print("better luck next time")    
else:
    print("enter valid data")        