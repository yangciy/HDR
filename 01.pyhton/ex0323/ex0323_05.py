from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

rs = request.urlopen('https://www.naver.com')
print(rs.read())


# import time
# print('프로그램 시작')
# print('cat은 무슨 뜻 일까요?')
# time.sleep(5)
# print('고양이 입니다.')