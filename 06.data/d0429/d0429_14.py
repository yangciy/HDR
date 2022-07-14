import pandas as pd
import numpy as np

# df=pd.read_excel('시가총액1-200.xlsx')
# print(df.sort_values('종목명'))
df=pd.read_excel('user.xlsx')
# print(df.sort_values('first_name',ascending=False))
print(df.sort_values(['gender','first_name'],ascending=[True,False]))
