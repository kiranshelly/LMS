from django.shortcuts import render , redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from Blog.models import  *
# Create your views here.




def register(request):
    if request.method == "POST":
        get_username = request.POST.get('username')
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')
        user_model = User.objects.create_user(username=get_email,password=get_password)
        user_model.set_password(get_password)
        user_model.save()
        save_info = RegisterTeacherModel.objects.create(Username = get_username, 
        Email = get_email, Password= get_password)
        save_info.save()
        print("Data Saved")
        return render(request, "teacher_login.html")

    else:
        register_form = RegisterTeacherForm()
        return render(request, "teacher_register.html",{"register_form":register_form})



def login(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')
        print(get_email, get_password)
        user_auth = authenticate(username=get_email,password=get_password)
        if user_auth:
            auth.login(request,user_auth)
            print(user_auth)
            return redirect("teacher:teacher_main")

        else:
            print("Does not exists")
            return render(request, "teacher_login.html")

    else:
        login_form = LoginTeacherForm()
        return render(request, "teacher_login.html",{"login_form":login_form})
    
    return render(request, "teacher_login.html")


@login_required
def t_main(request):

    return render(request, "teacher_main.html" )

@login_required
def User_Profile(request,id):
    get_user = User.objects.get(id = id)
    print("User here",id)
    return render(request, "teacher_user_profile.html" ,{"get_user":get_user})


@login_required
def logout(request):
    auth.logout(request)
    return redirect("teacher:teacher_login")


# Lesson


