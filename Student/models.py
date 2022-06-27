from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegisterStudentModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=50,null=True)
    Email = models.EmailField(null=True)
