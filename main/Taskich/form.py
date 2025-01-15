from django import forms
from .models import Task, Money

class TaskForm(forms.ModelForm):
   dead_line = forms.DateTimeField(label='Дедлайн',widget=forms.widgets.SelectDateWidget(years=['2025']))
   class Meta:
      model = Task
      fields = ('title','desc','category','dead_line')


class MoneyForm(forms.ModelForm):
   # type_money = forms.CharField(widget=forms.HiddenInput)
   class Meta:
      model = Money
      fields = ('title','type_money', 'category','value')