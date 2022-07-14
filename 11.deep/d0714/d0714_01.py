import sklearn
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras
(train_data,train_label),(test_data,test_label)= keras.datasets.fashion_mnist.load_data()
# train_x,test_x,train_y,test_y=train_test_split()

print(train_data.shape,train_label.shape)