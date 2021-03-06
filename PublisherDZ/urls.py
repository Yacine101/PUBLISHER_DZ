"""PublisherDZ URL Configuration
ss
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from PUBLISHER_DZ import views
from django.http import HttpResponseRedirect
urlpatterns = [
#    url(r'^$', 'django.views.generic.simple.redirect_to', {'url': '/home/'}),
    url(r'^$', lambda r: HttpResponseRedirect('home/')),
    url(r'^admin/', admin.site.urls),
    url(r'^add/', views.Add.as_view() , name="add"),
    url(r'^home/', views.Home.as_view() , name="home"),
    url(r'^featured/', views.Featured.as_view() , name="featured"),
    url(r'^sales/(?P<post_id>([0-9]*))/$', views.Specific.as_view() , name="sales"),
    url(r'^success/', views.success , name="success")
]
