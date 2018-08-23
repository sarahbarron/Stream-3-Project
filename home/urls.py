from django.conf.urls import url
from .views import treatments

urlpatterns = [
  url(r'^treatments/', treatments, name="treatments" )
 ]