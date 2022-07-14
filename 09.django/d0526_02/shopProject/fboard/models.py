from datetime import datetime
from django.db import models
from member.models import Member


class Fboard(models.Model):
    f_no = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
    f_title = models.CharField(max_length=1000)
    f_content = models.TextField()
    f_group = models.IntegerField(default=0)
    f_step = models.IntegerField(default=0)
    f_indent = models.IntegerField(default=0)
    f_hit = models.IntegerField(default=1)
    f_createdate =models.DateTimeField(default=datetime.now(),blank=True)
    f_updatedate = models.DateTimeField(default=datetime.now(),blank=True)
    f_file = models.ImageField(blank=True)
    
    def __str__(self):
        return self.f_title


class Comment(models.Model):
    c_no = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member,on_delete=models.DO_NOTHING)
    fboard = models.ForeignKey(Fboard,on_delete=models.CASCADE)
    c_pw = models.CharField(max_length=10,blank=True)
    c_content = models.TextField()
    c_date= models.DateTimeField(default=datetime.now(),blank=True)
    
    
    def __str__(self):
        return self.member