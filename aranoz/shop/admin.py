from django.contrib import admin
from .models import *

# Register your models here.
class user_data(admin.ModelAdmin):
    model=user
    readonly_fields=["password","email"]
admin.site.register(user,user_data)
admin.site.register(product)
admin.site.register(main_Category)
admin.site.register(add_cart)
admin.site.register(add_wishlist)
admin.site.register(cupan)
admin.site.register(rateing)
admin.site.register(billing_address)

class order_data(admin.ModelAdmin):
    model=user
    readonly_fields=["order_id","date","user","address","pname","qty","price","phone","zipcode"]
admin.site.register(order,order_data)