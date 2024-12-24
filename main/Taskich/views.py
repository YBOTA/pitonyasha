from django.shortcuts import render
from django.views.generic import ListView,UpdateView, CreateView, View,TemplateView, FormView
from .models import Task,Category,Finance,CatFin
from .form import TaskForm, FinanceForm,CatFinForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.views.generic.list import MultipleObjectMixin


class TaskListView(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'taskich/mainT.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context

class CategoryListView(ListView):
    context_object_name = 'task'
    template_name = "taskich/category_filter.html"
    
    def get_queryset(self):
       return Task.objects.filter(category= self.kwargs['cat_id'])

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
    print(t.done)
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
    
# FINANCE
class FinanceView(ListView,FormView):
    model = Finance
    context_object_name = "Lol"
    form_class = FinanceForm
    template_name = "finance/FinanceM.html"
    success_url = reverse_lazy("finance")

    def form_valid(self,form):
        template_name = self.request.POST.get('template_name')

        instance = form.save(commit=False)
        if template_name == 'addplusD':
            instance.Income = True
        elif template_name == 'addminusD':
            instance.Income = False
        instance.save()
        return super().form_valid(form)

def addFinCat(request):
    if request.method == "POST":
        cat = request.POST.get('cat')
        CatFin.objects.create(Cat=cat)
    return HttpResponseRedirect(reverse('finance'))