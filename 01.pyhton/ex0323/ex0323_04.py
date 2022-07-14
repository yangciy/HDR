import datetime
now= datetime.datetime.now()
year = now.year
month = now.month*10
day =now.day
hour = now.hour
minute = now.minute
second = now.second
print('{}-{:02d}-{}   {}:{}:{}'.format(year,month,day,hour,minute,second))

print(now)
# print(dir(datetime))
# stuSave=[]
# stuname= input('이름을 입력하세요.')
# now = datetime.datetime.now()
# print(now)
# temp={'stuname':stuname,'inputTime':'{}-{:02d}-{}'.format(now.year,now.month,now.day)}
# stuSave.append(temp)
# print(stuSave)