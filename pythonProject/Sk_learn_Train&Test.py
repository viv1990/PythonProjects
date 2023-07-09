from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression
Lr=LinearRegression()
df=pd.read_excel('CarModel_price.xlsx')

DummyDF=pd.get_dummies(df['Car Model'])

Merged_DF=pd.concat([df,DummyDF],axis=1)
print(Merged_DF.head(50))

X=Merged_DF.drop(['Sell Price($)','Audi A5','Car Model'],axis=1)
Y=Merged_DF['Sell Price($)']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=10)
Lr.fit(X_train,Y_train)
print(Lr.predict(X_test))
print(Y_test)
print(Lr.score(X_test,Y_test))



