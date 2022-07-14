# 함수 para_func(10,20,30,40,50,60,70,80,90,100)

def para_func(num,*para):
    plist=[]
    para_hap=0
    for i in num:
        para_hap+=i
        plist.append(i)
    # print(para_hap)
    plist.append(para_hap)
    # print(plist)   
    # plist.append(para)
    return plist
blist=[]
while True:
    a= int(input('숫자를 입력하세요.....( 0 입력시 입력 중단..!!)  '))
    if a==0:
        print('매개변수 입력 종료')
        break  
    blist.append(a)
  

alist=para_func(blist)
print('매개변수의 합 :', alist[-1])
print('매개변수 :', alist[0:-1])

# alist[0],alist[1],alist[2],alist[3],alist[4],alist[5],alist[6],alist[7],alist[8],alist[9]



# 매개변수의 개수를 지정하지 않고 전달하는 방법
# def para_func(v1,v2,*para):
#     print('v1: ',v1)
#     print('v2: ',v2)
#     for i in range(len(para)):
#         print('para: ',para[i])
    
#     return

# para_func(1,3,4,5,23,45,2,34,2323423,1235213,553421,52323234,243234,4412,5312,124,451,234,6,6,7,2,34,3,34,14,3125,1)
# print('프 실 완')

# def 함수이름() 함수선언
# (매개변수1, 매개변수2) - 매개변수는 호출개수와 함수선언의 매개변수개수 같아야함
# 매개변수 기본 값 설정, 매개변수에 디폴트 값을 설정할 수 있음. 
# 기본 값 설정이 되어 있는 매개변수는 호출에서 값이 입력되지 않으면 기본값이 세팅이 됨.
# return 개수는 상관없음, 리턴변수는 2개이상일때 튜플타입, 없으면 생략가능

