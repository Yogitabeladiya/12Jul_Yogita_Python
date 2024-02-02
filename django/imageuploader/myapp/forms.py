from django import forms
from .models import *



class imageform(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
        labels={'photo':''}   