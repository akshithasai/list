'''Find the sum of number digits in List.
The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]
Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
'''




# a=[12,43,67,78,21]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     c=a[i]%10+a[i]//10
#     b.append(c)
#     i=i+1
# print(b)



a=int(input("enter"))
b=int(input("enter")) 
c=a+b
print(c)
sum=0
while c>0:
    k=c%10
    sum=sum*10+k
    c=c//10
print(sum)

