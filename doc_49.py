''' Write a Python program to find the last occurrence of a specified item in a given list.
Original list:
['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
Last occurrence of f in the said list:
7
Last occurrence of c in the said list:
15
Last occurrence of k in the said list:
14
Last occurrence of w in the said list:
12
'''
a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
i=0
while i<len(a):
    if a[i]=="f":
        f=i
    elif a[i]=="c":
        c=i
    elif a[i]=="k":
        k=i
    elif a[i]=="w":
        w=i
    i=i+1
print("Last occurrence of f in the said list:",f)
print("Last occurrence of c in the said list:",c)                    
print("Last occurrence of k in the said list:",k)                    
print("Last occurrence of w in the said list",w)                    