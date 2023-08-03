from django.contrib import admin
from mediciones.models import Area, Region, Measurements

# Register your models here.
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display=['id','name','owner','created_at']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display=['id','area','name','created_at']

@admin.register(Measurements)
class MeasurementsAdmin(admin.ModelAdmin):
    list_display=['id','region','temperature','humidity','created_at']