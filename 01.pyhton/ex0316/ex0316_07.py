words={
    '자동차':'car',
    '의자':'chair',
    '사랑':'love',
    '국수':'noodle',
    '돼지':'pig',
    '호랑이':'tiger',
    '사자':'lion',
    '직업':'job',
    '사과':'apple'
}
words_2={
    '연필':'pencil',
    '자':'ruler',
    '책':'book',
    '양말':'sock',
    '모자':'hat',
    '개':'dog',
    '잠':'sleep',
    '먹다':'eat',
    '읽다':'read',
    '피아노':'piano'
}
# cnt=0
# cnt_f=0
# cnt_list=[]
# cnt_f_list=[]
# flist=[]
while True:
    print('영어단어 수준을 판단해보자')
    print('1. easy')
    print('2. nomal')
    print('0. 프로그램 종료')
    choice= int(input('번호를 선택하세요..> '))

    if choice==1:
        wordlist=[]
        for word in words:
            inwords= input('{}을 영어로 입력하세요.>>> (0입력시 프로그램 종료) '.format(word))
            if inwords.isdigit():
                inwords=int(inwords)
            if words[word]==inwords:
                print('정답입니다. {} : {}'.format(word,words[word]))
                wlist=[inwords,'O',word,words[word]]
                wordlist.append(wlist)
                # cnt+=1
                # cnt_list.append([word,words[word]])
            
            elif inwords==0:
                print('프로그램 종료')
                
            else :
                print('오답입니다. {} : {}'.format(word,words[word]))
                wlist=[inwords,'X',word,words[word]]
                wordlist.append(wlist)
                # flist.append(inwords)
                # cnt_f+=1
                # cnt_f_list.append([word,words[word]])

        ocount, xcount= 0,0
        for idx,wlist in enumerate(wordlist):
            if 'O' in wlist:
                ocount+=1
                print('{}.{}'.format(idx+1,'정답',word,words[word]))
            else:
                xcount+=1
                print('{}.{} {} : {} \t입력값:{}'.format(idx+1,'오답',wlist[2],wlist[3],wlist[0]))
                
        print('정답: {}, 오답: {}, 점수: {}점'.format(ocount,xcount,ocount*10))
    elif choice==2:
        wordlist=[]
        for word in words_2:
            inwords= input('{}을 영어로 입력하세요.>>> (0입력시 프로그램 종료) '.format(word))
            if inwords.isdigit():
                inwords=int(inwords)
            if words_2[word]==inwords:
                print('정답입니다. {} : {}'.format(word,words_2[word]))
                wlist=[inwords,'O',word,words_2[word]]
                wordlist.append(wlist)
                # cnt+=1
                # cnt_list.append([word,words[word]])
            
            elif inwords==0:
                print('프로그램 종료')
                
            else :
                print('오답입니다. {} : {}'.format(word,words_2[word]))
                wlist=[inwords,'X',word,words_2[word]]
                wordlist.append(wlist)
                # flist.append(inwords)
                # cnt_f+=1
                # cnt_f_list.append([word,words[word]])

        ocount, xcount= 0,0
        for idx,wlist in enumerate(wordlist):
            if 'O' in wlist:
                ocount+=1
                print('{}.{}'.format(idx+1,'정답',word,words_2[word]))
            else:
                xcount+=1
                print('{}.{} {} : {} \t입력값:{}'.format(idx+1,'오답',wlist[2],wlist[3],wlist[0]))
                
        print('정답: {}, 오답: {}, 점수: {}점'.format(ocount,xcount,ocount*10))
    
    
    elif choice==0:
        print('프로그램 종료')
        break
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    # print('정답 : {}  오답 : {} 점수 : {}'.format(cnt,cnt_f,cnt*10))
    # if cnt_list==[]:
    #     print('전부 틀렸습니다.')
    # else:
    #     print('맞은 단어 {}, '.format(cnt_list))
    # # for i in cnt_f_list:      
    # #     for j in i:
    # if cnt_f_list==[]:
    #     print("다 맞았습니다!")
    # else:
    #     for i in cnt_f_list:
    #         for j in flist:
    #             print('틀린 단어 {}, 입력단어 {} '.format(i,j))
