# 은행 대기번호 010
num1 = 1
print(str(num1).zfill(3))

for i in range(10):
    if i==9:
        print(str(i+1).zfill(3), end='')
    else:
        print(str(i+1).zfill(3), end=',')

# str1= '파이썬'
# print(str1.ljust(10,'_'))
# print(str1.rjust(10,'_'))
# print(str1.center(10))
# print('{:10}'.format(str1))

# num1 ='12'
# print(num1.zfill(13))


# map() 타입을 일률적으로 변경
# before = ['2022','3','21']   # list타입 str
# after = list(map(int,before))
# print(before)
# print(after)




# str1= '990101-1105555'
# print(str1.split('-'))
# str2= '나는 바보는 아닙니다는 또 아닙니다는 아닙니다'
# print(str2.split('는'))



# str1 = '1교시 2교시 3교시 4교시'
# a=str1.split()                             # split()  리스트화
# print(type(str1))
# print(a)

# str2= '1교시,2교시,3교시,4교시'
# b=str2.split(',')
# print(b)


# str3= '기준연도,기준월,읍면동,세대수,전체인구,전체인구남,전체인구여,내국인구수,내국인남,내국인여,외국인구수,외국인남,외국인여,연령별소계(내국인),0세,1세,2세,3세,4세,5세,6세,7세,8세,9세,10세,11세,12세,13세,14세,15세,16세,17세,18세,19세,20세,21세,22세,23세,24세,25세,26세,27세,28세,29세,30세,31세,32세,33세,34세,35세,36세,37세,38세,39세,40세,41세,42세,43세,44세,45세,46세,47세,48세,49세,50세,51세,52세,53세,54세,55세,56세,57세,58세,59세,60세,61세,62세,63세,64세,65세,66세,67세,68세,69세,70세,71세,72세,73세,74세,75세,76세,77세,78세,79세,80세,81세,82세,83세,84세,85세,86세,87세,88세,89세,90세,91세,92세,93세,94세,95세,96세,97세,98세,99세,100세,101세,102세,103세,104세,105세,106세,107세,108세,109세,110세이상'
# str3_list= str3.split(',')
# print(str3_list)
# str1 = '      파이           썬         수업'
# str2 =  str1.replace(' ','')
# print(str2)
# print(str1.strip())
# #strip(앞뒤 공백 제거), replace(대체)