import json
import os
import student
stuSave=[]
cnt=0
# json 읽기
def jsonRead():
    global stuSave
    if 'stuData.json' in os.listdir():
        stuSave= json.load(open('stuData.json','r'))
    else:
        stuSave=[]
# json 저장
def jsonSave():
    if 'stuData.json' in os.listdir():
        json.dump(stuSave,open('stuData.Json','w'))
    else:
        json.dump(stuSave,open('stuData.Json','w'))
# 카운트
def stuCount():
    global cnt
    cnt = stuSave[-1]['sno']+1
    return cnt
def screen_print():
    jsonRead()
    print(' [ 학생 성적 프로그램 ]')
    print(' 1. 학생 성적 입력')
    print(' 2. 학생 성적 수정')
    print(' 3. 학생 성적 삭제')
    print(' 4. 학생 성적 전체 출력')
    print(' 5. 학생 검색 출력')
    print(' 6. 등수 처리')
    print(' 0. 프로그램 종료')
    print('='*20)
    choice= input('번호를 입력해주세요. ')
    if not choice.isdigit():
        print('숫자만 입력가능합니다.')
    return int(choice)
    # 학생성적입력함수 호출 (sCount, stuSave)
    
def stuInput() :
        jsonRead()
        cnt=stuCount()
        print('학생 성적 입력을 선택하셨습니다.')
        print('{}번째 학생의 성적을 입력해주세요.'.format(cnt))
        name= input('이름을 입력해주세요.  ')
        kor= int(input('국어 성적을 입력해주세요.  '))
        eng= int(input('영어 성적을 입력해주세요.  '))
        math= int(input('수학 성적을 입력해주세요.  '))
        # temp=student.Student(cnt,name,kor,eng,math)
        temp={'sno':cnt,'stuname':name,'kor':kor,'eng':eng,'math':math,'total':kor+eng+math,'avg':(kor+eng+math)/3,'rank':0}
        # Student객체 저장
        # stuSave.append(student.Student(cnt,name,kor,eng,math))
        stuSave.append(temp)
        # if not 'stuData.json' in os.listdir():
        jsonSave()
        # else:
        #     json.dump(stuSave,open('stuData.json','a'))
        cnt+=1
        return cnt
    # 학생성적수정함수 호출 (stuSave)
    
def stuModify():
    count=0
    jsonRead()
    print('[ 학생 성적 수정페이지 ]')
    print('='*50)
    name_r=input('수정할 학생의 이름을 입력해주세요.  ')
    for i,stu in enumerate(stuSave):
        if name_r in stu.values():
            print('{} 학생이 존재합니다.'.format(name_r))
            count=1
            choice = input('수정할 과목을 입력하세요.>> (0입력시 메인메뉴로 돌아갑니다.)\n')
            if choice=='0':
                int(choice)
                break
            if choice == '국어':
                print('현재 국어점수 : ',stu['kor'])
                kor= int(input('변경할 국어 성적을 입력해주세요.  '))
                stu['kor']=kor
                stu['total']=stu['kor']+stu['eng']+stu['math']
                stu['avg']=stu['total']/3
                jsonSave()
            elif choice == '영어':
                print('현재 영어 점수 : ',stu['eng'])
                eng= int(input('영어 성적을 입력해주세요.  '))
                stu['eng']=eng
                stu['total']=stu['kor']+stu['eng']+stu['math']
                stu['avg']=stu['total']/3
                jsonSave()
            elif choice == '수학':
                print('현재 수학 점수 : ',stu['math'])
                math= int(input('수학 성적을 입력해주세요.  '))
                stu['math']=math
                stu['total']=stu['kor']+stu['eng']+stu['math']
                stu['avg']=stu['total']/3
                jsonSave()
            else :
                print('잘못 입력하셨습니다. 다시 입력해주세요.')
                continue                
            break
    if count==0:   
        print('{} 학생이 없습니다.'.format(name_r))
        
def stuDelete():
    count=0
    jsonRead()
    print('학생 성적 삭제를 선택하셨습니다.')
    name_d=input('삭제할 학생의 이름 입력해주세요.  ')
    for i,stu in enumerate(stuSave):
        if name_d in stu.values():
            del(stuSave[i])
            print('{} 학생이 삭제되었습니다.'.format(name_d))
            count=1
            jsonSave()  # 수정파일저장
            break
    if count==0:   
        print('{} 학생이 없습니다.'.format(name_d))
        
# 학생성적 전체출력
def stuPrint():
    jsonRead()
    print('학생 성적 전체 출력을 선택하셨습니다.')
    print('='*65)
    # print('{:5s}{:5s}{:5s}{:5s}{:5s}{:5s}{:.5s}{:.5s}'.format('번호','이름','국어','영어','수학','합계','평균','등수'))
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
    print('='*65)
    for i in stuSave:
        for k,v in i.items():
            # print(j,end='\t')
            print('{}\t'.format(v),end='')
        print()  
        print('='*65)  
        
# 학생 검색 출력
def stuSearch():
    jsonRead()
    print('학생 검색 출력을 선택하셨습니다.')
    print('='*65)
    name_s=input('검색할 학생의 이름을 입력하세요.')
    count=0
    for i,stu in enumerate(stuSave):
        if name_s in stu.values():
            print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
            print(stu['sno'],stu['stuname'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg'],stu['rank'],sep='\t')
            count=1
            break
        if count==0:
            print('입력한 학생이 없습니다. 다시 검색해주세요')
# 학생 등수 처리
def stuRank():
    jsonRead()
    print('등수 처리를 선택하셨습니다.')
        
    for stu in stuSave:
        rcount=1
        for stu2 in stuSave:
            if stu['total']<stu2['total']:            
                rcount +=1
        stu['rank']=rcount
    print('등수 처리가 완료되었습니다.')
    jsonSave()