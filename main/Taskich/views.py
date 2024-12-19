from django.shortcuts import render
from django.views.generic import ListView
from .models import Task,Category
from django.http import HttpResponseRedirect

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

    
   

