Quiz = {1:{"Q1":"Q1.Identify the term which denotes that only authorized users are capable of accessing the information?"
        ,"A1":"1","O1":"1. Confidentiality\n2. Integrity\n3. Availability\n4. Non-Repudiation"},
        2:{"Q2":"Q2 State whether True or False: Data encryption is primarily used to ensure confidentiality?"
                ,"A2":"1","O2":"1. True\n2. False\n3. Cannot be interpreted\n4. None"},
        3:{"Q3":"Q3. Identify the Debian-based OS which has 2 virtual machines and focuses on preserving users’ data."
                ,"A3":"2","O3":"1. Fedora\n2. Ubuntu\n3. Whonix\n4. Kubantu"},
        4:{"Q4":"Q4. In which of the following, a person is constantly followed/chased by another person or group of several peoples?"
            ,"A4":"3","O4":"1. Phishing\n2. Bulling\n3. Stalking\n4. Identity Theft"},
        5:{"Q5":"Q5. Which one of the following can be considered as the class of computer threats?"
            ,"A5":"1","O5":"1. Dos Attack\n2. Phishing\n3. Soliciting\n4. Both A & C"},
        6:{"Q6":"Q6. 3) Which of the following is considered as the unsolicited commercial email?"
            ,"A6":"3","O6":"1. Virus\n2. Malware\n3. Spam\n4. All of the above"},
        }

Res_List1=[]
i=1

while(i<len(Quiz)+1):
    try:
        print(Quiz[i][f"Q{i}"])
        print(Quiz[i][f"O{i}"])
        user_choice=int(input("Enter your choice from 1,2,3 & 4\n"))
        if(0<user_choice<=4):
            if user_choice == int(Quiz[i][f"A{i}"]):
                Res_List1.append("True")
                i+=1
            else:
                Res_List1.append("False")
                i+=1
        else:
            print("Invalid User_choice")
    except(ValueError):
        print("Enter appropriate choice")

if(Res_List1.count("False")>0):
    print("Total Incorrect Answers: ",Res_List1.count("False"))

print("Total Correct Answers: ",Res_List1.count("True"))
print("Your Percentage is: ",(Res_List1.count("True")/6)*100,"%")





