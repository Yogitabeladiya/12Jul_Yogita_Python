from django import forms
from .models import *



class displayform(forms.ModelForm):
    class Meta:
        model=product_sub_cat
        fields='__all__'
     