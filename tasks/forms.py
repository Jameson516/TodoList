from django import forms
from .models import Todo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

        """widgets = {
            'task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add a new task"
            })
        }"""
