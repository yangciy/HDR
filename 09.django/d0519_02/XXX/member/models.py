from datetime import datetime
from django.db import models

class Member(models.Model):
    
    s_no= models.AutoField(primary_key=True)
    s_id = models.CharField(max_length=30)
    s_pw = models.CharField(max_length=100)
    s_name = models.CharField(max_length=100)
    s_tel = models.CharField(max_length=13)
    s_zipcode = models.CharField(max_length=5)
    s_ads1 = models.CharField(max_length=1000)
    s_ads2 = models.CharField(max_length=1000)
    s_date = models.DateTimeField(default=datetime.now(),blank=True)
    
    
    def __str__(self):
        return self.s_id