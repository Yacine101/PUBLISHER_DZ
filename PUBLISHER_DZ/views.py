from django.shortcuts import render
from django.views import generic 
from .models import Post
# Create your views here.

class Home(generic.ListView):

	def get_queryset(self):
		return Post.objects.all() 	

	def view(self,request):
		return render(request,"home.html",{})


