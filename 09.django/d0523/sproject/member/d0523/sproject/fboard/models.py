from datetime import datetime
from django.db import models
from member.models import Member

class Fboard(models.Model):
    fNo=models.AutoField(primary_key=True)
    fmember=models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
    #primary_key=Member 객체 : id 1개의 컬럼으로 받는데 외래키는 Member 객체|객체의 primary_key를 자동으로 읽어서 저장함
    fTitle=models.CharField(max_length=1000)
    fContent=models.TextField()
    fGroup=models.IntegerField(default=0)
    fStep=models.IntegerField(default=0)
    fIndent=models.IntegerField(default=0)
    fHit=models.IntegerField(default=1)
    fCreatedate=models.DateTimeField(default=datetime.now(),blank=True)
    fUpdatedate=models.DateTimeField(default=datetime.now(),blank=True)
    fFile=models.ImageField(blank=True)
    
    def __str__(self):
        return self.fTitle

