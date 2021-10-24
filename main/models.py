from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Alex (models.Model):
    experience = models.CharField(max_length=256)


class Jobs (models.Model):
    title = models.CharField(max_length=256)
    image = CloudinaryField('image')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title
