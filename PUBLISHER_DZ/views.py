from django.shortcuts import render
from django.views import generic 
from .models import Post
# Create your views here.

class Home(generic.ListView):
	
	template_name="PUBLISHER_DZ/home.html"	

	def get_queryset(self):
		return Post.objects.all() 	

#	@api_view(['POST'])
	
#class Add(generic.edit.UpdateView):
#   	template_name="PUBLISHER_DZ/add.html"
#	model = Post
#   	success_url = '/adde'
#    	fields = '__all__'
	
#	def post_add(self,request):
#		p = Post();
		#p.description=request.POST['inputData']		
#		p.description="Yacine"
#		p.handle_post()
#		return render(request,"home.html",{})


