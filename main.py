import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#zad1
# imiona=pd.ExcelFile("imiona.xlsx")
# df=pd.read_excel(imiona, header=0)
# print(df)
# df1=df.groupby(['Rok'])['Liczba'].sum()
# print(df1)
# df1.plot()
# plt.show()

#zad 2
imiona2=pd.ExcelFile('imiona.xlsx')
df2=pd.read_excel(imiona2, header=0)
grupa=df2.groupby(['Plec']).agg({'Liczba': {'sum'}})
wykres =grupa.plot.bar()
wykres.set_ylabel('Mld')
plt.show()

