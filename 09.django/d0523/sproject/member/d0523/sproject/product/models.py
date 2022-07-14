from django.db import models

class Product(models.Model):
    pNo=models.AutoField(primary_key=True)
    pName=models.CharField(max_length=100)
    pServing=models.CharField(max_length=100)
    pUnitPrice=models.IntegerField(default=0,max_length=10)
    pDescription=models.TextField()
    pCategory=models.CharField(max_length=20)
    pManufacturer=models.CharField(max_length=20)
    pUnit=models.IntegerField(default=20)
    pFileName=models.ImageField(blank=True)
    
    def __str__(self):
        return self.pName