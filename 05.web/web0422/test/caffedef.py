money=[0]
orderlist=[]
def selectMain():
    print("1.금액충전  2.메뉴 9.종료")
    select= int(input("원하는 기능을 선택해주세요.>> "))
    return select
def charge():
    
    while True:
        print("금액충전을 선택하셨습니다.")
        charge= int(input("원하는 충전금액을 입력해주세요."))
        print("{}원을 입력하셨습니다.".format(charge))
        money[0]=money[0]+charge
        print("충전 후 금액은 {}원 입니다.".format(money[0]))
        
        return money[0]
def menu():
    while True:
        print("1.아메리카노(hot) 2000원 2.아메리카노(ice) 2500원 3.카페라떼 4000원")
        want=int(input('원하는 메뉴를 선택하세요.>>'))
        if want==1:
            print("아메리카노(hot)를 선택하셨습니다.")
            name="아메리카노(hot)"
            price=2000
            if money[0]-price<0:
                print("1.금액충전이동 2.주문 취소")
                waring=int(input("잔액이 부족합니다. 금액을 충전하시겠습니까?1.금액충전이동 2.상위로 이동 3.주문 취소 \n" ))
                if waring==1:
                    print('금액 충전으로 이동')
                    break
                elif waring==2:
                    print("주문취소되었습니다. {}:{}원이 반환되었습니다.".format(name,price))
                    break
            else:
                money[0]=money[0]-price
                print('결제 후 잔액은 {}'.format(money[0]))
                flag=int(input("1.계속 주문  2.주문 취소"))
                orderlist.append(name)
                if flag==1:
                    print('계속 주문')
                elif flag==2:
                    print("주문 취소")
                    break
        elif want==2:
            print("아메리카노(ice)를 선택하셨습니다.")
            name="아메리카노(ice)"
            price=2500
            if money[0]-price<0:
                waring=int(input("잔액이 부족합니다. 금액을 충전하시겠습니까?1.금액충전이동 2.상위로 이동 3.주문 취소 \n" ))
    
                if waring==1:
                    print('금액 충전으로 이동')
                    break
                elif waring==2:
                    print("주문취소되었습니다. {}:{}원이 반환되었습니다.".format(name,price))
                    break

            else:
                money[0]=money[0]-price
                print('결제 후 잔액은 {}'.format(money[0]))
                flag=int(input("1.계속 주문  2.주문 취소"))
                orderlist.append(name)                
                if flag==1:
                    print('계속 주문')
                elif flag==2:
                    print("주문 취소")
                    break
        elif want==3:
            print("카페라떼를 선택하셨습니다.")
            name="카페라떼"
            price=4000
            if money[0]-price<0:
                waring=int(input("잔액이 부족합니다. 금액을 충전하시겠습니까?1.금액충전이동 2.상위로 이동 3.주문 취소 \n" ))
                if waring==1:
                    print('금액 충전으로 이동')
                    break
                elif waring==2:
                    print("주문취소되었습니다. {}:{}원이 반환되었습니다.".format(name,price))
                    break
            else:
                money[0]=money[0]-price
                print('결제 후 잔액은 {}'.format(money[0]))
                orderlist.append(name)
                flag=int(input("1.계속 주문  2.주문 취소"))
                if flag==1:
                    print('계속 주문')
                elif flag==2:
                    print("주문 취소")
                    break

