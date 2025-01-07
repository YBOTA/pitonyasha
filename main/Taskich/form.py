from django import forms
from .models import Task, Money

class TaskForm(forms.ModelForm):
   class Meta:
      model = Task
      fields = ('title','desc','category')


class MoneyForm(forms.ModelForm):
   # type_money = forms.CharField(widget=forms.HiddenInput)
   class Meta:
      model = Money
      fields = ('title','type_money', 'category','value')