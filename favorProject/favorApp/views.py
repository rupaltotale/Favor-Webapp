from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, AddFavorForm
from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponseForbidden
from .models import Favor, User, UserProfile

# Signup/Login stuff
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.db.models import Q # new
from django.http import JsonResponse
from django.core.mail import EmailMessage

def check_and_make_new_profile(user):
    profile = UserProfile.objects.filter(user=user)
    if not profile.exists():
        profile = UserProfile.objects.create(user=user).save()
    else:
        profile = profile.first()
    return profile
    

def landing(request):
    return render(request, 'landing.html')


@login_required
def show_services(request):
    query = request.GET.get('q')
    cards = Favor.objects.all()
    current_user = request.user
    check_and_make_new_profile(current_user)
    if request.method == "POST":
        card_id = request.POST.get('card_id')
        favor = Favor.objects.get(id=card_id)
        favor.pendingUsers.add(current_user) 
        owner_email = favor.owner.email
        title = "You have a new request - Favor"
        body = "Hooray! Someone has requested your service: {}. \nReach out to {} at {}. \
            \nYou can also confirm or deny their on your profile page.".format(
            favor.title,
            current_user.first_name + " " + current_user.last_name,
            current_user.email
        )
        email = EmailMessage(title, body, to=[owner_email])
        email.send()
    if query:
        cards = Favor.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    return render(request, 'home.html', {
        "cards": [card for card in cards if current_user != card.owner],
        "user_favors" : UserProfile.objects.get(user=current_user).number_of_favors,
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
            new_profile = UserProfile.objects.create(user=user)
            new_profile.save()
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
            doc = form.save(commit=False)
            doc.owner = request.user
            doc.save()
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
def show_profile_page(request, show_modal="no", favor_id=-1):
    current_user = request.user
    profile = check_and_make_new_profile(current_user)
    favorsOwned = Favor.objects.all().filter(owner=request.user).order_by("-date")
    pendingFavors = Favor.objects.all().filter(pendingUsers=request.user).order_by("-date")
    confirmedFavors = Favor.objects.all().filter(confirmedUsers=request.user).order_by("-date")

    context = {
        'user' : current_user,
        'profile' : profile,
        'ownedFavors': favorsOwned,
        'pendingFavors' : pendingFavors,
        'confirmedFavors' : confirmedFavors,
        'show_modal' : show_modal,
        'favor_id' : favor_id
    }

    return render(request, 'profile.html', context)

@login_required
def process_profile_page_req(request):
    if request.method == "POST":
        current_user = request.user
        user_id = request.POST.get("user_id")
        favor_id = request.POST.get("favor_id")
        action = request.POST.get("action")
        user = get_object_or_404(User, pk=user_id)
        favor = get_object_or_404(Favor, pk=favor_id)
        if current_user != favor.owner:
            return HttpResponseForbidden('<h1>Forbidden: requesting user not favor owner</h1>')

        if action == "ACCEPT":
            favor.pendingUsers.remove(user)
            favor.confirmedUsers.add(user)
            UserProfile.objects.get(user=current_user).number_of_favors += favor.number_of_favors
            UserProfile.objects.get(user=user).number_of_favors -= favor.number_of_favors
        elif action == "DENY":
            favor.pendingUsers.remove(user)
        else:
            return HttpResponseNotAllowed('<h1>Unacceptable ACTION received</h1>')
        return HttpResponseRedirect("/user/")
    else:
        return HttpResponseNotAllowed('<h1>GET service unavailable</h1>')

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

