from django.shortcuts import render
from django.views import generic 
from .models import Post
# Create your views here.

class Home(generic.ListView):
	
	template_name="PUBLISHER_DZ/home.html"	
	context_object_name = "posts"

	def get_queryset(self):
		return Post.objects.all().order_by('-id') 


class Specific(generic.ListView):

        template_name="PUBLISHER_DZ/specific.html"
        context_object_name = "post"

        def get_queryset(self, **kwargs):
                return Post.objects.get(id=self.kwargs['post_id'])

	
class Add(generic.edit.CreateView):
   	template_name="PUBLISHER_DZ/add.html"
	model = Post
   	success_url = '/home'
    	fields = ['description','phone','e_mail','location']


class Featured(generic.ListView):

        template_name="PUBLISHER_DZ/featured.html"
#        context_object_name = "posts"

        def get_queryset(self):
                return ""

def success(request):
	return render(request,"PUBLISHER_DZ/success.html",{})
	
