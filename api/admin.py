from django.contrib import admin
from .models import Carlist

# Register your models here.
@admin.register(Carlist)
class CarlistAdmin(admin.ModelAdmin):
    list_display = ('id','name','des','active','color')
