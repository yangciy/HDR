import json

data = [
    {'stuno':1, 'stuname':'aaa','kor':100,'eng':100,'total':200,'avg':200/2,'rank':0},
    {'stuno':2, 'stuname':'bbb','kor':100,'eng':100,'total':200,'avg':200/2,'rank':0},
    {'stuno':3, 'stuname':'ccc','kor':100,'eng':100,'total':200,'avg':200/2,'rank':0}
]

# json 파일 저장함수
json.dump(data,open('1.json','w'))
# json 파일 호출함수
data2= json.load(open('1.json'))
print(data2)
print(data2[2])
print(type(data2))






# with open('2.txt','w',encoding='utf-8') as file:
#     for i in data:
#         file.write('{}'.format(data))


# with open('2.txt','r',encoding='utf-8') as file:
#     line=file.readline()
#     print(type(line))
    # print(type(dict(line)))