from django.conf.urls import url
from django.views.generic import TemplateView
from BookShop import views

app_name = 'BookShop'
urlpatterns = [
    url(r'^register/$', views.RegisterFormView.as_view()), # Регистрация 
    url(r'^login/$', views.LoginFormView.as_view()), # Аутентификация
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^$', TemplateView.as_view(template_name='home.html')), 
    url(r'^product/$', views.product, name='product'), # Товары
    url(r'^product/?select=max', views.product, name='product'), # Сортировка товаров от макисмальной цены к минимальной
    url(r'^product/?select=min', views.product, name='product'), # Сортировка товаров от минимальной цены к максимальной
    url(r'^contact/$', views.contact, name='contact'), # Пользователи
]
