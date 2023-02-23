# a=[1,2,3,4,5,6]
# b=[2,1,0,6,7,3]
# c=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         c.append(a[i])
#     i=i+1
# print(c)         


a=[1,2,3,4,5,6]
b=[2,1,0,6,7,3]
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(c)        