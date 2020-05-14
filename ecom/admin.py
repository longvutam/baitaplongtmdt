
from django.contrib import admin
from ecom.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'phone')
    search_fields = ('lastname',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('priceOrder', 'amount')
    search_fields = ('lastname',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Transaction, TransactionAdmin)