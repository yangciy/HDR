from studef import *
while True:
    choice= screenPrint()
    if choice==1:
        stuInput()
    elif choice==2:
        stuOutput()
    elif choice==3:
        stuSearch()
    elif choice==4:
        stuModify()
    elif choice==5:
        stuDel()
    elif choice==6:
        rank()
    elif choice==0:
        print("프로그램 종료")
        break