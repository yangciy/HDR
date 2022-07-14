from random import *
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
rno = randint(0,9)

a=list(words.keys())

# print(list(words.keys()))
rantemp=[]

count=0
while count<5:
    rno =randint(0,9)
    if not a[rno] in rantemp:
        rantemp.append(a[rno])
        count+=1
    
    # a[i],a[rno] = a[rno],a[i]
    
print(rantemp)