from django.contrib import admin
from django.urls import path,re_path
from Taskich.views import TaskListView,CategoryListView,deleteTask, TaskUpdateView,set_done_Task,FiltreDone,MoneyListView,CategoryMoneyListView,FiltreTypeMoneyListView,TestDateView,ZametkiListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskListView.as_view(),name='main'),
    path('category/<int:cat_id>',CategoryListView.as_view(), name='category'),
    path('delete/<int:task_id>',deleteTask,name='delete'),
    path('edit/<int:t_id>',TaskUpdateView.as_view(),name='edit'),
    path('done/<int:t_id>',set_done_Task,name='setdone'),
    path('task/<str:filtre>',FiltreDone.as_view(),name='done'),
    #финансы
    path('finance/',MoneyListView.as_view(),name='finance'),
    path('finance/category/<slug:slug>',CategoryMoneyListView.as_view(),name='financeCategory'),
    path('finance/type/<str:type>',FiltreTypeMoneyListView.as_view(),name='type_money'),
    path('testing/2025/week/3',TestDateView.as_view(),name='date'),
    #заметки
    path('zametki',ZametkiListView.as_view(),name='zametki')
    
]
