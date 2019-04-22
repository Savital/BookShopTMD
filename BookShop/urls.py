"""@package api
Documentation for api.
@brief Elegant URL scheme is an important in a high-quality Web application.
Django lets you design URLs however you want, with no framework limitations.
To design URLs you create a Python module informally called a URLconf.
This module is a mapping between URL path expressions to views.
This mapping can be as short or as long as needed.
It can reference other mappings.
And, because it’s pure Python code, it can be constructed dynamically.
"""

from django.conf.urls import url
from django.views.generic import TemplateView
from BookShop import views

'''
 This patterns of requests

 Registration
    Parameters: name, email, password
    Method: POST
 Example:
    >>>url(r'^register/$', views.RegisterFormView.as_view())

 Login
     Parameters: name/email, password
     Method: POST
 Example:
     >>>url(r'^login/$', views.LoginFormView.as_view())

 Logout
     Parameters: name/email, password
     Method: POST
 Example:
     >>>url(r'^login/$', views.LoginFormView.as_view())

 Home
     Parameters:
     Method: GET
 Example:
     >>>url(r'^login/$', views.LoginFormView.as_view())

 Products
    Parameters: ID, price, name
    Method: GET
 Example:
    >>>url(r'^product/$', views.product, name='product')

 Sort of Products by max
    Parameters: max
    Method: POST
 Example:
    >>>url(r'^product/?select=max', views.product, name='product')

 Sort of Products by min
    Parameters: min
    Method: POST
 Example:
    >>>url(r'^product/?select=min', views.product, name='product')

 Users
    Parameters: name, email
    Method: GET
 Example:
    >>>url(r'^contact/$', views.contact, name='contact')'''


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
