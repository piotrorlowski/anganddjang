from django.contrib import admin
from .models import ToDoList, ToDoListElement

# Register your models here.

admin.site.register(ToDoList)
admin.site.register(ToDoListElement)
