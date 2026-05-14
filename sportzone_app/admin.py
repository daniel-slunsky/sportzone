from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Trenink, Rezervace

admin.site.register(Trenink)
admin.site.register(Rezervace)
