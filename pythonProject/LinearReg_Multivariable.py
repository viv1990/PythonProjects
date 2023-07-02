from sklearn.linear_model import LinearRegression
import pandas as pd
import math
import pickle
import numpy as np


rg=LinearRegression()
df=pd.read_excel('LinearReg_Multi.xlsx',sheet_name='Sheet1')
df['Bedroom'].fillna(math.floor(df['Bedroom'].median()),inplace=True)
df.loc[df['Bedroom'].isnull(),'Bedroom']=3
# df['Bedroom].isnull() gives a dataframe with index and True where the value is None , False where we have some value
# putting inside df.loc give the complete dataframe with Area , bedroom (where there is Null), Age and Price
# Next we have given 'Bedroom' as col. indexer where we want to make change and assign it to 0
print(df.head(50))
rg.fit(df[['Area','Bedroom','Age']],df['Price'])

with open('LinearReg_Multi','wb') as f:
    pickle.dump(rg,f)
print("Sample1",rg.predict([[3000,3,40]]))
print("Sample2",rg.predict([[2500,4,5]]))
print("Coefficient are",rg.coef_)
print("Coefficient are",rg.intercept_)
