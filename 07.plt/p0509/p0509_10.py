import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
import re
plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

df=pd.read_csv('chipotle.tsv',sep='\t')
def dol(x):
    dx=float(re.sub(r'[^0-9.]','',x))
    return dx
    
df['price']=df['item_price'].apply(dol)

#1. 가장 주문 많이 한 상품 5개

a=df.groupby('item_name')['quantity'].sum().sort_values(ascending=False).head(5)
print('상위주문5개')
print(a)

#2-1)메뉴의 종류
print('메뉴 종류')
print(df['item_name'].unique())

#2-2)메뉴의 종류 수
print('메뉴 종류 수')
print(df['item_name'].nunique())

#2. 메뉴당 주문자수
print('주문id수')
print(df.groupby('item_name')['order_id'].count())
#2. 메뉴당 주문수량
print('주문량')
print(df.groupby('item_name')['quantity'].sum())
#4. 평균 금액
print(df.groupby('order_id')['price'].mean())

#5. 막대그래프
x=np.arange(50)
y=df.groupby('item_name')['quantity'].sum()
plt.bar(x,y)
print(y)

plt.title('주문량 그래프')
plt.ylabel('주문량')
plt.xlabel('주문번호')
plt.xticks(x,df['item_name'].unique(),rotation=90,size=5)
plt.show()