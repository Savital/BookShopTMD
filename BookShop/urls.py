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
    url(r'^register/$', views.RegisterFormView.as_view()),  # Регистрация
    url(r'^login/$', views.LoginFormView.as_view()),  # Аутентификация
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^product/$', views.product, name='product'),  # Товары
    # Сортировка товаров от макисмальной цены к минимальной
    url(r'^product/?select=max', views.product, name='product'),
    # Сортировка товаров от минимальной цены к максимальной
    url(r'^product/?select=min', views.product, name='product'),
    url(r'^contact/$', views.contact, name='contact'),  # Пользователи
]
