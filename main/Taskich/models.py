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
   
class Money(models.Model):
    INCOME = 'i'
    DEBTS = 'd'
    KINDS = (
        (INCOME,'Доход'),
        (DEBTS,'Расход')
    )
    title = models.CharField(max_length=30, verbose_name='Наименование транзакции')
    type_money = models.BooleanField(null=True,verbose_name='Тип транзакции')
    category = models.ForeignKey("CategoryMoney", verbose_name=("Категория"),null=True, on_delete=models.PROTECT)
    value = models.BigIntegerField(verbose_name='Сумма')
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ['-createdAt']

    def __str__(self):
        return self.title
    
class CategoryMoney(models.Model):
    name = models.CharField(max_length=20,verbose_name='Наименование категории')
    def __str__(self):
       return self.name
   



