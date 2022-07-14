import pandas as pd

def add_cm(height):
    if height>=188:
        height= str(height)+'cm'
    else :
        height= str(height)+'센티미터'
    return height

def capChange(word):
    if pd.notnull(word):
        word = word.capitalize()

    return word



df= pd.read_excel('score.xlsx',index_col='지원번호')
# df.fillna('java',inplace=True)
# df['키']=df['키'].apply(add_cm)
# df['SW특기']=df['SW특기'].apply(capChange)
df['국어점수 평가']='F'
print(df)

