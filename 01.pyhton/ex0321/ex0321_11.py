# def 함수이름() 함수선언
# (매개변수1, 매개변수2) - 매개변수는 호출개수와 함수선언의 매개변수개수 같아야함
# 매개변수 기본 값 설정, 매개변수에 디폴트 값을 설정할 수 있음. 
# 기본 값 설정이 되어 있는 매개변수는 호출에서 값이 입력되지 않으면 기본값이 세팅이 됨.
# return 개수는 상관없음, 리턴변수는 2개이상일때 튜플타입, 없으면 생략가능
# 가변 매개 변수 *para 
# 딕셔너리 가변 매개변수(**para)



def dic_func(**para):
    for k in para.keys():
        print('k,v의 값 : ',k)
    return

dic_func(트와이스=9,소녀시대=7,걸스데이=4,블랙핑크=4)