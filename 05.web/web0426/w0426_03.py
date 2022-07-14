from selenium import webdriver



options = webdriver.ChromeOptions()
options.headless =True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15")

browser= webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver",options=options)

userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)
txt_userAgent=browser.find_element_by_id("detected_value")
print(txt_userAgent.text)
print(userAgent)