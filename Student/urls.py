
from django.contrib import admin
from django.urls import path
from Quiz.urls import *
from Blog.urls import *
from django.urls import include
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/',register,name="register"),

    path('login/',login,name="login"),
    path('student_base/',student_base,name="student_base"),
    path('logout/',logout,name="logout"),
    path('user_profile/<id>/',User_Profile,name="user_profile"),
    path('student_nav/',student_nav,name="student_nav"),
    path('learn_more/<id>/',learn_more,name="learn_more"),





] 


