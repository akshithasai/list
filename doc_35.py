'''Write a Python program to check if first digit/character of each element in a given list is same or not.
Original list:
[1234, 122, 1984, 19372, 100]
Check if first digit in each element of the said given list is same or not!
True
Original list:
[1234, 922, 1984, 19372, 100]
Check if the first digit in each element of the given list is the same or not!
False
'''






a=[1234, 122, 1984, 1372, 100]
i=0
r=True
while i<len(a):
    if str(a[i])[0]!="1":
        r=False
        break
    else:
        r=True
    i=i+1
print(r)



            