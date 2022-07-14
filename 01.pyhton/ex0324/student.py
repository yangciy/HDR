class Student:
    stuno=0
    stuname=''
    kor=0
    eng=0
    math=0
    total=0
    avg=0
    rank=0
    def __init__(self,stuno,stuname,kor,eng,math):
        self.stuno=stuno
        self.stuname=stuname
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=(kor+eng+math)/3
    def __str__(self):
        return '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,self.stuname,self.kor,self.eng,self,self.total,self.avg,self.rank)
    def setKor(self,kor):
        if kor>=0:
            self.kor=kor
            self.total=kor+self.eng
            self.avg=self.total/2
        else :
            print('입력값이 잘못되었습니다.')
            
    def getKor(self):
        return self.kor
    
    def setName(self,stuname):
        if stuname.isalpha():
            self.stuname=stuname
        else:
            print('문자만 입력하세요')
        # tempno=0    
        # for name in stuname:
        #     if not name.isdigit():
        #         print('문자만 입력하세요.')
        #         tempno=1
        #         break
        #     else:
        #         self.stuname=stuname
    
# temp={'stuno':cnt,'stuname':name,'kor':kor,'eng':eng,'math':math,'total':kor+eng+math,'avg':(kor+eng+math)/3,'rank':0}
