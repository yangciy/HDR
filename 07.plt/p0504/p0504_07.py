import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=8

df=pd.read_excel('movie.xlsx')
print(df)
x=df['영화']
y=df['평점']
plt.title('영화 관객수',size=14)
plt.plot(x,y,'ko-',ms=5,mec='w',mfc='g',label='평점',linewidth=2)
plt.legend(loc='upper right')
plt.xlabel('제목')
plt.ylabel('평점')
plt.show()