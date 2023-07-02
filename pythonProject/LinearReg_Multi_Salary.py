from sklearn.linear_model import LinearRegression
import pandas as pd
import word2num as wn
from word2num import w2n
import matplotlib.pyplot as plt
import math

rg=LinearRegression()
df=pd.read_csv('hiring.csv')

df.loc[df['experience'].isnull(),'experience']='zero'
# Alternate statement : df['experience'].fillna('zero')
for index, value in df.iterrows():
    df.at[index,'experience']=int(wn.word2num(df.at[index, 'experience']))

k=math.floor(df['test_score(out of 10)'].mean())
df.loc[df['test_score(out of 10)'].isnull(),'test_score(out of 10)']=k
print(df.head(50))

rg.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']],df['salary($)'])
print("Prediction",rg.predict([[2,9,6]]))
print("Coefficient are",rg.coef_)
print("Coefficient are",rg.intercept_)

plt.plot(df.experience,df['test_score(out of 10)'],df['interview_score(out of 10)'],df['salary($)'],color='blue')
plt.show()
