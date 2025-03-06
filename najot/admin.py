from django.contrib import admin

# Register your models here.
from .models import Data, Students

admin.site.register(Data)
admin.site.register(Students)