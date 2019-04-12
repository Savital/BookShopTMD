from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    customer_id = models.Index
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "Customer %s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class Order(models.Model):
    order_id = models.Index
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, default=0)
    date = models.DateField(auto_now_add=True, auto_now=False)
    time = models.TimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Order %s" % self.id

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class Producers(models.Model):
    producer_id = models.Index
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return "Producer %s" % self.id

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'

class Product(models.Model):
    product_id = models.Index
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.01)
    article = models.IntegerField(default=0)
    producer_id = models.ForeignKey(Producers, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "Product %s" % self.id

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Shop(models.Model):
    shop_id = models.Index
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=12)
    email = models.EmailField

    def __str__(self):
        return "Shop %s" % self.id

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

class Relations(models.Model):
    id = models.Index
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return "Relation %s" % self.id

    class Meta:
        verbose_name = 'Relation'
        verbose_name_plural = 'Relations'

class Stock(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    article = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "Stock %s" % self.id

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'

class Staff(models.Model):
    id = models.Index
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth = models.DateField
    passport = models.CharField(max_length=10)
    tel = models.CharField(max_length=12)

    def __str__(self):
        return "Staff %s" % self.id

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'