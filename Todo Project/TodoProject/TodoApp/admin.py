from django.contrib import admin #type: ignore
from .models import Todo #type: ignore
# Register your models here.

admin.site.register(Todo)