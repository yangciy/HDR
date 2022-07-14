import sklearn
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras
(train_x,train_y),(test_x,test_y)= keras.datasets.fashion_mnist.load_data()


train_scaled = train_x/255.0
test_scaled = test_x/255.0

print(train_scaled.shape)
sc = SGDClassifier(loss='log_loss', max_iter=5, random_state=42)
# early_stopping_cb=keras.callbacks.EarlyStopping(patience=5,restore_best_weight=True)
model=keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100,activation='relu',name='a1'))
# model.add(keras.layers.Dense(100,activation='relu',name='a2'))
model.add(keras.layers.Dense(10,activation='softmax'))
# sparse 원핫인코딩 자동적용
# model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics='accuracy')
# sgd= keras.optimizers.SGD(learning_rate=0.1)
# sgd= keras.optimizers.SGD(momentum=0.9,nesterov=True)
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics='accuracy')
model.fit(train_scaled,train_y,epochs=5)
score= model.evaluate(test_scaled,test_y)
print(score)
print(model.summary())