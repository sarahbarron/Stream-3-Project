from django.shortcuts import render

# Create your views here.
def get_index(request):
    #views to retrieve the index.html page
    return render(request, "index.html")