def selectMain():
    print("1.금액충전  2.메뉴 9.종료")
    select= int(input("원하는 기능을 선택해주세요.>> "))
def charge():
    
    while True:
        print("금액충전을 선택하셨습니다.")
        charge= int(input("원하는 충전금액을 입력해주세요."))
        print("{}원을 입력하셨습니다.".format(charge))
        money[0]=money[0]+charge
        print("충전 후 금액은 {}원 입니다.".format(money[0]))
        break
# def menu():
def exit():
    print("프로그램을 종료합니다.")
    break
                