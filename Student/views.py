from django.shortcuts import render , redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.http import HttpResponse, HttpResponseRedirect
from Blog.models import *

# Create your views here.


def register(request):
    if request.method == "POST":
        get_username = request.POST.get('username')
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')
        save_info = RegisterStudentModel.objects.create(Username = get_username, 
        Email = get_email, Password= get_password)
        user_model = User.objects.create_user(username=get_email,password=get_password)
        user_model.set_password(get_password)
        user_model.save()
        save_info.save()
        print("Data Saved")
        return redirect("student:login")

    else:
        register_form = RegisterStudentForm()
        return render(request, "register.html",{"register_form":register_form})

def student_base(request):
    form =  BlogModel.objects.all()
    return render(request, "student_base.html",{"form": form})

def student_nav(request):
    return render(request, "student_nav.html")


def login(request):
    Title= "Login"
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')
        print(get_email, get_password)
        user_auth = authenticate(username=get_email,password=get_password)
        if user_auth:
            auth.login(request,user_auth)
            print(user_auth)
            return redirect("student:student_base")
        else:
            print("Does not exists")
            return render(request, "login.html" ,)

    else:
        login_form = LoginStudentForm()
        return render(request, "login.html",{"login_form":login_form})
    
    return render(request, "login.html")


@login_required
def home(request):
    return render(request, "home.html" )

@login_required
def User_Profile(request,id):
    get_user = RegisterStudentModel.objects.get(id = id)
    print("User here",id)
    print("User here",get_user)
    return render(request, "User_Profile.html" ,{"get_user":get_user})

def index(request):
    return render(request, "Index.html" )

@login_required
def logout(request):
    auth.logout(request)
    return redirect("student:student_base" )



@login_required
def learn_more(request,id):
    print("ID",id)
    form = BlogModel.objects.get(id = id)

    return render(request, "learn_more.html",{"form":form})

