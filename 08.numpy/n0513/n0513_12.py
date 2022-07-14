import numpy as np
import pandas as pd
countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']
gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

df=pd.DataFrame()
df2=pd.DataFrame()
point=np.array([4,2,1])

df['conturies_name']=countries
df2['gold']=gold
df2['silver']=silver
df2['bronze']=bronze

# arr=np.array([gold,silver,bronze])
arr=np.array(df2)
print(arr.shape)
print(point.shape)
result=np.dot(arr,point)
print(result)
df['gold']=df2['gold']
df['silver']=df2['silver']
df['bronze']=df2['bronze']
df['point']=result
print(df)
df.to_excel('medal.xlsx')