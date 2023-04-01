test_string = input("Enter a string")
Result_string = " "
list1 = list(test_string) #for converting string directly into list
# list1.extend(test_string) but list1 should be empty list

for i,char1 in enumerate(list1):
    if(i<len(list1)-1):
        if((char1.islower() and list1[i+1].isupper()) or (char1.isupper() and list1[i+1].islower())):
            list1.insert(i+1,'*')
print(Result_string.join(list1))

