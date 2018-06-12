"""GinasBeautyStudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from home.views import get_index
from accounts import urls as urls_accounts
from posts import urls as urls_posts
from django.views.static import serve
from .settings import MEDIA_ROOT
from django.views.generic import RedirectView

urlpatterns = [
    # url to direct to the django's admin area
    url(r'^admin/', admin.site.urls),
    # url to direct to the index.html file
    #url(r'^$', get_index, name="get_index"),
    
    
    url(r'^$', RedirectView.as_view(url='posts/')),
    
    
    # url to include the urls.py urls from the accounts app
    url(r'^accounts/', include(urls_accounts)),
    url(r'^posts/', include(urls_posts)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    
    
]
