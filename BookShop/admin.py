from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]
    search_fields = [field.name for field in Customer._meta.fields]
    list_filter = [field.name for field in Customer._meta.fields]
    exclude = []

    class Meta:
        model = Customer

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    search_fields = [field.name for field in Order._meta.fields]
    list_filter = [field.name for field in Order._meta.fields]
    exclude = []

    class Meta:
        model = Order
        
class ProducersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Producers._meta.fields]
    search_fields = [field.name for field in Producers._meta.fields]
    list_filter = [field.name for field in Producers._meta.fields]
    exclude = []

    class Meta:
        model = Producers
      
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    search_fields = [field.name for field in Product._meta.fields]
    list_filter = [field.name for field in Product._meta.fields]
    exclude = []

    class Meta:
        model = Product

class ShopAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Shop._meta.fields]
    search_fields = [field.name for field in Shop._meta.fields]
    list_filter = [field.name for field in Shop._meta.fields]
    exclude = []

    class Meta:
        model = Shop

class RelationsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Relations._meta.fields]
    search_fields = [field.name for field in Relations._meta.fields]
    list_filter = [field.name for field in Relations._meta.fields]
    exclude = []

    class Meta:
        model = Relations    

class StockAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Stock._meta.fields]
    search_fields = [field.name for field in Stock._meta.fields]
    list_filter = [field.name for field in Stock._meta.fields]
    exclude = []

    class Meta:
        model = Stock

class StaffAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Staff._meta.fields]
    search_fields = [field.name for field in Staff._meta.fields]
    list_filter = [field.name for field in Staff._meta.fields]
    exclude = []

    class Meta:
        model = Staff

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    search_fields = [field.name for field in Category._meta.fields]
    list_filter = [field.name for field in Category._meta.fields]
    exclude = []

    class Meta:
        model = Category

class OrderProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderProduct._meta.fields]
    search_fields = [field.name for field in OrderProduct._meta.fields]
    list_filter = [field.name for field in OrderProduct._meta.fields]
    exclude = []

    class Meta:
        model = OrderProduct        
        
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Producers, ProducersAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Relations, RelationsAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
