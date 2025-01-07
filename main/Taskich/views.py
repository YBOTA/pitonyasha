from django.shortcuts import render
from django.views.generic import ListView,UpdateView, CreateView
from .models import Task,Category,Money,CategoryMoney
from .form import TaskForm,MoneyForm
from django.http import HttpResponseRedirect

class TaskListView(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'taskich/mainT.html'

    def post(self, request, *args, **kwargs):
      form = TaskForm(request.POST)
      if form.is_valid():
         form.save()
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


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = "taskich/add_task.html"
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class DoneListView(ListView):
    queryset = Task.objects.filter(done = True)
    context_object_name = 'task'
    template_name = "taskich/done_filter.html"

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
    

    


