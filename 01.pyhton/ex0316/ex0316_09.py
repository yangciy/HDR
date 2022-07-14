words={
    '자동차':'car',
    '의자':'chair',
    '사랑':'love',
    '국수':'noodle',
    '돼지':'pig',
    '호랑이':'tiger',
    '사자':'lion',
    '직업':'job',
    '사과':'apple',
    '여우':'fox'
}
words_2={
    '연필':'pencil',
    '자':'ruler',
    '책':'book',
    '양말':'sock',
    '모자':'hat',
    '개':'dog',
    '잠':'sleep',
    '먹다':'eat',
    '읽다':'read',
    '피아노':'piano'
}

# total_list=[키]
# words 5개,
# words_2 5개


# list(words.items())= (key ,value) 가져옴


from random import *
total_list=[]
totalV_list=[]
atemp=[]
atemp1=[]
btemp=[]
btemp1=[]
a=list(words.items())
aV=list(words.values())

# print(a)
b=list(words_2.items())
bV=list(words_2.values())
# print(b)
num=int(input('비율을 정할 숫자를 입력하세요.. >'))
# a에서 n개
count=0
while count < num:
    rdn= randint(0,9)
    if not a[rdn] in atemp:
        atemp.append(a[rdn])
        # atempV.append(aV[rdn])
        count+=1
print(atemp)        
for i in range(num):
    total_list.append(atemp[i])
    # totalV_list.append(atempV[i])
# b에서 10-n개
count=0
while count < 10-num:
    rdn= randint(0,9)
    if not b[rdn] in btemp:
        btemp.append(b[rdn])
    else :
        continue
       # btempV.append(bV[rdn])
    count+=1   
print(btemp)       

for i in range(10-num):
    total_list.append(btemp[i])        
    # totalV_list.append(btempV[i])
print(total_list)        
# print(totalV_list)

# value값을 가져오세요
tdic=dict(total_list)
print(tdic)
    

# stu1['kor']=100