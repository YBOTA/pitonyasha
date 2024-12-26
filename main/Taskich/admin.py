from django.contrib import admin
from .models import Category, Task,Money,CategoryMoney


class TaskPanel(admin.ModelAdmin):
   list_display = ('title','desc', 'category', 'done', 'createdAt')
   list_display_links = ('title',)

class MoneyPanel(admin.ModelAdmin):
   list_display = ('title','type_money','category','value','createdAt')
   
admin.site.register(Task,TaskPanel)
admin.site.register(Category)
admin.site.register(Money,MoneyPanel)
admin.site.register(CategoryMoney)

# Register your models here.
