import requests
res=requests.get("https://www.melon.com")
res.raise_for_status() # 코드200이 아니면 프로그램을 자동 종료

# 오류코드 200-정상, 403-권한없음, 404-페이지없음, 50x - 프로그램오류
if res.status_code == requests.codes.ok:
    print('정상')
else:
    print('비정상')
# print(res.text)
print(res.text)

