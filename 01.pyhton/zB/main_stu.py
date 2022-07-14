from student.stu_def import *

while True:
    choice = screePrint()
    
    if choice==1:
        setInput()
    elif choice==2:
        stuOutput()
    elif choice==3:
        stuSearch()
    elif choice ==4:
        stuModify()
    elif choice ==5:
        stuDelete()
    elif choice == 6:
        stuRank()
        
    else:
        print('프로그램을 종료합니다.!')
        break
            
    