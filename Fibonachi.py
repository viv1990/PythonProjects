
user_input = input("Enter number of digits to print")

if(user_input.startswith("-")):
    print("Negative Number Entered")

elif(user_input.isnumeric()!=True):
    print("Entered String, please enter valid input")

elif(user_input.isnumeric()==True):
    i = int(user_input)
    if(i==0 or i<0):
      print("Enter valid input")

    elif(i==1):
        print(0)

    elif(i==2):
        print(0,1)

    else:
        Final_list = [0,1]
        while (len(Final_list)<i):
            y = len(Final_list)
            Final_list.append(Final_list[y-1]+Final_list[y-2])
        print(Final_list)







