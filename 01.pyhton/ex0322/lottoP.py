from random import *
# 로또 번호 생성
def lottoProduce(lottoNum):
    for i in range(45):
        lottoNum.append(i+1)
# 로또 번호 셔플
def lottoSuffle(lottoNum,lotto6):
    for i in range(500):
        randNum= randint(0,44)
        lottoNum[0],lottoNum[randNum] = lottoNum[randNum], lottoNum[0]
    for i in range(6):
        lotto6.append(lottoNum[i])
# 로또 번호입력
def inputNo(lottoInput):
    for i in range(6):
        a=int(input('숫자를 입력하라 '))
        lottoInput.append(a)
# 맞춘 번호

def lottoOf(lottoInput,lotto6,lottoList):
    for i in lottoInput:
        if i in lotto6:
            lottoList.append(i)