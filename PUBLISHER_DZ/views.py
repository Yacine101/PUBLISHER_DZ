from django.shortcuts import render
#from django.views import generic 
from .models import Post
# Create your views here.

def get_list(request):
	return Post.objects.all() 	
def view(request):
	return render(request,"home.html",{})


