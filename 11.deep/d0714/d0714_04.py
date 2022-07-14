import sklearn
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras
(train_x,train_y),(test_x,test_y)= keras.datasets.fashion_mnist.load_data()

train_s= train_x/255.0
test_s=test_x/255.0


model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100,activation='relu'))
model.add(keras.layers.Dense(10,activation='softmax'))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics='accuracy')
history=model.fit(train_s,train_y,validation_data=(test_s,test_y),epochs=20)
print(history.history['loss'])
print(history.history['accuracy'])

plt.plot(history.history['loss'])
plt.plot(history.history['accuracy'])
plt.show()

plt.plot(history.history['val_loss'])
plt.plot(history.history['val_accuracy'])
plt.show()