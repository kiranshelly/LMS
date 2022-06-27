from django.shortcuts import render ,redirect
from .models import *
from .forms import *

# Create your views here.



def BlogPost(request):
    if request.method == "POST": 
        form =  BlogForm(request.POST , request.FILES)
        print(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            print("Data Saved")
            return redirect("teacher:teacher_main")
    else:
        form =  BlogForm()
        print("Else part")

    return render(request, "create_post.html",{'form': form })

def ShowPost(request):
        form =  BlogModel.objects.all()
        return render(request, "all_blog.html",{"form": form})



def EditPost(request, id):
    order = BlogModel.objects.get(id=id)
    form = BlogForm(instance=order)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    
    context = {'form':form}
    return render(request, 'edit_data.html', context)




def delete(request, id):
	order = BlogModel.objects.get(id=id)
	if request.method == "POST":
		order.delete()
		return redirect("teacher:teacher_main")

	context = {'item':order}
	return render(request, 'delete.html', context)