import pandas as pd
lista= [1,2,3,4,56,8,9,7,78,56,45,35,765,345,34,2]

list= pd.Series(lista).describe()
print(list)

