from konlpy.tag import Okt

f=open('/Users/uk/Desktop/HDR/book.txt',encoding='utf-8')
book=f.read()

okt=Okt()
word_dic={}
lines=book.split("\r\n")
for line in lines:
    malist = okt.pos(line,norm=True,stem=True)
    for taeso,pumsa in malist:
        if pumsa == 'Noun':
            if not (taeso in word_dic):
                word_dic[taeso]=0
            word_dic[taeso] += 1
            
# 숫자역순정렧
keys = sorted(word_dic.items(),key=lambda x:x[1],reverse=True) # 50개 데이터 정렧
for word,count in keys[:50]:
    print(f"{word}:{count}",end="") 
print()