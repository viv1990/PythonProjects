Fin_List = []
Total_Deposit=0
Total_Withdrawl=0
Remaining_Balance=0
i=0
IFlag = False
while True:
    List1 = []

    if IFlag==False:
        A=input("Enter D for deposit, W for Withdrawal")
        A=A.strip().upper()
    if((A=="D" or A=="W") and len(A)==1):
        try:
            B= input("Enter Amount")
            B= int(B)
            IFlag=False
            if B>0:
                List1.append(A)
                List1.append(B)
                Fin_List.extend(List1)
            else:
                print("Amount cannot be 0 or less than 0")
        except(ValueError):
            print("Only natural numbers allowed in the input for Amount")
            IFlag = True
            continue
    else:
        print("Invalid Input")


print(Fin_List)

while(i<len(Fin_List)-1):
    if (Fin_List[i] =='D'or Fin_List=='d'):
        Total_Deposit=Total_Deposit+Fin_List[i+1]
        Remaining_Balance=Remaining_Balance+Fin_List[i+1]
        i+=2
    elif(Fin_List[i] =='W' and Remaining_Balance>=Fin_List[i+1]):
        Total_Withdrawl = Total_Withdrawl + Fin_List[i + 1]
        Remaining_Balance = Remaining_Balance-Fin_List[i+1]
        i += 2
    elif(Fin_List[0]=='W'):
        print(f"Insufficient funds, Your Balance is 0/, you cannot withdraw {Fin_List[i+1]}/")
        break
    else:
        print(f"Insufficient funds, Your Balance is {Remaining_Balance}/, you cannot withdraw {Fin_List[i+1]}/ ")
        print(f"You need {Fin_List[i+1]-Remaining_Balance}/ more to transact")
        break
print("Your account balance is:", Remaining_Balance)

