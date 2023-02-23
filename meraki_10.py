
# a= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# c1=0
# c2=0
# i=0 
# while i<len(a):
#     if a[i]%2==0:
#         c1=c1+1
#     else:
#         c2=c2+1
#     i=i+1
# print("evennum",c1)
# print("oddnum",c2)            




a= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
c1=0
c2=0
for i in a:
    if i%2==0:
        c1=c1+1
    else:
        c2=c2+1
print("evennum",c1)
print("oddnum",c2)            