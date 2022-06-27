
from django.contrib import admin
from django.urls import path
from Quiz.urls import *
from Blog.urls import *
from Teacher.urls import *
from django.urls import include
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('teacher_register/',register,name="teacher_register"),
    path('teacher_login/',login,name="teacher_login"),
    path('teacher_logout/',logout,name="teacher_logout"),
    path('teacher_user_profile/<id>/',User_Profile,name="teacher_user_profile"),
    path('teacher_main/',t_main,name="teacher_main"),


]

