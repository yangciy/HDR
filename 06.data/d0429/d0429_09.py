import pandas as pd

df = pd.read_excel('user.xlsx')
# print(df)
# de시작하는 이름을 검색하시오.
# filt=df['first_name'].str.startswith('De')

# filt=df['first_name'].str.contains('de',case=False)
# print(df[filt])


# langs=['De','de']
# filt=df['first_name'].isin(langs)
# print(df[filt])
# lang=['java','Java','Python','python']
df=pd.read_excel('score.xlsx')
filt=df['SW특기'].str.contains('python',case=False,na=False)
print(df[filt])
# print(df1[df1['SW특기'].isin(lang)])