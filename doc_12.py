''''
You will be given a number and you need to return it as a string in Expanded Form. For example:
12  # Should return '10 + 2'
42 # Should return '40 + 2'
70304  # Should return '70000 + 300 + 4'
'''





a=int(input("enter the number:"))
b=[]
i=len(str(a))-1
for k in str(a):
    if k!="0":
        b.append(k+"0"*i)
    i=i-1
    x="+".join(b)
print("'"+x+"'")        