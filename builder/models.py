from django.db import models

# Create your models here.
class Home(models.Model):
    heading_title1=models.CharField(max_length=150,blank=True)
    heading_title2=models.TextField(max_length=150,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    modified_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)