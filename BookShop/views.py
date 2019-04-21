from django.db.models import *
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views.generic.base import View, logger

from BookShop.models import *

# Method for rendering contact.html


def contact(request):
    return render(request, './contact.html', locals())

# Method for rendering product.html


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
            customer_id__first_name=request.user), product_id=Product.objects.filter(
            price__in=[
                1, 200]))
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
    return render(request, './contact.html', locals())


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"  # Redirect to main page if success

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
