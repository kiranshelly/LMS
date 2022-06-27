
from django.urls import path
from Blog import views


app_name = "Blog"



urlpatterns = [
     path('create/', views.BlogPost, name="create"),
     path('show/', views.ShowPost, name="show"),
    path('edit/<id>/',views.EditPost,name="edit"),
    path('delete/<id>/', views.delete,name ="delete"),  


]

