from django.contrib import admin
from django.urls import path
from Taskich.views import TaskListView,CategoryListView,deleteTask, TaskUpdateView,set_done_Task,TaskCreateView, FinanceView,addFinCat
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskListView.as_view(),name='main'),
    path('category/<int:cat_id>',CategoryListView.as_view(), name='category'),
    path('delete/<int:task_id>',deleteTask,name='delete'),
    path('edit/<int:t_id>',TaskUpdateView.as_view(),name='edit'),
    path('done/<int:t_id>',set_done_Task,name='setdone'),
    path('add',TaskCreateView.as_view(),name='add'),
    path('finance', FinanceView.as_view(),name='finance'),
    path('addFinCat/', addFinCat,name='addFinCat'),

]
