from django.contrib import admin

from chat.models import  Hotel, HotelCategory

# Register your models here.
admin.site.register(HotelCategory)
admin.site.register(Hotel)
