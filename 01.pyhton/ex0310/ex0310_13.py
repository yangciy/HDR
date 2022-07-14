id='aaa'
pw='1111'

user_id= input('아이디를 입력하세요.>>>')
user_pw= input('패스워드를 입력하세요.>>>')

if id==user_id and pw==user_pw:
    print('로그인 되었습니다.')
else:
    print('아이디나 비밀번호를 확인해주세요.')

# if id==user_id:
#     print('아이디가 같습니다')
#     if pw==user_pw:
#         print('로그인되었습니다.')
#     else:
#         print('비밀번호를 확인해주세요')
# else:
#     print('아이디를 확인해주세요')