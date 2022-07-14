from lotto_creat import *

# from random import *
class LottoCreat:
    count=0
    lotto_num=[(i+1 for i in range(45))]
    reward =['0 원','1 만원','100 만원','1000 만원','1 억','10 억']
    lotto=[]
    in_lotto=[]
    in_num=[]
    def lottoCreat(self):
            for i in range(500):
                rno= randint(0,44)
                lotto_num[0], lotto_num[rno] = lotto_num[rno], lotto_num[0]
            lotto =  lotto_num[:6]
            print('당첨 번호 : ',lotto)

        
    def lottoInput():
        for i in range(6):
            temp_num=int(input('로또번호를 입력하세요.'))
            in_num.append(temp_num)
            
    def lottoConfirm():
        for num in in_num:
            if num in lotto:
                in_lotto.append(num)
                
    def lottoOutput():
        print('당첨번호 : ',lotto)
        print('입력번호 : ',in_num)
        print('당첨 개수 : {}개, {}'.format(len(in_lotto),in_lotto))
        print('당첨 금액 :',reward[len(in_lotto)])
          

# lotto_num=[i+1 for i in range(45)]
# reward =['0 원','1 만원','100 만원','1000 만원','1 억','10 억']
# lotto=[]
# in_lotto=[]
# in_num=[]
# lottoSave=[]
# 10

# 몇개 맞음?

# 우선 로또 입력