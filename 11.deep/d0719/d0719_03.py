from tensorflow import keras
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['axes.unicode_minus']=False
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# 데이터 로드

(train_x,train_y),(test_x,test_y)= keras.datasets.fashion_mnist.load_data()

print(train_x[:5])