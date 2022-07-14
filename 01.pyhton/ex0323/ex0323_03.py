import json


list = [1,2,3,4,10]

data= json.load(open('stuData.json','r'))

print(data[-1]['sno'])