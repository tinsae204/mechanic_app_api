from django.contrib import admin
from .models import User, CustomAdmin, Customer, TRmanager, Mechanic


admin.site.register(User)
admin.site.register(Mechanic)
admin.site.register(CustomAdmin)
admin.site.register(Customer)
admin.site.register(TRmanager)






