from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    customer_id = models.Index
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return "Customer %s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class Order(models.Model):
    order_id = models.Index
    #customer_id = models.ForeignKey(Customer)
    date = models.DateField(auto_now_add=True, auto_now=False)
    time = models.TimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Order %s" % self.id

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'