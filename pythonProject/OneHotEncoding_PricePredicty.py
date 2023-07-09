# Predict prices if you have township as an extra column, 2 ways either use dummies library or onehotencoding
# Below is using onehotencoding method

import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.linear_model import LinearRegression
rg=LinearRegression()
le=LabelEncoder()
ohe=OneHotEncoder()
# this is done to add those dummy columns for townships
df=pd.read_excel('Township_PricePredict.xlsx')
# This will take the town column and assign labels/numbers to them and assign them back to the town column
print(df.head(50))
X=df[['town','area']].values
# I am coverting my dataframe into array by putting .values  as I want X to be 2D array and not dataframe
Y=df[['price']].values

encode_data=ohe.fit_transform(df[['town']])
# We need to give categorical data that we want unique columns
encoded_array = encode_data.toarray()
# As encode data is a sparse matrix and we need an array to work hence converting it back to array
print(encoded_array)
Df1=pd.DataFrame(encoded_array)
# How to convert an array into data frame, see above, encoded array is a sparse matrix that we need to convert
final=pd.concat([df,Df1],axis=1)
# How to concat two dataframe, see above
final.rename({0:'Monroe',1:'WestWindsor',2:'Robinsville'},axis=1,inplace=True)
# How to rename columns, you can see above

print(final.head(50))
final=final.drop(['town','Monroe'],axis=1)

x=final.drop('price',axis=1)
y=final['price']

print(x.head(50))
print(y.head(50))
rg.fit(x,y)
print(rg.predict([[3700,1,0.0]]))


