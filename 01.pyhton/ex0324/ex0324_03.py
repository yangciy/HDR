# Car라는 클래스
# color, tire, speed
# c1 객체 선언 후 색상 red, 타이어 , 5개, 속도 100증가, 속도 30 감소

class Car:
    color='white'
    tire=0
    speed=0
    def __init__(self,color,tire,speed):
        self.color= color
        self.tire= tire
        self.speed= speed
    def upSpeed(self,speed):
        self.speed+=speed
    def downSpeed(self,speed):
        self.speed-=speed
    def __str__(self):
        return '색상: {}, 타이어수: {}, 속도: {}'.format(self.color,self.tire,self.speed)
        
c1= Car('red',5,50)
print('색상: ',c1.color)
print('타이어수: ',c1.tire)
c1.upSpeed(100)
print('속도 100 증가: ',c1.speed)
c1.downSpeed(30)
print('속도 30 감소: ',c1.speed)
print('색상: {}, 타이어수: {}, 속도: {}'.format(c1.color,c1.tire,c1.speed))
print(c1)