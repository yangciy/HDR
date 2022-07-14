import lottoP
# def lottoProduce(lottoNum):
#     for i in range(45):
#         lottoNum.append(i+1)


# 프로그램 시작
lottoNum=[]
lotto6=[]
lottoInput=[]
lottoList=[]
lottoP.lottoProduce(lottoNum)                     #로또번호 생성
lottoP.lottoSuffle(lottoNum,lotto6)               #로또 섞기
lottoP.inputNo(lottoInput)                        #로또번호 입력
lottoP.lottoOf(lotto6, lottoInput,lottoList)      #로또번호 비교
print('당첨 번호 :',lotto6)
print('입력 번호 :',lottoInput)
print('맞춘 번호: ',lottoList)
print('맞춘 개수: ',len(lottoList))
# print(lottoNum)

