from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *

class BloggFormm(forms.ModelForm):
    class Meta:
        model = requestcat
        fields = ['name',] 

class BloggForm(forms.ModelForm):
    class Meta:
        model = categorymodel
        fields = ['name',] 

choices=categorymodel.objects.all().values_list('name','name')
choices_list=[]
for item in choices:
    choices_list.append(item)
class BlogForm(forms.ModelForm):
    class Meta:
        model = deardiaryModel
        fields = ['title', 'content','category']#'categories']
        widgets={
        'category':forms.Select(choices=choices_list,attrs={'class':'form-control'}),
        }


class BloggFForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields =['subject','review','rating']