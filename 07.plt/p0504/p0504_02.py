import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc 
# plt.rc['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='Apple Gothic'
# matplotlib.rcParams['font.family']='Apple Gothic'
rc('font', family='AppleGothic') 			## 이 두 줄을 
plt.rcParams['axes.unicode_minus']=False
x=[1,2,3]
y=[2,4,8]

plt.plot(x,y)
plt.title('졸리다')
plt.show()

# df= pd.read_excel('score.xlsx')
# x=df['지원번호']
# y=df['국어']
# z=df['수학']

# plt.bar(x,y)

# plt.show()