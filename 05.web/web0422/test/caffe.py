# 카페 프로그램
# 1. 금액충전 ( 1.번 선택시 금액 입력 )
# 2. 1. 아메리카노(hot):2000원 2. 아메리카노(ice):25000원 3. 카페라떼: 4000원
# 1.결제, 2.계속주문 3. 주문취소
from caffedef import *

while True:
    choice= selectMain()
    if choice == 1:
        charge()
       
    elif choice ==2:
        menu()
        
    elif choice ==9:
        print("주문내역")
        for i in orderlist:
            print(i)
        print("-"*30)
        print("프로그램을 종료합니다.")
        break
                
            
