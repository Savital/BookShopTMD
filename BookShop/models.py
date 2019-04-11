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