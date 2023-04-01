List1 = ['_1.txt','_2.txt','_3.txt']
List2 = []
# Using For loop
for item in List1:
    item1 = item.replace('_','',1)
    List2.append(item1)
print(List2)

#using list comprehension, just write a code in single line
# [] inside this will result into 3 items which will be initalised or assigned to the new List3
# Benefit of shorter code, also no need to declare the empty list like List3=[]
List3=[item.replace('_','',1) for item in List1]
print(List3)