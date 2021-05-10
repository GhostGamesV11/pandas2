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
# imiona2=pd.ExcelFile('imiona.xlsx')
# df2=pd.read_excel(imiona2, header=0)
# grupa=df2.groupby(['Plec']).agg({'Liczba': {'sum'}})
# wykres =grupa.plot.bar()
# wykres.set_ylabel('Mld')
# plt.show()

#zad 3
imiona3=pd.ExcelFile('imiona.xlsx')
df3=pd.read_excel(imiona3, header=0)
grupa = df3.where(df3['Rok'] > 2012).groupby(['Plec']).agg({'Liczba': {'sum'}})
wykres = grupa.plot.pie(subplots=True,autopct='%.2f %%',fontsize=20,figsize=(6,6),legend=(0,0))
plt.legend(loc='lower right')
plt.title('Suma')
plt.show()