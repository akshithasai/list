a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
i=0
sum=0
while i<len(a):
    j=0
    sum1=0
    while j<len(a[i]):
        # sum=sum+a[i][j]
        sum1=sum1+a[j][i]
        
        j=j+1
    sum=sum+sum1  
    i=i+1   
    avg=sum1/len(a)
    print(sum)
    print(avg)

# n=[]
# i=0
# while i<len(a):
#     sum=0
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
#     n.append(sum)
# print(n)        