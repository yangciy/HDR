# import stu_def
from stu_def import *
import json
#화면 출력 구성
#프로그램 무한 반복
#학생성적입력 부분을 구성


# 데이터 최종저장 리스트
while 1:
    choice=0                 # 화면출력 선택번호 변수   
    choice= screen_print()    # 화면출력 함수 호출

    if choice==1:      # 입력
        cnt =stuInput()
    
    elif choice==2:    # 수정
        stuModify()
        
    elif choice==3:    #삭제
        stuDelete()
        
    elif choice==4:    #출력
        stuPrint()
        
    elif choice==5:    #검색 출력
        stuSearch()
        
    elif choice==6:    #순위
        stuRank()
                
    elif choice==0:
        print('프로그램을 종료합니다.')
        break

        # rank=[]
        # avgg=[]
        # avgg1=[]
        # for i , stu in enumerate(stuSave):
        #     print('번호: {}, 평균: {}'.format(i+1,stu['avg']))
        #     avgg.append(stu['avg'])
        #     avgg1.append(stu['avg'])
        #     avgg.sort(reverse=True)
        #     print(avgg)
        # print(avgg)
        # for i in avgg1:
        #     rank.append(avgg.index(i)+1)
        # print(rank)
        # for i , stu in enumerate(stuSave):
        #     stu['rank']=rank[i]