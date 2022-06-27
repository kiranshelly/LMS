from django.shortcuts import render
from Blog.models import *

# Create your views here.
def student_base(request):
    form =  BlogModel.objects.all()
    return render(request, "student_base.html",{"form": form})