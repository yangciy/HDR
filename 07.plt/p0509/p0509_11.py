import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
import re
plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

df=pd.read_csv('chipotle.tsv',sep='\t')
# print(df.columns)
df.groupby('item_name')
df['order_id']=df['order_id'].astype(str)

# print(df['order_id'].unique())
item_count= df['item_name'].value_counts()[:10]
# print(item_count)

for i,(i_name,cnt) in enumerate(item_count.iteritems()):
    print('주문 : ',i_name,cnt)
    
order_count =df.groupby('item_name')['order_id'].count()
print(order_count)
item_quantity = df.groupby('item_name')['quantity'].sum()
print(item_quantity)

item_quantity = df.groupby('item_name')['quantity'].sum().sort_values()
print(item_quantity)

df.groupby('order_id')['item_price']

def fun(x):
    x= float(x[1:])
    return x
df['item_price']=df['item_price'].apply(lambda x:float(x[1:]))
print(df['item_price'])