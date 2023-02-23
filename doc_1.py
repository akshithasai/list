''''
Iterate over both the values in a list and their indices
grocery_list = ['flour','cheese','carrots']
Output: 
#=> 0: flour
#=> 1: cheese
#=> 2: carrots
'''




l=["flour","cheese","carrots"]
i=0
while i<len(l):
    print(i,":",l[i])
    i=i+1