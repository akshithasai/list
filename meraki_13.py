
char_list = ['a', 'n', 't', 'a', 'a', 't', 'n', 'n', 'a', 'x', 'u', 'g', 'a', 'x', 'a']
result_list = []
for elements in char_list:
     sub_list = []
     sub_list.append(elements)
     sub_list.append(char_list.count(elements))
     if (sub_list not in result_list):
        result_list.append(sub_list)
print(result_list)

# a= ['a',"k","s","h","i","t","h", 'a']
# b= []
# i=0
# while i<len(a):
#     c = []
#     c.append(a[i])
#     c.append(a.count(a[i]))
#     if (c not in b):
#         b.append(c)
#     i=i+1
# print(b)