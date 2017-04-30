from django.contrib import admin

from .models import *

admin.site.register(Flavoring)
admin.site.register(ELiquid)
admin.site.register(UsersFavouriteELiquids)
admin.site.register(UsersFlavoringInventory)
admin.site.register(UsersNicotineInventory)
admin.site.register(Composition)
