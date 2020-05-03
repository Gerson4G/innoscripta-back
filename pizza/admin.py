from django.contrib import admin
from pizza.models import *

admin.site.register(PizzaInfo)
admin.site.register(Pizza)
admin.site.register(User)
admin.site.register(Ingredients)
admin.site.register(Order)
