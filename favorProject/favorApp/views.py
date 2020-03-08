from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, AddFavorForm
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from .models import Favor

# Signup/Login stuff
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.db.models import Q # new
from django.http import JsonResponse



def landing(request):
    return render(request, 'landing.html')


@login_required
def show_services(request):
    query = request.GET.get('q')
    cards = Favor.objects.all();
    current_user = request.user
    if request.method == "POST":
        # print("Updating object: ", request.id)
        card_id = request.POST.get('card_id')
        favor = Favor.objects.get(id=card_id)
        favor.pendingUsers.add(current_user) 
    if query:
        cards = Favor.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    # for card in cards:
    #     if current_user in card.pendingUsers
    return render(request, 'home.html', {
        "cards": cards,
        "search_term": query if query else "",
        "current_user": current_user
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


@login_required
def add_favor(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = AddFavorForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/user')
    # If this is a GET (or any other method) create the default form.
    else:
        form = AddFavorForm()

    context = {
        'form': form,
    }

    return render(request, 'add_favor.html', context)

@login_required
def show_profile_page(request):
    current_user = request.user
    favors = Favor.objects.all().filter(owner=request.user).order_by("-date")
    context = {
        'user' : current_user,
        'favors': favors,
    }
    return render(request, 'profile.html', context)

@login_required
def edit_favor(request, pk):
    current_favor = get_object_or_404(Favor, pk=pk)
    form = AddFavorForm(request.POST or None, instance=current_favor)
    if form.is_valid():
        form.save()
        return redirect('show_profile_page')
    return render(request, "edit_favor.html", {'form' : form})

@login_required
def delete_favor(request, pk):
    current_favor = get_object_or_404(Favor, pk=pk)
    if request.method == 'POST':
        current_favor.delete()
        return redirect('show_profile_page')
    return render(request, "delete_favor.html", {'object' : current_favor})

