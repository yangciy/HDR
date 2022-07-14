import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10

df=pd.read_excel('score.xlsx')
df['합계']=df['국어']+df['영어']+df['수학']+df['사회']+df['과학']
x=df['이름']
y=df['합계']
z=df['국어']
plt.plot(x,y,label='성적',color='red')
plt.bar(x,z,label='국어',color='blue')
plt.legend(loc='upper right')
plt.title('학생성적그래프')
plt.xlabel('이름',loc='right',color='blue')
plt.ylabel('점수',loc='top',color='blue')
plt.yticks([50,100,200,300,400,500])
plt.show()