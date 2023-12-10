import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.express as px
###Inisialisasi data dan pengecekan missing value###
data = pd.read_csv("framingham.csv")
df =  pd.DataFrame(data)
df.isna().sum()
###Penanganan missing value###
df = df.fillna(method='ffill')
df.isna().sum()
###Menghapus beberapa atribut yang bukan data numerik###
kolom_yang_akan_dihapus = ['male','age','education','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabetes','TenYearCHD']
df = df.drop(kolom_yang_akan_dihapus, axis=1)
df = df.sum()
df = df.replace({df[0]:(df[0]/1000),df[1]:(df[1]/1000),df[2]:(df[2]/1000),df[3]:(df[3]/1000),df[4]:(df[4]/1000),df[5]:(df[5]/1000)})
print(df.head(8))
x= df.index
y= df
plt.plot(x, y)
plt.title('Line Chart')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.show()
df = pd.DataFrame({'Attribute':df.index, 'Val':df})
ax = df.plot.bar(x='Attribute', y='Val', rot=0, figsize=(12,8))
plt.figure(figsize = (6, 6))
plt.pie(df['Val'], labels = df['Attribute'], autopct = '%.1f')
plt.show()
data = pd.read_csv("framingham.csv")
df =  pd.DataFrame(data)
df.isna().sum()
df = df.fillna(method='ffill')
kolom_yang_akan_dihapus = ['male','age','education','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabetes','TenYearCHD']
df = df.drop(kolom_yang_akan_dihapus, axis=1)
print(df.head(8))
df.plot(kind='area')
plt.title('area chart')
plt.ylabel('Number of category')
plt.xlabel('Number of patient')
plt.show()
