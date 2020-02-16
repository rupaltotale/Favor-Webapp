from django.shortcuts import render, redirect
from .forms import SignUpForm, AddFavorForm
from django.http import HttpResponseRedirect


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


def test(request):
    # some code
    return render(request, 'test.html')


@login_required
def give(request):
    # some code
    return render(request, 'give.html', {
        "cards": [
            {
                "id": 1,
                "title": "Massage1",
                "favors": 2,
                "description": "2 hr massage in Cerro",
                "username": "John Casey",
                "date": "2019-01-07",
                "location": "Cerro Vista"
            },
            {
                "id": 2,
                "title": "Fix Bike1",
                "favors": 1,
                "description": "Will quickly fix your bike",
                "username": "Chuck Bartowski",
                "date": "2019-09-12",
                "location": "University Union shop"
            },
            {
                "id": 3,
                "title": "Help with C Science Homework1",
                "favors": 1,
                "description": "Will look over code and help fix bugs or help get started on assignment",
                "username": "Morgan Grimes",
                "date": "2019-01-09",
                "location": "CSL"
            },
            {
                "id": 4,
                "title": "Massage2",
                "favors": 2,
                "description": "2 hr massage in Cerro",
                "username": "John Casey",
                "date": "2019-01-07",
                "location": "Cerro Vista"
            },
            {
                "id": 5,
                "title": "Fix Bike2",
                "favors": 1,
                "description": "Will quickly fix your bike",
                "username": "Chuck Bartowski",
                "date": "2019-09-12",
                "location": "University Union shop"
            },
            {
                "id": 6,
                "title": "Help with CS Homework2",
                "favors": 1,
                "description": "Will look over code and help fix bugs or help get started on assignment",
                "username": "Morgan Grimes",
                "date": "2019-01-09",
                "location": "CSL"
            },
            {
                "id": 7,
                "title": "Massage3",
                "favors": 2,
                "description": "2 hr massage in Cerro",
                "username": "John Casey",
                "date": "2019-01-07",
                "location": "Cerro Vista"
            },
            {
                "id": 8,
                "title": "Fix Bike3",
                "favors": 1,
                "description": "Will quickly fix your bike",
                "username": "Chuck Bartowski",
                "date": "2019-09-12",
                "location": "University Union shop"
            },
            {
                "id": 9,
                "title": "Help with CS Homework3",
                "favors": 1,
                "description": "Will look over code and help fix bugs or help get started on assignment",
                "username": "Morgan Grimes",
                "date": "2019-01-09",
                "location": "CSL"
            },
            {
                "id": 10,
                "title": "Help with CS Homework4",
                "favors": 1,
                "description": "Will look over code and help fix bugs or help get started on assignment",
                "username": "Morgan Grimes",
                "date": "2019-01-09",
                "location": "CSL"
            },
        ]
    })


@login_required
def show_service(request):
    id = request.GET.get("id")
    if id == None:
        return render(request, "give.html", status=400)

    dic = {}
    for val in ["title", "description", "username", "date", "location", "favors", "id"]:
        dic[val] = request.GET.get(val)
    print(dic)
    return render(request, "service_info.html", {
        "service_info": dic
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

        # Create a new form instance:
        form = AddFavorForm()

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
