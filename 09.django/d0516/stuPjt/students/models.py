from django.db import models

# Student Class 선언
class Student(models.Model):
    s_name = models.CharField(max_length=100) # 문자 (CharField)
    s_major = models.CharField(max_length=100)
    s_age = models.IntegerField(default=0)    # 정수
    s_grage = models.IntegerField(default=0)
    s_gender = models.CharField(max_length=3) # 한글 3byte 영어 2byte
    
    
    def __str__(self):
        return self.s_name