# from django.forms import ModelForm
from .models import *
from django import forms


class BlogForm(forms.ModelForm):
    Title = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "form-control",
                                    "id": "my-id-for-textarea",
                                }
                            ) )
    Body = HTMLField( )
    Image = forms.ImageField()
    Video_URL = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Add URL",
                                    "class": "form-control",
                                }
                            ))
    Video = forms.FileField()


    class Meta:
        model = BlogModel
        fields = '__all__'