from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras
import tensorflow as tf




(train_x,train_y),(test_x,test_y)= keras.datasets.fashion_mnist.load_data()

train_s= train_x/255.0
test_s=test_x/255.0


model = keras.Sequential()

model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100,activation='relu'))
model.add(keras.layers.Dropout(0.3))
model.add(keras.layers.Dense(10,activation='softmax'))

model.summary()
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics='accuracy')
with tf.device("/device:CPU:0"):
    history=model.fit(train_s,train_y,epochs=5,validation_data=(test_s,test_y),n_jobs=-1)
# model.save_weights('model_test.h5')

model.save('model_all.h5')
# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss']) 
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.legend(['train','test'])
# # plt.show()
# print("CPU를 사용한 학습")

#     model.fit(train_s,train_y,epochs=5,validation_data=(test_s,test_y))

# print("GPU를 사용한 학습")
# with tf.device("/device:GPU:0"):
#     model.fit(train_s,train_y,epochs=5,validation_data=(test_s,test_y))