from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'home.html')

def slideshow(request):
    # some code
    return render(request, 'template/slideshow.html')

def test(request):
    # some code
    return render(request, 'test.html', {
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
                "title" : "Help with CS Homework",
                "favors" : 3,
                "description" : "Will look over code and help fix bugs or help get started on assignment",
                "username" : "Morgan Grimes",
                "date" : "2019-01-09",
                "location" : "CSL"
            },
        ]
    })

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