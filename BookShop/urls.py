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


app_name = 'BookShop'
urlpatterns = [
    # @brief api interface for bookshop app


    url(r'^register/$', views.RegisterFormView.as_view()),  # Registration
    url(r'^login/$', views.LoginFormView.as_view()),  # Auth
    url(r'^logout/$', views.LogoutView.as_view()),   # Logout
    url(r'^$', TemplateView.as_view(template_name='home.html')),  # Home
    url(r'^product/$', views.product, name='product'),  # Products
    url(r'^product/?select=max', views.product,
        name='product'),  # Sort from max price to min
    url(r'^product/?select=min', views.product,
        name='product'),  # Sort from min price to max
    url(r'^contact/$', views.contact, name='contact'),  # Users
]
