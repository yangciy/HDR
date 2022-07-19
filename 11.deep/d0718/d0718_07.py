from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParms['axes.unicode_minus']=False
from sklearn.model_selection import train_test_split


(train_data,train_label),(test_data,test_label)= keras.datasets.imdb.load_data(num_words=500)
# print(train_data[5])

# from keras.preprocessing.sequence import pad_sequences
train_seq= keras.preprocessing.sequence.pad_sequences(train_data,maxlen=100)
print(train_seq.shape)

model = keras.Sequential()
model.add(keras.layers.Embedding(500,16,input_length=100))
model.add(keras.layers.SeimpleRNN(8))
model.add(keras.layers.Dense(1,activation='sigmoid'))