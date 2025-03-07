from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(null=True,blank=True)
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=70)

    def __str__(self):
        return self.name
    
class Result(models.Model):
    stu_class = models.CharField(max_length=70)
    marks = models.IntegerField()

    def __str__(self):
        return self.stu_class