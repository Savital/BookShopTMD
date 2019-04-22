"""@package views
Documentation for views.
A view function, or view for short, is simply a Python function.
That takes a Web request and returns a Web response.
This response can be the HTML contents of a Web page.
The view itself contains whatever arbitrary logic necessary to return response.
This code can live anywhere you want, as long as it’s on your Python path.
There’s no other requirement–no “magic,” so to speak.
For the sake of putting the code somewhere.
"""

from django.db.models import *
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views.generic.base import View, logger

from BookShop.models import *

# Documentation for a function contact.
#
#  This functions is to render contact.html.


def contact(request):
    return render(request, './contact.html', locals())


# Documentation for a function product.
#
#  This functions is to render product.html.


def product(request):
    assert isinstance(request, HttpRequest)
    select = request.GET.get('select', '')

    if select == 'max':
        products = Product.objects.all().order_by('-price')[:3]
    elif select == 'min':
        products = Product.objects.all().order_by('price')[:3]
    else:
        products = Product.objects.all()
    count = Product.objects.count()
    orders = OrderProduct.objects.all().filter(
        order_id=Order.objects.all().filter(
            customer_id__first_name=request.user),
        product_id=Product.objects.filter(
            price__in=[1, 200]))
    average = Product.objects.all().aggregate(Avg('price'))
    logger.error(orders.query)
    avg = average['price__avg']

    return render(request, './product.html',
                  {
                      'products': products,
                      'count': count,
                      'orders_in': products,
                      'average': avg,
                  })


# Documentation for a function RegisterFormView.
#
#  This functions is to render register.html.


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


# Documentation for a function LoginFormView.
#
#  This functions is to render login.html.


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"  # Redirect to main page if success

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


# Documentation for a function LogoutView.
#
#  This functions is to redirect to home.html.


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
