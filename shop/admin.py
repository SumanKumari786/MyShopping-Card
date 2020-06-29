from django.contrib import admin
from shop.models import Product, Contact, Orders, OrderUpdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
