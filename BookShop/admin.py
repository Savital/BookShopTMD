from django.contrib import admin
from .models import *

# Register your models here.
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

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)