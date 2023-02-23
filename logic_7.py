
# a=[1,2,3,4,5]
# i=0
# b=[]
# c=str(a)
# k=int(c)
# while k>=(k[i]):
#     if k not in b:
#         d=c[i+5]
#         print(c)
#     i=i+1    

# a=[1,2,3,4,5]




# a=[1200,340,340,204,200]
# i=0
# b=[]
# while i<len(a):
#     c=a[i]
#     j=0
#     while j<c:
#         if c%10==0:
#             c=c//10
#         j=j+1
#     b.append(j)
#     i=i+1
# print(b)            


# a=[1,2,3,4,5,[3,5,6,7],9]
# b=[]
# i=0
# while i<len(a):
#     if type(a)==list:
#         j=0
#         while j<len(a):
#             b.append(a)
#             j=j+1
#     i=i+1
# print(b)            



# a="123"
# b=list(a)
# c=[]
# i=-1
# while i>=-len(b):
#      c.append(a[i])
#      i=i-1
# print(c)     


# a=[1,3,5,4,6,8]
# b=str(a)
# i=-1
# c=[]
# while i>-5:
#     d=int(b[i])+int(b[i+1])
#     if c not in b:
#        i=i-1
# print(c)    

# a=int(input("enter the time H:"))
# b=int(input("enter the min:"))
# c=int(input("enter the sec:"))
# if a>=12 and a<=24:
#     if b>=1 and b<=60:
#         if c>=1 and c<=60:
#            print(a,b,c,"AM")
#         else:
#             print("no") 
#     else:
#         print("enter valid data")
# else:
#     print(12+a,b,c,"PM")                   
                 
# a=int(input("enter the time"))  ``
# if a>12 and a<=24:
#     print(a+12)
# elif a==12:
#     print("00"+a)
# else:                          
#     print("0"+a)


# def bmi(weight,height):
#     b=weight/(height*0.01)**2
#     print(b)
#     if b<=18.5:
#         return "under weight"
#     elif b<=25:
#         return "normal"
#     elif b<=30:
#         return "over weight"
#     else:
#         return "obese"
# weight=int(input())
# height=int(input())
# print(bmi(weight,height))



a="python language"
b=''
i=0
while i<len(a):
    if a[i] in['a','e','i','o','u']:
        b=b+a[i]
    i=i+1
print(b)