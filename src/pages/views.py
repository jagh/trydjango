from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kargs):
    print(args, kargs)
    print(request.user)
    # return HttpResponse('<h1> Hello World </h1>') #string of HTML code
    return render(request, "homepage.html", {})

def contact_view(request, *args, **kargs):
    return HttpResponse('<h1> Contact page </h1>') #string of HTML code

def about_view(request, *args, **kargs):
    return HttpResponse('<h1> About page </h1>') #string of HTML code

def social_view(request, *args, **kargs):
    return HttpResponse('<h1> Social page </h1>') #string of HTML code
