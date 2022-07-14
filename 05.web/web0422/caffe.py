# 카페 프로그램
# 1. 금액충전 ( 1.번 선택시 금액 입력 )
# 2. 1. 아메리카노(hot):2000원 2. 아메리카노(ice):25000원 3. 카페라떼: 4000원
# 1.결제, 2.계속주문 3. 주문취소
from w0422.caffedef import *
money=[0]
while True:
    select= selectMain()
    if select == 1:
        while True:
            print("금액충전을 선택하셨습니다.")
            charge= int(input("원하는 충전금액을 입력해주세요."))
            print("{}원을 입력하셨습니다.".format(charge))
            money[0]=money[0]+charge
            print("충전 후 금액은 {}원 입니다.".format(money[0]))
            break
    elif select ==2:
        while True:
            print("1.아메리카노(hot) 2000원 2.아메리카노(ice) 2500원 3.카페라떼 4000원")
            want=int(input('원하는 메뉴를 선택하세요.>>'))
            if want==1:
                print("아메리카노(hot)를 선택하셨습니다.")
                if money[0]-2000<0:
                    print("1.금액충전이동 2.상위로 이동 3.주문 취소")
                    waring=int(input("잔액이 부족합니다. 금액을 충전하시겠습니까?1.금액충전이동 2.상위로 이동 3.주문 취소 \n" ))
                    if waring==1:
                        print('금액 충전으로 이동')
                        break
                    elif waring==2:
                        print("상위로 이동")
                        break
                    elif waring==3:
                        print("주문취소")
                        break
            elif want==2:
                print("아메리카노(ice)를 선택하셨습니다.")
                if money[0]-2500<0:
                    waring=int(input("잔액이 부족합니다. 금액을 충전하시겠습니까?1.금액충전이동 2.상위로 이동 3.주문 취소 \n" ))
        
                    if waring==1:
                        print('금액 충전으로 이동')
                        break
                    elif waring==2:
                        print("상위로 이동")
                        break
                    elif waring==3:
                        print("주문취소")
                        break
            elif want==3:
                print("카페라떼를 선택하셨습니다.")
                if money[0]-4000<0:
                    waring=int(input("잔액이 부족합니다. 금액을 충전하시겠습니까?1.금액충전이동 2.상위로 이동 3.주문 취소 \n" ))
                    if waring==1:
                        print('금액 충전으로 이동')
                        break
                    elif waring==2:
                        print("상위로 이동")
                        break
                    elif waring==3:
                        print("주문취소")
                        break
    elif select ==9:
        print("프로그램을 종료합니다.")
        break
                
            
