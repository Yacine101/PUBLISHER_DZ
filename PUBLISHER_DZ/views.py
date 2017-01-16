from django.shortcuts import render
from django.views import generic 
from .models import Post
# Create your views here.

class Home(generic.ListView):
	
	template_name="PUBLISHER_DZ/home.html"	
	context_object_name = "posts"

	def get_queryset(self):
		return Post.objects.all() 
	
class Add(generic.edit.CreateView):
   	template_name="PUBLISHER_DZ/add.html"
	model = Post
   	success_url = '/success'
    	fields = ['description']


def success(request):
	return render(request,"PUBLISHER_DZ/success.html",{})
	
