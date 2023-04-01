user_password = input("Enter a Password to check its strength")
count=0
Spec_Char = ['!','@','#','$','%','^','&','*','(',')','.','/','?']
Result_List = []
DigiFlag = False
UpFlag = False
LFlag=False
SFlag=False
if(len(user_password)>=8):
    Result_List.append('True')
else:
    Result_List.append('False')
for item in user_password:
    if(item.isdigit() and DigiFlag!=True):
        DigiFlag=True
    elif(item.isupper() and UpFlag!=True):
        UpFlag=True
    elif(item.islower() and LFlag!=True):
        LFlag=True
    elif((item in Spec_Char) and (SFlag!=True)):
        SFlag=True

if((DigiFlag==True) and(UpFlag==True) and (LFlag==True) and (SFlag==True) and ('True' in Result_List)):
    print("Strong Strength")
elif((DigiFlag==True) and(UpFlag==True) and (LFlag==True) and ('True' in Result_List)):
    print("Medium Strength")
elif('True' in Result_List):
    print("Low Strength")
else:
    print("Password not acceptable as it should be more than 8 characters in length")

