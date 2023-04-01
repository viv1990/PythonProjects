'''For items in the below list, do the following: "1.doc" should show as "1-doc.txt'''
'''Best example of using Fstring and List comprehension'''

# I started with for loop and then same output using List comprehension
List1 = ['1.doc','1.report','1.presentation']

for i,item in enumerate(List1):
    item1=item.replace('.','-',1)
    List1[i]=f"{item1}.txt"
print(List1)

List2 = ['1.doc','1.report','1.presentation'] # used for list comprehension
# using list comprehension
List2 = [f"{item.replace('.','-')}.txt" for item in List2]
# same can be done by below as strings can be concatenated
#List2 = [item.replace('.','-')+'.txt' for item in List2]

print(List2)