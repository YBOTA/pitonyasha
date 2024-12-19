from django.contrib import admin
from django.urls import path
from Taskich.views import TaskListView,CategoryListView,deleteTask
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskListView.as_view(),name='main'),
    path('category/<int:cat_id>',CategoryListView.as_view(), name='category'),
    path('delete/<int:task_id>',deleteTask,name='delete')
]
