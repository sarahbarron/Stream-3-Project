from django.shortcuts import render

# Create your views here.
# index page view 
def index(request):
    #views to retrieve the index.html page
    return render(request, "index.html")
    
#treatments page view
def treatments(request):
    #views to retrieve the index.html page
    return render(request, "treatments.html")