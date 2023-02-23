'''Write a Python program to check if a given string contains an element, which is present in a list. 
The original string and list:
https://www.w3resource.com/python-exercises/list/
['.com', '.edu', '.tv']
Check if https://www.w3resource.com/python-exercises/list/ contains an element, which is present in the list ['.com', '.edu', '.tv']
True
The original string and list: https://www.w3resource.net
https://www.w3resource.net
['.com', '.edu', '.tv']
Check if https://www.w3resource.net contains an element, which is present in the list ['.com', '.edu', '.tv']
False '''


a="https://www.w3resource.com/python-exercises/list/"
b=['.com', '.edu', '.tv']
i=0
c=0
while i<len(b):
    k=b[i]
    if k in a:
        c=c+1
    i=i+1
if c>=1:
    print("true")
else:
    print("false")            

