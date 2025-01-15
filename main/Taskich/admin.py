from django.contrib import admin
from .models import Category, Task,Money,CategoryMoney,CategoryZametki,Zametki


class TaskPanel(admin.ModelAdmin):
   list_display = ('title','desc', 'category', 'done', 'dead_line','createdAt')
   list_display_links = ('title',)

class MoneyPanel(admin.ModelAdmin):
   list_display = ('title','type_money','category','value','createdAt')

class ZametliPanel(admin.ModelAdmin):
   list_display = ('title','text','category','edited','createdAt')
   
admin.site.register(Task,TaskPanel)
admin.site.register(Category)
admin.site.register(Money,MoneyPanel)
admin.site.register(CategoryMoney)
admin.site.register(Zametki,ZametliPanel)
admin.site.register(CategoryZametki)

# Register your models here.
