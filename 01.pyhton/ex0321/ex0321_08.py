def cal(v1,v2,v3=1):
    temp=[]
    result1,result2,result3,result4 =0,0,0,0
    result1=v1+v2+v3
    temp.append(result1)
    result2=v1-v2-v3
    temp.append(result2)
    result3=v1*v2*v3
    temp.append(result3)
    result4=v1/v2/v3
    temp.append(result4)
    
    return temp

calList=cal(1,2)
print('더하기 값: {}, 뺴기 값: {}, 곱하기 값: {} , 나누기 값: {} '.format(calList[0],calList[1],calList[2],calList[3]))
print()
calList=cal(20,1,5)
print('더하기 값: {}, 뺴기 값: {}, 곱하기 값: {} , 나누기 값: {} '.format(calList[0],calList[1],calList[2],calList[3]))
print()
calList=cal(100,5)
print('더하기 값: {}, 뺴기 값: {}, 곱하기 값: {} , 나누기 값: {} '.format(calList[0],calList[1],calList[2],calList[3]))



# def para_func(v1,v2,v3=0):   # 매개변수 기본 값
#     result = 0
#     result= v1+v2+v3
#     return result

# result=para_func(1,2,4)
# print(result)

# 함수 내 변수 - 지역변수

# 함수 선언은 def a(매개변수1, 매개변수2):
# return

# 함수 매개변수 개수는 동일, 동일하지 않으면 error

# def cal(v1,v2):
#     return v1
# cal(1,2)

