from django.db import models

class Student(models.Model):
    s_name=models.CharField(max_length=100)
    s_major=models.CharField(max_length=100)
    s_age=models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.s_name
    