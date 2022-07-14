# 학 생 성 적 프 로 그 램
# 3명의 학생의 성적을 입력받아 번호, 이름, 국어, 영어, 합계, 평균, 등수
# 1. 학생성적입력
# 2. 학생파일저장
# 3. 학생파일읽기
# 4. 학생성적모두출력
# [ 학생성적 프로그램 ]
#---------------------
# 원하는 번호를 입력하세요.
# 3명 입력 
# 학생성적모두출력 
# 1명 더 입력 
# 파일 저장 
# 파일 읽기 
# 1명 더 입력
# 모두 출력
# 파일 저장
import os
import json
count=0
score=[]
while True:
    print(' [ 학생 성적 프로그램 ]')
    print('1. 학생성적입력')
    print('2. 학생파일저장')
    print('3. 학생파일읽기')
    print('4. 학생성적모두출력')
    print('-'*30)
    
    num= int(input('원하는 번호를 입력하세요. (0입력시 프로그램 종료)'))
    if num == 1:
        print('학생성적입력을 선택하셨습니다.')
        name= input('학생의 이름을 입력해주세요..>>')
        kor= int(input('국어 점수를 입력하세요. '))
        eng= int(input('영어 점수를 입력하세요. '))
        count+=1
        temp={'num':count,'name':name,'kor':kor,'eng':eng,'total':kor+eng,'avg':(kor+eng)/2,'rank':0}
        score.append(temp)
        
    elif num == 2:
        print('학생파일저장을 선택하셨습니다.')
        json.dump(score,open('학생성적.json','w'))
        # with open('학생성적.txt','a',encoding='utf-8') as file:
        #     file.write('{}'.format(score[0]))
    elif num == 3:
        print('학생파일읽기를 선택하셨습니다.')
        a=json.load(open('학생성적.json'))
        name_s= input('학생의 이름을 입력해주세요..>>')
        for i,stu in enumerate(score):
            if name_s in stu.values:
                print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
                print(stu['sno'],stu['stuname'],stu['kor'],stu['eng'],stu['total'],stu['avg'],stu['rank'],sep='\t')
       
        # with open('학생성적.txt','r',encoding='utf-8') as file:
        #     line =file.readline()
        #     name_d=line.split(',')
        #     for i in name_d:
        #         if name in i:
        #             print(name_d)
        #             break
    elif num == 4:
        print('학생성적모두출력을 선택하셨습니다.')
        a=json.load(open('학생성적.json'))
        
        
        # with open('학생성적.txt','r',encoding='utf-8') as file:
        
        #     while True:
        #         line =file.readline()
        #         if not line:
        #             break
        #         print(line,end='')
        #         print(file.readline())
       
    elif num == 0:
        print('프로그램 종료')
        break