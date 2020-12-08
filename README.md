# trydjango
Basic steps for developing Python Django applications


--------------
## Basic steps to initialize Django

* Create a Django project
`django-admin startproject trydjango .`  
> It generayes the base django framewrok

* Execute a django server
`python3 manage.py runserver`     
> Check default in http://127.0.0.1:8000/

* Django execute database definitions on settings.py
`python3 manage.py migrate`


--------------
## Built components as third party apps

* Create a super user for Django administration in 127.0.0.1:8000/admin
`python3 manage.py createsuperuser`   

* Create the first component
`python3 manage.py startapp products`
> It generates a folder products,
> Then we create a class Product with their attributes inside the products.models.py

* Execute manage migration to generate the products database structure
```
python3 manage.py makemigrations
python3 manage.py migrate
```
> Once we have defined the model, we register it into the admin.py, like:
> admin.site.register(Product), to be showed in Django administration



--------------
## Create product object in the python shell
`python3 manage.py shell`

*Then is possible to import Product using the bases of python, as:
`from products.models import Product`

* List all registers inside the Products
```
Product.objects.all()
Output: <QuerySet [<Product: Product object (1)>]>
```

* Add values into the Product
```
Product.objects.create(title='Newer', price=29,99, summary='sweet')
Output: <Product: Product object (2)>
```


--------------
## Adding new fields
* Django field references -> https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.Field
```
class Product(models.Model):
    title       = models.CharField(max_length=120)  # max_length will require
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField()
```

--------------
## Change a model
* Adding a new feature into the Product model, using the basic intuition:
`featured     = models.BooleanField()  # null=True, default=True`

* The second option is to select a fix option: to Provide a one-off default now + True
```
python3 manage.py makemigrations
Please select a fix:
  1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
Type 'exit' to exit this prompt
>>> True
```


--------------
## Default Homepage to custom Homepage
* Create other component called pages
`python3 manage.py startapp pages`
> Then add 'pages' into settings.py -> apps

* We will add HTML code into the component pages -> view.py:
```
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view():
    return HttpResponse('<h1> Hello World </h1>') #string of HTML code
```

* Then import and add the function with the html into trydjango.urls.py
```
from django.contrib import admin
from django.urls import path

from pages.views import homepage_view

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('admin/', admin.site.urls),
]
```
> With this procedure its possible to add more views


--------------
## URL Routing and Requests
* Explicited we pass the name to be used as view route into urls.py
`path('about/', about_view, name='about'),`

* To manage the view requests we use the function args and we include a variable request like:
```
def homepage_view(request, *args, **kargs):
    print(args, kargs)
    print(request.user)
    return HttpResponse('<h1> Hello World </h1>') #string of HTML code
```


--------------
## Django Templates
* We will return a template from django defaults using 'render':
```
from django.http import HttpResponse

def homepage_view(request, *args, **kargs):
    return render(request, "homepage.html", {})
```
> But also it will required the homepage.html template.
> We make a new folder called templates and we add the file homepage.html.

* Then, we will add the templates folder into the trydjango settings.py file:
```
TEMPLATES = [
    {
      'DIRS': [os.path.join(BASE_DIR, 'templates')],
    }
```


--------------
## Django Templates Engine Basics
* In the templates like homepage.html, we can use the basics of django functions as the 'request':
```
<h1> Homepage </h1>
{{ request.user.is_authenticated }}
<p> This is the template </p>
```

* Also we create a base.htmml as a html framework for all the views:
```
<html>
<body>
  {% block content %}
  replace me
  {% endblock %}
</body>
</html>
```
> Also in the view html we need to reference the 'block <name>'
```
{% extends 'base.html' %}
{% block content %}
    <h1> Homepage </h1>
    {{ request.user.is_authenticated }}
    <p> This is the template </p>
{% endblock %}
```

## Include Template Tag
* Django enables to use inlude modules of html code, for example we add navbar.html code in the base.html:
```
<html>
<body>
  {% include 'navbar.html' %}
</html>
</body>
```

## Rendering Context in a Template
* django redering data as int, list and dicts from each view function like def about_view() in views.py:
```
def about_view(request, *args, **kargs):
    my_context = {
        "my_text": "This is a general text in views",
        "my_number": 123,
        "my_lists": [123,456,678]
    }
    return render(request, "about.html", my_context)
```

* And it can be called directly from their correspond html page, like:
```
<p>
{{ my_text }}, {{ my_number }}, {{my_lists}}
</p>
```

## For loops in a Templates
* Once we send a list from a view funtion, we could deploy a list, like:
```
<ul>
  <p> My list: </p>
{% for my_sub_item in my_lists %}
  <li> {{forloop.counter}} - {{ my_sub_item }} </li>
{% endfor %}
</ul>
```

## Using conditionals in Templates
```
<ul>
  <p> My list: </p>
{% for abc in my_lists %}
  {% if abc == 123 %}
    <li> {{forloop.counter}} - {{ abc|add:22 }} </li>
  {% elif abc == "Abc" %}
    <li> This is not the network </li>
  {% else %}
    <li> {{forloop.counter}} - {{ abc}} </li>
  {% endif %}
{% endfor %}
</ul>
```

## Filters in Templates
```
<h3> {{ title|capfirst|title }} </h3>
```
