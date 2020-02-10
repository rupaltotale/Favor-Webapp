from django.shortcuts import render, redirect
from .forms import SignUpForm

# Signup/Login stuff
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def test(request):
    # some code
    return render(request, 'test.html')

def give(request):
    # some code
    return render(request, 'give.html', {
        "cards" : [
            {
                "title" : "Massage",
                "favors" : 2,
                "description" : "2 hr massage in Cerro",
                "username" : "John Casey",
                "date" : "2019-01-07",
                "location" : "Cerro Vista"
            },
            {
                "title" : "Fix Bike",
                "favors" : 1,
                "description" : "Will quickly fix your bike",
                "username" : "Chuck Bartowski",
                "date" : "2019-09-12",
                "location" : "University Union shop"
            },
            {
                "title" : "Help with C Science Homework",
                "favors" : 1,
                "description" : "Will look over code and help fix bugs or help get started on assignment",
                "username" : "Morgan Grimes",
                "date" : "2019-01-09",
                "location" : "CSL"
            },
            {
                "title" : "Massage",
                "favors" : 2,
                "description" : "2 hr massage in Cerro",
                "username" : "John Casey",
                "date" : "2019-01-07",
                "location" : "Cerro Vista"
            },
            {
                "title" : "Fix Bike",
                "favors" : 1,
                "description" : "Will quickly fix your bike",
                "username" : "Chuck Bartowski",
                "date" : "2019-09-12",
                "location" : "University Union shop"
            },
            {
                "title" : "Help with CS Homework",
                "favors" : 1,
                "description" : "Will look over code and help fix bugs or help get started on assignment",
                "username" : "Morgan Grimes",
                "date" : "2019-01-09",
                "location" : "CSL"
            },
            {
                "title" : "Massage",
                "favors" : 2,
                "description" : "2 hr massage in Cerro",
                "username" : "John Casey",
                "date" : "2019-01-07",
                "location" : "Cerro Vista"
            },
            {
                "title" : "Fix Bike",
                "favors" : 1,
                "description" : "Will quickly fix your bike",
                "username" : "Chuck Bartowski",
                "date" : "2019-09-12",
                "location" : "University Union shop"
            },
            {
                "title" : "Help with CS Homework",
                "favors" : 1,
                "description" : "Will look over code and help fix bugs or help get started on assignment",
                "username" : "Morgan Grimes",
                "date" : "2019-01-09",
                "location" : "CSL"
            },
        ]
    })
def signup(request):
   if request.method == "POST":
      form = SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username, password=raw_password)
         login(request, user)
         return redirect('/')
      else:
         print("form not valid")
   else:
      form = SignUpForm()
   return render(request, "signup.html", {"form":form})
