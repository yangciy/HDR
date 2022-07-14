class Student:
    stuno=0
    stuname=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0
    
    def __init__(self,stuname='',kor=0,eng=0):
        Student.stuno +=1
        self.stuname= stuname
        self.kor=kor
        self.eng=eng
        self.total =kor +eng
        self.avg=self.total/2
        self.rank=0
        
        def __str__(self):
            stuprint='{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,self.stuname,self.kor,self.eng,self.total,self.avg,self.rank)
            return stuprint
        
        def __eq__(self,stuname):
            return self.stuname == stuname
        
        def __lt__(self,other):
            return self.total <other.total
        
        def getKor(self):
            return self.__kor
        
        def setKor(self,kor):
            if kor>=0:
                self.kor=kor
                self.total=kor+self.eng
                self.avg =self.total/2
            else :
                print('잘못입력했어요.')
                
                
        def setEng(self,eng):
            if eng>=0:
                self.eng=eng
                self.total=eng+self.kor
                self.avg =self.total/2
            else :
                print('잘못입력했어요.')
            
            