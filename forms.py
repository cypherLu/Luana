from pyexpat import model
from django import forms
from .models import fanfic

class fanficForm(forms.ModelForm):
    class Meta:
        model = fanfic
        fields = ('title', 'sinopse', 'status')