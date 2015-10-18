from django.contrib import admin

# Register your models here.
from inventory.models import *

admin.site.register(Product)
admin.site.register(Sku)
admin.site.register(User)
admin.site.register(PurchaseHistory)
admin.site.register(Predictions)