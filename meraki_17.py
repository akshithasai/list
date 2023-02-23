
# list = [17, 12, 17, 17, 18, 10, 17, 14,  13, 11]
# ak= []
# for a in list:
#     n = list.count(a)
#     if n > 1:
#         if ak.count(a) == 0:
#          ak.append(a)

# print(ak)



# a=[3,4,2,4,5,6,7,1,3,2]
# i=0
# b=[]
# while i<len(a):
#     c=a.count(a[i])
#     if c==1:
          
#         print(a[i])
#     i=i+1
       



a=[3,4,2,4,5,6,7,1,3,2]
i=0
b=[]
while i<len(a):
    c=a.count(a[i])
    if c>=1: 
        if a[i] not in b:

            b.append(a[i]) 
    i=i+1
print(b)    