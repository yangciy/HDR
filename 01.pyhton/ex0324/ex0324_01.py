class Car:        # 클래스명은 대문자, 함수는 소문자
    color="white"
    speed=0
    
    def upSpeed(self,speed):                  #변수 선언한 값 가져옴 self
        self.speed += speed
    def downSpeed(self,speed):
        self.speed -= speed
        
a= Car()        


print('현재속도: ',a.speed)
a.upSpeed(10)
print('현재속도: ',a.speed)
