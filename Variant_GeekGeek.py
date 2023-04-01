#Take input from user , if you find 2 continuous lower case characters, put * in front of those character
# in resulting string, if found more than 2 continuous lower cases, then from 3 onwards place the same character
# and '* symbol
# if found 3 coninuous upper case letters, place $ after those characters in resulting string

#Ex: GeeeKSLsdf o/p: Gee*e*eKSL$sd*f*
test_string = input("Enter a test string")
list1 = list(test_string)
list2 = []
i=0

while(i <len(list1)-1):
    if (list1[i].isupper() != list1[i + 1].isupper()):
        list2.append(test_string[i])
        i=i+1

    elif (list1[i].islower() and list1[i + 1].islower()):
        list2.append(test_string[i:i+2])
        list2.append("*")
        i = i + 1

        while(i<len(list1)-1 and list1[i+1].islower()):
            list2.append(test_string[i+1])
            list2.append("*")
            i = i + 1

    elif (list1[i].isupper() and list1[i + 1].isupper() and list1[i+2].isupper()):
        list2.append(test_string[i:i+3])
        list2.append("$")
        i=i+3

if((i == len(list1) - 1) and list1[i].isupper()):
    list2.append(test_string[i])

if((i == len(list1) - 1) and list1[i].islower() and list1[i-1].islower()!=True):
    list2.append(test_string[i])

print(list2)
Result_string=''.join(list2)
print(Result_string)