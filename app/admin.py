
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from app.models import Customer,Product,Newsletter,Queries,Order,OrderItem,ShippingAddress,ProductReview
from django.contrib.auth.models import Group
# Register your models here.


admin.site.register(Customer)
admin.site.unregister(Group)
admin.site.register(Product)
admin.site.register(Newsletter)
admin.site.register(Queries)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ProductReview)