import re
text='123abc456'
re_text = re.sub(r'[^0-9]','',text)
print(re_text)

rate= '후기평점 4.8'

re_rate= re.sub(r'[^0-9.]','',rate)
print(re_rate)