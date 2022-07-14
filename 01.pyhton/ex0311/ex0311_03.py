score = int(input("점수를 입력하세요.>>>>"))
msg=''

msg='합격' if score>=60 else '불합격'
print(msg)  
if score >= 60:
    msg = '합격'
else:
    msg= '불합격'
print(msg)    