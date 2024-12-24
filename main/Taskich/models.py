from django.db import models

class Task(models.Model):
   title = models.CharField (max_length=50, unique=True,verbose_name='Наименование задачи')
   desc = models.CharField(max_length=100, null=True, blank=True, verbose_name='Описание задачи')
   category = models.ForeignKey("Category", verbose_name=("Категория"), on_delete=models.PROTECT, null=True)
   done = models.BooleanField(default=False, verbose_name='Отметка о выполнеии')
   createdAt = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

   class Meta:
       verbose_name = 'Задача' # название модели в ед. числе
       ordering = ['-createdAt'] #сортировка по-умолчанию
       unique_together = ('title','createdAt')

   def __str__(self):
       return self.title
   

class Category(models.Model):
   name = models.CharField(max_length=35, verbose_name='Название категории')
   
   def __str__(self):
       return self.name

# FINANCE
class CatFin(models.Model):
    Cat = models.TextField()

    def __str__(self):
       return self.Cat

class Finance(models.Model):
    nameF = models.TextField(verbose_name='Название транзакции')
    desc = models.TextField(verbose_name='Описание транзакции')
    Income = models.BooleanField(null=True, blank=True)
    count = models.BigIntegerField(default=0,verbose_name='Сколько')
    category = models.ForeignKey(CatFin, on_delete=models.PROTECT,verbose_name='Категория',null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.nameF
   
   

