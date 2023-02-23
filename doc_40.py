'''Write a Python program to sum two or more lists, the lengths of the lists may be different. 
Original list:
[[1, 2, 4], [2, 4, 4], [1, 2]]
Sum said lists with different lengths:
[4, 8, 8]
Original list:
[[1], [2, 4, 4], [1, 2], [4]]
Sum said lists with different lengths:
[8, 6, 4]
'''


a=[[1, 2, 4], [2, 4, 4], [1, 2,0]]
i=0
b=[]
while i<int(len(a)):
    j=0
    sum=0
    while j<len(a[i]):
        c=a[j][i]
        sum=sum+(c)
        j=j+1
    avg=sum/len(a)    
    b.append(avg)
    i=i+1
print(b)
    

