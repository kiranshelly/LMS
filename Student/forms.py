from .models import *
from django import forms


class RegisterStudentForm(forms.ModelForm):

    class Meta:
        model = RegisterStudentModel
        fields = '__all__'

class LoginStudentForm(forms.ModelForm):
     
    class Meta:
        model = RegisterStudentModel
        fields = '__all__'

