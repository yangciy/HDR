import requests

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
# res= requests.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
res=requests.get("https://www.melon.com",headers=headers)
res.raise_for_status()
with open("melon.html","w",encoding="utf-8") as f:
    f.write(res.text)
print(res.text)