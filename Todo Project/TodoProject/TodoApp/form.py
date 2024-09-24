from django import forms #type: ignore
from .models import Todo

class TodoFrom(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'description', 'status']  # Include the fields you want in the form

    
