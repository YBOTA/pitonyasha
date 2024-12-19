from django.contrib import admin
from .models import Category, Task


class TaskPanel(admin.ModelAdmin):
   list_display = ('title','desc', 'category', 'done', 'createdAt')
   list_display_links = ('title',)
   
admin.site.register(Task,TaskPanel)
admin.site.register(Category)
# Register your models here.
