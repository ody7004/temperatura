from django.db import models
from django.utils import timezone

# Create your models here.
class Area(models.Model):
    name= models.CharField(max_length=180)
    owner= models.CharField(max_length=200)
    phone= models.CharField(max_length=12)
    email= models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=100, null=True, blank=True)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Region(models.Model):
    area = models.ForeignKey(Area, related_name='region_area', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name



class Measurements(models.Model):
    region=models.ForeignKey(Region,related_name='region',on_delete=models.CASCADE)
    temperature= models.FloatField(default=0)
    humidity= models.FloatField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    note=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.region.name

