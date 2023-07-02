import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
import pickle



df=pd.read_excel("Price_House.xlsx",sheet_name='Sheet1')
# print(df.head(30))
# plt.plot(df['Area'],df['Price'])
# plt.xlabel('Area')
# plt.ylabel('Price')
# plt.show()

lrg=linear_model.LinearRegression()
lrg.fit(df[['Area']],df['Price'])
print(lrg.predict([[3300]]))
print("Coefficient or the m in y=mx+b is",lrg.coef_)
print("Intercept or the b in y=mx+b is",lrg.intercept_)

with open('LinearReg_single','wb') as f:
    pickle.dump(lrg,f)

# Scenario is you have Areas mentioned in csv and you need to take the values and predict prices of the house using the model

DF=pd.read_excel('Price_Prediction.xlsx',sheet_name='Sheet1')

if 'Price' in DF.columns:
    for index,price in DF['Price'].items():
        if pd.isnull(price) or price==' ':
            Area=DF.loc[index,'Area']
            print(Area)

            DF.at[index,'Price'] = lrg.predict([[Area]])
else:
    DF['Price'] = lrg.predict(DF[['Area']])

DF['Price']=DF['Price'].apply(lambda x:max(x,0))
print(DF.head(50))
DF.to_excel('Price_Prediction.xlsx',index=None)

filtered_df=DF[DF['Price']>0]
plt.scatter(filtered_df['Area'],filtered_df['Price'],color='blue',marker='+')
plt.plot(filtered_df['Area'],lrg.predict(filtered_df[['Area']]),color='blue',marker='+')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()

# The below code is used to load a model which is linear regression with multiple variable. You need to give
#Area, Bedroom and Age for the model to predict. The model loaded is created in the file LinearReg_Multivariable.py
# We saved the model there in a binary file and here we loaded it as per our requirements

with open('LinearReg_Multi','rb') as f:
    multimodel=pickle.load(f)

print(multimodel.predict([[3000,3,40]]))