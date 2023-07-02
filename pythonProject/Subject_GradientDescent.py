import pandas as pd
import numpy as np
from Gradient_Descent import gradient_descent

df=pd.read_excel('Exercise_SubjectCorr.xlsx')
print(df.head(50))
x=np.array(df['Math'])
y=np.array(df['CS'])
print(x)
print(y)
gradient_descent(x,y)
