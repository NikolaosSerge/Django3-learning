from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    """docstring for TodoForm."""
    class Meta:
        model = Todo
        fields = ['title','memo','Important']
