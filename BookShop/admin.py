from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]
    search_fields = [field.name for field in Customer._meta.fields]
    list_filter = [field.name for field in Customer._meta.fields]
    exclude = []

    class Meta:
        model = Customer

admin.site.register(Customer, CustomerAdmin)