from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published', default = datetime.now, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
