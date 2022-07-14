# 입력된 문자의 첫글자가 대문자인지 

str= input('입력하세요')

# if str[0].isupper():
#     print('대문자입니다.')
# else:
#     print('대문자가 아닙니다.')

if str.startswith('>>'):
    print('>>로 시작합니다.')
    print(str)
else:
    print('>>가 없습니다.')
    str='>>'+str
    print(str)