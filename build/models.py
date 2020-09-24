from django.db import models
from PIL import Image

from datetime import datetime
# Create your models here.

class Prop(models.Model):
    city = models.CharField(max_length=30,unique=False)
    state = models.CharField(max_length=30,unique=False)
    photo = models.ImageField(default='default.png',upload_to='site_photos',blank=True,null=True)
    vastu = models.CharField(max_length=50,unique=False)
    cost = models.IntegerField(unique=False,default=100)
    facilities = models.CharField(max_length=50,unique=False)
    date_added = models.DateTimeField(default=datetime.now,blank=True)
    
    def save(self, *args, **kwargs):
        super(Prop, self).save(*args, **kwargs)

        photo = Image.open(self.photo.path)

        if photo.height > 300 or photo.width > 300:
            output_size = (300, 300)
            photo.thumbnail(output_size)
            photo.save(self.photo.path)