from django.contrib import admin
from .models import TodoItem

# Register your models here.
# migration required every time a model is changed/ change in database
admin.site.register(TodoItem)