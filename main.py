import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#zad1
imiona=pd.ExcelFile("imiona.xlsx")
df=pd.read_excel(imiona, header=0)
print(df)
df2=df.groupby(['Rok'])['Liczba'].sum()
print(df2)
df2.plot()
plt.show()
