from django.contrib import admin
from .models import handlers,items,mylist,mysale,monthlysale
# Register your models here.
# mymodels = 
admin.site.register([handlers,items,mylist,mysale,monthlysale])