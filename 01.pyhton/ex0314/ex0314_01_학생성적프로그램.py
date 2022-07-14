# 학생성적프로그램
# 번호, 이름, 국어, 영어, 합계, 평균, 등수
stuSave = [[0]*8 for _ in range(10)]
# print(stuSave)

cnt=0
while True:
    print('[ 학생 성적 프로그램 ]')
    print('-'*25)
    print('1. 학생 성적 입력')
    print('2. 학생 성적 수정')
    print('3. 학생 성적 삭제')
    print('0. 프로그램 종료')
    print('-'*25)
    choice = input('원하는 번호를 입력하세요.>>')
  
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        print()
        continue
    choice =int(choice)
    if choice==1 :
        print('학생 성적 입력을 선택하셨습니다.')
        print('=={}번째 학생 등록 =='.format(cnt+1))
        name= input('학생 이름을 입력하세요.>>')
        kor= int(input('국어 성적을 입력하세요.>>'))
        eng= int(input('영어 성적을 입력하세요.>>'))
        math= int(input('수학 성적을 입력하세요.>>'))
        stuSave[cnt][0]=cnt+1
        stuSave[cnt][1]=name
        stuSave[cnt][2]=kor
        stuSave[cnt][3]=eng
        stuSave[cnt][4]=math
        stuSave[cnt][5]=kor+eng+math
        stuSave[cnt][6]=kor+eng+math/3
        stuSave[cnt][7]=0
        cnt+=1
    elif choice==2 :
        print('학생성적수정을 선택하셨습니다.')
    elif choice==3 :
        print('학생성적삭제를 선택하셨습니다.')
    elif choice==0 :
        print('프로그램을 종료합니다.')
        print(stuSave)
        break