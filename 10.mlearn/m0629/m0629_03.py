from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


df=pd.read_csv('mushroom.csv')
data= df[[ 'cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment',\
        'gill-spacing','gill-size','gill-color','stalk-shape','stalk-root','stalk-surface-above-ring',\
        'stalk-surface-below-ring','stalk-color-above-ring','stalk-color-below-ring',\
        'veil-type','veil-color','ring-number','ring-type','spore-print-color','population','habitat']]
label= df['poisonous']


data_a = []
for i in range(len(data)):
    row_data=[]
    for v in range(len(data.iloc[i])):
        row_data.append(ord(data.iloc[i,v]))
    data_a.append(row_data)

data=data_a
print(data)







# data=[]
# label=[]
# attr_list=[]

# for index,rows in df.iterrows():
#     label.append(rows[0])
#     row_data=[]
#     for v in rows[1:]:
#         row_data.append(ord(v))
#     data.append(row_data)
# # print(data[0])

# train_x,test_x,train_y,test_y= train_test_split(data,label)

# clf=KNeighborsClassifier(n_neighbors=3)
# clf.fit(train_x,train_y)
# pred=clf.predict(test_x)
# score=clf.score(test_x,test_y)

# print(pred)
# print(score)