from django.db import models

# Create your models here.
class Data(models.Model):
    title=models.CharField(max_length=256,null=True)
    Location1_name=models.CharField(max_length=256,null=True)
    Location2_name=models.CharField(max_length=256,null=True)
    Location3_name=models.CharField(max_length=256,null=True)
    Location4_name=models.CharField(max_length=256,null=True)

    file1=models.FileField(null=True,blank=True)
    file2=models.FileField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        ordering=['title']

    def __str__(self):
        return self.title
