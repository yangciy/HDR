import sklearn
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras
import tensorflow as tf


df=pd.read_csv('./bmi.csv')
one_encording = pd.get_dummies(df['label'])
df= df.join(one_encording)
print(df.describe())
print(df.columns)
train=df[['height', 'weight']]
test=df[['fat', 'normal', 'thin']]
# print(test)
# Train test
train_x,test_x,train_y,test_y=train_test_split(train,test)
# 정규화
train['height']=train['height']/200
train['weight']=train['weight']/100
# print(train_x.shape,train_y.shape)
print(test_x.shape,test_y.shape)

model=keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(2,)))
model.add(keras.layers.Dense(512,activation='relu'))
# model.add(keras.layers.Dense(256,activation='relu'))
model.add(keras.layers.Dense(128,activation='relu'))
# model.add(keras.layers.Dense(64,activation='relu'))
# model.add(keras.layers.Dense(32,activation='relu'))
# model.add(keras.layers.Dense(16,activation='relu'))
# model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(3,activation='softmax'))
model.summary()
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics='accuracy')
checkpoint_cb= keras.callbacks.ModelCheckpoint('best-model.h5')
early_stopping_cb= keras.callbacks.EarlyStopping(patience=3,restore_best_weights=True)
history=model.fit(train_x,train_y,epochs=50,validation_data=(test_x,test_y),callbacks=[checkpoint_cb,early_stopping_cb])
print('epoch 진행수: ',early_stopping_cb.stopped_epoch+1)
model.save('model_all.h5')
score= model.evaluate(test_x,test_y)
print(score)
pred=model.predict([[141,64]])
val_labels= np.argmax(model.predict([[0.91,0.79]]))
val_labels2= np.argmax(model.predict([[0.68,0.63]]))
val_labels3= np.argmax(model.predict([[0.82,0.75]]))
print('결과: ',val_labels)
print('결과2: ',val_labels2)
print('결과3: ',val_labels3)
print('141,64는 : ',pred)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train','test'])
plt.show()
# /141,64는 :  [[9.992562e-01 7.437427e-04 4.212101e-08]]