from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'home.html')

def slideshow(request):
    # some code
    return render(request, 'template/slideshow.html')