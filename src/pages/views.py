from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kargs):
    print(args, kargs)
    print(request.user)
    # return HttpResponse('<h1> Hello World </h1>') #string of HTML code
    return render(request, "homepage.html", {})

def contact_view(request, *args, **kargs):
    # return HttpResponse('<h1> Contact page </h1>') #string of HTML code
    return render(request, "contact.html", {})

def about_view(request, *args, **kargs):
    my_context = {
        "title": "this is a general text in views",
        "this_is_true": True,
        "my_number": 123,
        "my_lists": [123,456,678,"Abc"],
        "my_html": "<h3> Parser HTML code</h3>"
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kargs):
    # return HttpResponse('<h1> Social page </h1>') #string of HTML code
    return render(request, "social.html", {})
