import os

def strFileSave(str1,content):
    if str1 in os.listdir():
        print('{} 파일이 있습니다.'.format(str1))
        str1 =str1[:str1.find('.')]+'_1'+str1[str1.find('.'):]
        with open(str1,'w',encoding='utf-8') as file:
            for i in range(len(content)):
                file.write(content[i])

            file.write('파일이름저장완료')
    else:
        print('중복되는 이름이 없습니다.')    
        with open(str1,'w',encoding='utf-8') as file:
            for i in range(len(content)):
                file.write(content[i])
def strInput(str1,content):
    str1=input('저장 할 파일의 이름을 입력하세요.')
    count=1
    while True:
        temp = input('{}줄'.format(count))
        if temp=='0':
            break
        content.append(temp+'\n')
        count+=1
    return str1

