# Password Complexity Check
import csv
import re

Length_reg = r"(\w{8,})"
Upper_reg = r"([A-Z])"
Lower_reg = r"([a-z])"
NonWord_reg = r"(\W)"
Digit_reg = r"([0-9])"

header=[]
with open(r"C:\Users\athar\OneDrive\Desktop\User_account_Python.csv",'r') as f:
    reader=csv.reader(f)
    next(reader)
    print(reader)
    for row in reader:
        header=row[0].split('\t')
        password=header[3]
        if(re.search(Length_reg,password)):
            print("{} has met length requirements".format(header[1]))
        else:
            print("{} has not met length requirements, hence no further checks are done. It is a Non-Compliance".format(header[1]))
            continue
        if(re.search(Upper_reg,password) and re.search(Lower_reg,password)):
            print("{} has met combination of Upper & Lower case requirements".format(header[1]))
        else:
            print("{} has not met  combination of Upper & Lower case requirements".format(header[1]))
        if (re.search(Digit_reg, password)):
            count=0
            for i in range(len(password)-2):
                if password[i:i+3].isdigit():
                    if ((int(password[i])==int(password[i+1])-1) and (int(password[i])==int(password[i+2])-2)):
                        print("{} has met digit character requirements but Consecutive number found in the password".format(header[1]))
                        break
                    else:
                        count+=1
            if(count>0):
                print("{} has met digit character requirements and no consecutive numbers".format(header[1]))
        else:
            print("{} has not met  digit character requirements".format(header[1]))
        if (re.search(NonWord_reg, password)):
            print("{} has met special character requirements".format(header[1]))
        else:
            print("{} has not met  special character requirements".format(header[1]))



