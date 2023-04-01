i=0
List1=[]

A=input("Enter a 4 digit binary number separated by comma")
A.strip()
B=A.split(',')

for item in B:
    if item.isnumeric()==True:
        if(len(item)==4):
            if (int(item[0])<=1 and int(item[1])<=1 and int(item[2])<=1 and int(item[3])<=1):
                Sum = int(item[0])*(2**i)+int(item[1])*(2**(i+1))+int(item[2])*(2**(i+2))+int(item[3])*(2**(i+3))
                if(Sum%5==0 and Sum!=0):
                    print(f"{item} where the decimal notation is {Sum} is divisible by 5")
                elif(Sum==0):
                    print("No point in dividing 0 by 5, result is 0")
                else:
                    print(f"{item} where the decimal notation is {Sum} is not divisible by 5")
            else:
                print("Please enter only Binary Numbers")
        else:
            print(f"{item} is not 4 digit number")
    else:
        print("Decimal numbers/special characters/alphabets not allowed")


