from django.db import models

# Create your models here.

class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    