from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=30)
    pdesc=models.TextField(max_length=200)
    pimage=models.ImageField()
    def __str__(self):
        return "%s %s %s"%(self.pname,self.pdesc,self.pimage)

