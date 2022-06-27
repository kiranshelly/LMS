from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from tinymce.models import HTMLField
    
 
class BlogModel(models.Model):
    Title = models.CharField(max_length=255,blank=True, null= True, )
    # Body = HTMLField(max_length=255, blank=True, null= True)
    # Body = RichTextField()
    Body = RichTextUploadingField()
    Image = models.ImageField(upload_to='images/',blank=True, null= True)
    Video_URL = models.CharField(max_length=255, blank=True, null= True)
    Video = models.FileField(upload_to='videos/', null=True)


    def __str__(self):
        return " Blog Title: " + self.Title
   
