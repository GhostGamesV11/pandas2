import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#zad1
imiona=pd.ExcelFile("imiona.xlsx")
df=pd.read_excel(imiona, header=0)
print(df)
df1=df.groupby(['Rok'])['Liczba'].sum()
print(df1)
df1.plot()
plt.show()

#zad 2
df2 = df[(df.Plec=='M')]['Liczba'].sum()
df3 = df[(df.Plec=='K')]['Liczba'].sum()
e = ['K','M']
w = [df3, df2]
plt.bar(e,w)
plt.show()


