from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView,UpdateView, CreateView
from django.views.generic.dates import ArchiveIndexView, DateMixin,TodayArchiveView,WeekArchiveView
from .models import Task,Category,Money,CategoryMoney,Zametki
from .form import TaskForm,MoneyForm
from django.http import HttpResponseRedirect

class TaskListView(ListView):
    model = Task
    paginate_by = 6 #кол-во записей на странице
    context_object_name = 'task'
    template_name = 'taskich/mainT.html'

    def post(self, request, *args, **kwargs):
      form = TaskForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request,message='Задача добавлена')
         return HttpResponseRedirect('/')
      
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context['form'] = TaskForm
        context['moneyForm'] = MoneyForm
        return context

class CategoryListView(ListView):
    context_object_name = 'task'
    template_name = "taskich/category_filter.html"
    
    def get_queryset(self):
       return Task.objects.filter(category= self.kwargs['cat_id'])
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["category"] = Category.objects.all()
       return context
   

def deleteTask(request,task_id):
    Task.objects.filter(id=task_id).delete()
    messages.success(request,'Задача удалена')
    return HttpResponseRedirect('/')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    pk_url_kwarg = 't_id'
    success_url = '/'
    template_name = "taskich/edit_task.html"

def set_done_Task(request,t_id):
    t = Task.objects.get(pk=t_id)
    t.done = True
    t.save()
    return HttpResponseRedirect('/')


class FiltreDone(ListView):
   model = Task
   context_object_name = 'task'
   template_name = "taskich/done_filter.html"

   def get_queryset(self):
         if self.kwargs['filtre'] == 'done':
               return Task.objects.filter(done =True)
         else:
               return Task.objects.filter(done =False)
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["category"] = Category.objects.all()
       return context
   
class TestDateView(WeekArchiveView):
   model = Task
   template_name = 'taskich/testing_date.html'
   date_field = 'dead_line'
   

#Finace
class MoneyListView(ListView):
    model = Money
    template_name = "finance/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["income"] = Money.objects.filter(type_money = 'i')
        context['debets'] = Money.objects.filter(type_money = 'd')
        context['category']= CategoryMoney.objects.all()
        return context
    
class CategoryMoneyListView(ListView):
    model = Money
    context_object_name = 'data'
    template_name = "finance/detail_finance.html"

    def get_queryset(self):
        cat =  CategoryMoney.objects.get(slug = self.kwargs['slug'])
        return Money.objects.filter(category = cat.pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryMoney.objects.get(slug = self.kwargs['slug'])
        return context
    

class FiltreTypeMoneyListView(ListView):
    model = Money
    template_name = "finance/detail_type_money.html"
    context_object_name ='data'

    def get_queryset(self):
        return Money.objects.filter(type_money = self.kwargs['type'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type_money"] = Money.objects.get(type_money = self.kwargs['type'])
        return context
    
    
#Заметки

class ZametkiListView(ListView):
    model = Zametki
    template_name = "zametki/main.html"
    context_object_name = 'data'




