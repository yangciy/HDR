class Student:
    stuNo=0
    stuName=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0
    def __init__(self,stuNo,stuName,kor,eng):
        self.stuNo=stuNo
        self.stuName=stuName
        self.kor=kor
        self.eng=eng
        self.total=kor+eng
        self.avg=self.total/2