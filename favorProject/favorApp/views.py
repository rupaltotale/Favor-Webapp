from django.shortcuts import render, redirect
from .forms import SignUpForm, AddFavorForm
from django.http import HttpResponseRedirect
from favorApp.models import Favor


# Signup/Login stuff
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html')


def landing(request):
    return render(request, 'landing.html')



@login_required
def give(request):
    # some code
    return render(request, 'give.html', {
        "cards": Favor.objects.all()
    })


@login_required
def show_service(request):
    id = request.GET.get("id")
    if id == None:
        return render(request, "give.html", status=400)

    return render(request, "service_info.html", {
        "service_info": Favor.objects.get(id=id)
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
    return render(request, "signup.html", {"form": form})


def add_favor(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = AddFavorForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')
    # If this is a GET (or any other method) create the default form.
    else:
        form = AddFavorForm()

    context = {
        'form': form,
    }

    return render(request, 'add_favor.html', context)
