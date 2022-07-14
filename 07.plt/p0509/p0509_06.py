import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

df=pd.read_excel('score.xlsx')

label=df['이름']
values=df['키']
# values1=df['국어']
# values2=df['영어']

# bar 패턴을 그리기
plt.figure(figsize=(10,5))
bar=plt.bar(label,values)
bar[0].set_hatch('/')
bar[1].set_hatch('|')
bar[2].set_hatch('*')
# plt.barh(label,values2)
# plt.xlim(165,210)
for i, txt in enumerate(values):
    plt.text(i,values[i],txt,ha='center')


plt.show()