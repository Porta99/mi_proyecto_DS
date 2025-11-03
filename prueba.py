import pandas as pd

lista=[1,4,5,3,6,2,8,9,0,22,43,65,34,12,32,64,76]

df= pd.DataFrame(lista,columns=['datos'])
print(df.describe())
