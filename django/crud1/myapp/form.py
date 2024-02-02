from django import forms
from .models import *



class studentinfoform(forms.ModelForm):
    class Meta:
        models=studentinfo
        fields='__all__'
    