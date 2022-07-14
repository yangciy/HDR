from datetime import datetime
from django.db import models

class Board(models.Model):
    Z_no = models.AutoField(primary_key=True)
    id = models.CharField(max_length=100)
    Z_title = models.CharField(max_length=1000)
    Z_content = models.TextField()
    Z_group = models.IntegerField(default=0)
    Z_step = models.IntegerField(default=0)
    Z_indent = models.IntegerField(default=0)
    Z_hit = models.IntegerField(default=1)
    Z_createdate =models.DateTimeField(default=datetime.now(),blank=True)
    Z_updatedate = models.DateTimeField(default=datetime.now(),blank=True)
    Z_file = models.ImageField(blank=True)
    
    def __str__(self):
        return self.Z_title
    