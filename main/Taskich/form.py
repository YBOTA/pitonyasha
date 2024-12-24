from django import forms
from .models import Task,Finance,CatFin

class TaskForm(forms.ModelForm):
   class Meta:
      model = Task
      fields = ('title','desc','category')

class FinanceForm(forms.ModelForm):
   class Meta:
      model = Finance
      fields = ('nameF','desc','count',   'category')


class CatFinForm(forms.ModelForm):
   class Meta:
      model = CatFin
      fields = ('Cat',)