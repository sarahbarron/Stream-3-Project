from django.conf.urls import url
from .views import treatments

# url to the treatments view
urlpatterns = [
  url(r'^treatments/', treatments, name="treatments" )
 ]