import re
import pandas as pd
import spacy
import openpyxl
chat1="Hey customer service, my order id is 181818118 and is not deleivered. My phone no is this 9892281996\
and my alternate number is 8887788878. Also my email id is shys878_TR@gmail.com"
chat2="You people just find my order with order:772727777 and order id:888938338. My phone number is (123)-292-9292. My email id is vivek.124S@ai.io"

pattern='\d{9}'
email_pattern='[a-zA-Z0-9_.]*@[a-zA-Z]*\.[a-zA-Z]*'
phoneno_pattern='\d{10}|\(\d{3}\)-\d{3}-\d{4}'
orders='order[^\d]*(\d*)'

text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''


# Funda of enclosing group used here. First extract information on orders and then from those order details,
# extract order number

def findpattern(pattern,text):
    match1=re.findall(pattern,text)
    return match1



pattern1='https:\/\/twitter.com\/([^,\n]*)'
pattern2='FY(\d{4}.*?\d)'
# Refer this link: https://stackoverflow.com/questions/3075130/what-is-the-difference-between-and-regular-expressions
print("Order ID are \n",findpattern(pattern,chat1))
print(findpattern(pattern,chat2))
print("EMail Patterns are \n",findpattern(email_pattern,chat1))
print(findpattern(email_pattern,chat2))
print("PhoneNumber Patterns are\n",findpattern(phoneno_pattern,chat1))
print(findpattern(phoneno_pattern,chat2))
print("Twitter Handles are",findpattern(pattern1,text))
print("Quarterly and SemiAnnual Reporting periods are",findpattern(pattern2,text))

# using pandas on an excel to extract email address
File=pd.read_excel("Book1.xlsx",sheet_name='Sheet1')
print(File.head(50))

for col in File.columns:
    for cell in File[col]:
        print(cell)

# using spacy on a text file to extract email address
with open("Text_Spacy.txt") as f:
    file1=f.read()

print(file1)

nlp=spacy.blank('en')
# This is a blank pipeline which means it just has a tokeniser, to add anything you need to use ORTH, add_pipepline functions
# Trained pipelines which we used like spacy.load("en_web_core") have lot more than tokenisers, they are intelligent
# They have parsers, etc.
doc1=nlp(file1)
email_addr=[]
for token in doc1:
    if token.like_email:
        email_addr.append(token)

print(email_addr)

# Exercises, Extract URL and all money transactions
text2='''
Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.
'''
pattern5 = 'https?:\/\/[^\s\/]*(?:\/[^\s,.]*)?'
matches = re.findall(pattern5, text2.replace('\n',''))
print(matches)
# nlp1=spacy.blank('en')
# doc=nlp1(text2)
# url=[]
#
# for token in doc:
#     print(token)
#     if token.like_url:
#         url.append(token)
#
# print(url)



