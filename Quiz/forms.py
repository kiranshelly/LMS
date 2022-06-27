from .models import *
from django import forms


class MultipleChoiceForm(forms.ModelForm):
    Level = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Level",
                                    "class": "form-control",
                                }
                            ))
    Question = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Question ",
                                    "class": "form-control",
                                }
                            ))
    Answer = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Answer",
                                    "class": "form-control",
                                }
                            ))
    Option1 = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Option1 ",
                                    "class": "form-control",
                                }
                            ))
    Option2 = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Option2",
                                    "class": "form-control",
                                }
                            ))
    Option3 = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Option3",
                                    "class": "form-control",
                                }
                            ))
    Option4 = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Option4",
                                    "class": "form-control",
                                }
                            ))
    Marks = forms.IntegerField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Marks",
                                    "class": "form-control",
                                }
                            ))


    class Meta:
        model = MultipleChoiceModel
        fields = '__all__'

class TrueandFalseForm(forms.ModelForm):
    Level = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Level",
                                    "class": "form-control",
                                }
                            ))
    Question = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Question ",
                                    "class": "form-control",
                                }
                            ))
    Answer = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Answer",
                                    "class": "form-control",
                                }
                            ))
    Option1 = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Option1 ",
                                    "class": "form-control",
                                }
                            ))
    Option2 = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Option2",
                                    "class": "form-control",
                                }
                            ))
    Marks = forms.IntegerField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Marks",
                                    "class": "form-control",
                                }
                            ))


    class Meta:
        model = TrueandFalseModel
        fields = '__all__'


class FillintheBlanksForm(forms.ModelForm):
    Level = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Level",
                                    "class": "form-control",
                                }
                            ))
    Question = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Question ",
                                    "class": "form-control",
                                }
                            ))
    Answer = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Answer",
                                    "class": "form-control",
                                }
                            ))
    Option1 = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Option1 ",
                                    "class": "form-control",
                                }
                            ))
    Marks = forms.IntegerField( widget=forms.TextInput(
                                attrs={
                                    "placeholder": " Marks",
                                    "class": "form-control",
                                }
                            ))



    class Meta:
        model = FillintheBlanksModel
        fields = '__all__'