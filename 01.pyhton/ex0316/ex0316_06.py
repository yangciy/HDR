foods={
    '떡볶이':'오뎅',
    '짜장면':'단무지',
    '라면':'김치',
    '피자':'피클',
    '맥주':'땅콩',
    '치킨':'치킨무',
    '삼겹살':'상추'        
}

    # print(foods.keys())
while 1:
    input1=input('원하는 음식을 입력하세요\n(숫자 0입력시 프로그램이 종료됩니다.)\n')
    if input1.isdigit():
        input1=int(input1)
   
   
    if input1 in foods:
        print('{}와 어울리는 음식은 {} 입니다.'.format(input1,foods[input1]))
        
    elif input1==0:
        print('프로그램 종료')
        break
    else:
        print('{}에 대한 정보가 없습니다.'.format(input1))