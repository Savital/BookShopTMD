"""@package api
Documentation for api.
Elegant URL scheme is an important in a high-quality Web application.
Django lets you design URLs however you want, with no framework limitations.
To design URLs you create a Python module informally called a URLconf.
This module is a mapping between URL path expressions to views.
This mapping can be as short or as long as needed.
It can reference other mappings.
And, because it’s pure Python code, it can be constructed dynamically.

@brief This patterns of requests
 Registration http://127.0.0.1:8000/register/
    Parameters: name, email, password
    Method: POST
 Example:
    >>>url(r'^register/$', views.RegisterFormView.as_view())

 Login http://127.0.0.1:8000/login/
     Parameters: name/email, password
     Method: POST
 Example:
     >>>url(r'^login/$', views.LoginFormView.as_view())

 Logout http://127.0.0.1:8000/logout/
     Parameters: name/email, password
     Method: POST
 Example:
     >>>url(r'^logout/$', views.LoginFormView.as_view())

 Home http://127.0.0.1:8000/
     Parameters:
     Method: GET
 Example:
     >>>url(r'^/$', views.LoginFormView.as_view())

 Products http://127.0.0.1:8000/product/?select=all
    Parameters: ID, price, name
    Method: GET
 Example:
    >>>url(r'^product/$', views.product, name='product')

 Sort of Products by max http://127.0.0.1:8000/product/?select=max
    Parameters: max
    Method: POST
 Example:
    >>>url(r'^product/?select=max', views.product, name='product')

 Sort of Products by min http://127.0.0.1:8000/product/?select=min
    Parameters: min
    Method: POST
 Example:
    >>>url(r'^product/?select=min', views.product, name='product')

 Users http://127.0.0.1:8000/contact/
    Parameters: name, email
    Method: GET
 Example:
    >>>url(r'^contact/$', views.contact, name='contact')"""

from django.conf.urls import url
from django.views.generic import TemplateView
from BookShop import views


app_name = 'BookShop'
urlpatterns = [
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^product/$', views.product, name='product'),
    url(r'^product/?select=max', views.product,
        name='product'),
    url(r'^product/?select=min', views.product,
        name='product'),
    url(r'^contact/$', views.contact, name='contact'),
]
