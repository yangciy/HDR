from tensorflow import keras
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['axes.unicode_minus']=False
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.datasets import imdb
import urllib.request

# urllib.request.urlretrieve('https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt',filename='ratings_train.txt')
# urllib.request.urlretrieve('https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt',filename='ratings_test.txt')

train_data= pd.read_table('ratings_train.txt')
test_data= pd.read_table('ratings_test.txt')

# train_data.to_csv('train_data.csv')
# test_data.to_csv('test_data.csv')
# print(train_data)
