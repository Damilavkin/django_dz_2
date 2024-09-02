from django.contrib import admin
from .models import Buyer,Game



class BuyerAdmin(admin.ModelAdmin):
    list_display = ['name', 'balance', 'age']



class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'cost', 'size', 'description', 'age_limited']


admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Game, GameAdmin)