from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()


class People(models.Model):
    Name = models.CharField(max_length=250)
    Img = models.ImageField(upload_to='pics')
    position = models.TextField()

