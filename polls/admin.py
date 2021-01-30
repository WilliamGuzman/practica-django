from django.contrib import admin

# Register your models here. Se registra aca el modelo para que aparesca el modulo en la parte administrativa proporcinada por Django
from django.contrib import admin
from .models import Questions

admin.site.register(Questions)