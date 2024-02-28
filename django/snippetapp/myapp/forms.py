from django import forms
from .models import *

class MyModelForm(forms.ModelForm):
    class Meta:
        model = snippest
        fields = ['id', 'title','code','linenos','language','style']