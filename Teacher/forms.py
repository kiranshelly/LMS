from .models import *
from django import forms


class RegisterTeacherForm(forms.ModelForm):

    class Meta:
        model = RegisterTeacherModel
        fields = '__all__'

class LoginTeacherForm(forms.ModelForm):
     
    class Meta:
        model = RegisterTeacherModel
        fields = '__all__'

