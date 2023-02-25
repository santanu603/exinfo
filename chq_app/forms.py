from django.forms import ModelForm
from django import forms
from .models import master, order, replacement



class chq_form(ModelForm):
    
    class Meta:
        model = master
        fields = '__all__'


class order_form(ModelForm):
    class Meta:
        model=order
        fields = '__all__'
       

class replace_form(ModelForm):
    class Meta:
        model=replacement
        fields = '__all__'