from django.db import models
import os

# Create your models here.

class FileUpload(models.Model):
    imgfile = models.ImageField(null=True, upload_to="", blank=True)