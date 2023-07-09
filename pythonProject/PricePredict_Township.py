# Predict prices if you have township as an extra column, 2 ways either use dummies library or onehotencoding
# Below is using dummies method
import pandas as pd
from sklearn.linear_model import LinearRegression
from pandas import get_dummies
pricetown=LinearRegression()
df=pd.read_excel('Township_PricePredict.xlsx')
print(df.head(50))
df1=pd.get_dummies(df['town'],dummy_na=False)
# This step add dummy columns with town as an reference
merge_df=pd.concat([df,df1],axis='columns')
# Next we merged the original df with the dummy columns dataframe
print(merge_df.head(50))
final=merge_df.drop(['town','monroe township'],axis='columns')
print(final.head(50))
# Rule of thumb is if we have have added three dummy columns, delete 1 out of it. If 4, again delete any one out of it
# so we deleted monroe township, we deleted town because we already have a representation by those dummy data added
# Also ML understand numbers so we dropped NA
X=final.drop(['price'],axis='columns')
# X (Independent variable) is all except price, Y is the prediction or the price here(dependent variable)
y=final['price']
pricetown.fit(X,y)
print(pricetown.predict([[2800,1,0]]))
print(pricetown.predict([[3400,0,1]]))
print(pricetown.score(X,y))

