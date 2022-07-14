a= int(input('숫자를 입력하세요. >>>'))
b= int(input('두번째 숫자를 입력하세요. >>>'))

print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {}'.format(a,b,a/b))

kor= int(input('국어성적을 입력하세요. >>>'))
eng= int(input('영어성적을 입력하세요. >>>'))
math= int(input('수학성적을 입력하세요. >>>'))

print('국어: {} 영어: {} 수학: {} 합계: {} 평균: {:.2f}'.format(kor,eng,math,(kor+eng+math),((kor+eng+math)/3)))

c = int(input('숫자를 입력하세요.>>> '))
d = int(input('두번째 숫자를 입력하세요.>>>'))

print('나눈 값: {} 몫: {} 나머지: {}'.format(c/d,c//d,c%d))
      
    
# a= input('숫자를 입력하세요.>>')
# b= input('두번째 숫자를 입력하세요.>>')

# print(a,'+',b,'=',int(a)+int(b))
# print(a,'-',b,'=',int(a)-int(b))
# print(a,'*',b,'=',int(a)*int(b))
# print(a,'/',b,'=',int(a)/int(b))

# print('{}+{}={}'.format(int(a),int(b),(int(a)+int(b))))
# print('{} / {} = {:.2f}'.format(a,b,int(a)/int(b)))