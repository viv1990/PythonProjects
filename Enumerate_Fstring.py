'''Enumerate fn enumerates starting from 0 index, hence index+1 is used to make it align to actual numbering'''
'''Enumerate object does not have a proper representation but can be used to print inside a list'''
'''Use of f strings to get more control on strings and variable during printing'''
'''Tuple can be initiated without parenthesis'''
'''Use of Remove and pop function of list'''

list1 = ["Clean","Wash","Rinse","Playing","Mop"]
tuple1 = "Meeting","Lunch","Evening Snacks"
k = enumerate(['a','b','c'])
print(k)
# O/P <enumerate object at 0x00000204812D7700> not a correct representation
print(type(k))
print(list(k))
# the above will print the enumerate object in form of tuples in a list

print("Items in list are \n")
for index, item in enumerate(list1):
    print(index,item)


print("\n Items in tuple are \n")
for index, item in enumerate(tuple1):
    print(index+1,item)


print("\n Print Items using f string \n")
for index,item in enumerate(list1):
    row = f"{index+1}::-{item}"
    print(row)

# Remove function in list takes the item name and remove from list
# Pop function takes the index and delete the item form there, if you do not specify an index, it takes the last item
#from the list that is at -1 position
list1.remove("Clean")
print(list1)

value_removed=list1.pop(2)
print(value_removed)