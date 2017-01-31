from django.shortcuts import render
from django.views import generic 
from .models import Post
# Create your views here.

class Home(generic.ListView):
	
	template_name="PUBLISHER_DZ/home.html"	
	context_object_name = "posts"

	def get_queryset(self):
		return Post.objects.all().order_by('-id') 
	
class Add(generic.edit.CreateView):
   	template_name="PUBLISHER_DZ/add.html"
	model = Post
   	success_url = '/home'
    	fields = ['description','location','keywords']



def success(request):
	return render(request,"PUBLISHER_DZ/success.html",{})
	
