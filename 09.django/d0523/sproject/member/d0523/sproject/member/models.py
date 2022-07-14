from django.db import models
from datetime import datetime

class Member(models.Model):
    mId=models.CharField(max_length=30,primary_key=True)
    mPw=models.CharField(max_length=300)
    mName=models.CharField(max_length=100)
    mNickname=models.CharField(max_length=100)
    mTel=models.CharField(max_length=13,blank=True)
    mzipcode = models.CharField(max_length=6,blank=True)
    maddress1 = models.CharField(max_length=300,blank=True)
    maddress2 = models.CharField(max_length=300,blank=True)
    mgender = models.CharField(max_length=10,default='남자')
    mhobby = models.CharField(max_length=100,blank=True)
    mCreatedate = models.DateTimeField(default=datetime.now(),blank=True)
    mUpdatedate = models.DateTimeField(default=datetime.now(),blank=True)
    
    def __str__(self):
        return self.mId