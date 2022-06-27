
from django.urls import path
from Quiz import views


app_name = "Quiz"

urlpatterns = [
     
     path('Types_of_Quiz/', views.Types_of_Quiz, name="Types_of_Quiz"),
     path('Play_Quiz/', views.Play_Quiz, name="Play_Quiz"),
     path('Result/', views.Result, name="Result"),
     path('Index/',views.Index,name="Index"),

     path('Create_Multiple_Quiz/', views.Create_Multiple_Quiz, name="Create_Multiple_Quiz"),
     path('Fill_in_the_Blanks_Quiz/', views.Fill_in_the_Blanks_Quiz, name="Fill_in_the_Blanks_Quiz"),
     path('True_False_Quiz/', views.True_False_Quiz, name="True_False_Quiz"),

     path('Get_Multiple_Choice/', views.Get_Multiple_Choice, name="Get_Multiple_Quiz"),
     path('Get_Fill_in_the_Blanks_Quiz/', views.Get_Fill_in_the_Blanks_Quiz, name="Get_Fill_in_the_Blanks_Quiz"),
     path('Get_True_False_Quiz/', views.Get_True_False_Quiz, name="Get_True_False_Quiz"),

]
