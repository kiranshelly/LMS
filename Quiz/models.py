from django.db import models
from django.contrib.auth.models import User


# Create models here.
class FillintheBlanksModel(models.Model):
    Question = models.CharField(max_length=70,blank=True, null=True)
    Answer = models.CharField(max_length=100, blank=True, null=True)
    Option1 = models.CharField(max_length=50,blank=True, null=True)
    Marks = models.IntegerField(max_length=50,blank=True, null=True)


class MultipleChoiceModel(models.Model):
    Level = models.CharField(max_length=50,blank=True, null=True)
    Question = models.CharField(max_length=70,blank=True, null=True)
    Answer = models.CharField(max_length=100, blank=True, null=True)
    Option1 = models.CharField(max_length=50,blank=True, null=True)
    Option2 = models.CharField(max_length=50,blank=True, null=True)
    Option3 = models.CharField(max_length=50,blank=True, null=True)
    Option4 = models.CharField(max_length=50,blank=True, null=True)
    Marks = models.IntegerField(max_length=50,blank=True, null=True)



class TrueandFalseModel(models.Model):
    Question = models.CharField(max_length=70,blank=True, null=True)
    Answer = models.CharField(max_length=100, blank=True, null=True)
    Option1 = models.CharField(max_length=50,blank=True, null=True)
    Option2 = models.CharField(max_length=50,blank=True, null=True)
    Marks = models.IntegerField(max_length=50,blank=True, null=True)




# Answer Model

# class AnswerModel(models.Model):
#     AtemptedQuestion = models.IntegerField(blank=True, null=True)
#     AtemptedQuestion = models.IntegerField( blank=True, null=True)
#     Correct = models.IntegerField(blank=True, null=True)
#     Wrong = models.IntegerField(blank=True, null=True)
#     GetMarks  = models.IntegerField(blank=True, null=True)
#     TotalNumber  = models.IntegerField(blank=True, null=True)


