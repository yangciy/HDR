import pandas as pd

df = pd.read_excel('user.xlsx')

# df['first_name'].str.lower()
# print(type(df['first_name'].str.lower()))

# gender =['female','male']
# filt=df['gender'].str.lower().isin(gender)
# print(df[filt])

# email bg가 포함되어 있는 단어를 출력하세요

# filt=df['email'].str.endswith('.com')
# filt=df['email'].str.startswith('a',2)
filt=df['email'].str[2].isin(['a'])
print(filt)
print(df[filt])
df[filt].to_excel('aaa.xlsx')
filt=df['email'].str.find('a',2)
print(df[filt==2])
df[filt==2].to_excel('bbb.xlsx')