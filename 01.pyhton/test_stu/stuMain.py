from studentDef import *

while True:
    
    choice = screenPrint()
    
    if choice ==1:
        stuInput()
    elif choice ==2:
        stuOutput()
    elif choice ==3:
        stuSearch()
    elif choice ==4:
        stuModify()
    elif choice== 5:
        stuDelete()
    elif choice== 6:
        stuRank()
    else:
        print('프로그램을 종료합니다.')
        break