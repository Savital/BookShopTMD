"""@package models
Documentation for database models.
A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.
Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.
"""

from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """Documentation for a class Customer.
    Customer is the person who order books.
    """

    customer_id = models.Index
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "Customer %s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Order(models.Model):
    """Documentation for a class Order.
    Order is a class for ordering products list.
    """

    order_id = models.Index
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, default=0)
    date = models.DateField(auto_now_add=True, auto_now=False)
    time = models.TimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Order %s" % self.id

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class Producers(models.Model):
    """Documentation for a class Producers.
    Producers make books for customers.
    """

    producer_id = models.Index
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return "Producer %s" % self.id

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'


class Product(models.Model):
    """Documentation for a class Product.
    Product is a book itself.
    """

    product_id = models.Index
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.01)
    article = models.IntegerField(default=0)
    producer_id = models.ForeignKey(
        Producers, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "Product %s" % self.id

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Shop(models.Model):
    """Documentation for a class Shop.
    Shop is a place for ordering books.
    """

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
    """Documentation for a class Relations.
    Relations is a entity for multiply connections.
    """

    id = models.Index
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return "Relation %s" % self.id

    class Meta:
        verbose_name = 'Relation'
        verbose_name_plural = 'Relations'


class Stock(models.Model):
    """Documentation for a class Stock.
    Stock is a place to hold goods.
    """

    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    article = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "Stock %s" % self.id

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'


class Staff(models.Model):
    """Documentation for a class Staff.
    Staff is a place to manage personal.
    """

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


class Category(models.Model):
    """Documentation for a class Category.
    Category is a way to classify different kinds of books.
    """

    category = models.CharField(max_length=30)
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Product")

    def __str__(self):
        return "Category %s" % self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class OrderProduct(models.Model):
    """Documentation for a class OrderProduct.
    OrderProduct is a way to make orders.
    """

    order_id = models.ForeignKey(Order, on_delete=models.SET(Order.order_id))
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "Products in order %s" % self.id

    class Meta:
        verbose_name = 'Product in order'
        verbose_name_plural = 'Products in order'
