from django.db import models
from datetime import datetime


# Create your models here.
class Album(models.Model):
    image = models.ImageField(upload_to='photo/%y/%m/%d/')
    list_date = models.DateTimeField(default=datetime.now, blank=True)
