from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth.models import User
from .models import *
import random
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .forms import *
 



def first(request):
    return render(request, "first.html" )



@login_required
def Index(request):
    return render(request, "Index.html" )
    
def Types_of_Quiz(request):
    return render(request, "Types_of_Quiz.html")




def  index(request):
    return render(request, "Index.html")

def  Play_Quiz(request):
    return render(request, "Play_Quiz.html")



def  Result(request):
    return render(request, "Result.html")
   

def Create_Multiple_Quiz(request):
    if request.method == "POST":
        form =  MultipleChoiceForm(request.POST )
        print(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            print("Data Saved")
            return redirect("teacher:teacher_main")
    else:
        Create_Multiple_Quiz =   MultipleChoiceForm()
    return render(request, "Create_Multiple_Choice.html" ,{"Create_Multiple":Create_Multiple_Quiz})


def True_False_Quiz(request):
    if request.method == "POST":
        form =  TrueandFalseForm(request.POST )
        print(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            print("Data Saved")
            return redirect("teacher:teacher_main")
    else:       
        True_False_Quiz =   TrueandFalseForm()
    return render(request, "True_False_Choice.html" ,{"True_False":True_False_Quiz})




def Fill_in_the_Blanks_Quiz(request):
    if request.method == "POST":
        form =  FillintheBlanksForm(request.POST )
        print(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            print("Data Saved")
            return redirect("teacher:teacher_main")
    else:
        Fill_in_the_Blanks_Quiz =   FillintheBlanksForm()
    return render(request, "Fill_in_the_Blanks_Choice.html" ,{"Fill_in_the_Blanks":Fill_in_the_Blanks_Quiz})

def Get_Multiple_Choice(request):
    if request.method == 'POST':
        print(request.POST)
        questions=MultipleChoiceModel.objects.all()
        marks=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.Question))
            print(q.Answer)
            print()
            if q.Answer ==  request.POST.get(q.Question):
                marks+= marks + q.Marks
                correct+=1
            else:
                wrong+=1
        context = {
            'marks':marks,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'total':total
        }
        return render(request,'Result.html',context)
    
    else:   
        Get_Multiple_Choice =  MultipleChoiceModel.objects.all()
        return render(request, "Get_Multiple_Choice.html" ,{"Get_Multiple_Choice":Get_Multiple_Choice})

def Get_Fill_in_the_Blanks_Quiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions=FillintheBlanksModel.objects.all()
        marks=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.Question))
            print(q.Answer)
            print()
            if q.Answer ==  request.POST.get(q.Question):
                marks+= marks + q.Marks
                correct+=1
            else:
                wrong+=1
        context = {
            'marks':marks,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'total':total
        }
        return render(request,'Result.html',context)
    
    else:
        Get_Fill_in_the_Blanks_Quiz =  FillintheBlanksModel.objects.all()
        return render(request, "Get_Fill_in_the_Blanks_Quiz.html" ,{"Get_Fill_in_the_Blanks_Quiz":Get_Fill_in_the_Blanks_Quiz})


def Get_True_False_Quiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions=TrueandFalseModel.objects.all()
        marks=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.Question))
            print(q.Answer)
            print()
            if q.Answer ==  request.POST.get(q.Question):
                marks+= marks + q.Marks
                correct+=1
            else:
                wrong+=1
        context = {
            'marks':marks,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'total':total
        }
        return render(request,'Result.html',context)
    
    else:
        Get_True_False_Quiz =  TrueandFalseModel.objects.all()
        return render(request, "Get_True_False_Quiz.html" ,{"Get_True_False_Quiz":Get_True_False_Quiz})
