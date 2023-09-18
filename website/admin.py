from django.contrib import admin

# Register your models here.
from website.models import Train,Coures
admin.site.register((Train,Coures))