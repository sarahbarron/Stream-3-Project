from django.shortcuts import render

# Create your views here.

def index(request):
    # view for index.html
    return render(request, 'index.html')
