import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures, StandardScaler


# df = pd.read_csv('10.mlearn/m0630/perch_full.csv') 
# perch_full = df.to_numpy() #numpy타입으로 변경
# # 무게 데이터 
# perch_weight = np.array(
# [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0, 1000.0]
# )
# df['weight']=perch_weight
# print(df)
# df.to_csv('10.mlearn/m0630/perch_full2.csv',index=False)

df=pd.read_csv('10.mlearn/m0630/perch_full2.csv')

perch_full=df.to_numpy()
