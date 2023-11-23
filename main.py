import pandas as pd
import matplotlib.pyplot as ply
import matplotlib as mpl

df1=pd.read_csv("C:\Users\apara\Downloads\archive\car data.csv")
df1.columns = df1.columns.str.upper()
df1.info()

df1.drop('Car_Name', axis=1, inplace=True)
maximum=df1['Year'].max()
Age=df1['Year'].apply(lambda x:(maximum+1)-x)
df1.drop('Year',axis=1,inplace=True)
df1.insert(0,'Age',Age);df1

fig=ply.figure(figsize=(20,15))
fs=mpl.gridspec.GridSpec(2,2)
ax0=fig.add_subplot(fs[0:1,0:1])
ax0.scatter(df1['Age'],df1['Selling_Price'])

ax1=fig.add_subplot(fs[0:1,1:]);
ax1.scatter(df1['Present_Price'],df1['Selling_Price']);

ax2=fig.add_subplot(fs[1:2,0:1]);
ax2.scatter(df1['Kms_Driven'],df1['Selling_Price']);

ax3=fig.add_subplot(fs[1:2,1:]);
ax3.scatter(df1['Owner'],df1['Selling_Price'])