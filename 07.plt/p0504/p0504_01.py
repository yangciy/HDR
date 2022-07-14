import pandas as pd
import matplotlib.pyplot as plt

x=[1,2,3]
y=[2,4,8]

df= pd.read_excel('score.xlsx')
x=df['지원번호']
y=df['국어']
z=df['수학']
# print(df.iloc[4])
plt.bar(x,y)
plt.plot(x,z)
plt.show()