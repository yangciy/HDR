from django.db import models

class Product(models.Model):
    p_no= models.AutoField(primary_key=True)
    p_name= models.CharField(max_length=100)
    p_servings= models.CharField(max_length=100)
    p_unitPrice= models.IntegerField(default=0)
    p_description= models.TextField()
    p_category= models.CharField(max_length=20)
    p_manufacturer= models.CharField(default="CJ",max_length=30)
    p_unit=models.IntegerField(default=100)
    p_filename=models.ImageField(blank=True)
    p_hno= models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.p_name