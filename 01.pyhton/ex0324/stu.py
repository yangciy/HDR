class Student:
    stuNo=0
    stuName=''
    stuKor=0
    stuEng=0
    stuTotal=0
    stuAvg=0
    stuRank=0
    
    def __init__(self,stuName,stuKor,stuEng):
        # 클래스 변수에서 1 증가해서 자동 입력
        Student.stuNo+=1
        self.stuNo=Student.stuNo
        self.stuName=stuName
        self.stuKor=stuKor
        self.stuEng=stuEng
        self.total=stuKor+stuEng
        self.avg=(stuKor+stuEng)/2
        # 객체를 호출시 자동으로 함수 실행
    def __str__(self):
        return ('{},{},{},{}'.format(self.stuNo,self.stuName,self.stuKor,self.stuEng))
    def setKor(self,stuKor):
        if stuKor>=0:
            self.stuKor=stuKor
            self.total=stuKor+self.stuEng
            self.avg=self.total/2
        else :
            print('입력값이 잘못되었습니다.') 
        # 실행하는 곳이 자신인지 확인
    if __name__ == '__main__':
        print('현재 자신에서 호출되어 실행함. 클래스 이름은'+'Student')
    else :
        print('Student 클래스에서 호출 됨')
        