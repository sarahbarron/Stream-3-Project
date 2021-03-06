from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from posts import urls as urls_posts
from products import urls as urls_products
from cart import urls as urls_cart
from productsearch import urls as urls_productsearch
from checkout import urls as urls_checkout
from review import urls as urls_reviews
from home import urls as urls_home
from home.views import index
from products.views import all_products
from django.views.static import serve
from .settings import MEDIA_ROOT
from django.views.generic import RedirectView

''' Root urls for GinasBeautyStudio App '''

urlpatterns = [
    # url to direct to the django's admin area
    url(r'^admin/', admin.site.urls, name="admin"),
    # url to direct to the index.html file
    url(r'^$', index, name="index"),
    # include the urls.py files from all apps
    url(r'^accounts/', include(urls_accounts)),
    url(r'^home/', include(urls_home)),
    url(r'^posts/', include(urls_posts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_productsearch)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^reviews/', include(urls_reviews)),
    # urls to handle our media files
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
