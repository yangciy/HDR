from konlpy.tag import Okt


okt=Okt()

text='한글 자연어처리는 재밌냐. 이제부터 재밌냐 ㅋㅋㅋㅎㅋㅎㅋㅎㅋㅎㅋㅎ'

# 텍스트 단위
print(okt.morphs(text))
# 명사만 추출
print(okt.nouns(text))
# 어절단위로 추출
print(okt.phrases(text))
# 품사도 함께 추출(튜플)
print(okt.pos(text))
# 품사와 함께 추출
print(okt.pos(text,join=True))