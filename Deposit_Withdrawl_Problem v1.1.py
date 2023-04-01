Total_Deposit = 0
Remaining_Balance = 0
List1 = []
while True:
    A = input("Enter D for deposit, W for Withdrawal")
    A = A.strip().upper()
    if A == "D" and len(A) == 1:
        try:

            B = int(input("Enter Amount"))

            if B > 0:
                List1.append(A)
                List1.append(B)
                Total_Deposit = Total_Deposit+B
                print("Your account balance is now", Total_Deposit)
            else:
                print("Amount cannot be 0 or less than 0")

        except ValueError:
            print("Only natural numbers allowed in the input for Amount")

    elif (A == "W") and (len(A) == 1):
        List1.append(A)
        if List1[0]== 'D':
            try:
                if Total_Deposit!=0:
                    B = input("Enter Amount")
                    B = int(B)
                    if B > 0:
                        if Total_Deposit >= B:
                            List1.append(B)
                            Remaining_Balance = Total_Deposit-B
                            Total_Deposit = Remaining_Balance
                            print("Your Remaining Balance is",Remaining_Balance)
                        else:
                            print("Insufficient Funds")
                    else:
                        print("Amount cannot be 0 or less than 0")
                else:
                    print("Insufficient funds, Your Balance is 0/, you cannot withdraw")
            except ValueError:
                print("Only natural numbers allowed in the input for Amount")
                continue
        else:
            print("Insufficient funds, Your Balance is 0/, you cannot withdraw")
            List1 = []
    else:
        print("Invalid Input")

