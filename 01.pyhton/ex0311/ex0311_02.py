import datetime

now = datetime.datetime.now() #시간가져옴
a=now.month
a=a-2
while(a<=12):
    

    if a==12 or a == 1 or a == 2:
        print("{}월은 겨울".format(a))
    elif a==3 or a==4 or a == 5:
        print("{}월은 봄".format(a))
    elif a==6 or a ==7 or a == 8:
        print("{}월은 여름".format(a))
    elif a==9 or a ==10 or a == 11:
        print("{}월은 가을".format(a))
    a=a+1
# a=a-1
# if a==12 or a == 1 or a == 2:
#     print("겨울")
# elif a==3 or a==4 or a == 5:
#     print("봄")
# elif a==6 or a ==7 or a == 8:
#     print("여름")
# elif a==9 or a ==10 or a == 11:
#     print("가을")
# a=now.month
# a=a+3
# if a==12 or a == 1 or a == 2:
#     print("겨울")
# elif a==3 or a==4 or a == 5:
#     print("봄")
# elif a==6 or a ==7 or a == 8:
#     print("여름")
# elif a==9 or a ==10 or a == 11:
#     print("가을")
# a=a+3
# if a==12 or a == 1 or a == 2:
#     print("겨울")
# elif a==3 or a==4 or a == 5:
#     print("봄")
# elif a==6 or a ==7 or a == 8:
#     print("여름")
# elif a==9 or a ==10 or a == 11:
#     print("가을")

# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
