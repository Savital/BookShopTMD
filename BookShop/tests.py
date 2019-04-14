from django.test import TestCase
from BookShop.models import *
import datetime

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(first_name="Alek", last_name="Kulner")
        Customer.objects.create(first_name="Alex", last_name="Pak")
        Customer.objects.create(first_name="Serg", last_name="Napreev")

    def test_Customer(self):
        linonse = Customer.objects.get(first_name="Alek", last_name="Kulner")
        self.assertEqual('Customer Alek Kulner', linonse.__str__())

    def test_CustomerTwo(self):
        linonse = Customer.objects.get(first_name="Alek", last_name="Kulner")
        pak = Customer.objects.get(first_name="Alex", last_name="Pak")
        self.assertEqual('Customer Alek Kulner', linonse.__str__())
        self.assertEqual('Customer Alex Pak', pak.__str__())

    def test_CustomerMult(self):
        linonse = Customer.objects.get(first_name="Alek", last_name="Kulner")
        pak = Customer.objects.get(first_name="Alex", last_name="Pak")
        serg = Customer.objects.get(first_name="Serg", last_name="Napreev")
        self.assertEqual('Customer Alek Kulner', linonse.__str__())
        self.assertEqual('Customer Alex Pak', pak.__str__())
        self.assertEqual('Customer Serg Napreev', serg.__str__())

class OrderTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(first_name="Alek", last_name="Kulner")
        linonse = Customer.objects.get(first_name="Alek", last_name="Kulner")
        Order.objects.create(customer_id=linonse)

    def test_Order(self):
        linonse = Customer.objects.get(first_name="Alek", last_name="Kulner")
        order = Order.objects.get(customer_id=linonse)
        self.assertEqual('Order 1', order.__str__())

class ProducersTestCase(TestCase):
    def setUp(self):
        Producers.objects.create(name="Kulner", country="Alexandria")

    def test_Producers(self):
        linonse = Producers.objects.get(name="Kulner", country="Alexandria")
        self.assertEqual('Producer 1', linonse.__str__())

class ProductTestCase(TestCase):
    def setUp(self):
        Producers.objects.create(name="Kulner", country="Alexandria")
        linonse = Producers.objects.get(name="Kulner")
        Product.objects.create(name="KulnerBook", producer_id=linonse)

    def test_Product(self):
        book = Product.objects.get(name="KulnerBook")
        self.assertEqual('Product 1', book.__str__())

class ShopTestCase(TestCase):
    def setUp(self):
        Shop.objects.create(name="Alek", tel="+79256666666")

    def test_Shop(self):
        shop = Shop.objects.get(name="Alek")
        self.assertEqual('Shop 1', shop.__str__())

class RelationsTestCase(TestCase):
    def setUp(self):
        Shop.objects.create(name="Alek", tel="+79256666666")
        shop = Shop.objects.get(name="Alek", tel="+79256666666")
        print(shop)
        Relations.objects.create(shop_id=shop)

    def test_Relations(self):
        shop = Shop.objects.get(name="Alek", tel="+79256666666")
        relation = Relations.objects.get(shop_id=shop)
        self.assertEqual('Relation 1', relation.__str__())

class StockTestCase(TestCase):
    def setUp(self):
        Shop.objects.create(name="Alek", tel="+79256666666")
        Producers.objects.create(name="Kulner", country="Alexandria")
        linonse = Producers.objects.get(name="Kulner")
        Product.objects.create(name="KulnerBook", producer_id=linonse)

        shop = Shop.objects.get(name="Alek", tel="+79256666666")
        book = Product.objects.get(name="KulnerBook")
        Stock.objects.create(shop_id=shop, article=book)

    def test_Stock(self):
        shop = Shop.objects.get(name="Alek", tel="+79256666666")
        book = Product.objects.get(name="KulnerBook")
        Stock.objects.create(shop_id=shop, article=book)

        self.assertEqual('Shop 1', shop.__str__())

class StaffTestCase(TestCase):
    def setUp(self):
        Staff.objects.create(first_name="Alek", last_name="Kulner", passport="13", tel="666")

    def test_Staff(self):
        linonse = Staff.objects.get(first_name="Alek", last_name="Kulner")
        self.assertEqual('Staff 1', linonse.__str__())

class CategoryTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(first_name="Alek", last_name="Kulner")

    def test_Category(self):
        linonse = Customer.objects.get(first_name="Alek", last_name="Kulner")
        self.assertEqual('Customer Alek Kulner', linonse.__str__())
