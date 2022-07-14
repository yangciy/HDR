class Student:
    stuNo=0
    stuName=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0
    
    def __init__(self,stuName='',kor=0,eng=0):
        Student.stuNo +=1
        self.stuNo =Student.stuNo
        self.stuName =stuName
        self.kor =kor
        self.eng =eng
        self.total =kor +eng
        self.avg= self.total/2
        self.rank=0
        
        
    def __str__(self):
        stuprint = '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuNo,self.stuName,self.kor,self.eng,self.total,self.avg,self.rank)
        return stuprint
    
    def __eq__(self,stuName):
        return self.stuName ==stuName
    
    def __lt__(self,other):
        return self.total < other.total
    
    def getKor(self):
        return self.__kor
    
    def setKor(self,kor):
        if kor>=0:
            self.kor=kor
            self.total= kor+self.eng
            self.avg =self.total/2
        else:
            print('입력이 잘못되었습니다.')
            
    def setEng(self,eng):
        if eng>=0:
            self.eng=eng
            self.total = self.kor+eng
            self.avg=self.total/2
            
        else:
            print('입력이 잘못되었습니다.')
    
