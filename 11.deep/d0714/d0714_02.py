import sklearn
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras

train=pd.read_csv('/Users/uk/Desktop/HDR/mnist/train.csv')
test=pd.read_csv('/Users/uk/Desktop/HDR/mnist/test.csv')

# def func(a):
#     output=[]
#     for i in a:
#         output.append(float(i)/255)
#     return output
# list(map(func,train.iloc[:,1:].values))

train_x=train.drop(columns='5').to_numpy()
train_y=train['5'].to_numpy()
test_x=test.drop(columns='7').to_numpy()
test_y=test['7'].to_numpy()

train_scaled = train_x/255.0
test_scaled = test_x/255.0

print(train_scaled.shape)
sc = SGDClassifier(loss='log_loss', max_iter=5, random_state=42)
# early_stopping_cb=keras.callbacks.EarlyStopping(patience=5,restore_best_weight=True)
model=keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(784,)))
model.add(keras.layers.Dense(100,activation='relu',name='a1'))
model.add(keras.layers.Dense(100,activation='relu',name='a2'))
model.add(keras.layers.Dense(10,activation='softmax'))
# sparse 원핫인코딩 자동적용
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics='accuracy')
model.fit(train_scaled,train_y,epochs=5)
print(model.summary())
score= model.evaluate(test_scaled,test_y)
print(score)