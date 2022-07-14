from test_sub.stu_def import *
while True:
    #화면출력
    choice = screenPrint()

    if choice==1:
        stuInput()    # 학생성적입력
        
    elif choice == 2:
        stuoutput()   # 학생전체출력 
        
    elif choice == 3:
        stuSearch()   # 학생검색출력 
           
    elif choice == 4:
        stuModify()   # 학생성적수정 
           
    elif choice == 5:
        stuDelete()   # 학생성적삭제 
           
    elif choice == 6:
        sturank()     # 학생등수처리   
        
    else:
        print('프로그램을 종료합니다.!')
        break     